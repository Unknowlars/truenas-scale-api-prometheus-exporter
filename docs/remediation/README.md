# Remediation Program — TrueNAS SCALE API Prometheus Exporter

This folder is the complete working package for fixing the findings of the 2026-07 deep code
review ([review-report.md](review-report.md)). It is written for an AI agent (or human) that
starts with **zero context**. Read this file fully before touching any code.

## How this folder is organized

| File | Purpose |
|---|---|
| `README.md` (this file) | Context, architecture primer, hard rules, workflow, verification standards |
| `TASKS.md` | The task board. Single source of truth for status. Update it every session. |
| `review-report.md` | The full review with evidence (`file:line`, API doc references). Read the sections your task cites — not the whole thing. |
| `tasks/T##-*.md` | One self-contained spec per fix. Each is designed to be completed in **one session** without reading anything beyond what it lists. |

## Operating protocol (read carefully)

1. **One task per session.** Pick the highest-priority `todo` task from `TASKS.md` unless told
   otherwise. Never work on two tasks at once; never "drive-by fix" something you notice in
   another task's territory — instead add a note to that task's file or to `TASKS.md`.
2. **Set status before you start.** Edit `TASKS.md`: status → `in-progress`, add the date.
3. **Read only what the task file lists.** Each task names the exact source files, line regions,
   doc files, and tests you need. `runtime.py` is 5,100 lines — read the listed regions, not the
   whole file.
4. **Finish or mark blocked.** When done: status → `done`, fill in the task file's **Outcome**
   section (what changed, files touched, tests added, anything a follow-up should know). If you
   cannot finish: status → `blocked` with a one-line reason in `TASKS.md` and details in the task
   file. Never leave a task `in-progress` at session end.
5. **One commit per task** on the current branch, message format:
   `T##: <imperative summary>` (e.g. `T03: stop reporting DDT bytes as pool dedup ratio`).
   Do not push unless explicitly asked.
6. **If a task turns out to be wrong** (the code changed, the premise doesn't hold), do not force
   it. Verify against the current code, mark the task `done` with outcome "no change needed:
   <reason>" or `blocked`, and say why.

## Architecture primer (5 minutes)

- **What it is:** a threaded (not asyncio) Python exporter. It talks JSON-RPC 2.0 over WebSocket
  to TrueNAS middleware and serves Prometheus metrics on `:9108`.
- **Modules** (`src/truenas_exporter/`):
  - `runtime.py` (~5,100 lines) — the `TrueNASExporter` class: `scrape_once()` polls ~120 API
    methods per cycle inside `self._lock`; `_event_stream_loop()` runs in a daemon thread and
    subscribes to push events (`reporting.realtime`, `app.stats`, instance metrics).
  - `metrics.py` — all metric declarations via `declare_gauge`/`declare_counter`, collected into
    `METRIC_SPECS` (this list *is* the public contract).
  - `events.py` — which metrics are owned by which event stream (`_EVENT_METRICS`,
    `_REALTIME_EVENT_SCALAR_METRICS`).
  - `collection.py` — pure parsers (`_as_float`, `_as_optional_bool`, `_as_percent`, `_parse_ts`, …).
  - `transport.py` — `JsonRpcWsClient`: bounded synchronous WebSocket JSON-RPC client.
  - `method_safety.py` + `api_catalog.py` — documentation-derived allowlists. **A method may only
    be called if the active compatibility profile allows it.**
  - `compat_profiles.py` — 25.10 / 26.0 / unknown profiles selected at runtime from
    `system.version_short`.
  - `config.py` — env-var config. `http.py` — WSGI server (`/metrics`, `/healthz`, `/readyz`).
- **Two modes** (`EXPORTER_MODE`): `collector` (default) — `/metrics` serves an immutable snapshot
  republished at the end of each poll cycle; `legacy` — `/metrics` reads the live registry under
  the scrape lock.
- **Ground truth for API shapes:** `docs/truenas-api/methods|events/` (25.10.2) and
  `docs/truenas-api-v26/` (26.0.0), plus captured fixtures in `tests/fixtures/`. When docs and a
  live-capture fixture disagree, the fixture wins (this has happened: `vm.get_available_memory`
  is documented as MB but returns bytes; see `compat_profiles.py:108-119`).

## Hard rules (violating any of these fails review)

1. **Zero-vs-absent policy — never fabricate values.** A metric is set only from a successfully
   parsed, documented field. If the API returns null / omits the key / the call fails, the metric
   must be *absent* (labeled series removed, scalar gauge NaN) — never a synthesized `0` and never
   a stale value beyond its declared freshness window. Several tasks exist precisely to restore
   this invariant.
2. **Metric contract compatibility** (`docs/VERSIONING.md`): metric names, types, HELP, and labels
   are public contracts. A corrected replacement metric must keep the old metric as a
   compatibility alias for at least one release, with the migration documented. You may fix a
   *wrong* HELP string; you may not silently rename or retype a metric.
3. **Method safety:** every remote call must go through `self._call()` /
   `self._safe_call_auto()` / `self._query_count()` and be permitted by the active
   `CompatibilityProfile`. Adding a new API call means the method must exist in
   `api_catalog.py`'s allowlists (and the profile sets in `compat_profiles.py` if
   version-specific). Never call a method that can return secrets/PII without a `select` that
   excludes them; when in doubt check `SENSITIVE_READ_METHODS`.
