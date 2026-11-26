"""Locate the record database using the local account identifier."""
import uuid
from pathlib import Path
from ..account.profile import current_profile


def record_path(root, account_id=None):
    profile = current_profile(root)
    if account_id is not None and account_id != profile['account_id']:
        raise ValueError('Account is not active')
    account_id = profile['account_id']
    try:
        if str(uuid.UUID(account_id)) != account_id:
            raise ValueError
    except (ValueError, TypeError, AttributeError):
        raise ValueError('Invalid account identifier') from None
    root = Path(root)
    path = root / f'account-{account_id}.sqlite3'
    if not path.is_file():
        raise FileNotFoundError('Account record database not found')
    return path
