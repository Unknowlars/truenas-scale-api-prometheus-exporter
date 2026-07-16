# Remediation-Review Follow-up Task Board

Standalone follow-up board produced by the independent T01–T21 review
([REVIEW.md](REVIEW.md)). Each row is self-contained enough to fix without
rereading the full review. Statuses: `todo` | `in-progress` | `blocked` |
`done` | `wont-fix`.

Rules (same program conventions as `docs/remediation/`):
- One task per session, one commit per task (`R##: <imperative summary>`).
- Regression test with every behavioral fix; `./scripts/validate.sh` must exit
  0 before `done`.
- Regenerate `docs/metrics-contract.json` and `docs/api-exporter-parity*` when
  any metric declaration, HELP text, or producer changes.
- No pushes, no hosted CI, no live TrueNAS calls, no mutating API calls.

| ID | Finding | Area | Severity | Suggested Fix | Status |
|----|---------|------|----------|---------------|--------|
| R01 | Legacy-mode delayed snapshot publish races the poll-cycle wipe: the `threading.Timer` scheduled by `_publish_metric_snapshot_throttled` (`runtime.py:863-887`) calls `_publish_metric_snapshot` (`runtime.py:856-861`), which runs `REGISTRY.collect()` **without** `self._lock`. If it fires while `scrape_once` holds the lock after `_reset_poll_cycle_metrics()` (`runtime.py:3441`), a partially-wiped registry is stored and served as the "last complete snapshot" in legacy mode. | reliability (T17) | Medium | Make the timer target a wrapper that acquires `self._lock` (RLock) before collecting, e.g. `_publish_metric_snapshot_locked`. Add a test: hold `exporter._lock` in the test thread, force the throttle timer to fire (monkeypatch `threading.Timer` or call the wrapper), assert the served snapshot is unchanged until the lock is released, then updated. No metric contract change. | done |
| R02 | `truenas_snapshot_oldest_timestamp_seconds` HELP lost the T16 cadence suffix: T19 (commit `18b0112`) replaced T16's HELP wholesale, dropping ", refreshed every ~5 minutes". Current text at `metrics.py:799-803`; `docs/metrics-contract.json` matches the regressed text. | metric contract (T16/T19) | Low | Change HELP to "Unix timestamp of the oldest ZFS snapshot; absent when there are no snapshots; refreshed every ~5 minutes." Update any test asserting the exact HELP line (grep `snapshot_oldest` in `tests/`), then regenerate metric contract + parity artifacts. HELP-only change; no rename/retype. | done |
| R03 | Event-stream dead-connection deadline only checked on `WebSocketTimeoutException` (`runtime.py:2119-2134`): steady non-`collection_update` WS traffic keeps `recv_json()` returning, so the idle deadline is never evaluated even when no event message arrives within `EVENT_READ_TIMEOUT_SECONDS`, leaving `truenas_event_stream_up=1` on a dead subscription. | reliability (T01) | Low | After every `recv_json()` return (before the `collection_update` filter), compute `idle = monotonic() - last_message_monotonic` and raise the same dead-connection `RuntimeError` when `idle >= event_read_timeout_seconds`. Extend `tests/test_event_stream_liveness.py` with a fake client that returns non-`collection_update` messages forever; assert teardown at the deadline and `event_stream_up == 0`. | done |
| R04 | Dead-connection teardown blocks on `core.unsubscribe` over the dead socket: `finally` block at `runtime.py:2154-2171` issues one unsubscribe per subscribed event, each blocking up to the socket timeout (default 15 s), delaying reconnect by up to N×15 s and emitting `event_unsubscribe` collector errors. | reliability (T01) | Low | Set a local `connection_dead = True` flag where the idle-deadline `RuntimeError` is raised; in the `finally` block skip the `core.unsubscribe` calls (still set `event_stream_up=0`, clear caches, expire events) when the flag is set. Keep clean unsubscribe for normal shutdown. Test: liveness fake counts unsubscribe calls; assert 0 after a dead-connection teardown and >0 after a clean stop. | done |
| R05 | `EXPORTER_BIND_ADDRESS` rejects IPv6 literals: `_bind_address_env` (`config.py:77-81`) rejects any value containing `:`, so `::1`/`fd00::…` cannot be configured, and README:219 does not state the limitation. | config/security (T18) | Low | Preferred: try `ipaddress.ip_address(raw)` first — accept valid IPv4/IPv6 literals as-is; keep the `:`-and-whitespace rejection only for values that are not valid IP literals (catches `host:port`). Verify `wsgiref.make_server` binds v6 (it uses `AF_INET` by default — if v6 binding is not feasible, instead document "IPv4/hostname only" in README + `.env.example` + the ValueError message). Add config tests for `::1` (accepted or clearly rejected per chosen path) and `host:9108` (rejected). | done |
| R06 | Heavy-query refresh cadence off-by-one: `current_cycle - last_attempt >= REFRESH_CYCLES - 1` (`runtime.py:4429-4433` disk temp agg; `runtime.py:4752-4755` snapshot oldest) refreshes every 9 cycles (~4.5 min at 30 s interval) while constants/comments/HELP say "every 10 cycles ≈ 5 minutes"; stale-expiry factor (3×10) is computed against the constant, not actual cadence. | performance/docs (T16) | Low | Pick one: (a) drop the `- 1` in both `should_refresh` computations and update the two cadence tests in `tests/test_phase1_metrics.py` that pin cycle-10 refetch; or (b) keep behavior and fix the comment at `runtime.py:522-526` + the `~5 minutes` HELP suffixes to say ~4.5 minutes, regenerating contract/parity. Option (a) matches the documented contract with the smaller doc churn. | done |
| R07 | Heavy-query failure accounting bypasses `_collector_error`: `runtime.py:4440` (temp-agg refresh), `runtime.py:4777` (snapshot-oldest refresh), `runtime.py:4737` (snapshot count) increment `COLLECTOR_ERRORS_TOTAL` directly, so the internal `self._collector_errors` diagnostics map is not updated, unlike every sibling collector. | conventions (T16) | Low | Replace the three direct `COLLECTOR_ERRORS_TOTAL.labels(...).inc()` + `LOG.debug` pairs with `self._collector_error("disks"/"snapshots", "<message>")`. Behavior-neutral for Prometheus output (same counter label); extend an existing T16 failure test to assert `exporter._collector_errors` gained the entry. | done |
| R08 | Parity row for `truenas_pool_status_code` is misleading (`docs/api-exporter-parity.md:1262`): cites 25.10 fixture `tests/fixtures/api_25_10_2/pool_query.json` for a v26-only `zpool.query` metric, says "undocumented/unavailable" although `docs/truenas-api-v26/methods/zpool/query.md` documents `status_code`, and omits the v26-only/profile-gated caveat while claiming "active dedicated". | generated artifacts (T21) | Low | In `scripts/generate_api_exporter_parity.py`, fix the hand-maintained override for `POOL_STATUS_CODE`: evidence should reference `tests/test_t21_low_cost_metrics.py` (not the pool_query fixture), and the note should state "v26-only zpool.query, profile-gated via V26_ADDED_METHODS; absent on 25.10/unknown; status_code documented in the v26 corpus". Regenerate `docs/api-exporter-parity.{md,json}` and confirm `--check` passes. | done |
| R09 | Auto-skip amnesty permanently disabled on missing timestamp: in `_safe_call_auto` (`runtime.py:1473-1478`), a method in `_auto_skipped_methods` with no `_auto_skipped_at` entry hits `skipped_at is None → return None` forever — the exact permanence T14 removed, chosen as the defensive default. | reliability (T14) | Low | Treat a missing timestamp as expired: when `skipped_at is None`, discard the method from the skip set and retry immediately (fall through to the call). Add a regression test that seeds `_auto_skipped_methods` without a timestamp and asserts the method is attempted on the next `_safe_call_auto`. | done |

