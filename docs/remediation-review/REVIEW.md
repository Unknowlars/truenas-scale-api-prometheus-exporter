# Independent Review — Remediation Program T01–T21

Date: 2026-07-16
Reviewer: independent review agent (read-only; no source changes, no push)
Scope: commits `cebe785` (T01) … `0dc1875` (T21) on branch `wired`, plus
`docs/remediation/` task specs/outcomes, generated artifacts, and tests.

## Review scope and method

- Read `AGENTS.md`, `docs/remediation/README.md`, `docs/remediation/TASKS.md`,
  every `docs/remediation/tasks/T01–T21.md` (Required behavior + Outcome), and
  `docs/modernization/README.md`.
- Inspected `runtime.py` (event loop, realtime cache, scrape_once, all
  remediation-touched collectors), `metrics.py`, `events.py`,
  `compat_profiles.py`, `api_catalog.py`, `method_safety.py`, `config.py`,
  `http.py`, `transport.py`, `scripts/generate_api_exporter_parity.py` output,
  `docs/metrics-contract.json`, `docs/api-exporter-parity.{md,json}`, and the
  test suite (including new `test_event_stream_liveness.py`,
  `test_t15_duplicate_api_calls.py`, `test_t21_low_cost_metrics.py`).
- Fixture/synthetic validation only. No live TrueNAS API was contacted and no
  mutating call exists in any reviewed path.

## Commands run and results

| Command | Result |
|---|---|
| `git status --short` | clean before and after review (only this review package added) |
| `python3 -m pytest tests/ -q` | **245 passed** (exit 0) |
| `python3 scripts/generate_metric_contract.py --check` | pass, no diff |
| `python3 scripts/generate_api_exporter_parity.py` | pass, regenerated output identical to committed artifacts (no git diff) |
| `python3 scripts/generate_truenas_dashboard.py` | pass, no dashboard diff |
| `./scripts/validate.sh` | **exit 0** — ruff, mypy, pytest+coverage, all `--check` generators, dashboard validation, `public_release_audit_ok`, Docker build, container version smoke `5.2.0`, `validation_ok` |

## Task board status

`docs/remediation/TASKS.md` shows **all 21 rows T01–T21 as `done`**, each with a
filled Outcome section, a completed-log entry, and a matching `T##:` commit
(T01 `cebe785` … T21 `0dc1875`). Task premises were compared against the
current code; no task was found marked done without its required behavior
substantially implemented. The findings below are gaps, regressions between
tasks, or hardening deltas versus the written specs — not missing tasks.

## Findings (ordered by severity)

### F1 — Medium — Legacy-mode delayed snapshot publish races the poll-cycle wipe (T17)

- **Affected task(s):** T17
- **Files:** `src/truenas_exporter/runtime.py:856-887`
  (`_publish_metric_snapshot`, `_publish_metric_snapshot_throttled`),
  wipe at `runtime.py:3441` (`_reset_poll_cycle_metrics` inside `scrape_once`).
- **Issue:** the throttled publish path schedules a `threading.Timer` whose
  callback is `_publish_metric_snapshot` directly. The timer thread calls
  `REGISTRY.collect()` **without acquiring `self._lock`**. Every other publish
  site runs under the scrape lock (scrape tail, event dispatch), but a timer
  armed just before a poll cycle starts can fire while `scrape_once` holds the
  lock and has wiped/partially refilled the registry. The resulting families
  tuple is stored as "the last complete snapshot" and served on `/metrics` in
  legacy mode until the cycle-end publish replaces it.
- **Why it matters:** T17's whole design premise is that a snapshot is always a
  *complete, consistent* cycle. This race can serve a mostly-empty or
  half-filled registry to Prometheus for up to a full scrape duration —
  exactly the inconsistent-read problem the task set out to remove. Legacy
  mode only; collector mode never schedules the timer.
- **Suggested fix:** make the timer callback acquire `self._lock` (it is an
  `RLock`) around the collect, e.g. wrap in a small
  `_publish_metric_snapshot_locked()` used as the timer target; add a
  regression test that holds `exporter._lock`, forces the timer to fire, and
  asserts the published snapshot is not replaced until the lock is released.

### F2 — Low — T19 silently regressed T16's cadence HELP suffix on the oldest-snapshot metric

- **Affected task(s):** T16, T19 (item 4)
- **Files:** `src/truenas_exporter/metrics.py:799-803` (`SNAPSHOT_OLDEST_TS`),
  `docs/metrics-contract.json` (reflects current text).
- **Issue:** T16 (commit `96cbb8a`) appended ", refreshed every ~5 minutes" to
  the `truenas_snapshot_oldest_timestamp_seconds` HELP as its compatibility
  rule required. T19 (commit `18b0112`) then replaced the entire HELP with its
  prescribed text "Unix timestamp of the oldest ZFS snapshot; absent when
  there are no snapshots." — dropping the cadence suffix. Confirmed via
  `git log -L`. The T16 outcome ("HELP cadence suffixes changed", plural) is
  now only true for `truenas_disk_temperature_agg_celsius`.
