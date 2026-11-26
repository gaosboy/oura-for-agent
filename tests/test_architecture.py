import ast
import tempfile
import unittest
from pathlib import Path
from oura_app.action.operations import Application

class ArchitectureTests(unittest.TestCase):
    def test_initialize_via_operations(self):
        with tempfile.TemporaryDirectory() as directory:
            app = Application(Path(directory))
            path = app.initialize()
            self.assertTrue(path.is_file())
            self.assertEqual(app.initialize(), path)

    def test_cli_only_imports_operations_from_application(self):
        source = Path('oura_app/action/cli/main.py').read_text()
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.level:
                self.assertTrue(node.module and node.module.startswith('operations'), node.module)

    def test_login_operation_preserves_credentials_and_reuses_account(self):
        from unittest.mock import patch
        import sqlite3
        from oura_app.core.account.login import LoginSession
        class Callback:
            def __init__(self, redirect, state): pass
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def wait(self, timeout): return 'code'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            app = Application(root)
            app.initialize()
            token = {'access_token': 'fake', 'token_type': 'bearer'}
            with patch('oura_app.core.account.login.CallbackServer', Callback), \
                 patch('oura_app.core.account.login.authorization', return_value=('url', 'state', 'verifier')), \
                 patch('oura_app.core.account.login.exchange', return_value=token), \
                 patch('oura_app.core.account.login.personal_id', return_value='user'):
                with LoginSession(root, 'client', 'secret', 'http://localhost:1234/cb', lambda s: ('enc:' + s).encode()) as session:
                    first = session.complete()
                with LoginSession(root, 'client', 'secret', 'http://localhost:1234/cb', lambda s: ('enc:' + s).encode()) as session:
                    self.assertEqual(first, session.complete())
            with sqlite3.connect(root / 'auth.sqlite3') as db:
                self.assertEqual(db.execute('select count(*) from accounts').fetchone()[0], 1)
                self.assertEqual(db.execute('select access_token_ciphertext from credentials').fetchone()[0], b'enc:fake')

    def test_business_models_inherit_generic_data_object(self):
        from oura_app.common.storage import DataObject
        from oura_app.core.account.model import AccountData, CredentialData
        from oura_app.core.record.model import RecordIdentity
        self.assertTrue(issubclass(AccountData, DataObject))
        self.assertTrue(issubclass(CredentialData, DataObject))
        self.assertTrue(issubclass(RecordIdentity, DataObject))
