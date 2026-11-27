"""Account initialization and credential state."""
import os
from pathlib import Path
from ...common.storage import create_database, transaction
from .model import CredentialData, SchemaVersion
from ..record.model import RecordIdentity


def initialize(data_dir):
    root = Path(data_dir)
    root.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(root, 0o700)
    path = root / 'auth.sqlite3'
    if not path.exists():
        create_database(path, 'auth')
    with transaction(path) as db:
        if SchemaVersion.count(db) != 1 or not SchemaVersion.find_one(db, version=1):
            raise ValueError('Unsupported authentication database; reinitialize development data')
        from .model import AccountData
        if not db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='active_account'").fetchone():
            raise ValueError('Legacy authentication database; reinitialize development data')
        if 'data_db_name' in [row[1] for row in db.execute('PRAGMA table_info(accounts)')]:
            raise ValueError('Legacy authentication database; reinitialize development data')
    return path


def has_credentials(data_dir):
    root = Path(data_dir)
    with transaction(root / 'auth.sqlite3') as db:
        return CredentialData.count(db) > 0



def get_access_token(data_dir, account_id):
    """Read and decrypt stored access token; do not log its value."""
    import keyring
    from cryptography.fernet import Fernet
    from datetime import datetime, timezone
    from .model import AccountData
    root = Path(data_dir)
    from .profile import current_profile
    if current_profile(root)['account_id'] != account_id:
        raise ValueError('Account is not active')
    with transaction(root / 'auth.sqlite3') as db:
        account = AccountData.find_one(db, account_id=account_id)
        credential = CredentialData.find_one(db, account_id=account_id)
    if not account or not credential:
        raise ValueError('Account or credentials not found')
    expiry = credential['expires_at']
    if expiry and datetime.fromisoformat(expiry.replace('Z', '+00:00')) <= datetime.now(timezone.utc):
        raise ValueError('Access token expired; reauthorize account')
    key = keyring.get_password('data-from-oura', str(root.resolve()))
    if not key:
        raise RuntimeError('Encryption key missing from system keyring')
    return Fernet(key.encode()).decrypt(credential['access_token_ciphertext']).decode()


def initialize_record(path, account_id, timestamp):
    create_database(path, 'record')
    with transaction(path) as db:
        RecordIdentity.insert(db, {'singleton': 1, 'account_id': account_id, 'created_at': timestamp})


def verify_record(path, account_id):
    if not path.is_file():
        raise FileNotFoundError('Account record database not found')
    with transaction(path) as db:
        identity = RecordIdentity.find_one(db, singleton=1)
        if not identity or identity['account_id'] != account_id:
            raise ValueError('Account database identity mismatch')
