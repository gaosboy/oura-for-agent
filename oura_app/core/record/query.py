"""Read locally synchronized records and samples."""
import json
from pathlib import Path
from datetime import date, datetime, time, timedelta, timezone
from ...common.storage import transaction
from .access import record_path
from .model import Record, Sample
from .sync import ALL_KINDS, SAMPLE_KINDS


def read_records(root, account_id, kinds=None, start=None, end=None, source_id=None, limit=1000):
    kinds = tuple(kinds or ALL_KINDS)
    if any(k not in ALL_KINDS for k in kinds) or (limit is not None and limit < 1):
        raise ValueError('Invalid query')
    start_date = date.fromisoformat(start) if start else None
    end_date = date.fromisoformat(end) if end else None
    if start_date and end_date and start_date > end_date:
        raise ValueError('Start date must not be after end date')
    path = record_path(Path(root), account_id)
    output = []
    with transaction(path) as db:
        for kind in kinds:
            if kind in SAMPLE_KINDS:
                if source_id:
                    continue
                filters = [('kind','=',kind)]
                if start_date: filters.append(('timestamp_ms','>=',int(datetime.combine(start_date,time.min,timezone.utc).timestamp()*1000)))
                if end_date: filters.append(('timestamp_ms','<',int(datetime.combine(end_date+timedelta(days=1),time.min,timezone.utc).timestamp()*1000)))
                rows = Sample.select(db, filters=filters, order=['timestamp_ms'], limit=limit)
            else:
                filters = [('kind','=',kind)]
                if start: filters.append(('day','>=',start))
                if end: filters.append(('day','<=',end))
                if source_id: filters.append(('source_id','=',source_id))
                rows = Record.select(db, filters=filters, order=['day'], limit=limit)
            for row in rows:
                row['data'] = json.loads(row.pop('payload_json'))
                output.append(row)
                if limit is not None and len(output) >= limit:
                    return output
    return output
