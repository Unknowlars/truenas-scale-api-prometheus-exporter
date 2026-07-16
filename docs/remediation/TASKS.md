# Task Board

Single source of truth for remediation progress. **Update this file at the start and end of
every session** (see protocol in [README.md](README.md)).

Status values: `todo` | `in-progress` | `blocked` | `done` | `wont-fix`

Rules for updating:
- Set `in-progress` + date + your session identifier when you start.
- Set `done` only after `./scripts/validate.sh` exits 0 and the task file's **Outcome** section
  is filled in.
- `blocked` requires a one-line reason here and details in the task file.
- Never edit another task's row except to add a note in **Discovered during work**.

## P1 — Wrong values / silent data loss (do first, in order)

| ID | Task | Area | Size | Depends on | Status | Updated | Notes |
|----|------|------|------|------------|--------|---------|-------|
| [T01](tasks/T01-event-stream-dead-connection.md) | Event stream: detect dead connections, reconnect, honest `event_stream_up` | reliability | M | — | done | 2026-07-16 | |
| [T02](tasks/T02-cpu-user-idle-fabrication.md) | Stop fabricating `cpu_user_percent` / `cpu_idle_percent` | metric value | S | — | done | 2026-07-16 | patch-worthy behavior fix |
| [T03](tasks/T03-pool-dedup-ratio.md) | `pool_dedup_ratio` reports bytes under a ratio name | metric value | S | — | done | 2026-07-16 | patch-worthy behavior fix |
| [T04](tasks/T04-realtime-pool-metrics.md) | Realtime `pools` section: retire dead read/write rates, emit used/available/total bytes | metric value + gap | M | — | done | 2026-07-16 | minor-version-worthy |
| [T05](tasks/T05-network-rate-fallback.md) | Remove cumulative-bytes fallback in network rx/tx rate gauges | metric value | S | — | done | 2026-07-16 | patch-worthy behavior fix |
| [T06](tasks/T06-fabricated-zeros.md) | Eliminate fabricated zeros on partial failure (job flags, reporting_enabled) | metric value | S | — | done | 2026-07-16 | patch-worthy behavior fix |
| [T07](tasks/T07-dataset-snapshot-count.md) | Make `dataset_snapshot_count` actually emit | metric gap | S | — | done | 2026-07-16 | minor-version-worthy |
| [T08](tasks/T08-task-outcome-metrics.md) | Emit replication/cloudsync/rsync/snapshottask outcome state + last-run | metric gap | L | — | done | 2026-07-16 | minor-version-worthy |

## P2 — Hardening + high-value gaps

| ID | Task | Area | Size | Depends on | Status | Updated | Notes |
|----|------|------|------|------------|--------|---------|-------|
| [T09](tasks/T09-vdev-error-metrics.md) | Re-enable pool vdev read/write/checksum error metrics via `pool.query` topology | metric gap | M | — | done | 2026-07-16 | minor-version-worthy |
| [T10](tasks/T10-disk-temperature-alerts.md) | Wire `disk.temperature_alerts` → `disk_temperature_alert_count` | metric gap | S | — | done | 2026-07-16 | minor-version-worthy |
| [T11](tasks/T11-profile-unknown-intersection.md) | Make `PROFILE_UNKNOWN` a true 25.10∩26.0 intersection | version compat | S | — | done | 2026-07-16 | patch-worthy behavior fix |
| [T12](tasks/T12-profile-thread-race.md) | Fix cross-thread `compatibility_profile` race | reliability | M | T11 | done | 2026-07-16 | patch-worthy behavior fix |
| [T13](tasks/T13-wipe-on-failure.md) | Don't wipe all metrics on pre-auth connection failure | reliability | M | — | done | 2026-07-16 | patch-worthy behavior fix |
| [T14](tasks/T14-auto-skip-permanence.md) | Re-try auto-skipped methods on profile change / periodically | reliability | S | T11 | done | 2026-07-16 | patch-worthy behavior fix |
| [T15](tasks/T15-duplicate-api-calls.md) | Deduplicate per-cycle API calls (disk.query ×2, service.query ×3, list+count pairs) | performance | M | — | done | 2026-07-16 | performance/no metric contract change; default synthetic scrape 128→117 calls |
| [T16](tasks/T16-expensive-query-cadence.md) | Reduce cadence of server-heavy queries (7-day temp agg, snapshot sort) | performance | S | — | done | 2026-07-16 | performance/no metric name or label contract change; HELP cadence documented |

## P3 — Conventions, security polish, cleanup

| ID | Task | Area | Size | Depends on | Status | Updated | Notes |
|----|------|------|------|------------|--------|---------|-------|
| [T17](tasks/T17-legacy-metrics-blocking.md) | Legacy mode: `/metrics` must not block for the whole poll cycle | performance | M | — | done | 2026-07-16 | performance/no metric contract change |
| [T18](tasks/T18-bind-address-and-log-leak.md) | Configurable bind address + stop hostname leaking via tracebacks | security | S | — | done | 2026-07-16 | minor-version-worthy new env var |
| [T19](tasks/T19-help-and-conventions.md) | HELP/type/naming corrections (gateway_reachable, blkio counters, smb LOCKS, snapshot-oldest HELP, per-disk HELP) | conventions | M | T03 | todo | | |
| [T20](tasks/T20-dead-code-and-docs.md) | Remove dead code and the misleading 230-line version-history docstring | cleanup | S | — | todo | | Do last-ish; low conflict risk |
| [T21](tasks/T21-new-low-cost-metrics.md) | Optional batch: api_key expiry, failover.reboot.info, kmip_sync_pending, v26 interface speed | metric gap | M | T11 | todo | | Stretch; minor-version worthy |

