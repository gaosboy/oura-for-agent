"""Local authorized account profiles and the active authorization."""
from pathlib import Path
from ...common.storage import transaction
from .model import AccountData, CredentialData, ActiveAccount


def current_profile(data_dir):
    with transaction(Path(data_dir) / 'auth.sqlite3') as db:
        active = ActiveAccount.find_one(db, singleton=1)
        if not active:
            raise ValueError('No active Oura account')
        account = AccountData.find_one(db, account_id=active['account_id'])
        credential = CredentialData.find_one(db, account_id=active['account_id'])
        if not account or not credential:
            raise ValueError('Active account credentials not found')
        return {**account, 'expires_at': credential['expires_at'], 'granted_scopes_json': credential['granted_scopes_json']}


def list_profiles(data_dir):
    with transaction(Path(data_dir) / 'auth.sqlite3') as db:
        active = ActiveAccount.find_one(db, singleton=1)
        accounts = AccountData.select(db, order=['created_at'])
        return [{**row, 'active': bool(active and active['account_id'] == row['account_id'])} for row in accounts]


def activate_in_transaction(db, account_id):
    if not AccountData.find_one(db, account_id=account_id) or not CredentialData.find_one(db, account_id=account_id):
        raise ValueError('Account or credentials not found')
    if ActiveAccount.find_one(db, singleton=1):
        ActiveAccount.update(db, {'account_id':account_id}, singleton=1)
    else:
        ActiveAccount.insert(db, {'singleton':1, 'account_id':account_id})


def activate(data_dir, account_id):
    with transaction(Path(data_dir) / 'auth.sqlite3') as db:
        activate_in_transaction(db, account_id)
