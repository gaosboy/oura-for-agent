"""Data objects corresponding to authentication tables."""
from ...common.storage import DataObject


class AccountData(DataObject):
    table = 'accounts'


class CredentialData(DataObject):
    table = 'credentials'


class SchemaVersion(DataObject):
    table = 'schema_migrations'


class ActiveAccount(DataObject):
    table = 'active_account'
