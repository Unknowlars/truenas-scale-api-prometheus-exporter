# T01 — Event stream: detect dead connections, reconnect, honest `event_stream_up`

- **Priority:** P1 (highest single reliability risk)
- **Size:** M
- **Depends on:** nothing
- **Review reference:** review-report.md finding D1 (also config foot-gun (e)10)

## Problem

After subscribing, `_event_stream_loop` only ever calls `client.recv_json()` with a socket
timeout of `min(event_read_timeout_seconds, event_stale_after_seconds)` (= 15 s by default).
`WebSocketTimeoutException` is caught and treated as a quiet period — the loop just expires stale
event metrics and calls `recv` again, forever. No WebSocket ping is ever sent and there is no
"no message for N seconds ⇒ connection is dead" rule.

`reporting.realtime` is contractually a heartbeat: TrueNAS emits it every `event_interval`
(≥ 2 s) while subscribed. Prolonged silence therefore *is* failure, but the code treats it as
normal.

Additionally, `truenas_event_stream_up{event=...}` is set to 1.0 at subscribe time and only set
to 0.0 in the unsubscribe/error paths — so during a silent-dead connection the health metric a
dashboard would alert on keeps reporting healthy.

**Failure scenario:** TrueNAS power-cycles, or a NAT/firewall drops the idle mapping, with no
FIN/RST delivered. `recv` blocks, times out every 15 s, loop continues. Event-owned metrics
(CPU, memory, disk I/O, app stats) correctly expire to NaN after 15 s — and then never come back
until the exporter process is restarted. `truenas_event_stream_up` stays 1 the whole time.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` — `_event_stream_loop` (~lines 1989–2108),
  `_event_is_fresh` / `_expire_stale_events` (~814–858), `_dispatch_event` tail (~1978).
- `src/truenas_exporter/transport.py` — whole file (122 lines).
- `src/truenas_exporter/config.py` — `event_read_timeout_seconds`, `event_stale_after_seconds`,
  `event_interval_seconds` (lines ~107–112, 146–147).
- `tests/test_phase2_events.py`, `tests/test_reliability.py::test_busy_event_path_expires_silent_subscription`
  (read to follow existing test patterns for the event loop).

## Required behavior

1. Track the wall-clock/monotonic time of the last received `collection_update` (any event) on
   the current connection. If no message has arrived within
   `event_read_timeout_seconds` (default 60 s; keep the existing env var), treat the connection
   as dead: log a warning (no hostname), tear down the connection, and let the existing
   reconnect/backoff loop re-establish and re-subscribe.
2. Stop clamping the socket timeout to `event_stale_after_seconds`
   (`timeout_seconds=min(...)` at ~line 1996). The socket recv timeout should stay short
   (e.g. `min(event_stale_after_seconds, event_read_timeout_seconds)` is fine as a *poll tick*)
   — the point is that repeated timeouts must count toward the dead-connection deadline instead
   of resetting nothing.
3. When the dead-connection deadline trips (and in general whenever the connection is torn
   down), set `_collector_event_stream_up[event] = 0.0` for all subscribed events and publish
   (same as the existing error path does), so `truenas_event_stream_up` goes to 0 while
   disconnected.
4. Config validation hardening (small, related): in `config.py`, require
   `EVENT_STALE_AFTER_SECONDS >= 2 * EVENT_INTERVAL_SECONDS` (currently only `>=`), so an event
   arriving exactly at the expiry boundary can't flap present/absent. Update the existing
   validation error message and its test
   (`tests/test_reliability.py::test_load_config_rejects_event_ttl_shorter_than_interval`).
5. Preserve existing behavior otherwise: backoff 2→120 s with reset-on-success, resubscription of
   all configured events after reconnect, stale-expiry semantics.

Notes/choices left to you: an explicit WebSocket ping (websocket-client `.ping()`) is an
acceptable *addition* but not a substitute for the max-idle rule — middleware liveness is what we
actually care about, and the idle rule needs no server support.

## Compatibility rules that apply

- No new metrics required. If you add one anyway (e.g. reconnect counter), it must be declared in
  `metrics.py` via `declare_counter`, and you must regenerate the metric contract + parity + dashboard
  (README rule 6).
- The `EVENT_READ_TIMEOUT_SECONDS` env var already exists and is documented as the read timeout —
  reusing it as the dead-connection deadline is the intended fix, not a breaking change.

## Tests

Add to `tests/test_phase2_events.py` (or a new `tests/test_event_stream_liveness.py`):

1. A fake client whose `recv_json` raises `WebSocketTimeoutException` repeatedly: assert the loop
   abandons the connection after `event_read_timeout_seconds` (monkeypatch `time.monotonic` like
   `test_collector_omits_expired_event_metrics` does — do not sleep for real).
2. Assert `_collector_event_stream_up` values are 0.0 for all events after the teardown.
3. Assert a message arriving resets the idle deadline (no spurious teardown under normal 2 s
   event flow).
4. The updated config-validation test for the ≥ 2× rule.

## Verification

```
python3 -m pytest tests/test_phase2_events.py tests/test_reliability.py tests/test_transport.py -q
./scripts/validate.sh
```

## Definition of done

- Silent-dead connection reconnects within `event_read_timeout_seconds` (proven by test, no real
  sleeps).
- `truenas_event_stream_up` is 0 while disconnected (proven by test).
- No behavior change for healthy streams; full validate.sh green; TASKS.md updated.

## Outcome

Implemented the max-idle dead-connection rule and tightened config validation as specified.

**Files touched:**
- `src/truenas_exporter/runtime.py` — `_event_stream_loop`: track `last_message_monotonic`
  (reset only on a `collection_update` message). On `WebSocketTimeoutException`, compute idle
  time since the last message; once it reaches `event_read_timeout_seconds`, raise `RuntimeError`
  instead of looping forever. This is caught by the existing outer `except Exception` handler,
  which already sets `truenas_event_stream_up` to 0 for all configured events, force-expires
  cached event metrics, logs a warning (no hostname/API key), and runs the existing 2→120s
  backoff-with-reset-on-success reconnect. No changes were needed to that handler or to the
  resubscribe-after-reconnect logic — both already matched the required behavior. Left the socket
  recv timeout as `min(event_read_timeout_seconds, event_stale_after_seconds)` (still just a poll
  tick, not the dead-connection deadline itself), per the task's note that this is fine.
- `src/truenas_exporter/config.py` — `EVENT_STALE_AFTER_SECONDS` validation now requires
  `>= 2 * EVENT_INTERVAL_SECONDS` (was `>= EVENT_INTERVAL_SECONDS`); updated the error message.
- `docs/api-exporter-parity.json` / `docs/api-exporter-parity.md` — regenerated (no content
  change, only `runtime.py:<line>` references shifted because the fix added lines to
  `_event_stream_loop`).

**Tests added:**
- `tests/test_event_stream_liveness.py` (new) — `_LivenessClient` fake drives
  `_event_stream_loop()` end-to-end with a monkeypatched `time.monotonic`:
  - `test_dead_connection_detected_after_read_timeout` — repeated timeouts spaced 25s apart
    trip the 60s idle deadline on the 3rd read; asserts the loop tears down after exactly 3
    reads and `truenas_event_stream_up` is 0.0 afterward. This test fails on pre-fix code (the
    old loop never raises on repeated timeouts, so it would spin forever / `recv_count` would
    never stabilize at 3).
  - `test_message_arrival_resets_idle_deadline` — 2 timeouts, then a live `collection_update`
    message, then 3 more timeouts: proves the idle clock resets on message receipt (6 reads
    total) rather than tripping at the 4th read as it would if the deadline were measured from
    connection start.
- `tests/test_reliability.py`:
  - Updated `test_load_config_rejects_event_ttl_shorter_than_interval` to match the new error
    message.
  - Added `test_load_config_rejects_event_ttl_below_twice_the_interval` — boundary test: 1s
    below `2 * interval` rejected, exactly `2 * interval` accepted.

**Verification:** targeted suite (`test_phase2_events.py`, `test_reliability.py`,
`test_transport.py`, plus the new liveness file and `test_runtime_lifecycle.py`) — 59 passed.
Full `./scripts/validate.sh` — exit 0 (ruff, mypy, pytest+coverage 90.49%, all `--check`
generators after regenerating the parity docs, dashboard validation, docker build/run).

**Follow-ups for other tasks:** none identified beyond what's already tracked. The explicit
WebSocket `.ping()` mentioned as optional in the task notes was not added — the max-idle rule
alone satisfies the required behavior and needs no server-side support.
