# TrueNAS Exporter Review and Remediation Playbook (for Claude Code)

This document packages a focused code review of `truenas_exporter.py` and turns it into an implementation plan you can hand directly to a coding agent.

Scope reviewed:

- Exporter code: `truenas_exporter.py`
- Tests: `tests/test_phase1_metrics.py`, `tests/test_phase2_events.py`
- API docs snapshot: `docs/truenas-api/`


## 1) Executive Summary

The exporter is feature-rich and already uses many good patterns (safe defaults, bounded recursion/list traversal, use of query options like `count`/`select`/`order_by`, and resilient event handling).

The largest gaps are:

1. **Architecture vs Prometheus best practice**: target metrics are updated by a background polling loop rather than produced on scrape via a custom collector.
2. **Potential scrape consistency race**: writes are protected by a lock, but `/metrics` exposition is not lock-synchronized with those writes.
3. **Performance overhead**: very large clear-and-refill cycle plus high API call volume in some collectors.
4. **Cardinality and storage risk**: broad generic method/event extraction can create many series and high churn on larger systems.


## 2) What Is Already Good

- Reads credentials from environment (`TRUENAS_WS_URL`, `TRUENAS_API_KEY`).
- Uses explicit WebSocket timeouts.
- Uses query options correctly in multiple places (including `count`, `select`, `order_by`, `limit`).
- Handles TrueNAS v25 realtime event details, including `disls` in `reporting.realtime`.
- Includes health endpoint (`/healthz`) and exporter health metrics (`truenas_up`, `truenas_scrape_duration_seconds`).


## 3) Findings and Recommended Fixes

### F1 - Background polling architecture (high impact)

**Finding**

- Exporter runs an internal polling loop (`run_forever`) and updates global metrics out-of-band.
- Prometheus exporter guidance strongly prefers synchronous scrape collection via custom collector(s).

**Why it matters**

- Harder to reason about scrape freshness.
- More race surfaces with event thread + polling thread + HTTP scrape thread.
- Requires manual stale-series cleanup (`clear()` everywhere).

**Fix direction**

- Long-term target: migrate to a custom collector architecture using fresh `MetricFamily` objects per scrape.
- Keep event stream optional; if retained, clearly separate it from scrape-produced metrics.


### F2 - Lock coverage during `/metrics` exposition (high impact)

**Finding**

- Writes to metrics are protected by `self._lock` in scrape/event paths, but the WSGI `/metrics` response path does not acquire that lock.

**Why it matters**

- A scrape can observe partially-updated state.

**Fix direction**

- Short-term: wrap metrics exposition in the same lock (by passing exporter lock into HTTP app function).
- Long-term: custom collector architecture naturally avoids this mutable shared-state issue.


### F3 - Large per-scrape clear block (medium/high impact)

**Finding**

- Huge `clear()` section at the top of each scrape.

**Why it matters**

- Extra CPU and lock hold time.
- Error-prone to maintain as new metrics are added.

**Fix direction**

- Short-term: centralize clearables into grouped lists and iterate (maintainability).
- Mid/long-term: custom collector removes most clear requirements.


### F4 - API call amplification in collectors (medium/high impact)

**Finding**

- Some collectors do `count` + list query; some do per-entity calls inside loops.
- Dataset snapshot count fallback can produce many extra calls.

**Why it matters**

- Increased scrape duration and backend load on larger deployments.

**Fix direction**

- Use list length where exact global counts are not required.
- Keep exact count where metrics are explicitly inventory-style and documented as exact.
- Add a config to cap/disable expensive per-dataset snapshot-count fallback by default.
- Consider batching patterns where suitable (for same-method repeated calls).


### F5 - Generic extractor cardinality and churn (medium/high impact)

**Finding**

- `METHOD_*` and `EVENT_*` generic recursive metrics can generate many series with method/path labels.

**Why it matters**

- TSDB growth and query cost increase.

**Fix direction**

- Add explicit config flags to disable generic method/event extraction by default.
- Keep dedicated, curated metrics enabled by default.
- If generic extraction stays enabled, restrict by allowlist and tighter depth/list limits.


### F6 - Generic label key `type` usage (low/medium impact)

**Finding**

- Some metrics use `type` as a label name.

**Why it matters**

- `type` is discouraged because it is vague in queries.

**Fix direction**

- Rename to specific labels (`interface_type`, `instance_type`, `alertservice_type`).
- Keep backward compatibility by deprecating old metric names/labels over one release cycle.


### F7 - Root endpoint behavior (low impact)

**Finding**

- `/` currently falls through to Prometheus metrics app behavior.

**Why it matters**

- Exporter convention is a simple landing page at `/` with a link to `/metrics`.

**Fix direction**

- Add lightweight HTML/text landing page at `/`.


### F8 - `_created` series noise (low impact)

**Finding**

- Python client default `_created` series are not disabled.

**Why it matters**

- Unnecessary extra series in many environments.

**Fix direction**

- Call `disable_created_metrics()` at startup (or use env var `PROMETHEUS_DISABLE_CREATED_SERIES=True`).


