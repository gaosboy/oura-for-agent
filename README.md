# Data from Oura

[English](README.md) | [简体中文](README-zh.md)

Manage local health data through the Oura API, with a CLI, a Python application interface, and an installable Skill.

## Design and API references

- [Design index](docs/design/README.md).
- [Oura OpenAPI snapshot](docs/openapi-1.43.json) and [generated API documentation](docs/oura-api/README.md).
- [Repository guidelines](AGENTS.md).

## Code structure

- `core/action/operations/`: shared application operations; `core/action/cli/` handles command-line interaction.
- `core/core/account/` and `core/core/record/`: account authorization and local record management.
- `core/link/oura_v2/`: Oura API integration. The local OAuth callback is managed by `core/core/account/`.
- `core/common/`: shared data objects, storage, encryption, and timeout utilities. Domain data objects live in their respective Core modules. `core/config/` handles environment configuration separately.
- `core/resource/migrations/`: initial SQL migrations for the authentication and record databases.

## Initialize

Python 3 is required. Initialize the authentication database:

```sh
python3 -m core.action
```

Set `OURA_DATA_DIR` to choose the data directory. Relative paths resolve from the project root; the default is `~/.local/share/data-from-oura/`. The `--data-dir PATH` option overrides configuration. Repeated initialization does not erase data. Initializing the authentication database requires neither login nor third-party dependencies.

## Optional: connect an Oura account

