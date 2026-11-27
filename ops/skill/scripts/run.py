#!/usr/bin/env python3
"""Run the application CLI, preparing the environment on first use."""
import hashlib
import subprocess
import sys
from setup import ROOT, PYTHON, MARKER, setup

try:
    digest = hashlib.sha256((ROOT / 'requirements.txt').read_bytes()).hexdigest()
    if not PYTHON.is_file() or not MARKER.is_file() or MARKER.read_text() != digest:
        setup()
    result = subprocess.run([str(PYTHON), '-m', 'core.action', *sys.argv[1:]], cwd=ROOT)
    sys.exit(result.returncode)
except (OSError, subprocess.CalledProcessError, ValueError) as exc:
    print(f'Unable to run application: {exc}. Run python3 scripts/setup.py in a terminal.', file=sys.stderr)
    sys.exit(1)
