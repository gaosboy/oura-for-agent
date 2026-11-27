# Data from Oura

[English](README.md) | [简体中文](README-zh.md)

通过 Oura API 维护本地健康数据，提供 CLI、脚本操作和可安装的 Skill。

## 设计与平台资料

- [设计文档索引](docs/design/README.md)。
- [Oura OpenAPI 快照](docs/openapi-1.43.json)、[导出文档](docs/oura-api/README.md)。
- [工程约束](AGENTS-zh.md)。

## 代码结构

- `core/action/operations/`：统一应用操作；`core/action/cli/` 负责命令行交互。
- `core/core/account/`、`core/core/record/`：账号授权与本地记录业务。
- `core/link/oura_v2/`：Oura API；本地 OAuth 回调由 `core/core/account/` 管理。
- `core/common/`：通用数据对象、存储、加密及超时工具；业务数据对象定义在各自的 Core 模块；`core/config/`：独立环境配置。
- `core/resource/migrations/`：认证库和记录库各自的初始 SQL。

## 初始化

需要 Python 3。初始化认证数据库：

```sh
python3 -m core.action
```

使用 `OURA_DATA_DIR` 配置数据目录，相对路径以项目根目录为基准；未配置时默认使用 `~/.local/share/data-from-oura/`。`--data-dir PATH` 优先于配置。重复运行不会清空数据。认证数据库初始化不需要登录或安装第三方依赖。

## 可选：连接 Oura 账号

