---
name: data-from-oura
description: Connect an Oura account, synchronize authorized Oura health data, read local records, and generate activity trend reports. Use when the user asks to work with their Oura data.
---

# Data from Oura

Run commands from this Skill's directory. At first use, run `python3 scripts/setup.py`; it creates a virtual environment, installs dependencies, and initializes the local authentication database. It is safe to rerun. The script needs Python 3 with `venv`, pip, and network access for dependency installation. If the host cannot run commands automatically or has no interactive terminal, give the user the exact command and ask them to run it in a terminal, then continue after they report the result. For installation errors, show the error and guide the user to fix the missing prerequisite and rerun setup.

All application commands below use `python3 scripts/run.py` followed by the arguments shown. The runner invokes setup when needed and then the application CLI. For interactive commands, use a terminal attached to the user; never request or reproduce client secrets in chat.

- Initialize only: `python3 scripts/run.py`
- Authorize or reauthorize: `python3 scripts/run.py --login`. The terminal directs the user to https://developer.ouraring.com/applications to view their client ID and client secret or register a new application. The application automatically uses the fixed redirect URI `http://localhost:8765/callback` and displays it; the user must register this exact URI in their Oura application settings and enter only the requested credentials in the terminal. The terminal displays the authorization URL and counts down 3 seconds before trying to open the browser; if it does not open, the user should open that URL manually. Login allows 60 seconds after the browser-opening attempt and requires personal information authorization to identify the account. A working system keyring is required. The callback page counts down 3 seconds after a valid callback and tries to close; if the browser blocks this, close the tab manually. After the terminal confirms the account is saved, the callback service stays responsive during a 5-second countdown, then closes automatically. Ctrl+C during this countdown exits early and keeps the saved account. Timeout, failure, or cancellation during authorization closes the service; retry the login command as needed. Interactive terminal output uses color; redirected output and NO_COLOR use plain text.
- Active account: `python3 scripts/run.py profile`
- Initial history: `python3 scripts/run.py sync full --start YYYY-MM-DD [--end YYYY-MM-DD]`
- Selected types: `python3 scripts/run.py sync range --start YYYY-MM-DD --end YYYY-MM-DD --types daily_sleep heartrate`
- Incremental update: `python3 scripts/run.py sync incremental [--end YYYY-MM-DD] [--types daily_sleep heartrate] [--overlap-days 7]`. Each selected type requires an earlier successful sync.
- Local records: `python3 scripts/run.py read [--types daily_sleep] [--start YYYY-MM-DD] [--end YYYY-MM-DD] [--source-id ID] [--limit 100]`
- Local report: `python3 scripts/run.py report activity-trend --start YYYY-MM-DD --end YYYY-MM-DD [--force]`. It uses already synchronized `daily_activity` and `workout` data.

Use `python3 scripts/run.py --help` and the subcommand `--help` for complete options. Dates are inclusive. Available types: `daily_activity`, `daily_cardiovascular_age`, `daily_readiness`, `daily_resilience`, `daily_sleep`, `daily_spo2`, `daily_stress`, `enhanced_tag`, `rest_mode_period`, `session`, `sleep`, `sleep_time`, `tag`, `vO2_max`, `workout`, `heartrate`, `ring_battery_level`, `personal_info`, `ring_configuration`. Availability depends on authorization and Oura. Synchronization may partially fail; check its JSON status and exit code. Incremental sync does not guarantee detection of older changes or deletions. Expired tokens require reauthorization.

Data defaults to `~/.local/share/data-from-oura/`; set `OURA_DATA_DIR` or pass the global `--data-dir PATH` before a subcommand to choose another location. Credentials entered at login are saved in the Skill's private local configuration, while encrypted tokens are stored in the database and their encryption key in the system keyring. Keep these and generated reports private. Do not expose health records or credentials in messages unless the user requests the relevant output.