## Notes for the fixing agent

- R01 is the only Medium; do it first. R03/R04 are both inside
  `_event_stream_loop` — they can share one session if kept as two commits or
  a single `R03+R04` commit with both tests (call it out in the commit body).
- R02, R06(b), and R08 touch generated artifacts — always run the generators
  (without `--check`) and commit their output alongside the source change.
- Nothing here changes metric names, types, or label sets; R02/R06 touch HELP
  text only, which is a permitted correction per `docs/VERSIONING.md`.

## Discovered

- `scripts/generate_api_exporter_parity.py`'s `_test_fixture_evidence` matches
  fixture/test evidence by plain substring search over every file under
  `tests/` (source name → fixture stem, and needle-in-file-text for test
  citations), capped to the first 2 hits in corpus order (alphabetical by
  path). This is fragile beyond the R08 `POOL_STATUS_CODE` case fixed here:
  adding *any* new test file whose raw text happens to contain another
  metric's source-method substring (e.g. a docstring mentioning `pool.query`)
  can silently steal that metric's evidence citation if the new file sorts
  before the legitimate one alphabetically — discovered firsthand while
  writing `tests/test_generate_api_exporter_parity.py` for R08, where an
  earlier draft's docstring text pulled evidence away from ~20 unrelated
  `pool.query`-sourced rows before the wording was reworked to avoid literal
  method-name substrings. Not fixed here (out of R08's scope): worth a
  follow-up to make the matcher word-boundary-aware or require an explicit
  per-file allowlist of which metrics it's evidence for.
