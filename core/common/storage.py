"""SQLite connection and initial schema creation."""
from contextlib import closing
from datetime import datetime, timezone
import os
import sqlite3
import re
from contextlib import contextmanager
from pathlib import Path
from ..config import ROOT, load_config


def now():
    return datetime.now(timezone.utc)


def stamp(value):
    return value.isoformat().replace('+00:00', 'Z')


def connect(path):
    db = sqlite3.connect(path)
    db.execute('PRAGMA foreign_keys = ON')
    return db


def create_database(path, schema):
    fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    os.close(fd)
    try:
        with closing(connect(path)) as db, db:
            db.executescript((Path(__file__).resolve().parents[1] / 'resource' / 'migrations' / schema / '001.sql').read_text())
            db.execute('INSERT INTO schema_migrations VALUES (?, ?)', (1, stamp(now())))
    except BaseException:
        path.unlink(missing_ok=True)
        raise




def resolve_data_dir(override=None, config_root=ROOT, environ=None):
    """Resolve CLI override, configured path, or the default application directory."""
    if override is not None:
        return Path(override).expanduser().resolve()
    _, config = load_config(config_root, environ)
    value = config.get('OURA_DATA_DIR')
    if not value:
        return Path.home() / '.local' / 'share' / 'data-from-oura'
    path = Path(value).expanduser()
    return (path if path.is_absolute() else config_root / path).resolve()



@contextmanager
def transaction(path, deadline=None):
    import time
    with closing(connect(path)) as db, db:
        db.row_factory = sqlite3.Row
        if deadline is not None:
            db.execute('PRAGMA busy_timeout = %d' % max(0, int((deadline - time.monotonic()) * 1000)))
        db.execute('BEGIN IMMEDIATE')
        yield db
        if deadline is not None and time.monotonic() >= deadline:
            raise TimeoutError('Login timed out')


class DataObject:
    """Generic mapping of field dictionaries to a SQLite table."""
    table = None

    @staticmethod
    def _identifier(value):
        if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*', value):
            raise ValueError('Invalid field or table name')
        return '"' + value + '"'

    @classmethod
    def count(cls, db):
        return db.execute('SELECT COUNT(*) FROM ' + cls._identifier(cls.table)).fetchone()[0]

    @classmethod
    def find_one(cls, db, **where):
        if not where:
            raise ValueError('A filter is required')
        clause = ' AND '.join(cls._identifier(k) + ' = ?' for k in where)
        row = db.execute('SELECT * FROM ' + cls._identifier(cls.table) + ' WHERE ' + clause + ' LIMIT 1', tuple(where.values())).fetchone()
        return dict(row) if row is not None else None

    @classmethod
    def insert(cls, db, values):
        fields = ', '.join(cls._identifier(k) for k in values)
        placeholders = ', '.join('?' for _ in values)
        db.execute('INSERT INTO ' + cls._identifier(cls.table) + ' (' + fields + ') VALUES (' + placeholders + ')', tuple(values.values()))

    @classmethod
    def update(cls, db, values, **where):
        if not values or not where:
            raise ValueError('Values and a filter are required')
        changes = ', '.join(cls._identifier(k) + ' = ?' for k in values)
        condition = ' AND '.join(cls._identifier(k) + ' = ?' for k in where)
        db.execute('UPDATE ' + cls._identifier(cls.table) + ' SET ' + changes + ' WHERE ' + condition, tuple(values.values()) + tuple(where.values()))

    @classmethod
    def select(cls, db, *, filters=None, order=None, limit=None):
        filters = filters or []
        clauses, params = [], []
        for field, op, value in filters:
            if op not in ('=', '>=', '<=', '>', '<'):
                raise ValueError('Unsupported comparison')
            clauses.append(cls._identifier(field) + ' ' + op + ' ?')
            params.append(value)
        sql = 'SELECT * FROM ' + cls._identifier(cls.table)
        if clauses:
            sql += ' WHERE ' + ' AND '.join(clauses)
        if order:
            sql += ' ORDER BY ' + ', '.join(cls._identifier(key) for key in order)
        if limit is not None:
            if not isinstance(limit, int) or limit < 1:
                raise ValueError('Limit must be positive')
            sql += ' LIMIT ?'
            params.append(limit)
        return [dict(row) for row in db.execute(sql, params)]

    @classmethod
    def delete(cls, db, **where):
        if not where:
            raise ValueError('A filter is required')
        clause = ' AND '.join(cls._identifier(k) + ' = ?' for k in where)
        db.execute('DELETE FROM ' + cls._identifier(cls.table) + ' WHERE ' + clause, tuple(where.values()))
