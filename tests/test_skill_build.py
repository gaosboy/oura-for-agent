import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'ops' / 'skill' / 'build_skill.py'


class SkillBuildTests(unittest.TestCase):
    def test_build_archive_is_runtime_only_and_version_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            cmd = [sys.executable, str(BUILD), '--output', tmp]
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            version = json.loads((ROOT / 'ops' / 'skill' / 'build.json').read_text())['version']
            archive = Path(tmp) / f'data-from-oura-{version}.zip'
            with zipfile.ZipFile(archive) as z:
                names = z.namelist()
                self.assertIn('data-from-oura/SKILL.md', names)
                self.assertIn('data-from-oura/core/resource/migrations/auth/001.sql', names)
                self.assertFalse(any('__pycache__' in n or '/tests/' in n or '/docs/' in n or '.env' in n for n in names))
            check = subprocess.run(cmd + ['--check-version'], capture_output=True, text=True)
            self.assertEqual(check.returncode, 0, check.stderr)
            self.assertIn(version, check.stdout)
            duplicate = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(duplicate.returncode, 0)

    def test_extracted_cli_initializes_without_credentials(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([sys.executable, str(BUILD), '--output', tmp], check=True, capture_output=True)
            skill = Path(tmp) / 'data-from-oura'
            env = dict(os.environ, OURA_DATA_DIR=str(Path(tmp) / 'data'))
            for key in ('OURA_ENV', 'OURA_CLIENT_ID', 'OURA_CLIENT_SECRET', 'OURA_REDIRECT_URI'):
                env.pop(key, None)
            result = subprocess.run([sys.executable, '-m', 'core.action'], cwd=skill, env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('Authentication database ready', result.stdout)
            self.assertTrue(list((Path(tmp) / 'data').glob('*.sqlite3')))
