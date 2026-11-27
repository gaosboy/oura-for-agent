import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch, MagicMock
from core.action.cli.main import main
from core.config import load_config

class CliTests(unittest.TestCase):
    def test_login_guides_credentials_and_uses_fixed_redirect_without_prompt(self):
        for existing in ({}, {'OURA_CLIENT_ID': 'test-client'},
                         {'OURA_CLIENT_SECRET': 'test-secret'},
                         {'OURA_CLIENT_ID': 'test-client', 'OURA_CLIENT_SECRET': 'test-secret'}):
            with self.subTest(existing_keys=list(existing)), tempfile.TemporaryDirectory() as d:
                root = Path(d)
                (root / '.env.local').write_text(''.join(f'{k}={v}\n' for k, v in existing.items()))
                out = io.StringIO()

                def enter_client(prompt):
                    self.assertIn('client ID', prompt)
                    self.assertIn('https://developer.ouraring.com/applications', out.getvalue())
                    return 'test-client'

                def enter_secret(prompt):
                    self.assertIn('client secret', prompt)
                    self.assertIn('https://developer.ouraring.com/applications', out.getvalue())
                    return 'test-secret'

                session = MagicMock()
                session.url = 'https://example.com/authorize'
                session.complete.return_value = 'test-account'
                with patch('sys.argv', ['oura', '--data-dir', str(root / 'data'), '--login']), \
                     patch('core.action.operations.ROOT', root), \
                     patch('core.action.operations.load_config', side_effect=lambda: load_config(root, {})), \
                     patch('builtins.input', side_effect=enter_client) as client_input, \
                     patch('core.action.cli.main.getpass.getpass', side_effect=enter_secret) as secret_input, \
                     patch('time.sleep'), \
                     patch('core.action.cli.main.webbrowser.open'), \
                     patch('core.action.operations.Application.login', return_value=session) as login, \
                     redirect_stdout(out):
                    self.assertEqual(main(), 0)
                self.assertEqual(client_input.call_count, int('OURA_CLIENT_ID' not in existing))
                self.assertEqual(secret_input.call_count, int('OURA_CLIENT_SECRET' not in existing))
                self.assertIn('http://localhost:8765/callback', out.getvalue())
                self.assertIn('Account initialized: test-account', out.getvalue())
                self.assertEqual(login.call_args.args[0], {
                    'OURA_CLIENT_ID': 'test-client', 'OURA_CLIENT_SECRET': 'test-secret',
                    'OURA_REDIRECT_URI': 'http://localhost:8765/callback'})
                self.assertEqual(load_config(root, {})[1]['OURA_CLIENT_SECRET'], 'test-secret')

    def test_login_counts_down_and_closes_callback_five_seconds_after_success(self):
        app = MagicMock()
        app.log_level.return_value = 'DEBUG'
        app.configuration.return_value = ('local', {
            'OURA_CLIENT_ID': 'test-client', 'OURA_CLIENT_SECRET': 'test-secret',
            'OURA_REDIRECT_URI': 'http://localhost:8765/callback'})
        session = app.login.return_value
        session.url = 'https://example.com/authorize'
        session.complete.return_value = 'test-account'
        events = []
        out = io.StringIO()

        def open_browser(url):
            self.assertIn(url, out.getvalue())
            self.assertIn('3 秒后', out.getvalue())
            self.assertIn('如果', out.getvalue())
            self.assertIn('浏览器', out.getvalue())
            events.append('open')
            return False

        def sleep(seconds):
            if 'open' in events:
                self.assertIn('Account initialized: test-account', out.getvalue())
                self.assertFalse(session.__exit__.called)
            events.append(seconds)

        with patch('sys.argv', ['oura', '--login']), \
             patch('core.action.cli.main.Application', return_value=app), \
             patch('time.sleep', side_effect=sleep), \
             patch('core.action.cli.main.webbrowser.open', side_effect=open_browser), \
             redirect_stdout(out):
            self.assertEqual(main(), 0)
        self.assertEqual(events, [1, 1, 1, 'open', 1, 1, 1, 1, 1])
        self.assertEqual(session.complete.call_args.kwargs['timeout'], 60)
        for remaining in range(5, 0, -1):
            self.assertIn(f'{remaining} 秒后关闭回调服务', out.getvalue())
        session.__exit__.assert_called_once()

    def test_terminal_highlights_interactive_output_and_respects_no_color(self):
        import os
        import re
        ansi = re.compile(r'\x1b\[[0-9;]*m')
        app = MagicMock()
        app.log_level.return_value = 'DEBUG'
        app.configuration.return_value = ('local', {
            'OURA_CLIENT_ID': 'test-client', 'OURA_CLIENT_SECRET': 'test-secret',
            'OURA_REDIRECT_URI': 'http://localhost:8765/callback'})
        session = app.login.return_value
        session.url = 'https://example.com/authorize'
        session.complete.return_value = 'test-account'
        for tty, no_color, expected_color in ((True, False, True), (False, False, False), (True, True, False)):
            with self.subTest(tty=tty, no_color=no_color), \
                 patch.dict(os.environ, {'TERM': 'xterm-256color'}, clear=True):
                if no_color:
                    os.environ['NO_COLOR'] = ''
                out = io.StringIO()
                with patch('sys.argv', ['oura', '--login']), \
                     patch('core.action.cli.main.Application', return_value=app), \
                     patch('time.sleep'), patch('core.action.cli.main.webbrowser.open'), \
                     patch.object(out, 'isatty', return_value=tty), redirect_stdout(out):
                    self.assertEqual(main(), 0)
                output = out.getvalue()
                self.assertEqual(bool(ansi.search(output)), expected_color)
                self.assertIn('https://example.com/authorize', ansi.sub('', output))
                self.assertIn('回调服务已关闭', ansi.sub('', output))

    def test_login_timeout_message_uses_sixty_seconds(self):
        app = MagicMock()
        app.log_level.return_value = 'DEBUG'
        app.configuration.return_value = ('local', {
            'OURA_CLIENT_ID': 'test-client', 'OURA_CLIENT_SECRET': 'test-secret',
            'OURA_REDIRECT_URI': 'http://localhost:8765/callback'})
        app.login.return_value.url = 'https://example.com/authorize'
        app.login.return_value.complete.side_effect = TimeoutError
        from contextlib import redirect_stderr
        with patch('sys.argv', ['oura', '--login']), \
             patch('core.action.cli.main.Application', return_value=app), \
             patch('time.sleep') as sleep, \
             patch('core.action.cli.main.webbrowser.open'), \
             redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()) as error:
            self.assertEqual(main(), 1)
        self.assertIn('60', error.getvalue())
        self.assertEqual(sleep.call_count, 3)

    def run_cli(self, args, app):
        with patch('sys.argv', ['oura'] + args), patch('core.action.cli.main.Application', return_value=app), redirect_stdout(io.StringIO()) as out:
            code = main()
        return code, json.loads(out.getvalue())

    def test_sync_range_uses_active_account(self):
        app = MagicMock(); app.log_level.return_value = 'DEBUG'; app.current_profile.return_value = {'account_id':'id'}
        app.sync_range.return_value = {'status':'succeeded','items':{}}
        code, result = self.run_cli(['sync','range','--start','2026-01-01','--end','2026-01-02','--types','daily_sleep'], app)
        self.assertEqual(code, 0); self.assertEqual(result['status'],'succeeded')
        app.sync_range.assert_called_once_with('id','2026-01-01','2026-01-02',['daily_sleep'])

    def test_partial_sync_fails_and_query_outputs_json(self):
        app=MagicMock(); app.log_level.return_value='DEBUG'; app.current_profile.return_value={'account_id':'id'}
        app.sync_full.return_value={'status':'partial','items':{}}
        self.assertEqual(self.run_cli(['sync','full','--start','2026-01-01'],app)[0],1)
        app.read_records.return_value=[{'kind':'daily_sleep','data':{'score':80}}]
        code, rows=self.run_cli(['read','--types','daily_sleep','--limit','5'],app)
        self.assertEqual(code,0); self.assertEqual(rows[0]['data']['score'],80)
