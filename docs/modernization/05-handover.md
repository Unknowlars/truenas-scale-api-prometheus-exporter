# Phase 5: Midway Review Findings and Handover

Written 2026-07-12 after a multi-angle midway code review of the uncommitted
modernization working tree (monolith → `src/truenas_exporter/` package).
This document is the entry point for the next agent: fix the findings below,
then finish Phase 2 per [02-architecture.md](02-architecture.md).

## State at handover

- The entire modernization is **uncommitted** working-tree state on `main`.
  Commit a checkpoint before further changes.
- Phases 1, 3, 4 are complete; Phase 2 is in progress. The remaining
  Phase 2 work and its recommended order are in
  [02-architecture.md](02-architecture.md) ("Remaining work queue").
- Review verdict on locked decisions: **metric contract fully preserved**
  (382 metric/label tuples identical to HEAD; only 3 additive counters),
  no CI files, MIT license, dry-run release, and read-only live-smoke rules
  all honored.
- `./scripts/validate.sh` is the single verification gate. Coverage is 48%
  (target 85%, gated at 48% in validate.sh; raise the gate as coverage rises).

## Verified review findings (fix in this order)

Verification legend: CONFIRMED = trigger and mechanism proven from code;
PLAUSIBLE = mechanism real, trigger depends on environment.

- [ ] 1. **CONFIRMED — collector mode runs the full API scrape inside every
  `/metrics` GET on a single-threaded server.**
  `src/truenas_exporter/runtime.py:6344` (`FullParityCollector.collect` →
  `scrape_once`, up to `SCRAPE_BUDGET_SECONDS=25`s) served by wsgiref
  `make_server` (`runtime.py:6410`, non-threading). A queued `/healthz`
  (Dockerfile HEALTHCHECK, 3s HTTP timeout, 3 retries) times out during slow
  scrapes → container marked unhealthy. Fix is the Phase 2 atomic-snapshot
  task: background scrape loop + snapshot exposition (see 02-architecture.md);
  do not band-aid with a threaded server alone (that would resurrect the
  torn-read risk the single thread currently prevents).
- [ ] 2. **CONFIRMED — `truenas_interface_link_up` is constant 0.**
  `runtime.py:4488`: `_as_bool(candidate.get("link_state") or ...)` —
  TrueNAS returns `LINK_STATE_UP`/`LINK_STATE_DOWN` (middleware
  `netif.InterfaceLinkState`), which `_as_bool` (`runtime.py:686`) maps to
  False; the truthy string also short-circuits the or-chain so fallbacks
  never run. Pre-existing in HEAD, still wrong. Map `LINK_STATE_*` explicitly
  and add a fixture test with the real enum values.
- [ ] 3. **CONFIRMED — `docker-compose.yml` does not forward `EXPORTER_MODE`,
  `ENABLE_GENERIC_METHOD_METRICS`, `ENABLE_GENERIC_EVENT_METRICS`,
  `DATASET_SNAPSHOT_FALLBACK_LIMIT`.** The `environment:` block forwards ~30
  documented vars via `${VAR:-default}` but omits exactly these four, so
  `EXPORTER_MODE=collector docker compose up` silently runs legacy mode.
  Add the four entries; consider a test that diffs `.env.example` keys
  against the compose `environment:` keys.
- [ ] 4. **CONFIRMED — `scripts/live_smoke.py` cannot run from a fresh
  checkout.** It imports `truenas_exporter.config` with no `sys.path`
  bootstrap, and no documented step installs the package (`requirements*.txt`
  have no `-e .`). `python3 scripts/live_smoke.py` →
  ModuleNotFoundError. Add the repo-root/src bootstrap or document
  `pip install -e .`.
- [ ] 5. **CONFIRMED — legacy-mode stale-event expiry starves under a busy
  stream.** `_expire_stale_events()` runs only on `ws.recv()` timeout
  (`runtime.py:2930`) or stream error (`:2958`); with `reporting.realtime`
  arriving every ~2s the timeout never fires, so series from a dead
  subscription (e.g. `app.stats` after Docker stops) stay frozen forever —
  violating the Phase 1 acceptance "event series disappear after their TTL".
  Also run expiry on the per-message path (cheap monotonic check).
- [ ] 6. **CONFIRMED — collector-mode `/readyz` is never ready until
  something scrapes `/metrics`.** `is_ready()` (`runtime.py:1450`) depends on
  `_last_scrape_success_monotonic`, which in collector mode is only set
  inside scrapes triggered by `/metrics`; `main()` starts no background loop
  (waits on `_stop_event`). A k8s readinessProbe on `/readyz` gating traffic
  deadlocks. Fixed naturally by the background scrape loop in finding 1.
