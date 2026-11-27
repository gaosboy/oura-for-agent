CREATE TABLE schema_migrations (
  version INTEGER PRIMARY KEY,
  applied_at TEXT NOT NULL
);
CREATE TABLE database_identity (
  singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
  account_id TEXT NOT NULL UNIQUE,          -- 对应 auth.accounts.account_id
  created_at TEXT NOT NULL
);
CREATE TABLE records (
  record_id INTEGER PRIMARY KEY,
  kind TEXT NOT NULL,
  source_id TEXT NOT NULL,
  day TEXT,                                 -- 上游提供的业务日
  start_at TEXT,
  end_at TEXT,
  observed_at TEXT,
  payload_json TEXT NOT NULL,               -- 完整原始单条记录
  first_seen_at TEXT NOT NULL,
  last_seen_at TEXT NOT NULL,
  UNIQUE (kind, source_id)
);
CREATE INDEX records_kind_day ON records(kind, day);
CREATE INDEX records_kind_observed ON records(kind, observed_at);
CREATE TABLE samples (
  sample_id INTEGER PRIMARY KEY,
  kind TEXT NOT NULL,                        -- heartrate / ring_battery_level
  timestamp_ms INTEGER NOT NULL,
  source TEXT,                               -- 心率来源；电量可为空
  payload_hash TEXT NOT NULL,                -- 规范化 JSON 的 SHA-256
  payload_json TEXT NOT NULL,
  first_seen_at TEXT NOT NULL,
  last_seen_at TEXT NOT NULL,
  UNIQUE (kind, timestamp_ms, payload_hash)
);
CREATE INDEX samples_kind_time ON samples(kind, timestamp_ms);
CREATE TABLE sync_runs (
  run_id TEXT PRIMARY KEY,
  mode TEXT NOT NULL CHECK (mode IN ('range', 'full')),
  requested_start TEXT NOT NULL,
  requested_end TEXT NOT NULL,
  started_at TEXT NOT NULL,
  finished_at TEXT,
  status TEXT NOT NULL CHECK (status IN ('running', 'succeeded', 'partial', 'failed'))
);
CREATE TABLE sync_items (
  run_id TEXT NOT NULL REFERENCES sync_runs(run_id) ON DELETE CASCADE,
  kind TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('pending', 'running', 'succeeded', 'failed', 'skipped')),
  records_received INTEGER NOT NULL DEFAULT 0,
  error_code TEXT,
  error_message TEXT,                        -- 脱敏，禁止令牌和健康数据
  started_at TEXT,
  finished_at TEXT,
  PRIMARY KEY (run_id, kind)
);
