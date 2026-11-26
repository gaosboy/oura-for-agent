"""Application operations and composition for supported entry points."""
from pathlib import Path
from ...config import ROOT, load_config, save_local, log_level
from ...core.account.setup import initialize, has_credentials, get_access_token
from ...core.record.sync import sync_range, sync_full, sync_incremental
from ...core.record.query import read_records
from ...core.account.login import LoginSession
from ...core.account.profile import current_profile, list_profiles, activate
from ...common.security import encryption_key
from ...common.storage import resolve_data_dir
from .report import generate_report


class Application:
    def __init__(self, data_dir=None):
        self.data_dir = resolve_data_dir(data_dir)

    def initialize(self):
        return initialize(self.data_dir)

    def log_level(self):
        return log_level(load_config()[1])

    def configuration(self):
        return load_config()

    def save_configuration(self, selected, values):
        save_local(ROOT, values, selected)
        return load_config()

    def login(self, config):
        return LoginSession(self.data_dir, config['OURA_CLIENT_ID'], config['OURA_CLIENT_SECRET'],
                            config['OURA_REDIRECT_URI'], encryption_key(self.data_dir, has_credentials(self.data_dir)))

    def sync_range(self, account_id, start, end, kinds):
        return sync_range(self.data_dir, account_id, get_access_token(self.data_dir, account_id), start, end, kinds)

    def sync_full(self, account_id, start, end=None):
        return sync_full(self.data_dir, account_id, get_access_token(self.data_dir, account_id), start, end)

    def sync_incremental(self, account_id, end=None, kinds=None, overlap_days=7):
        return sync_incremental(self.data_dir, account_id, get_access_token(self.data_dir, account_id), end, kinds, overlap_days=overlap_days)

    def read_records(self, account_id, kinds=None, start=None, end=None, source_id=None, limit=1000):
        return read_records(self.data_dir, account_id, kinds, start, end, source_id, limit)

    def current_profile(self):
        return current_profile(self.data_dir)

    def list_profiles(self):
        return list_profiles(self.data_dir)

    def activate_account(self, account_id):
        activate(self.data_dir, account_id)
        return current_profile(self.data_dir)

    def report(self, report_type, start, end, force=False):
        account_id = current_profile(self.data_dir)['account_id']
        return generate_report(self.data_dir, account_id, report_type, start, end, force)