## 4) TrueNAS API Context to Keep

Use these docs as source of truth when adjusting calls:

- Query options semantics: `docs/truenas-api/shared/query_methods.md`
- JSON-RPC event envelope: `docs/truenas-api/shared/jsonrpc.md`
- `core.subscribe`: `docs/truenas-api/methods/core/subscribe.md`
- `core.bulk`: `docs/truenas-api/methods/core/bulk.md`
- `reporting.realtime` subscription interval and payload notes: `docs/truenas-api/events/reporting/realtime.md`
- `virt.instance.metrics` interval subscription format: `docs/truenas-api/events/virt/instance/metrics.md`


## 5) Suggested Implementation Plan

### Phase 1 (safe, low-risk improvements first)

1. Add lock synchronization around `/metrics` exposition.
2. Add `/` landing page that links to `/metrics` and `/healthz`.
3. Add `disable_created_metrics()` in startup path.
4. Add feature flags:
   - `ENABLE_GENERIC_METHOD_METRICS` (default `false`)
   - `ENABLE_GENERIC_EVENT_METRICS` (default `false`)
5. Add `DATASET_SNAPSHOT_FALLBACK_LIMIT` (default `0`) to cap expensive per-dataset fallback calls.
6. Update `.env.example` and `README.md` with new flags and behavior.
7. Add/update tests for the above behavior.

### Phase 2 (performance and cardinality tuning)

1. Audit `count` + list pairs and keep exact counts only where operationally useful.
2. Reduce unnecessary API calls by reusing cached list responses where possible.
3. Tighten generic extractor defaults (`max_depth`, `max_list_items`) if generic extraction is enabled.
4. Add metric count/cardinality guidance to README (what toggles increase series count).

### Phase 3 (best-practice architecture migration)

1. Introduce a custom collector class that yields fresh metric families per scrape.
2. Port dedicated metrics first; keep metric names stable.
3. Remove global clear-and-set pattern for target metrics.
4. Keep compatibility mode temporarily if needed, then remove old path.


## 6) Agent Rules (for Claude Code)

Use these strict rules while implementing:

1. Do not change existing metric names/labels unless explicitly listed in the current task.
2. If renaming labels/metrics, provide backward-compatible metrics for one release cycle.
3. Keep units in base units (`seconds`, `bytes`) and counters with `_total` suffix.
4. Do not add unbounded-cardinality labels (UUIDs, full paths, IPs, usernames, etc.).
5. Preserve read-only API behavior; never add mutating TrueNAS API calls.
6. Validate method/event signatures against `docs/truenas-api/` before changing params.
7. Add tests for each behavior change.
8. Keep changes incremental and reviewable; avoid giant all-at-once refactors.


## 7) Definition of Done Per Phase

### For each phase

- Code changes are minimal and focused.
- Tests pass.
- README and `.env.example` reflect new behavior/toggles.
- No regression in existing metric names (unless intentionally deprecated with compatibility path).


## 8) Validation Commands

Run from repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
pytest
python -m compileall truenas_exporter.py tests
```


## 9) Copy/Paste Prompt for Claude Code

Use this prompt directly in Claude Code:

```text
You are working in a TrueNAS Prometheus exporter repo.

Read these files first:
- truenas_exporter.py
- docs/claude-code-exporter-review-remediation-playbook.md
- docs/truenas-api/shared/query_methods.md
- docs/truenas-api/events/reporting/realtime.md
- tests/test_phase1_metrics.py
- tests/test_phase2_events.py

Goal:
Implement Phase 1 from docs/claude-code-exporter-review-remediation-playbook.md.

Hard requirements:
1) Add lock-synchronized metrics exposition so /metrics cannot read partially updated metrics.
2) Add a simple landing page on / with links to /metrics and /healthz.
3) Disable Prometheus client _created series at startup.
4) Add config flags with defaults:
   - ENABLE_GENERIC_METHOD_METRICS=false
   - ENABLE_GENERIC_EVENT_METRICS=false
5) Add DATASET_SNAPSHOT_FALLBACK_LIMIT=0 and enforce it in dataset snapshot fallback logic.
6) Update .env.example and README.md for all new flags/behavior.
7) Add/adjust tests accordingly and run pytest.

Guardrails:
- Keep existing metric names stable unless absolutely required.
- Do not add mutating TrueNAS API calls.
- Keep base units and Prometheus naming best practices.
- Keep changes small and readable.

Output format:
- Short summary of files changed and why.
- Test results.
- Any follow-up suggestions for Phase 2.
```


## 10) Optional Next Prompt (Phase 2)

```text
Implement Phase 2 from docs/claude-code-exporter-review-remediation-playbook.md.

Focus only on performance and cardinality:
- Audit count+list query pairs and remove unnecessary duplicates.
- Reuse cached responses to reduce API calls.
- Keep exact inventory counts where they are semantically important.
- Add tests for changed collector behavior.
- Keep metric names stable.

Run pytest and report before/after call-count impact for the touched collectors.
```
