import time
import unittest
from core.common.deadline import run_with_deadline

class DeadlineTests(unittest.TestCase):
    def test_login_allows_authorization_taking_more_than_thirty_seconds(self):
        from unittest.mock import patch
        from core.core.account.login import LoginSession
        clock = [100.0]
        with patch('core.core.account.login.CallbackServer') as callback, \
             patch('core.core.account.login.time.monotonic', side_effect=lambda: clock[0]), \
             patch('core.core.account.login.exchange', return_value={'access_token': 'fake'}), \
             patch('core.core.account.login.personal_id', return_value='test-user'), \
             patch('core.core.account.login.save_authorization', return_value='test-account') as save:
            def authorize(timeout):
                clock[0] += 45
                return 'code'
            callback.return_value.wait.side_effect = authorize
            session = LoginSession(None, 'client', 'secret', 'http://localhost:8765/callback', lambda s: s)
            self.assertEqual(session.complete(), 'test-account')
            self.assertEqual(save.call_args.kwargs['deadline'], 160.0)

    def test_times_out_even_when_worker_blocks(self):
        started = time.monotonic()
        with self.assertRaises(TimeoutError):
            run_with_deadline(lambda: time.sleep(1), time.monotonic() + 0.08, interval=0.02, report=lambda _: None)
        self.assertLess(time.monotonic() - started, 0.5)

    def test_returns_result_and_propagates_errors(self):
        self.assertEqual(run_with_deadline(lambda: 42, time.monotonic() + 1), 42)
        def fail(): raise ValueError('failure')
        with self.assertRaisesRegex(ValueError, 'failure'):
            run_with_deadline(fail, time.monotonic() + 1)

    def test_expired_save_does_not_write_credentials(self):
        import sqlite3
        import tempfile
        from pathlib import Path
        from core.core.account.setup import initialize
        from core.core.account.login import save_authorization
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            initialize(root)
            def slow_encrypt(value):
                time.sleep(0.03)
                return value.encode()
            with self.assertRaises(TimeoutError):
                save_authorization(root, 'user', {'access_token': 'token'}, slow_encrypt,
                             deadline=time.monotonic() + 0.01)
            with sqlite3.connect(root / 'auth.sqlite3') as db:
                self.assertEqual(db.execute('select count(*) from credentials').fetchone()[0], 0)
                self.assertEqual(db.execute('select count(*) from accounts').fetchone()[0], 0)
            self.assertEqual(list(root.glob('account-*.sqlite3')), [])