- **Why it matters:** operators reading HELP will assume the timestamp is
  per-scrape fresh; it can be up to ~5 minutes (and after failures up to 3×
  cadence) old. This is exactly the documented-freshness contract T16 was
  required to establish.
- **Suggested fix:** merge both texts, e.g. "Unix timestamp of the oldest ZFS
  snapshot; absent when there are no snapshots; refreshed every ~5 minutes."
  Regenerate metric contract + parity artifacts.

### F3 — Low — Event-stream idle deadline is only evaluated on socket timeout (T01)

- **Affected task(s):** T01
- **Files:** `src/truenas_exporter/runtime.py:2119-2134` (`_event_stream_loop`
  recv loop).
- **Issue:** the dead-connection check (`idle_seconds >=
  event_read_timeout_seconds`) lives solely inside the
  `except WebSocketTimeoutException` handler, and `last_message_monotonic`
  resets only on `collection_update` messages. A connection that keeps
  delivering *any other* WS traffic (server notifications, non-subscription
  JSON-RPC messages) never times out on recv, so the idle deadline is never
  evaluated even if no event message arrives for hours. T01's required
  behavior #1 is a max-idle rule on message arrival, not on socket silence.
- **Why it matters:** the exact T01 failure mode (event metrics permanently
  dark with `truenas_event_stream_up` stuck at 1) can still occur whenever the
  socket stays chatty while the subscription source is dead.
- **Suggested fix:** evaluate the idle deadline after **every** `recv_json()`
  return (before the `collection_update` filter), not only in the timeout
  branch. Add a regression test with a client that returns non-
  `collection_update` messages forever and assert teardown at the deadline.

### F4 — Low — Dead-connection teardown blocks on `core.unsubscribe` against a dead socket (T01)

- **Affected task(s):** T01
- **Files:** `src/truenas_exporter/runtime.py:2154-2171` (`finally` block of
  the recv loop).
- **Issue:** when the max-idle rule raises `RuntimeError("...dead
  connection")`, the `finally` block still issues one `core.unsubscribe` call
  per subscribed event over the very socket just judged dead. Each call blocks
  until the socket timeout (default 15 s). With several subscriptions the
  teardown can add ~15 s × N before the reconnect/backoff path even starts,
  and each failure also increments `event_unsubscribe` collector errors.
- **Why it matters:** delays honest reconnection well past
  `EVENT_READ_TIMEOUT_SECONDS` and produces noise errors, partially defeating
  T01's "reconnects within event_read_timeout_seconds" goal in the dead-socket
  case.
- **Suggested fix:** set a `connection_dead` flag when the idle rule trips and
  skip the unsubscribe loop (or close the socket first) in that case; clean
  unsubscribe should remain for orderly shutdown/reconnect paths.

### F5 — Low — `EXPORTER_BIND_ADDRESS` cannot express IPv6 literals (T18)

- **Affected task(s):** T18
- **Files:** `src/truenas_exporter/config.py:77-81` (`_bind_address_env`),
  `README.md:219`.
- **Issue:** validation rejects any value containing `:`, which excludes every
  IPv6 literal (`::1`, `fd00::5`), not just `host:port` mistakes. The README
  row ("HTTP bind host/IP") does not mention the limitation.