- [ ] 7. **PLAUSIBLE — shipped Prometheus config times out on full-budget
  scrapes.** `deploy/prometheus/prometheus.yml:13` sets `scrape_timeout: 25s`
  equal to `SCRAPE_BUDGET_SECONDS=25`; `/metrics` can take budget + connect/
  auth overhead (collector mode inline scrape; legacy mode blocks on the
  scrape lock held for the whole cycle, `runtime.py:4036`). Set timeout
  comfortably above worst-case (or lower the default budget).
- [ ] 8. **PLAUSIBLE — no validation that `EVENT_STALE_AFTER_SECONDS` ≥
  `EVENT_INTERVAL_SECONDS`.** Defaults are 15 and 2, but a documented
  `EVENT_INTERVAL_SECONDS=30` with the default TTL of 15 makes event-derived
  series flap fresh→stale between events. Add a cross-check in
  `config.py` validation (or clamp TTL to ≥ interval).

### Below the cut (document, don't necessarily fix)

- Container invocation changed from `CMD ["python", "/app/truenas_exporter.py"]`
  to `ENTRYPOINT ["truenas-exporter"]`; old `command:` overrides now fail.
  Intentional; add a migration note to CHANGELOG/README.
- Config parsing became strict (bool env values outside the recognized set
  now raise at startup; URL/port/path validation is fatal). Intentional
  Phase 1 design ("invalid configuration fails before threads or sockets
  start") and listed in CHANGELOG — but add an upgrade note with examples of
  previously-tolerated values that now abort.
- `README.md` repository-structure table still describes
  `truenas_exporter.py` as "Exporter implementation"; it is a 27-line shim
  and `src/truenas_exporter/` is missing from the table.

## Cleanup queue (fold into Phase 2 work, not separate PRs)

- **Version triplication**: `pyproject.toml version`, `version.py`,
  CHANGELOG heading. Use `dynamic = ["version"]` with
  `[tool.setuptools.dynamic] version = {attr = "truenas_exporter.version.__version__"}`.
- **Four copies of `make_config()`** across `tests/test_phase1_metrics.py`,
  `test_phase2_events.py`, `test_phase3_collector_mode.py`,
  `test_reliability.py` → one factory in `tests/conftest.py` (whose
  `sys.path` insert duplicates pyproject `pythonpath` and can go).
- **Auth/login sequence duplicated 4×** (three sites in `runtime.py`
  ~2895/4180/6089 plus `scripts/live_smoke.py`, which already drifted) →
  `JsonRpcWsClient.authenticate()` on `transport.py`.
- **check-or-write scaffold triplicated** across
  `scripts/generate_metric_contract.py`, `generate_api_docs_manifest.py`,
  and `generate_truenas_dashboard.py --check` → shared helper; also unify the
  three hardcoded `25.10.2` pins.
- **validate.sh hand-maintained ruff/mypy file lists** → directory targets
  (`ruff check src scripts tests`, `mypy src/truenas_exporter`) with a
  pyproject per-module override exempting `runtime.py` until decomposed.
- **Dead parallel scrape pipeline**: `TrueNASCollector` +
  `collect_collector_snapshot()` (`runtime.py:6069–6328`) is unregistered in
  `main()`; `_call()`'s `_diagnostic_lock` dict bookkeeping partially feeds
  it. Decision recorded in 02-architecture.md: its snapshot design is the
  convergence target — wire it to full parity, then delete
  `FullParityCollector`; do not keep both.
- **Hand-maintained `_COLLECTOR_SCALAR_METRICS`/`_COLLECTOR_SERIES_METRICS`
  tuples** (`runtime.py:~1116`) → derive scalar/series split from metric
  declarations (`labelnames`), removing the silent-omission trap for new
  metrics.
- **`generate_metric_contract.py` parses `metrics.py` with ast** and only
  recognizes top-level positional `Gauge/Counter` assignments — a future
  idiomatic refactor silently shrinks the contract. Derive the contract from
  the imported registry/metric specs instead.
- Minor: O(n²) duplicate-panel-ID check in `scripts/validate_dashboard.py:34`
  (use `collections.Counter`); O(n·m) `extra_methods` list scan in
  `_discover_all_methods` (`runtime.py:~4017`); duplicated `/readyz` test
  between `test_phase3_collector_mode.py` and `test_http_integration.py`;
  Dockerfile copies `src/` before building dependency wheels (bust-proof the
  dep layer by copying `requirements.txt` first).

## Verification for every change

1. `./scripts/validate.sh` passes end-to-end.
2. `python3 scripts/generate_metric_contract.py --check` reports no removed
   or changed metrics/labels (locked decision).
3. Each correctness fix lands with a regression test (fixture-based; live
   validation stays optional).
4. For the collector rework: two overlapping `/metrics` requests must return
   complete, consistent families, and `/healthz` must answer < 1s while a
   slow scrape is in flight.
