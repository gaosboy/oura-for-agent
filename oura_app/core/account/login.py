"""Oura account authorization and local credential persistence."""
import time
import json
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from ...common.storage import transaction
from .setup import initialize_record, verify_record
from ...common.deadline import run_with_deadline
from ...link.oura_v2.api import authorization, exchange, personal_id
from .callback import CallbackServer
from .model import AccountData, CredentialData
from .profile import activate_in_transaction


class LoginSession:
    def __init__(self, root, client_id, secret, redirect, encrypt):
        self.root, self.client_id, self.secret = root, client_id, secret
        self.redirect, self.encrypt = redirect, encrypt
        self.url, state, self.verifier = authorization(client_id, redirect)
        self.callback = CallbackServer(redirect, state)

    def __enter__(self):
        self.callback.__enter__()
        return self

    def __exit__(self, *args):
        return self.callback.__exit__(*args)

    def complete(self, timeout=60, report=None):
        deadline = time.monotonic() + timeout
        def fetch():
            code = self.callback.wait(timeout=max(0, deadline - time.monotonic()))
            if time.monotonic() >= deadline:
                raise TimeoutError('Login timed out')
            token = exchange(self.client_id, self.secret, self.redirect, code, self.verifier)
            if time.monotonic() >= deadline:
                raise TimeoutError('Login timed out')
            return token, personal_id(token['access_token'])
        token, provider_id = run_with_deadline(fetch, deadline, report=report)
        return save_authorization(self.root, provider_id, token, self.encrypt, deadline=deadline)

def stamp(value):
    return value.isoformat().replace('+00:00', 'Z')


def save_authorization(data_dir, provider_id, token, encrypt, deadline=None):
    root = Path(data_dir)
    if not provider_id or not token.get('access_token'):
        raise ValueError('Missing account ID or access token')
    def check():
        if deadline is not None and time.monotonic() >= deadline:
            raise TimeoutError('Login timed out')
    check()
    access = encrypt(token['access_token'])
    refresh = encrypt(token['refresh_token']) if token.get('refresh_token') else None
    now = datetime.now(timezone.utc)
    expires = stamp(now + timedelta(seconds=int(token['expires_in']))) if token.get('expires_in') is not None else None
    scopes = token.get('scope') or []
    if isinstance(scopes, str): scopes = scopes.split()
    timestamp = stamp(now)
    created = None
    try:
        check()
        with transaction(root / 'auth.sqlite3', deadline) as db:
            check()
            row = AccountData.find_one(db, provider='oura', provider_user_id=provider_id)
            if row:
                account_id = row['account_id']
                verify_record(root / f'account-{account_id}.sqlite3', account_id)
                AccountData.update(db, {'updated_at': timestamp}, account_id=account_id)
            else:
                account_id = str(uuid.uuid4())
                name = f'account-{account_id}.sqlite3'
                created = root / name
                initialize_record(created, account_id, timestamp)
                AccountData.insert(db, {'account_id': account_id, 'provider': 'oura', 'provider_user_id': provider_id, 'created_at': timestamp, 'updated_at': timestamp})
            values = {'access_token_ciphertext': access, 'refresh_token_ciphertext': refresh, 'expires_at': expires, 'token_type': token.get('token_type', 'bearer'), 'granted_scopes_json': json.dumps(scopes), 'updated_at': timestamp}
            if CredentialData.find_one(db, account_id=account_id):
                CredentialData.update(db, values, account_id=account_id)
            else:
                CredentialData.insert(db, {'account_id': account_id, **values})
            activate_in_transaction(db, account_id)
            check()
        return account_id
    except BaseException:
        if created:
            created.unlink(missing_ok=True)
        raise
