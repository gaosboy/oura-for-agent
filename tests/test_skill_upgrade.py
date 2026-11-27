import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'ops/skill/upgrade.py'

class UpgradeTests(unittest.TestCase):
    def test_upgrade_preserves_private_files_and_backup(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); skill = root / 'data-from-oura'; skill.mkdir()
            (skill / '.env.local').write_text('private')
            (skill / 'SKILL.md').write_text('old')
            archive = root / 'new.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('data-from-oura/SKILL.md', 'new')
                z.writestr('data-from-oura/VERSION', '2.0.0')
                z.writestr('data-from-oura/scripts/run.py', 'runner')
            result = subprocess.run([sys.executable, str(SCRIPT), str(archive), '--skill-dir', str(skill)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((skill / 'SKILL.md').read_text(), 'new')
            self.assertEqual((skill / '.env.local').read_text(), 'private')
            backup = next(root.glob('data-from-oura-backup-*'))
            self.assertEqual((backup / 'SKILL.md').read_text(), 'old')
            self.assertEqual((backup / '.env.local').read_text(), 'private')

    def test_rejects_archive_with_private_files_or_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); skill = root / 'data-from-oura'; skill.mkdir()
            (skill / '.env.local').write_text('private')
            archive = root / 'bad.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('data-from-oura/SKILL.md', 'new')
                z.writestr('data-from-oura/.env.local', 'overwrite')
            result = subprocess.run([sys.executable, str(SCRIPT), str(archive), '--skill-dir', str(skill)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual((skill / '.env.local').read_text(), 'private')
