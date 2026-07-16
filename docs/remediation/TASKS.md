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
| [T02](tasks/T02-cpu-user-idle-fabrication.md) | Stop fabricating `cpu_user_percent` / `cpu_idle_percent` | metric value | S | — | todo | | |
| [T03](tasks/T03-pool-dedup-ratio.md) | `pool_dedup_ratio` reports bytes under a ratio name | metric value | S | — | todo | | |
| [T04](tasks/T04-realtime-pool-metrics.md) | Realtime `pools` section: retire dead read/write rates, emit used/available/total bytes | metric value + gap | M | — | todo | | |
| [T05](tasks/T05-network-rate-fallback.md) | Remove cumulative-bytes fallback in network rx/tx rate gauges | metric value | S | — | todo | | |
| [T06](tasks/T06-fabricated-zeros.md) | Eliminate fabricated zeros on partial failure (job flags, reporting_enabled) | metric value | S | — | todo | | |
| [T07](tasks/T07-dataset-snapshot-count.md) | Make `dataset_snapshot_count` actually emit | metric gap | S | — | todo | | |
| [T08](tasks/T08-task-outcome-metrics.md) | Emit replication/cloudsync/rsync/snapshottask outcome state + last-run | metric gap | L | — | todo | | Biggest operational blind spot |

## P2 — Hardening + high-value gaps

| ID | Task | Area | Size | Depends on | Status | Updated | Notes |
|----|------|------|------|------------|--------|---------|-------|
| [T09](tasks/T09-vdev-error-metrics.md) | Re-enable pool vdev read/write/checksum error metrics via `pool.query` topology | metric gap | M | — | todo | | |
| [T10](tasks/T10-disk-temperature-alerts.md) | Wire `disk.temperature_alerts` → `disk_temperature_alert_count` | metric gap | S | — | todo | | |
| [T11](tasks/T11-profile-unknown-intersection.md) | Make `PROFILE_UNKNOWN` a true 25.10∩26.0 intersection | version compat | S | — | todo | | |
| [T12](tasks/T12-profile-thread-race.md) | Fix cross-thread `compatibility_profile` race | reliability | M | T11 | todo | | |
| [T13](tasks/T13-wipe-on-failure.md) | Don't wipe all metrics on pre-auth connection failure | reliability | M | — | todo | | Policy change — read spec carefully |
| [T14](tasks/T14-auto-skip-permanence.md) | Re-try auto-skipped methods on profile change / periodically | reliability | S | T11 | todo | | |
| [T15](tasks/T15-duplicate-api-calls.md) | Deduplicate per-cycle API calls (disk.query ×2, service.query ×3, list+count pairs) | performance | M | — | todo | | |
| [T16](tasks/T16-expensive-query-cadence.md) | Reduce cadence of server-heavy queries (7-day temp agg, snapshot sort) | performance | S | — | todo | | |

## P3 — Conventions, security polish, cleanup

| ID | Task | Area | Size | Depends on | Status | Updated | Notes |
|----|------|------|------|------------|--------|---------|-------|
| [T17](tasks/T17-legacy-metrics-blocking.md) | Legacy mode: `/metrics` must not block for the whole poll cycle | performance | M | — | todo | | |
| [T18](tasks/T18-bind-address-and-log-leak.md) | Configurable bind address + stop hostname leaking via tracebacks | security | S | — | todo | | |
| [T19](tasks/T19-help-and-conventions.md) | HELP/type/naming corrections (gateway_reachable, blkio counters, smb LOCKS, snapshot-oldest HELP, per-disk HELP) | conventions | M | T03 | todo | | |
| [T20](tasks/T20-dead-code-and-docs.md) | Remove dead code and the misleading 230-line version-history docstring | cleanup | S | — | todo | | Do last-ish; low conflict risk |
| [T21](tasks/T21-new-low-cost-metrics.md) | Optional batch: api_key expiry, failover.reboot.info, kmip_sync_pending, v26 interface speed | metric gap | M | T11 | todo | | Stretch; minor-version worthy |

## Discovered during work

Add findings here that you noticed but that are out of scope for your current task. Include
file:line and one sentence. Do not fix them.

- (empty)

## Completed log

Move a one-line summary here when a task reaches `done`:
`T## — <date> — <one-line outcome> — <commit sha>`

- T01 — 2026-07-16 — event stream now detects silently-dead connections via a max-idle
  deadline (`EVENT_READ_TIMEOUT_SECONDS`), reports `truenas_event_stream_up=0` while
  disconnected, and `EVENT_STALE_AFTER_SECONDS` config validation now requires `>= 2x`
  the interval — pending commit