登录 [Oura 开发者平台](https://developer.ouraring.com/applications) 查看已有应用的 client ID 和 client secret，或注册新应用。将应用的 Registered redirect URI 设置为 `http://localhost:8765/callback`，然后创建虚拟环境并安装依赖：

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 -m core.action --login
```

登录分为准备应用凭据、浏览器授权和保存账号三个步骤。输入应用的 client ID 和 client secret；也可分别通过 `OURA_CLIENT_ID`、`OURA_CLIENT_SECRET` 环境变量提供。终端会提示开发者平台链接，secret 输入时不显示。回调地址固定为 `http://localhost:8765/callback`，由程序自动配置并显示，无需输入；请在 Oura 应用后台登记相同地址。

程序先启动本机回调服务、展示授权 URL，再倒计时 3 秒尝试打开浏览器。如果 3 秒后没有自动打开，请将终端显示的 URL 复制到浏览器完成授权。倒计时不占用授权等待时间；打开浏览器后等待最多 60 秒，涵盖回调、令牌交换、个人信息读取和账号保存，终端每 2 秒显示剩余时间。超时后需重新运行登录命令。Oura 允许用户选择授权范围，账号识别需要个人信息访问权限。

回调页面收到有效授权后倒计时 3 秒尝试关闭；如果浏览器阻止自动关闭，可手动关闭标签页。终端确认账号保存成功后，回调服务倒计时 5 秒自动关闭，期间仍可响应回调请求。关闭倒计时中按 `Ctrl+C` 可提前退出，已保存的账号会保留。授权超时、失败或在授权中取消时会关闭服务。如果端口被其他程序占用，请先关闭该程序。

交互式终端使用青色步骤标题和链接、绿色成功提示、黄色提醒及红色错误提示；重定向输出时自动使用纯文本。设置 `NO_COLOR` 环境变量或使用 `TERM=dumb` 可关闭颜色。

## 环境配置

配置文件位于项目根目录。设置 `OURA_ENV=local|dev|test|prod` 选择对应的 `.env.<环境>`；未设置时依次选择存在的 `.env.local`、`.env.dev`、`.env.test`、`.env.prod` 中的第一个。只读取选中的环境及其私有覆盖文件，不合并其他环境；显式选择的环境文件不存在时会报错。系统环境变量 `OURA_CLIENT_ID`、`OURA_CLIENT_SECRET`、`OURA_DATA_DIR`、`OURA_LOG_LEVEL` 优先于文件中的值。文件采用每行 `KEY=value`，不使用引号或 shell 语法。旧配置中的 `OURA_REDIRECT_URI` 仍可被读取，但文件和环境变量中的值均不再生效，统一使用固定回调地址。

`.env.local` 和 `.env.dev` 不提交；`.env.test` 与 `.env.prod` 是可提交的非敏感配置模板。切勿将密钥写入后两者，通过系统环境变量注入。尚未配置的 client ID 和 client secret 会在登录时提示输入并保存到私有配置（local 使用 `.env.local`，其他环境使用 `.env.<环境>.local`），然后继续登录；固定回调地址须与 Oura 注册值完全一致。

令牌经 Fernet 加密后保存在认证库，密钥存放于系统密钥库；登录要求可用的安全 keyring 后端。备份和迁移数据时须同时安全保存密钥库密钥，否则无法恢复令牌。同步命令使用已保存的授权；当前尚未实现令牌自动刷新。

运行测试：`python3 -m unittest discover -s tests`。

账号记录库按 `account-<本地账号UUID>.sqlite3` 命名。保留已有数据库、原数据目录和系统密钥库密钥，不自动清理或重建私人数据。

## 同步和读取数据

通过统一操作接口调用。应用可保存多个授权，登录成功后激活该账号；可使用 `app.list_profiles()` 和 `app.activate_account(account_id)` 查看及切换。同步和读取只能访问当前激活账号：

```python
from core.action.operations import Application

app = Application()
account_id = app.current_profile()['account_id']
# 日期为 YYYY-MM-DD；按项目同步指定日期范围。
result = app.sync_range(account_id, '2026-01-01', '2026-01-31', ['daily_sleep', 'heartrate'])
# 或从指定日期到今天同步全部数据类型。
result = app.sync_full(account_id, '2026-01-01')
# 增量同步需要所选每个项目至少成功同步过一次；默认回查 7 天。
result = app.sync_incremental(account_id, kinds=['daily_sleep'])
# 读取本地数据；日期范围包含两端，结果至多 100 条。
rows = app.read_records(account_id, kinds=['daily_sleep'], start='2026-01-01', end='2026-01-31', limit=100)
```

日期范围超过 21 天时，程序按最多 21 天拆分并串行请求，每个窗口的分页完成后再请求下一窗口。同步结果含每个项目的状态和记录数量；部分项目无权限或失败时，整体状态为 `partial` 或 `failed`。日历数据以 Oura 返回的业务日期过滤；心率和电量的日期范围按 UTC 计算，个人资料和设备配置没有业务日期，不应使用日期筛选。相同记录 ID 以远端数据更新；无 ID 的心率和电量样本按时间戳替换同时间远端返回的样本。未返回的记录不会推断为已删除。增量同步按上次成功窗口回查，不保证发现更早日期发生的修改或删除。令牌过期时需要重新授权；自动刷新尚未实现。

## 命令行同步与读取

```sh
python3 -m core.action profile
python3 -m core.action sync range --start 2026-01-01 --end 2026-01-31 --types daily_sleep heartrate
python3 -m core.action sync full --start 2026-01-01
python3 -m core.action sync incremental --types daily_sleep heartrate
python3 -m core.action read --types daily_sleep --start 2026-01-01 --end 2026-01-31 --limit 10
```

命令使用当前激活账号，读取结果包含健康数据，请勿公开分享。同步日志等级由 `OURA_LOG_LEVEL` 设置，支持 DEBUG、INFO、WARNING、ERROR、CRITICAL；未配置时为 DEBUG。窗口和分页进度为 DEBUG，输出到标准错误；JSON 结果仍写入标准输出。增量同步需要各所选项目有成功的历史同步。同步返回 JSON；部分失败或全部失败时退出码为 1。

## 本地运动趋势报告

```sh
python3 -m core.action report activity-trend --start 2026-10-01 --end 2026-10-31
# 同步新数据后，强制重新生成同一份报告
python3 -m core.action report activity-trend --start 2026-10-01 --end 2026-10-31 --force
```

报告使用当前账号已同步的 `daily_activity` 和 `workout`，不会自动同步。文件保存在数据库目录的同级 `reports/`（例如数据目录为项目内的 `data/` 时，报告位于项目内的 `reports/`），是可离线打开的 HTML；命令返回路径和缓存状态。相同账号、日期和模板默认复用旧文件，数据或模板变化后需使用 `--force`。报告包含个人健康数据，请妥善保管。

## 构建及安装 Skill

Skill 打包脚本、配置和安装脚本统一存放在 `ops/skill/`。指令模板为 `ops/skill/SKILL.md.template`，构建时输出标准的 `SKILL.md`。打包配置独立保存在 `ops/skill/build.json`，使用 `MAJOR.MINOR.PATCH` 版本。运行 `python3 ops/skill/build_skill.py` 在 `build/` 生成 Skill 目录和版本化 ZIP；`python3 ops/skill/build_skill.py --check-version` 比较配置与该目录中已有的版本，低于已有版本时退出码为 1。同版本重建需要 `--force`，包含本地虚拟环境或配置的输出目录不会被覆盖。发布新版本前修改配置版本。输出位置可通过 `--output PATH` 指定。

将 ZIP 中的 `data-from-oura` 目录完整解压到对应 Skill 目录：Codex 为 `~/.codex/skills/`，Claude Code 为 `~/.claude/skills/`，Hermes 为 `~/.hermes/skills/`，OpenClaw 为 `~/.openclaw/skills/`。重新启动会话以加载。首次使用由 Skill 引导运行 `python3 scripts/setup.py`；登录需要用户在终端交互并完成浏览器授权。升级前备份已安装 Skill 中的 `.env.local`，升级后恢复该文件并重新运行初始化；数据库及系统密钥库也必须保留。不要将本地配置或数据库打包发布。
