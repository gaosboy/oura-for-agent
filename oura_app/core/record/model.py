"""Local record database identity."""
from ...common.storage import DataObject


class RecordIdentity(DataObject):
    table = 'database_identity'


class Record(DataObject):
    table = 'records'


class Sample(DataObject):
    table = 'samples'


class SyncRun(DataObject):
    table = 'sync_runs'


class SyncItem(DataObject):
    table = 'sync_items'
