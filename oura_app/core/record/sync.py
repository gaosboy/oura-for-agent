"""Synchronize Oura collections into the local record model."""
import hashlib
import json
import uuid
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from ...common.storage import transaction
from ...link.oura_v2.api import collection
from .access import record_path
from .model import Record, Sample, SyncRun, SyncItem

DATE_KINDS = ('daily_activity','daily_cardiovascular_age','daily_readiness','daily_resilience','daily_sleep','daily_spo2','daily_stress','enhanced_tag','rest_mode_period','session','sleep','sleep_time','tag','vO2_max','workout')
SAMPLE_KINDS = ('heartrate', 'ring_battery_level')
ALL_KINDS = DATE_KINDS + SAMPLE_KINDS + ('personal_info', 'ring_configuration')


def now():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def _dates(start, end):
    start, end = date.fromisoformat(start), date.fromisoformat(end)
    if start > end:
        raise ValueError('Start date must not be after end date')
    return start.isoformat(), end.isoformat()


def _store(db, kind, items):
    timestamp = now()
    if kind in SAMPLE_KINDS:
        groups = {}
        for item in items:
            ms = item.get('timestamp_unix')
            if not isinstance(ms, int) or isinstance(ms, bool):
                raw = item.get('timestamp')
                if not isinstance(raw, str):
                    raise ValueError('Sample missing timestamp')
                instant = datetime.fromisoformat(raw.replace('Z', '+00:00'))
                if instant.tzinfo is None or instant.utcoffset() is None:
                    raise ValueError('Sample timestamp requires timezone')
                ms = int(instant.timestamp() * 1000)
            groups.setdefault(ms, []).append(item)
        for ms, group in groups.items():
            Sample.delete(db, kind=kind, timestamp_ms=ms)
            for item in group:
                payload = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
                digest = hashlib.sha256(payload.encode()).hexdigest()
                if Sample.find_one(db, kind=kind, timestamp_ms=ms, payload_hash=digest):
                    continue
                Sample.insert(db, {'kind':kind, 'timestamp_ms':ms, 'source':item.get('source'), 'payload_hash':digest, 'payload_json':payload, 'first_seen_at':timestamp, 'last_seen_at':timestamp})
        return
    for item in items:
        source_id = item.get('id')
        if not isinstance(source_id, str) or not source_id:
            raise ValueError('Oura record missing id')
        existing = Record.find_one(db, kind=kind, source_id=source_id)
        fields = {'day':item.get('day') or item.get('start_day'), 'start_at':item.get('start_datetime') or item.get('start_time') or item.get('bedtime_start'), 'end_at':item.get('end_datetime') or item.get('end_time') or item.get('bedtime_end'), 'observed_at':item.get('timestamp'), 'payload_json':json.dumps(item, ensure_ascii=False, separators=(',', ':')), 'last_seen_at':timestamp}
        if existing:
            Record.update(db, fields, kind=kind, source_id=source_id)
        else:
            Record.insert(db, {'kind':kind, 'source_id':source_id, 'first_seen_at':timestamp, **fields})


def sync_range(root, account_id, token, start, end, kinds, fetch=None, mode='range'):
    start, end = _dates(start, end)
    kinds = tuple(dict.fromkeys(kinds))
    if not kinds or any(kind not in ALL_KINDS for kind in kinds):
        raise ValueError('Unknown or empty data types')
    path = record_path(Path(root), account_id)
    run_id = str(uuid.uuid4())
    with transaction(path) as db:
        SyncRun.insert(db, {'run_id':run_id,'mode':mode,'requested_start':start,'requested_end':end,'started_at':now(),'status':'running'})
    result = {}
    for kind in kinds:
        try:
            category = 'datetime' if kind in SAMPLE_KINDS else 'single' if kind == 'personal_info' else 'snapshot' if kind == 'ring_configuration' else 'date'
            source = fetch(kind, start, end) if fetch else collection(kind, start, end, token, category)
            items = list(source)
            with transaction(path) as db:
                _store(db, kind, items)
                SyncItem.insert(db, {'run_id':run_id,'kind':kind,'status':'succeeded','records_received':len(items),'finished_at':now()})
            result[kind] = {'status':'succeeded','count':len(items)}
        except Exception as exc:
            code = str(getattr(exc, 'code', type(exc).__name__))
            with transaction(path) as db:
                SyncItem.insert(db, {'run_id':run_id,'kind':kind,'status':'failed','records_received':0,'error_code':code,'finished_at':now()})
            result[kind] = {'status':'failed','error_code':code}
    passed = sum(value['status'] == 'succeeded' for value in result.values())
    status = 'succeeded' if passed == len(kinds) else 'partial' if passed else 'failed'
    with transaction(path) as db:
        SyncRun.update(db, {'status':status,'finished_at':now()}, run_id=run_id)
    return {'run_id':run_id, 'status':status, 'items':result}


def sync_full(root, account_id, token, start, end=None, fetch=None):
    return sync_range(root, account_id, token, start, end or date.today().isoformat(), ALL_KINDS, fetch, mode='full')


def sync_incremental(root, account_id, token, end=None, kinds=None, fetch=None, overlap_days=7):
    end = end or date.today().isoformat()
    if not isinstance(overlap_days, int) or overlap_days < 0:
        raise ValueError('Invalid overlap')
    kinds = tuple(kinds or ALL_KINDS)
    path = record_path(Path(root), account_id)
    with transaction(path) as db:
        runs = SyncRun.select(db, filters=[('status','=', 'succeeded')]) + SyncRun.select(db, filters=[('status','=', 'partial')])
        starts = []
        for kind in kinds:
            finished = [r['requested_end'] for r in runs if SyncItem.find_one(db, run_id=r['run_id'], kind=kind, status='succeeded')]
            if not finished:
                raise ValueError(f'No successful initial sync for {kind}; run sync range for this type first')
            starts.append(date.fromisoformat(max(finished)) - timedelta(days=overlap_days))
    return sync_range(root, account_id, token, min(starts).isoformat(), end, kinds, fetch)
