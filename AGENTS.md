# Repository Guidelines

[English](AGENTS.md) | [简体中文](AGENTS-zh.md)

Keep `README.md`, `AGENTS.md`, and their corresponding `-zh.md` files synchronized when updating them, so both languages describe the same behavior and engineering requirements.

## Product goal and references

Data from Oura is an application for agents. It retrieves and maintains health data accessible through the Oura API, stores it in local databases, and makes it available for analysis and application calls. The goal is to cover all available data types; actual access depends on user authorization, API capabilities, and platform restrictions.

`docs/` contains Oura API documentation. The online reference is https://cloud.ouraring.com/v2/docs. Consult the documentation when implementing interfaces and check the official online reference when current platform requirements need confirmation. Application code lives in `core/`: within that package, `link/oura_v2/` integrates with Oura, `core/account/` and `core/record/` handle domain logic, `action/operations/` exposes shared operations, and `action/cli/` provides the CLI. Configuration is isolated in `config/`. Tests live in `tests/`.

## Architecture and module organization

Consult the [design index](docs/design/README.md), [engineering design](docs/design/02-oura-core/project-architecture.md), and [database design](docs/design/02-oura-core/database-schema.md). See the [README](README.md) for implemented behavior.

Keep responsibilities separate. These layers may evolve, but their boundaries must remain clear:

- **Link** encapsulates the Oura API, OAuth authorization and validation, requests, pagination, errors, and synchronization protocols. It isolates platform details.
- **Core** handles local data models, persistence, and domain logic for processing and analyzing data, independently of application entry points.
- **Action** provides reusable operations for scripts, Skills, and other callers. CLI and Web entry points may call only `action/operations/`; the operation layer calls Core. Avoid duplicating domain logic.

Design local models independently of Oura response structures. Document mappings between external data and local models, including field semantics, without silently losing data. Organize new code, tests, and resources by responsibility, and document dependency direction and directory purposes.

## Synchronization and data protection

Plan for initial historical imports and incremental updates. Handle pagination, duplicate events, updates, deletions, retries, and synchronization progress; consider webhooks where supported. Respect authorization scopes, user consent, and rate limits. Handle token expiration and revocation explicitly. Never put real health data, OAuth tokens, or client secrets in the repository, logs, or test fixtures. Use synthetic data, mock services, and temporary directories. Actual data access, retention, and deletion must match the privacy policy.

## Supporting pages

Maintain a product introduction, privacy policy, terms of service, and other platform-required pages alongside the application. Their content must accurately describe data uses, retention, sharing, and user rights. Verify platform requirements and legal text before publication; do not treat placeholder content as final policy.

## Development and verification

Skill build resources live in `ops/skill/`: `build_skill.py` is the build entry point, `build.json` contains version configuration, `SKILL.md.template` is the instruction template, and `scripts/` contains the installation and runner scripts distributed with the Skill. Run `python3 ops/skill/build_skill.py --output /tmp/oura-skill-build` to verify packaging. The packaged instruction file must still be named `SKILL.md`.

Run commands from the repository root. Version control contains only source code, documentation, tests, development tools, and non-sensitive configuration templates. Do not commit private configuration, dependency environments, databases, reports, or build artifacts. Before cleaning project-local runtime state, move it to a private backup directory outside the repository and verify its integrity. Preserve system keyring keys; never rebuild or clear private data for testing. Dependencies are listed in `requirements.txt`; use a separate environment when a new one is needed.

```sh
python3 -m unittest discover -s tests
python3 -m core.action --help
python3 -m json.tool docs/openapi-1.43.json > /dev/null
```

Tests use only synthetic data, platform substitutes, and temporary directories. Real Oura authorization or synchronization requires separate user authorization. Automatic token refresh is not implemented. See the usage documentation for pagination, incremental overlap, and deletion limits.

Use `python3 -m core.action` to initialize the authentication database. The optional `--login` flag authorizes an account; login requires dependencies installed with `pip install -r requirements.txt`. Use `python3 scripts/export_openapi.py` to export the specification into `docs/oura-api/`. Run `python3 -m unittest discover -s tests` to verify the application, Skill builder, and export script.

When changing the API specification, check JSON syntax and, when an OpenAPI 3.1 validator is available, validate semantics and references. Preserve the specification's two-space indentation and existing names; avoid unrelated whole-file formatting. Add appropriate tests for new code, covering mappings, authorization, synchronization, and error handling. Record actual installation, execution, and test commands here.

Login displays an authorization URL, waits three seconds before attempting to open the browser, and then allows 60 seconds for authorization and account saving. If the browser does not open, the user can visit the URL manually. After a valid callback, the callback page waits three seconds and tries to close. After the account is saved, the callback server remains responsive during a five-second shutdown countdown. Interactive terminals support colors; redirected output and `NO_COLOR` use plain text. Run `python3 -m unittest discover -s tests` to verify authorization timeouts, callback availability, shutdown countdowns, interactive guidance, color compatibility, and other regressions.

## Commits and reviews

The project uses Git. Unless the user explicitly requests otherwise, validate and commit every independent, complete change—including code, documentation, and configuration—to local Git before ending the task. Routine local commits do not require repeated confirmation. Verify and commit each independently verifiable logical change as soon as it is complete, rather than waiting until the end of a multi-stage task. This also applies to architecture designs, plans, and documentation. Before finishing, check Git status and ensure all non-ignored changes made for the task are committed. Explain anything that cannot be committed. Group commits by logical change; a commit is not required for every file save.

- Check `git status` and existing diffs before starting. Distinguish task changes from pre-existing uncommitted work.
- Review working-tree and staged diffs before committing. Stage only files or hunks belonging to the task. Do not include, overwrite, or discard unrelated existing changes.
- Never commit real health data, tokens, keys, local databases, or generated private reports. Track environment files only after confirming that they are non-sensitive templates.
- Report commit IDs, verification results, and any related uncommitted work when finished. If committing is blocked, explain why and preserve the working state. A local commit does not imply a push; push or publish only as authorized by the user.

Use short imperative commit messages, such as `Add Oura sync client`. Pull requests should describe the purpose, affected data types or interfaces, verification results, and related issues. Include screenshots for UI changes. For model or synchronization changes, explain compatibility and migration impacts.
