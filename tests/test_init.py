import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from core.core.account.setup import initialize
from core.core.account.login import save_authorization
from core.link.oura_v2.api import validate_callback

class InitTests(unittest.TestCase):
    def test_successful_login_keeps_serving_until_session_exits(self):
        import urllib.request
        from core.core.account.login import LoginSession
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            initialize(root)
            with patch('core.core.account.login.exchange', return_value={'access_token': 'fake'}), \
                 patch('core.core.account.login.personal_id', return_value='test-user'):
                with LoginSession(root, 'client', 'secret', 'http://localhost:0/callback', lambda s: s.encode()) as session:
                    from urllib.parse import parse_qs, urlsplit
                    state = parse_qs(urlsplit(session.url).query)['state'][0]
                    url = f'http://127.0.0.1:{session.callback.port}/callback?code=fake&state={state}'
                    with urllib.request.urlopen(url, timeout=1) as response:
                        self.assertEqual(response.status, 200)
                    self.assertTrue(session.complete())
                    with urllib.request.urlopen(url, timeout=1) as response:
                        self.assertEqual(response.status, 200)
                self.assertEqual(session.callback.server.fileno(), -1)

    def test_initialize_is_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)
            initialize(path); initialize(path)
            with sqlite3.connect(path / 'auth.sqlite3') as db:
                self.assertEqual(db.execute('select count(*) from schema_migrations').fetchone()[0], 1)
            self.assertEqual(list(path.glob('account-*.sqlite3')), [])

    def test_account_is_reused_and_tokens_encrypted(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d); initialize(path)
            encrypt = lambda s: ('encrypted:' + s).encode()
            first = save_authorization(path, 'user', {'access_token':'secret', 'token_type':'bearer'}, encrypt)
            second = save_authorization(path, 'user', {'access_token':'new', 'token_type':'bearer'}, encrypt)
            self.assertEqual(first, second)
            with sqlite3.connect(path / 'auth.sqlite3') as db:
                self.assertEqual(db.execute('select count(*) from accounts').fetchone()[0], 1)
                self.assertEqual(db.execute('select access_token_ciphertext from credentials').fetchone()[0], b'encrypted:new')
                name = f'account-{first}.sqlite3'
            with sqlite3.connect(path / name) as db:
                self.assertEqual(db.execute('select account_id from database_identity').fetchone()[0], first)
                self.assertTrue(db.execute("select name from sqlite_master where name='records'").fetchone())

    def test_callback_checks_state_and_redirect(self):
        self.assertEqual(validate_callback('http://127.0.0.1:8765/callback?code=x&state=abc', 'http://127.0.0.1:8765/callback', 'abc'), 'x')
        with self.assertRaises(ValueError):
            validate_callback('http://evil/callback?code=x&state=abc', 'http://127.0.0.1:8765/callback', 'abc')
        with self.assertRaises(ValueError):
            validate_callback('http://127.0.0.1:8765/callback?code=x&state=wrong', 'http://127.0.0.1:8765/callback', 'abc')

    def test_record_database_name_is_derived_from_account_id(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)
            initialize(path)
            account = save_authorization(path, 'user', {'access_token': 'fake'}, lambda s: s.encode())
            self.assertTrue((path / f'account-{account}.sqlite3').is_file())
            with sqlite3.connect(path / 'auth.sqlite3') as db:
                self.assertNotIn('data_db_name', [row[1] for row in db.execute('PRAGMA table_info(accounts)')])