Visit the [Oura developer portal](https://developer.ouraring.com/applications) to find an existing application's client ID and client secret, or register a new application. Set its Registered redirect URI to `http://localhost:8765/callback`, then create a virtual environment and install dependencies:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 -m core.action --login
```

Login has three steps: prepare application credentials, authorize in the browser, and save the account. Enter the application's client ID and client secret, or provide them through `OURA_CLIENT_ID` and `OURA_CLIENT_SECRET`. The terminal displays the developer portal link and hides secret input. The callback URI is fixed at `http://localhost:8765/callback`; the application configures and displays it automatically. Register that exact URI in the Oura application settings.

The application starts a local callback server, displays the authorization URL, and waits three seconds before attempting to open the browser. If the browser does not open, copy the displayed URL into it. This countdown does not consume the authorization timeout. After the browser-opening attempt, you have up to 60 seconds for the callback, token exchange, personal information request, and account save. The terminal displays the remaining time every two seconds. Run the login command again if it times out. Oura lets users select authorization scopes; identifying an account requires access to personal information.

After a valid callback, the callback page waits three seconds and attempts to close. Close the tab manually if the browser blocks this. Once the terminal confirms the account is saved, the callback server remains responsive for another five seconds before shutting down. Pressing `Ctrl+C` during this final countdown exits early and keeps the saved account. Authorization timeout, failure, or cancellation also closes the server. If another application is using the callback port, close it first.

Interactive terminals use cyan headings and links, green success messages, yellow notices, and red errors. Redirected output uses plain text. Set `NO_COLOR` or use `TERM=dumb` to disable colors.

## Environment configuration

Configuration files live in the project root. Set `OURA_ENV=local|dev|test|prod` to select `.env.<environment>`. Without an explicit selection, the application uses the first existing file in this order: `.env.local`, `.env.dev`, `.env.test`, `.env.prod`. It reads only the selected environment and its private overrides; it does not merge other environments. Explicitly selecting a missing environment file is an error. The process environment variables `OURA_CLIENT_ID`, `OURA_CLIENT_SECRET`, `OURA_DATA_DIR`, and `OURA_LOG_LEVEL` override file values. Files use one `KEY=value` entry per line, without quotes or shell syntax. Legacy `OURA_REDIRECT_URI` entries can still be read, but values from files or environment variables no longer override the fixed callback URI.

Do not commit `.env.local` or `.env.dev`. The tracked `.env.test` and `.env.prod` files are non-sensitive templates; never put secrets in them. Inject secrets through process environment variables instead. Login prompts for missing client credentials and saves them to private configuration: `.env.local` for the local environment, or `.env.<environment>.local` for other environments. Login then continues. The fixed callback URI must exactly match the one registered with Oura.

Tokens are encrypted with Fernet and stored in the authentication database. The encryption key is stored in the system keyring; login requires a working secure keyring backend. Back up the keyring key securely when backing up or migrating data, since tokens cannot be recovered without it. Synchronization uses the saved authorization. Automatic token refresh is not implemented yet.

Run tests with `python3 -m unittest discover -s tests`.

Each account's record database is named `account-<local-account-UUID>.sqlite3`. Preserve existing databases, data directories, and system keyring keys. Private data is not automatically cleared or rebuilt.

## Synchronize and read data

Use the shared application interface. The application can store multiple authorizations and activates an account after a successful login. Use `app.list_profiles()` and `app.activate_account(account_id)` to list and switch accounts. Synchronization and reads can access only the active account:

```python
from core.action.operations import Application

app = Application()
account_id = app.current_profile()['account_id']
# Dates use YYYY-MM-DD. Synchronize selected types for a date range.
result = app.sync_range(account_id, '2026-01-01', '2026-01-31', ['daily_sleep', 'heartrate'])
# Or synchronize all data types from a start date through today.
result = app.sync_full(account_id, '2026-01-01')
# Incremental sync requires a successful earlier sync for every selected type.
# The default overlap is seven days.
result = app.sync_incremental(account_id, kinds=['daily_sleep'])
# Read local records. Both date bounds are inclusive; return at most 100 rows.
rows = app.read_records(account_id, kinds=['daily_sleep'], start='2026-01-01', end='2026-01-31', limit=100)
```

Ranges longer than 21 days are split into windows of at most 21 days and requested sequentially. Pagination completes for one window before the next begins. Results include each data type's status and record count. Missing permissions or failures produce an overall `partial` or `failed` status. Calendar data is filtered by the business date returned by Oura. Heart rate and battery date ranges use UTC. Personal information and device configuration have no business date and should not use date filters.

Records with the same ID are updated from the remote response. Heart rate and battery samples without IDs replace existing samples at the same timestamp. Missing records are not inferred to have been deleted. Incremental sync overlaps the last successful window; it does not guarantee detection of older changes or deletions. Expired tokens require reauthorization because automatic refresh is not implemented.

## CLI synchronization and reads

```sh
python3 -m core.action profile
python3 -m core.action sync range --start 2026-01-01 --end 2026-01-31 --types daily_sleep heartrate
python3 -m core.action sync full --start 2026-01-01
python3 -m core.action sync incremental --types daily_sleep heartrate
python3 -m core.action read --types daily_sleep --start 2026-01-01 --end 2026-01-31 --limit 10
```

Commands use the active account. Read results contain health data and should not be shared publicly. Set `OURA_LOG_LEVEL` to `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`; the fallback is `DEBUG` when no level is configured. Window and pagination progress is logged at `DEBUG` to standard error, while JSON results go to standard output. Incremental sync requires a successful earlier sync for every selected type. Synchronization returns JSON and exits with status 1 on partial or complete failure.

## Local activity trend reports

```sh
python3 -m core.action report activity-trend --start 2026-10-01 --end 2026-10-31
# Regenerate the same report after synchronizing new data.
python3 -m core.action report activity-trend --start 2026-10-01 --end 2026-10-31 --force
```

Reports use the active account's previously synchronized `daily_activity` and `workout` records; they do not trigger synchronization. Reports are standalone HTML files that work offline, stored in a `reports/` directory alongside the database directory. For example, a project-local `data/` directory produces reports in the project's `reports/` directory. The command returns the path and cache status. Requests for the same account, dates, and template reuse the existing report by default. Use `--force` after data or template changes. Reports contain personal health data; keep them private.

## Build and install the Skill

Skill build scripts, configuration, and installation scripts live in `ops/skill/`. The instruction template is `ops/skill/SKILL.md.template`; the builder outputs it as `SKILL.md`. The separate build configuration, `ops/skill/build.json`, uses `MAJOR.MINOR.PATCH` versions.

Run `python3 ops/skill/build_skill.py` to create a Skill directory and a versioned ZIP in `build/`. Run `python3 ops/skill/build_skill.py --check-version` to compare the configured version with existing local artifacts; it exits with status 1 if the configured version is older. Rebuilding an existing version requires `--force`. The builder will not overwrite an output directory containing a local virtual environment or private configuration. Update the configured version before releasing a new version. Use `--output PATH` to select another output directory.

Extract the complete `data-from-oura` directory from the ZIP into your tool's Skill directory: `~/.codex/skills/` for Codex, `~/.claude/skills/` for Claude Code, `~/.hermes/skills/` for Hermes, or `~/.openclaw/skills/` for OpenClaw. Restart the session to load it. On first use, the Skill guides you through `python3 scripts/setup.py`. Login requires an interactive terminal and browser authorization. Before upgrading, back up the installed Skill's `.env.local`, restore it afterward, and rerun initialization. Preserve the databases and system keyring keys as well. Never include local configuration or databases in a release package.
