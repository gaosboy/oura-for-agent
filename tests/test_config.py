import tempfile
import unittest
from pathlib import Path
from core.config import load_config

class ConfigTests(unittest.TestCase):
    def test_redirect_is_fixed_without_user_configuration(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for redirect in (None, '', 'http://localhost:9999/old-callback'):
                with self.subTest(redirect=redirect):
                    (root / '.env.local').write_text(
                        '' if redirect is None else f'OURA_REDIRECT_URI={redirect}\n')
                    _, values = load_config(root, {'OURA_REDIRECT_URI': 'http://localhost:9998/old'})
                    self.assertEqual(values['OURA_REDIRECT_URI'], 'http://localhost:8765/callback')

    def test_priority_and_environment_override(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / '.env.prod').write_text('OURA_CLIENT_ID=prod\n')
            (p / '.env.dev').write_text('OURA_CLIENT_ID=dev\n')
            (p / '.env.local').write_text('OURA_CLIENT_ID=local\n')
            self.assertEqual(load_config(p, {})[1]['OURA_CLIENT_ID'], 'local')
            self.assertEqual(load_config(p, {'OURA_ENV':'prod'})[1]['OURA_CLIENT_ID'], 'prod')
            self.assertEqual(load_config(p, {'OURA_ENV':'dev', 'OURA_CLIENT_ID':'env'})[1]['OURA_CLIENT_ID'], 'env')

    def test_explicit_missing_and_invalid_environment_fail(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError): load_config(Path(d), {'OURA_ENV':'bogus'})
            with self.assertRaises(FileNotFoundError): load_config(Path(d), {'OURA_ENV':'local'})

class LocalCompletionTests(unittest.TestCase):
    def test_saved_values_fill_missing_selected_environment(self):
        from core.config import save_local
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / '.env.prod').write_text('OURA_CLIENT_ID=production\n')
            save_local(root, {'OURA_CLIENT_SECRET': 'secret', 'OURA_REDIRECT_URI': 'http://localhost:8765/callback'}, 'prod')
            _, values = load_config(root, {'OURA_ENV': 'prod'})
            self.assertEqual(values['OURA_CLIENT_ID'], 'production')
            self.assertEqual(values['OURA_CLIENT_SECRET'], 'secret')
            self.assertEqual((root / '.env.prod.local').stat().st_mode & 0o777, 0o600)

class DataDirectoryTests(unittest.TestCase):
    def test_storage_directory_resolution(self):
        from core.common.storage import resolve_data_dir
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '.env.local').write_text('OURA_DATA_DIR=data\n')
            self.assertEqual(resolve_data_dir(config_root=root, environ={}), (root / 'data').resolve())
            self.assertEqual(resolve_data_dir(config_root=root, environ={'OURA_DATA_DIR': '/tmp/oura-test'}), Path('/tmp/oura-test').resolve())
            self.assertEqual(resolve_data_dir(Path('/tmp/explicit'), config_root=root, environ={}), Path('/tmp/explicit').resolve())
            (root / '.env.local').unlink()
            self.assertEqual(resolve_data_dir(config_root=root, environ={}), Path.home() / '.local/share/data-from-oura')

class LoggingConfigTests(unittest.TestCase):
    def test_log_level_from_file_and_environment(self):
        from core.config import log_level
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / '.env.local').write_text('OURA_LOG_LEVEL=info\n')
            self.assertEqual(log_level(load_config(root, {})[1]), 'INFO')
            self.assertEqual(log_level(load_config(root, {'OURA_LOG_LEVEL':'warning'})[1]), 'WARNING')
            self.assertEqual(log_level({}), 'DEBUG')
            with self.assertRaises(ValueError): log_level({'OURA_LOG_LEVEL':'invalid'})
