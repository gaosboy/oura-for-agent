#!/usr/bin/env python3
"""Upgrade an installed Data from Oura Skill from a release ZIP."""
import argparse
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import tempfile
import zipfile


def upgrade(archive, skill):
    if not skill.is_dir() or skill.is_symlink():
        raise ValueError('Installed Skill directory does not exist or is a symlink')
    with zipfile.ZipFile(archive) as package:
        files = []
        for info in package.infolist():
            path = PurePosixPath(info.filename)
            if (path.is_absolute() or '..' in path.parts or not path.parts or
                path.parts[0] != 'data-from-oura' or '\\' in info.filename or
                stat.S_ISLNK(info.external_attr >> 16)):
                raise ValueError('Unsafe archive entry')
            if info.is_dir():
                continue
            relative = path.parts[1:]
            if not relative or not (relative[0] in ('core', 'scripts') or
                                    len(relative) == 1 and relative[0] in ('SKILL.md', 'VERSION', 'requirements.txt')):
                raise ValueError('Unexpected archive entry')
            if any(part.startswith('.') for part in relative):
                raise ValueError('Hidden archive entry')
            files.append((info, relative))
        if not {'data-from-oura/SKILL.md', 'data-from-oura/VERSION', 'data-from-oura/scripts/run.py'}.issubset({i.filename for i, _ in files}):
            raise ValueError('Incomplete Skill archive')
        backup = Path(tempfile.mkdtemp(prefix='data-from-oura-backup-', dir=skill.parent))
        backup.rmdir()
        shutil.copytree(skill, backup, symlinks=True)
        print(f'Backup: {backup}', flush=True)
        try:
            for info, relative in files:
                target = skill.joinpath(*relative)
                for parent in [target, *target.parents]:
                    if parent == skill:
                        break
                    if parent.is_symlink():
                        raise ValueError('Installed path contains a symlink')
                target.parent.mkdir(parents=True, exist_ok=True)
                with package.open(info) as source, tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as temp:
                    try:
                        shutil.copyfileobj(source, temp)
                        temp.close()
                        os.replace(temp.name, target)
                    finally:
                        if os.path.exists(temp.name):
                            os.unlink(temp.name)
        except Exception:
            print(f'Upgrade incomplete. Restore the installed directory from {backup}.', flush=True)
            raise
    print('Upgrade complete. Restart your agent and run setup if needed.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path, help='Downloaded release ZIP')
    parser.add_argument('--skill-dir', type=Path, default=Path.home() / '.codex/skills/data-from-oura')
    args = parser.parse_args()
    try:
        upgrade(args.archive, args.skill_dir.expanduser().absolute())
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        parser.exit(1, f'Upgrade failed: {exc}\n')

if __name__ == '__main__':
    main()
