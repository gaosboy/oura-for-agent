#!/usr/bin/env python3
"""Prepare the Skill's private Python environment and initialize its database."""
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parents[1]
ENV = ROOT / '.venv'
PYTHON = ENV / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
MARKER = ENV / '.oura-requirements-sha256'


def setup():
    requirements = ROOT / 'requirements.txt'
    digest = hashlib.sha256(requirements.read_bytes()).hexdigest()
    if not PYTHON.is_file():
        print('Creating Python virtual environment...', flush=True)
        venv.create(ENV, with_pip=True)
    if not MARKER.is_file() or MARKER.read_text() != digest:
        print('Installing runtime dependencies...', flush=True)
        subprocess.run([str(PYTHON), '-m', 'pip', 'install', '-r', str(requirements)], check=True)
        MARKER.write_text(digest)
    print('Initializing local authentication database...', flush=True)
    subprocess.run([str(PYTHON), '-m', 'oura_app.action'], cwd=ROOT, check=True)


if __name__ == '__main__':
    try:
        setup()
    except (OSError, subprocess.CalledProcessError, ValueError) as exc:
        print(f'Setup failed: {exc}. Resolve the error and rerun python3 scripts/setup.py.', file=sys.stderr)
        sys.exit(1)
