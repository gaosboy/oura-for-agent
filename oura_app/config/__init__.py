"""Load one environment and its private local overrides."""
import os
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ENVIRONMENTS = ('local', 'dev', 'test', 'prod')
REDIRECT_URI = 'http://localhost:8765/callback'
# Accept legacy redirect entries when reading files; the application owns the value.
KEYS = ('OURA_CLIENT_ID', 'OURA_CLIENT_SECRET', 'OURA_REDIRECT_URI', 'OURA_DATA_DIR', 'OURA_LOG_LEVEL')


def read_file(path):
    config = {}
    if not path.exists():
        return config
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, separator, value = line.partition('=')
        if not separator or key.strip() not in KEYS:
            raise ValueError(f'Invalid configuration entry on line {number}')
        config[key.strip()] = value.strip()
    return config


def load_config(root=ROOT, environ=None):
    environ = os.environ if environ is None else environ
    selected = environ.get('OURA_ENV')
    if selected and selected not in ENVIRONMENTS:
        raise ValueError('OURA_ENV must be local, dev, test, or prod')
    if not selected:
        selected = next((name for name in ENVIRONMENTS if (root / ('.env.' + name)).is_file()), None)
    config = {}
    if selected:
        path = root / ('.env.' + selected)
        if not path.is_file():
            raise FileNotFoundError('Selected environment configuration does not exist')
        config.update(read_file(path))
        if selected != 'local':
            config.update(read_file(root / ('.env.' + selected + '.local')))
    for key in KEYS:
        if environ.get(key):
            config[key] = environ[key]
    config['OURA_REDIRECT_URI'] = REDIRECT_URI
    return selected, config


def save_local(root, values, selected='local'):
    if any(k not in KEYS or '\n' in v or '\r' in v for k, v in values.items()):
        raise ValueError('Invalid configuration value')
    name = '.env.local' if selected in (None, 'local') else '.env.' + selected + '.local'
    path = root / name
    current = read_file(path)
    current.update(values)
    fd, temp = tempfile.mkstemp(prefix='.env-', dir=root, text=True)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            for key, value in current.items():
                f.write(f'{key}={value}\n')
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def log_level(config):
    value = (config.get('OURA_LOG_LEVEL') or 'DEBUG').upper()
    if value not in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
        raise ValueError('OURA_LOG_LEVEL must be DEBUG, INFO, WARNING, ERROR or CRITICAL')
    return value