- **Why it matters:** an operator on an IPv6-only or loopback-v6 management
  network cannot restrict the bind address at all — the security knob T18
  added is unusable there, and the error message ("must be a host/IP without
  port") is misleading for a valid IP.
- **Suggested fix:** accept bracket-free IPv6 literals (e.g. try
  `ipaddress.ip_address()` before applying the `:` rejection) or explicitly
  document IPv4/hostname-only support in README and the ValueError text.

### F6 — Low — Heavy-query refresh cadence is 9 cycles, not the documented 10 (T16)

- **Affected task(s):** T16
- **Files:** `src/truenas_exporter/runtime.py:4429-4433` (disk temp agg),
  `runtime.py:4752-4755` (snapshot oldest); constants at `runtime.py:522-526`;
  HELP "refreshed every ~5 minutes" at `metrics.py:171`.
- **Issue:** `should_refresh` uses `current_cycle - last_attempt >=
  DISK_TEMP_AGG_REFRESH_CYCLES - 1`, i.e. refresh at cycles 1, 10, 19 … — a
  9-cycle gap (~4.5 min at the default 30 s interval), while the constants,
  comments, task text, and HELP all say "every 10 cycles ≈ 5 minutes".
  Likewise the stale-expiry factor multiplies the constant (30 cycles) while
  actual refresh attempts happen every 9.
- **Why it matters:** minor extra load on the middleware versus the documented
  budget and a code/comment mismatch that will confuse the next maintainer;
  the existing "cycle-10 refetch" tests pin the off-by-one as intended
  behavior.
- **Suggested fix:** either drop the `- 1` (and update the two cadence tests)
  or change the comment/HELP to state the real ~4.5-minute cadence. Keep code,
  comment, and HELP mutually consistent.

### F7 — Low — Heavy-query failures bypass `_collector_error` diagnostics (T16)

- **Affected task(s):** T16 (pattern also at the pre-existing snapshot count)
- **Files:** `src/truenas_exporter/runtime.py:4440` (temp agg refresh
  failure), `runtime.py:4777` (snapshot-oldest refresh failure),
  `runtime.py:4737` (snapshot count failure).
- **Issue:** these paths call `COLLECTOR_ERRORS_TOTAL.labels(...).inc()`
  directly instead of `self._collector_error(...)`, so the internal
  `_collector_errors` diagnostics map (used by the diagnostics surface and
  consistent everywhere else) is never updated for these failures.
- **Why it matters:** inconsistent failure accounting; T16 required "count a
  collector error" on refresh failure and the sibling-collector convention is
  the `_collector_error` helper.
- **Suggested fix:** route the three sites through `self._collector_error`
  with appropriate collector names and messages.

### F8 — Low — Parity row for `truenas_pool_status_code` carries misleading evidence (T21 item 5)

- **Affected task(s):** T21
- **Files:** `scripts/generate_api_exporter_parity.py` (hand-maintained
  mapping tables), `docs/api-exporter-parity.md:1262`.
- **Issue:** the default (25.10.2-target) parity row for
  `truenas_pool_status_code` lists fixture evidence
  `tests/fixtures/api_25_10_2/pool_query.json` (a `pool.query` fixture — the
  metric is produced from v26-only `zpool.query`) and describes the source as
  "zpool.query: undocumented/unavailable" while the disposition is
  "active dedicated". `docs/truenas-api-v26/methods/zpool/query.md` documents
  `status_code` (line ~202); the metric is correctly profile-gated at runtime
  (`runtime.py:3246-3272`), but the generated row does not say "v26-only,
  profile-gated; absent on 25.10".
- **Why it matters:** the remediation program's rule 6 requires generated
  artifacts to tell the truth; this row overstates 25.10 availability and
  cites the wrong fixture.
- **Suggested fix:** update the generator's override/note for
  `POOL_STATUS_CODE` to reference the v26 doc, the profile gate, and the T21
  test file as evidence; regenerate parity.

### F9 — Low — Auto-skip amnesty silently disabled if the timestamp entry is missing (T14)

- **Affected task(s):** T14
- **Files:** `src/truenas_exporter/runtime.py:1473-1478` (`_safe_call_auto`).
- **Issue:** `if skipped_at is None or time.monotonic() - skipped_at < 86400:
  return None` — a method present in `_auto_skipped_methods` without a
  matching `_auto_skipped_at` entry is skipped **forever**, the exact
  permanence T14 removed. Today the two structures are only mutated together,
  but the defensive branch chooses the unsafe default.
- **Why it matters:** any future code path (or state divergence across the two
  exporter threads) that adds to the set without the timestamp reintroduces
  permanent method darkness with no test to catch it.
- **Suggested fix:** treat a missing timestamp as expired (retry immediately)
  instead of skipping, and add a one-line regression test.

## Cross-cutting checks with no findings

- **Absent-on-failure / no fabricated zeros:** T02 (CPU split), T05 (network
  rates), T06 (job flags, reporting_enabled), T03 (dedup ratio), T13
  (pre-auth preservation + `max(3*interval,300)` stale guard) are all
  implemented as specified with regression tests. The remaining intentional
  zero-fills (disk temperature alert zero per queried disk on success, job
  zeroes when `total_active == 0`) are the documented legitimate cases.
- **Metric contract:** `generate_metric_contract.py --check` passes; no
  renames/retypes/label changes found across T01–T21; deprecated aliases
  (`truenas_pool_dedup_ratio`, `truenas_network_gateway_reachable`) remain
  declared/emitting per the alias policy.
- **Method safety / sensitive selects:** all new calls (`api_key.query` with
  strict select in a sensitive namespace, task queries with credential-free
  selects verified by wire-shape tests, `disk.temperature_alerts` with
  explicit names, `zpool.query` profile-gated) go through `_call`/profile
  gates; no mutating call and no bare call into a sensitive namespace was
  found. `REQUIRES_ENTITY_PARAM` still blocks auto-discovery of the
  entity-param methods.
- **v26 gating:** `V26_ADDED_METHODS`/`V26_ADDED_EVENTS` are excluded from
  `PROFILE_25_10` and `PROFILE_UNKNOWN`; `PROFILE_UNKNOWN` is a verified
  25.10∩26.0 intersection (set identities asserted in tests). The unknown
  profile transports neither `container.query` nor `virt.instance.query`.
- **Event ownership:** all new event metrics (T04 pool space trio, T21
  interface speed/link) are registered in `events.py` `_EVENT_METRICS` and
  covered by publish/expiry/poll-reset-survival tests.
- **Bounded labels:** new labels (pool, vdev name/path/guid, task name/state
  allowlist with `UNKNOWN` mapping, api-key name, node ∈ {this_node,
  other_node}, status_code enum-uppercased) are bounded.
- **No hosted CI**, no `.github/workflows`, no push performed, LF endings
  intact (`git diff --check` clean via validate.sh).

## Validation results summary

All six required commands pass (table above). Coverage in the validate gate is
~91.3% against the 85% floor. No command failures occurred during this review.