4. **Security invariants:** the API key must never appear in logs, exceptions, or metric labels.
   The code intends that the TrueNAS hostname never appears in logs either (see `runtime.py`
   `main()`); don't add log lines that leak it. No usernames, IPs, serial numbers, or session
   details as label values.
5. **Cardinality:** no unbounded label values. New labels must come from bounded sets (pool
   names, task IDs, enum states). No UUIDs that change over time, no snapshot names, no client
   addresses.
6. **Generated artifacts must be regenerated, never hand-edited:**
   - `docs/metrics-contract.json` ← `python3 scripts/generate_metric_contract.py`
   - `docs/api-exporter-parity*.{md,json}` + compat-diff ← `python3 scripts/generate_api_exporter_parity.py`
   - Grafana dashboard ← `python3 scripts/generate_truenas_dashboard.py`
   - `validate.sh` runs all of these with `--check`; if you change any metric declaration or
     producer, run the generators (without `--check`) and commit their output.
   - Note: `scripts/generate_api_exporter_parity.py` contains **hand-maintained mapping tables**
     (`_metric_source_overrides`, `owned_response_fields`, and per-metric "unavailable" notes).
     If your task changes a metric's source or brings a dead metric to life, you must update those
     tables so the regenerated parity report tells the truth.
7. **No hosted CI:** `validate.sh` fails if `.github/workflows` exists. Don't create workflows.
8. **Line endings:** repo enforces LF via `.gitattributes`.
9. **Coverage gate:** pytest runs with `--cov-fail-under=85` (branch). New code paths need tests.
10. **Don't expand scope.** If a fix reveals an adjacent problem, write it down (TASKS.md
    "Discovered" section) and move on.

## Verification standard (every task, in this order)

There is **no live TrueNAS** in the dev environment. Verification is: unit tests against
fixtures + the full validation suite. If `TRUENAS_WS_URL`/`TRUENAS_API_KEY` env vars are present
you may additionally run `python3 scripts/live_smoke.py`, but never require it.

1. **Targeted tests first** — run the specific test files your task names:
   `python3 -m pytest tests/test_xyz.py -q`
2. **Write the regression test before or with the fix.** Every behavioral fix needs a test that
   fails on the old code. Fixture-driven tests live in `tests/` with API payloads either inline
   or in `tests/fixtures/`. Follow existing patterns (`RecordingClient` fakes,
   `make_config(...)` from `conftest.py`, direct calls to `exporter._dispatch_event(...)` /
   `exporter.scrape_once()` with a fake client).
3. **Regenerate artifacts** if metrics/producers changed (see rule 6).
4. **Full gate:** `./scripts/validate.sh` must exit 0. It includes ruff, mypy, pytest+coverage,
   all `--check` generators, dashboard validation, and a docker build. Budget ~3–5 minutes.
5. **Behavioral spot-check where feasible:** for metric changes, add/extend a test that renders
   the registry (`prometheus_client.generate_latest()` or `REGISTRY.collect()`) and asserts the
   exact sample names/labels/values — this catches wrong HELP/type/name drift that unit logic
   tests miss.

## Beware: tests that cement bugs

Some existing tests assert the *buggy* behavior on purpose-at-the-time. Your task file will name
them. Changing such a test is expected and correct **when the task says so** — update the
assertion to the new required behavior and keep the test.

Known examples: `tests/test_reliability.py:22-24` (CPU user% = total fallback),
`tests/test_runtime_api_parity.py:106` (dedup bytes into the ratio metric).

## Versioning

Per `docs/VERSIONING.md`: behavior fixes = patch bump, new metrics/collectors/config = minor bump.
`src/truenas_exporter/version.py` is the single source. **Do not bump the version per task** —
the maintainer bumps once per release batch. Note in TASKS.md if your change is minor-worthy
(new metric/config) vs patch-worthy.

## Task priority model

- **P1** — wrong values being served or silent data loss today. Do these first, in order.
- **P2** — reliability/correctness hardening and high-value missing metrics.
- **P3** — performance, conventions, cleanup. Safe to defer.

Dependencies are listed per task; the board groups them. When in doubt, lower task number first.
