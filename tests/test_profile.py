import tempfile
import unittest
from pathlib import Path
from oura_app.core.account.setup import initialize
from oura_app.core.account.login import save_authorization
from oura_app.core.account.profile import current_profile, activate, list_profiles
from oura_app.core.record.access import record_path

class ProfileTests(unittest.TestCase):
    def test_multiple_accounts_one_active_and_switch(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); initialize(root)
            with self.assertRaises(ValueError): current_profile(root)
            first = save_authorization(root, 'one', {'access_token':'x'}, lambda s:s.encode())
            second = save_authorization(root, 'two', {'access_token':'x'}, lambda s:s.encode())
            self.assertEqual(current_profile(root)['account_id'], second)
            self.assertEqual(len(list_profiles(root)), 2)
            with self.assertRaises(ValueError): record_path(root, first)
            activate(root, first)
            self.assertEqual(current_profile(root)['account_id'], first)
            self.assertEqual(record_path(root).name, f'account-{first}.sqlite3')
            with self.assertRaises(ValueError): activate(root, 'missing')
            self.assertEqual(current_profile(root)['account_id'], first)
