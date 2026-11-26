CREATE TABLE schema_migrations (
  version INTEGER PRIMARY KEY,
  applied_at TEXT NOT NULL
);
CREATE TABLE accounts (
  account_id TEXT PRIMARY KEY,             -- 应用生成的随机 UUID
  provider TEXT NOT NULL DEFAULT 'oura',
  provider_user_id TEXT NOT NULL,          -- personal_info.id
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  UNIQUE (provider, provider_user_id)
);
CREATE TABLE credentials (
  account_id TEXT PRIMARY KEY REFERENCES accounts(account_id) ON DELETE CASCADE,
  access_token_ciphertext BLOB NOT NULL,
  refresh_token_ciphertext BLOB,
  expires_at TEXT,
  token_type TEXT NOT NULL,
  granted_scopes_json TEXT NOT NULL,        -- JSON 字符串数组
  updated_at TEXT NOT NULL
);
CREATE TABLE active_account (
  singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
  account_id TEXT NOT NULL REFERENCES accounts(account_id) ON DELETE CASCADE
);
