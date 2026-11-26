# 本地数据库表结构设计

本设计替代首期设计中“令牌按账号存放于文件”的约定：所有账号的授权信息统一放在 `auth.sqlite3`；每个账号的数据放在按 `account-<account_id>.sqlite3` 命名的独立 SQLite 文件；开发阶段旧版数据库需重新初始化。本文是设计稿，不代表数据库已实现。

## 共同约定

所有连接启用 `PRAGMA foreign_keys = ON`；`schema_migrations` 记录已应用的迁移版本。时间以带 `Z` 的 UTC ISO 8601 文本保存，日历日期以 `YYYY-MM-DD` 保存；上游日期保留原本语义，不推断时区。JSON 列保存有效 JSON 文本；数据库文件和目录应仅限本机用户访问。SQLite 默认不加密，文件权限不能替代加密：令牌应由操作系统密钥库提供的密钥加密后写入，密钥不存入 SQLite。

## 授权数据库 `auth.sqlite3`

```sql
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
```

OAuth 的 state 和授权码是短期数据，仅保存在正在执行的授权会话内，不持久化。客户端 ID 和密钥通过配置或系统密钥库提供，不保存于表中。刷新令牌时原子更新凭据；撤销或失效时保留账号与健康库，要求重新授权。令牌字段不得出现在日志或同步错误中。

## 每账号数据库

```sql
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
```

`records` 覆盖 personal_info、ring_configuration、daily_activity、daily_cardiovascular_age、daily_readiness、daily_resilience、daily_sleep、daily_spo2、daily_stress、enhanced_tag、rest_mode_period、session、sleep、sleep_time、tag、vO2_max 和 workout；`source_id` 使用对应对象的 `id`。个人信息是单条快照；设备配置按记录 ID 保存。webhook 订阅属于应用配置，不归入用户健康数据。

`samples` 保留同一时间的不同内容并去重完全相同的采样。上游未在规范中承诺采样唯一键，因此更正值会作为新样本保留；后续分析不得假设同时间只有一条。`payload_hash` 使用确定性 JSON 序列化（排序键、UTF-8、紧凑分隔符）的 SHA-256；这只能去除内容完全相同的重叠采样，不能识别更正或删除。

## 同步及一致性

每页写入独立事务，记录以 `(kind, source_id)` 更新，保留 `first_seen_at` 并更新 `last_seen_at`；采样按上述唯一键去重。分页完成后才将该类型标记成功。中途中断标记失败或在下次启动时识别遗留的 running 状态；重新执行整个区间，依靠幂等写入恢复。`next_token` 不作为跨运行的持久检查点。失败项及权限不足不得被记作成功；缺失记录不推断为删除。

`auth` 和账号数据库不共享事务：先创建账号库和 identity，再写入 auth 记录；失败时清理新建的孤儿文件，启动时核验 identity 与 auth 的映射，不匹配则停止操作。删除账号时须显式处理两个数据库及密钥材料，不能依赖跨库外键。

## 待验证边界

以上表结构以当前仓库规范为依据。授权作用域和刷新令牌行为、Oura 数据访问限制、采样重复与修订语义需在实现和真实联调时核实。完整 JSON 是保真存档，类型专属的分析字段与派生表应在明确查询需求后通过迁移增加，不应将上游字段的缺失与空值混为一谈。
