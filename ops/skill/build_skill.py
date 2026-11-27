#!/usr/bin/env python3
"""Build an installable runtime-only Skill and check local release versions."""
import argparse
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / 'ops' / 'skill' / 'build.json'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'build')
    parser.add_argument('--check-version', action='store_true', help='Compare configured version with local built artifacts')
    parser.add_argument('--force', action='store_true', help='Replace artifacts of the same version')
    args = parser.parse_args()
    config = json.loads(CONFIG.read_text(encoding='utf-8'))
    name, version = config['name'], config['version']
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or not re.fullmatch(r'(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)', version):
        raise ValueError('Invalid Skill name or version; use lowercase name and MAJOR.MINOR.PATCH')
    output = args.output.resolve()
    versions = []
    if output.exists():
        for path in output.glob(f'{name}-*.zip'):
            match = re.fullmatch(re.escape(name) + r'-(\d+)\.(\d+)\.(\d+)\.zip', path.name)
            if match:
                versions.append(tuple(map(int, match.groups())))
    current = tuple(map(int, version.split('.')))
    latest = max(versions, default=None)
    if args.check_version:
        print(f'Configured: {version}; latest local artifact: {".".join(map(str, latest)) if latest else "none"}')
        return int(latest is not None and current < latest)
    if latest is not None and current < latest:
        raise ValueError('Configured version is older than the latest local artifact')
    output.mkdir(parents=True, exist_ok=True)
    dest, archive = output / name, output / f'{name}-{version}.zip'
    if dest.exists() and any((dest / item).exists() for item in ('.venv', '.env.local', '.env.dev.local', '.env.test.local', '.env.prod.local')):
        raise ValueError('Output Skill contains local runtime state; move it before rebuilding')
    if archive.exists() and not args.force:
        raise ValueError('This version already exists; increment version or use --force')
    with tempfile.TemporaryDirectory(dir=output) as tmp:
        stage = Path(tmp) / name
        stage.mkdir()
        for source in (ROOT / 'core').rglob('*'):
            if source.is_file() and '__pycache__' not in source.parts and (source.suffix == '.py' or ('resource' in source.relative_to(ROOT / 'core').parts and source.suffix in ('.sql', '.html'))):
                target = stage / source.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        shutil.copy2(ROOT / 'requirements.txt', stage)
        shutil.copy2(ROOT / 'ops' / 'skill' / 'SKILL.md.template', stage / 'SKILL.md')
        shutil.copytree(ROOT / 'ops' / 'skill' / 'scripts', stage / 'scripts', ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        (stage / 'VERSION').write_text(version + '\n', encoding='utf-8')
        staged_zip = Path(tmp) / archive.name
        with zipfile.ZipFile(staged_zip, 'w', zipfile.ZIP_DEFLATED) as z:
            for path in sorted(stage.rglob('*')):
                if path.is_file():
                    z.write(path, path.relative_to(stage.parent))
        if dest.exists():
            shutil.rmtree(dest)
        shutil.move(str(stage), dest)
        staged_zip.replace(archive)
    print(f'Built {dest} and {archive}')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f'Build failed: {exc}', file=sys.stderr)
        sys.exit(1)