## Discovered during work

Add findings here that you noticed but that are out of scope for your current task. Include
file:line and one sentence. Do not fix them.

- T05 optional follow-up: `reporting.realtime` interface `received_bytes`/`sent_bytes`
  cumulative or interval byte fields are not exported under honest non-rate metric names;
  consider a T21 metric if operators need them.
- T08 dashboard follow-up: consider adding a bundled dashboard panel for recent task
  failures now that `truenas_task_state{state="ERROR|FAILED"}` emits for replication,
  cloudsync, rsynctask, and snapshottask tasks.

## Completed log

Move a one-line summary here when a task reaches `done`:
`T## — <date> — <one-line outcome> — <commit sha>`

- T01 — 2026-07-16 — event stream now detects silently-dead connections via a max-idle
  deadline (`EVENT_READ_TIMEOUT_SECONDS`), reports `truenas_event_stream_up=0` while
  disconnected, and `EVENT_STALE_AFTER_SECONDS` config validation now requires `>= 2x`
  the interval — pending commit
- T02 — 2026-07-16 — CPU user/idle split metrics are no longer fabricated from aggregate
  realtime usage; usage-only payloads leave them absent/NaN while real split fields still export
  — pending commit
- T03 — 2026-07-16 — `truenas_pool_dedup_ratio` remains declared but intentionally absent;
  DDT bytes continue through `truenas_pool_dedup_table_size_bytes` — pending commit
- T04 — 2026-07-16 — realtime pool used/available/total byte gauges now emit from
  `reporting.realtime` while read/write rate probes are documented as opportunistic —
  local commit; minor-version-worthy
- T05 — 2026-07-16 — network rx/tx `_per_second` gauges now ignore cumulative-only
  `received_bytes`/`sent_bytes` payloads and emit only from explicit rate fields —
  local commit; patch-worthy
- T06 — 2026-07-16 — job abortable/transient and reporting-enabled gauges now stay
  absent/NaN on unknown or failed source paths while legitimate zeroes still publish —
  local commit; patch-worthy
- T07 — 2026-07-16 — dataset snapshot counts now emit by default through the documented
  bounded `pool.dataset.snapshot_count` fallback — local commit; minor-version-worthy
- T08 — 2026-07-16 — replication, cloudsync, rsynctask, and snapshottask outcome
  state/last-run metrics now emit from safe selected fields — local commit;
  minor-version-worthy
- T09 — 2026-07-16 — pool vdev read/write/checksum error gauges now emit from
  `pool.query` topology with fail-closed extraction — local commit;
  minor-version-worthy
- T10 — 2026-07-16 — disk temperature alert counts now emit from documented
  `disk.temperature_alerts` rows with fail-closed absence on call failure —
  local commit; minor-version-worthy
- T11 — 2026-07-16 — `PROFILE_UNKNOWN` now uses the true 25.10/26.0
  compatibility intersection and excludes v26-added methods/events — local
  commit; patch-worthy
- T12 — 2026-07-16 — compatibility profile updates are now monotonic and
  lock-guarded, preserving concrete profiles across transient version-detection
  failures while allowing concrete version changes to clear auto-skips — local
  commit; patch-worthy
- T13 — 2026-07-16 — pre-auth scrape failures now preserve the previous
  collector snapshot with `truenas_up=0`, while stale data is bounded by a
  `max(3 * interval, 300s)` guard — local commit; patch-worthy
- T14 — 2026-07-16 — auto-skipped methods now retry on compatibility profile
  changes and after a per-method 24-hour amnesty window — local commit;
  patch-worthy
- T15 — 2026-07-16 — per-cycle duplicate disk/service/list+count calls were
  deduplicated with no metric or config contract change; default synthetic
  scrape fell from 128 to 117 calls — local commit; patch-worthy performance
  fix
- T16 — 2026-07-16 — server-heavy disk temperature aggregate and oldest-snapshot
  sorted queries now refresh every 10 cycles while cached values are re-emitted
  with bounded staleness; no metric name or label contract change — local
  commit; patch-worthy performance fix
- T17 — 2026-07-16 — legacy `/metrics` now serves the last complete snapshot
  without waiting on the scrape lock, with event-driven snapshot refresh
  throttled to one second; no metric contract change — local commit;
  patch-worthy performance fix
- T18 — 2026-07-16 — `EXPORTER_BIND_ADDRESS` now controls HTTP bind host/IP
  with unchanged all-interface default, and configured TrueNAS hosts are
  redacted from preserved traceback logs — local commit; minor-version-worthy
  new env var
