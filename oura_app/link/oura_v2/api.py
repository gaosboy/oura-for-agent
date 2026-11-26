import base64
import hashlib
import hmac
import json
import logging
import secrets
import urllib.parse
import urllib.request

logger = logging.getLogger(__name__)

AUTHORIZE = 'https://cloud.ouraring.com/oauth/authorize'
TOKEN = 'https://api.ouraring.com/oauth/token'
PERSONAL = 'https://api.ouraring.com/v2/usercollection/personal_info'


def authorization(client_id, redirect):
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b'=').decode()
    state = secrets.token_urlsafe(32)
    query = urllib.parse.urlencode({'response_type':'code', 'client_id':client_id, 'redirect_uri':redirect,
                                    'state':state, 'code_challenge':challenge, 'code_challenge_method':'S256'})
    return AUTHORIZE + '?' + query, state, verifier


def validate_callback(url, redirect, state):
    result = urllib.parse.urlsplit(url)
    expected = urllib.parse.urlsplit(redirect)
    if (result.scheme, result.netloc, result.path, result.fragment) != (expected.scheme, expected.netloc, expected.path, '') or expected.query or expected.fragment:
        raise ValueError('Redirect URL does not match configured callback')
    params = urllib.parse.parse_qs(result.query, keep_blank_values=True)
    if len(params.get('state', [])) != 1 or not hmac.compare_digest(params['state'][0], state):
        raise ValueError('Invalid OAuth state')
    if 'error' in params:
        raise ValueError('Authorization denied or failed')
    if len(params.get('code', [])) != 1 or not params['code'][0]:
        raise ValueError('Missing authorization code')
    return params['code'][0]


def request_json(url, data=None, token=None):
    headers = {'User-Agent':'DataFromOura/0.1', 'Accept':'application/json'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    encoded = urllib.parse.urlencode(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=encoded, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def exchange(client_id, secret, redirect, code, verifier):
    return request_json(TOKEN, {'grant_type':'authorization_code', 'client_id':client_id, 'client_secret':secret,
                                'redirect_uri':redirect, 'code':code, 'code_verifier':verifier})


def personal_id(token):
    value = request_json(PERSONAL, token=token).get('id')
    if not isinstance(value, str) or not value:
        raise ValueError('Oura did not return an account ID')
    return value


def collection(kind, start, end, token, mode='date'):
    """Yield every item, rejecting malformed or repeating page tokens."""
    from datetime import date, timedelta
    base = 'https://api.ouraring.com/v2/usercollection/' + urllib.parse.quote(kind, safe='')
    windows = [{}]
    if mode in ('date', 'datetime'):
        begin = date.fromisoformat(start)
        stop = date.fromisoformat(end) + timedelta(days=1)
        if begin >= stop:
            raise ValueError('Start date must not be after end date')
        windows = []
        while begin < stop:
            boundary = min(begin + timedelta(days=21), stop)
            if mode == 'date':
                windows.append({'start_date': begin.isoformat(),
                                'end_date': (boundary - timedelta(days=1)).isoformat()})
            else:
                windows.append({'start_datetime': begin.isoformat() + 'T00:00:00Z',
                                'end_datetime': boundary.isoformat() + 'T00:00:00Z'})
            begin = boundary
    for index, window in enumerate(windows, 1):
        logger.debug('同步 %s 窗口 %d/%d: %s', kind, index, len(windows), window or '全量快照')
        params = dict(window)
        page = 0
        seen = set()
        while True:
            url = base + ('?' + urllib.parse.urlencode(params) if params else '')
            page += 1
            logger.debug('请求 %s 窗口 %d/%d 第 %d 页', kind, index, len(windows), page)
            result = request_json(url, token=token)
            if mode == 'single':
                yield result
                return
            if not isinstance(result.get('data'), list):
                raise ValueError('Invalid Oura response')
            yield from result['data']
            next_token = result.get('next_token')
            if not next_token:
                break
            if not isinstance(next_token, str) or next_token in seen:
                raise ValueError('Invalid Oura pagination token')
            seen.add(next_token)
            params['next_token'] = next_token
