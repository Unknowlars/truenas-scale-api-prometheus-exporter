# Deep Code Review — TrueNAS SCALE API Prometheus Exporter

Scope: `src/truenas_exporter/` (all 12 modules, ~8,300 lines read in full), `tests/`, verified against
`docs/truenas-api/` (25.10.2) and `docs/truenas-api-v26/` (26.0.0) method/event docs and
`tests/fixtures/`. The repo's own parity/contract reports were treated as claims and checked
against the code. **`./scripts/validate.sh` passes end-to-end** (ruff, mypy, 186 tests, 90% branch
coverage, all `--check` generators, dashboard validation, docker build) — everything below comes
from analysis, not broken CI.

Overall verdict: this is an unusually careful exporter — the zero-vs-absent discipline, the
documented-method allowlisting, and the collector-mode snapshot design are all better than most
exporters in the wild. The significant problems are: a handful of metrics whose *values* are wrong
or misleading (dedup "ratio" carrying bytes, `cpu_user_percent` carrying total CPU), an event
stream that can silently die forever on a half-open TCP connection, ~50 declared metrics with no
producer (several of which the parity report wrongly marks "active"), and a scrape cycle that makes
~120 serial WebSocket round-trips where a fraction would do.

---

## (a) Bugs / wrong metric values (ranked)

### A1 — HIGH — `truenas_pool_dedup_ratio` reports a byte count under a ratio name with a ratio HELP string
`runtime.py:3483–3490`, `metrics.py:128`
The value comes from `pool.query.dedup_table_size`, documented as *"Size of the deduplication
table **in bytes**"* (`docs/truenas-api/methods/pool/query.md:241–250`). The HELP text says
*"Pool deduplication ratio (1.0 means no dedup savings)"*.
**Failure scenario:** a pool with a 1 GiB DDT reports `truenas_pool_dedup_ratio ≈ 1.07e9`; any
dashboard/alert built from the HELP text (`< 1.05` = "no savings") is nonsense. The code comment
calls it a "compatibility alias" and `truenas_pool_dedup_table_size_bytes` exists with the correct
name — but the aliased metric's HELP actively lies, and `tests/test_runtime_api_parity.py:106`
cements the behavior. At minimum fix the HELP; better, deprecate the series (emit nothing) since
no correct value for a "ratio" is available from this field.

### A2 — HIGH — `truenas_cpu_user_percent` silently reports **total** CPU usage on real 25.10/26.0 systems
`runtime.py:1713–1719`; fixture `tests/fixtures/realtime/reporting_realtime_25_10_shape.json`;
v26 doc `docs/truenas-api-v26/events/reporting/realtime.md` (per-core objects expose only
`usage` + `temp`).
The realtime payload on both supported versions has no `user` split, so the fallback
`elif total_cpu_percent is not None: CPU_USER_PERCENT = total` runs on *every* event. Likewise
`truenas_cpu_idle_percent` is fabricated as `100 − total` (`runtime.py:1732–1735`), and
`system`/`iowait`/`interrupt` stay NaN.
**Failure scenario:** a box at 80% CPU that is 75% iowait shows `user_percent = 80` — a dashboard
distinguishing user vs. system load is actively misled. The HELP strings admit the fallback
(`metrics.py:565,568`) and `tests/test_reliability.py:22–24` cements it, but a value that is
*always* the fallback is not a fallback — it's a mislabeled duplicate of
`truenas_cpu_usage_percent`. Emitting NaN (absent) when the split is unavailable would match the
exporter's own zero-vs-absent policy.

### A3 — HIGH — `truenas_pool_realtime_{read,write}_bytes_per_second` never emit on any supported version, yet parity marks them "active dedicated"
`runtime.py:1914–1930`; fixture shows the realtime `pools` section carries
`{available, used, total}` (space, bytes), not `read_bytes`/`write_bytes`; the v26 doc describes
`pools` only as "mapping of stat name to value".
**Failure scenario:** user reads `docs/api-exporter-parity.json` ("implementation_status":
"active dedicated", v5.1 changelog advertises the metric), builds a pool-throughput panel, gets
permanently empty series. This is the worst of both worlds: a dead metric *and* an ignored real
signal — the per-pool `used/available/total` bytes actually present in the payload are dropped on
the floor (see gap B7).

### A4 — MEDIUM — `truenas_network_{rx,tx}_bytes_per_second` can silently emit a *cumulative byte counter* as a rate
`runtime.py:1905–1906`
The code prefers `received_bytes_rate` but falls back to `received_bytes`. In the v26 schema both
are **optional** properties and `received_bytes` is the cumulative total
(`docs/truenas-api-v26/events/reporting/realtime.md`, interfaces section).
**Failure scenario:** a payload that includes only the cumulative fields (allowed by the schema)
makes `truenas_network_rx_bytes_per_second` jump to e.g. `4.7e13` and grow monotonically —
plausible-looking but wrong by ~6 orders of magnitude, and no alert on the exporter side catches
it. The fallback should be removed or mapped to a separate `_total` counter.

### A5 — MEDIUM — `truenas_dataset_snapshot_count` is dead with default config, parity claims "active dedicated"
`runtime.py:2562–2570`, `config.py:152` (`DATASET_SNAPSHOT_FALLBACK_LIMIT=0` default)
`pool.dataset.query` (25.10 doc) has **no** `snapshot_count` field, the query doesn't request one,
and the per-dataset `pool.dataset.snapshot_count` fallback is disabled by default.
**Failure scenario:** default deployment → metric absent for every dataset; the parity report
(`api-exporter-parity.json`: "active dedicated") says otherwise.

### A6 — MEDIUM — Fabricated zeros for job flags when the detail query fails
`runtime.py:1251–1252` + early return at `runtime.py:1279`
`JOB_ABORTABLE_ACTIVE_COUNT` and `JOB_TRANSIENT_ACTIVE_COUNT` are set to `0` *before* the detail
query. If the count queries succeed (`truenas_job_active_count = 7`) but the detail query fails,
both flags stay `0` — "API didn't answer" masquerading as "zero abortable jobs". This is exactly
the fabricated-zero pattern the rest of the codebase carefully avoids. Same pattern:
`REPORTING_ENABLED.set(0)` at `runtime.py:4810` when `service.query` returns an empty match (the
service name may simply not exist under the queried names on that version — "unknown" reported
as "disabled").

### A7 — MEDIUM — `truenas_network_gateway_reachable` measures route *presence*, not reachability
`runtime.py:3030–3041`, `metrics.py:179`
HELP: "1 if the default IPv4 gateway is reachable". The value is "a default route exists in
`route.system_routes`". A dead gateway with a configured route reports `1`.
Acknowledged in comments and parity ("deprecated compatibility",
`truenas_network_default_gateway_configured` is the honest twin), but the misleading series and
HELP still ship and will be alerted on by name.

### A8 — LOW — `truenas_app_blkio_{read,write}_bytes` are cumulative counters registered as gauges without `_total`
`metrics.py:646–647`, `runtime.py:1653–1660`; `docs/truenas-api/events/app/stats.md` ("Blkio read
bytes" — cumulative container block-I/O totals).
`rate()` over a gauge works numerically, but the type/naming contract is wrong and counter resets
(container restart) will look like negative-delta artifacts in gauge-oriented panels. Should be
`Counter`-typed `..._total` (or documented as cumulative in HELP).

### A9 — LOW — `truenas_smb_open_file_count` counts LOCKS, not open files
`runtime.py:2860–2864`: `("LOCKS", SMB_OPEN_FILE_COUNT)`. smbstatus "locks" ≠ open files (one file
can hold several locks; oplocks/leases counted differently). Off-by-semantics on v26.

### A10 — LOW — `truenas_snapshot_oldest_timestamp_seconds` HELP promises "(0 if no snapshots)" but the code leaves it NaN
`metrics.py:754` vs `runtime.py:4475–4483`. The NaN behavior is the *better* one; the HELP is wrong.

### A11 — LOW — Realtime disk I/O labels: on 25.10 the payload is aggregate-only, so `{disk="total"}` is the only series
`runtime.py:1885–1889`; fixture `disks` section is flat totals. HELP says "per disk"
(`metrics.py:585–589`). Not wrong values, but the label contract implied by HELP/name never
materializes on 25.10.

---

## (b) Missing-metric opportunities

The exporter already declares several of these metrics — they're registered, documented in the
contract, and never populated (parity honestly marks most "unavailable", but the fields are
practically obtainable):

| API method (version) | Field(s) | Proposed metric (type, labels) | Notes |
|---|---|---|---|
| `replication.query` | `state.state`, `state.datetime`, `state.error` | `truenas_task_state{task_type,name,state}` (gauge, exists dead at `metrics.py:302`), `truenas_task_last_run_timestamp_seconds` (exists dead) | Doc types the `state` object opaquely, but it's the stable middleware `EphemeralState` (`FINISHED`/`ERROR`/`RUNNING`). This is the #1 operational gap: **replication failures are currently invisible.** |
| `cloudsync.query` | `job.state`, `job.progress.percent`, `job.time_finished` | same `truenas_task_state` family + `truenas_cloudsync_progress_percent{name}` | select `["id","enabled","job.state",...]` keeps credentials out. |
| `rsynctask.query` / `pool.snapshottask.query` | `job.*` / `state.state` (documented: "Current state of the task", 25.10 doc line 926) | same family | snapshottask `state` **is** a documented string. |
| `reporting.realtime` event | `pools.<name>.{used,available,total}` (fixture-proven) | `truenas_pool_realtime_{used,available,total}_bytes{pool}` (gauge) | Replaces the dead read/write-rate mapping (A3). |
| `disk.temperature_alerts` | alert rows per disk | `truenas_disk_temperature_alert_count{disk}` (gauge — **already declared dead**, `metrics.py:169`) | Callable exactly like `disk.temperature_agg` with the disk-name list (`runtime.py:3571`). |
| `pool.query` | `topology.data[].children[].stats.{read_errors,write_errors,checksum_errors}` | `truenas_pool_vdev_{read,write,checksum}_errors{pool,vdev}` (declared dead, `metrics.py:652–666`; walker exists at `runtime.py:2818–2844` but topology is never selected, `runtime.py:3436`) | Schema is "object (opaque)" in docs, but the walker was written and tested once; a guarded re-enable restores the most important ZFS health signal the exporter lost. |
| `zpool.query` (v26 only) | explicit `topology`/`scan`/`properties` options, `status_code`, `status_detail` | `truenas_pool_status_code{pool,code}` info-gauge; vdev errors as above | Brand-new documented API in the v26 corpus; exporter ignores the whole `zpool.*`/`zfs.tier` namespaces on 26.0. |
| `reporting.realtime` (v26) | `interfaces.<n>.speed` (Mbit/s), `link_state` | `truenas_interface_speed_mbits{interface}` (gauge) | Documented required fields on v26. |
| `api_key.query` | key count, `expires_at` | `truenas_api_key_count`, `truenas_api_key_expiry_timestamp_seconds{name}` | In `TELEMETRY_CANDIDATE_METHOD_ALLOWLIST` but never referenced; security-hygiene metric analogous to cert expiry. |
| `failover.reboot.info` | per-node reboot-required | `truenas_failover_node_reboot_required{node}` (gauge) | Documented, read-only, unreferenced. |
| `kmip.kmip_sync_pending` | boolean | `truenas_kmip_sync_pending` | Trivial; already allowlisted. |
| `pool.dataset.query` | `extra: {"snapshot_count": true}` (undocumented but live) | make existing `truenas_dataset_snapshot_count` real (A5) | Or raise `DATASET_SNAPSHOT_FALLBACK_LIMIT` default above 0. |

**Inverse (claimed covered, not actually emitted):** `truenas_pool_realtime_read/write_bytes_per_second`
(A3), `truenas_dataset_snapshot_count` (A5), and `truenas_cpu_user_percent`'s parity row claims
field `cpu.user` while the emitted value is the total (A2). Beyond those three overclaims, the
parity report is honest: 48 declared metrics are explicitly marked "unavailable: no reachable
producer" (`metric_disposition_partition`), including all `MEMORY_SWAP_*`, `MEMORY_PHYSICAL_
{FREE,CACHED,BUFFERS}`, `ZFS_ARC_{MAX,MIN}_SIZE`, `ZFS_ARC_HIT_RATIO/HITS/MISSES`, `SMART_TEST_*`,
`FC_PORT_SPEED/ONLINE`, `UPS_*`, `TN_CONNECT_*`, `TRUECOMMAND_STATUS`, `KMIP_ENABLED`,
`SSH_PASSWORD_AUTH`, `CONSOLEMENU/SERIALCONSOLE`, `DATASET_REFERENCED_BYTES` — these are exposed
as permanent NaN scalars or absent labeled series.

---

## (c) Performance

### C1 — ~120–130 **serial** WebSocket round-trips per poll cycle, fresh TLS connection every cycle
`runtime.py:3113–3761` — every collector awaits one call at a time over a single
`JsonRpcWsClient`; a new connection + `auth.login_with_api_key` happens each cycle
(`runtime.py:3253`, default every 30 s). There is no concurrency, no `core.bulk`, and no
connection reuse. On a LAN this is a few seconds per cycle; on a loaded middleware or WAN it eats
most of the 25 s budget, and the budget expiry (`transport.py:79–84`) then truncates *later*
collectors every cycle (the tail of the collector list is systematically the first to go absent).

### C2 — Duplicate calls per cycle
- `disk.query` twice: main pass `runtime.py:3544` and `_collect_disk_extended_metrics`
  `runtime.py:2952` (different selects; one merged select would do).
- `service.query` three times: `runtime.py:3638`, plus `_query_service_enable_map` at
  `runtime.py:4577` and again at `runtime.py:4803`.
- `vm.query` full list is fetched (`runtime.py:2273`) and then **unused** when
  `ENABLE_GENERIC_METHOD_METRICS=false` (the default) — only the separate count query matters.
- ~15 collectors do a *list query + separate `count:true` query* for the same method
  (datasets `runtime.py:2465+2525`, each task type `runtime.py:2640–2684`, scrub, cloud_backup,
  cronjob, boot envs, virt instances…). Where the list is already fetched with a limit, the count
  is only needed when `len(items) == limit`; that would remove ~15 round-trips.

### C3 — Server-heavy queries every 30 s
- `disk.temperature_agg(disk_names, days=7)` (`runtime.py:3571`) asks middleware to aggregate a
  week of netdata temperature history per disk, per cycle.
- `pool.snapshot.query` with `order_by: properties.creation.parsed` (`runtime.py:4463`) forces a
  server-side sort of the full snapshot set (100k snapshots on busy systems) every cycle to fetch
  one row.

### C4 — `/metrics` under concurrent scrapes
- **Collector mode (default): correct and cheap.** `/metrics` serves an immutable snapshot tuple
  behind `_snapshot_lock` (`runtime.py:898–906`, `http.py:59–62` with `lock_metrics=False`);
  scrapes never observe a half-updated cycle and never block on the poll.
- **Legacy mode: `/metrics` blocks for the entire poll cycle.** `http.py:59–61` takes
  `exporter._lock`, which `scrape_once` holds for the whole multi-second serial API pass
  (`runtime.py:3119`). With Prometheus' default 10 s scrape timeout and a poll cycle that can
  legitimately run to `SCRAPE_BUDGET_SECONDS=25`, every scrape that lands mid-cycle times out.
  Consistency is preserved, availability isn't.

### C5 — Memory over weeks: no unbounded growth found
Verified: labeled poll gauges are cleared every cycle (`_reset_poll_metrics`, `runtime.py:778`);
event series are replaced wholesale per event and pruned via `_replace_event_metric_series` diffing
(`runtime.py:1007–1026`); removed disks/pools/datasets disappear on the next cycle;
`API_CALL_SUCCESS/DURATION` are cleared each cycle (`runtime.py:3249–3250`) so removed methods
don't zombie; counters have bounded label sets (`_status_like` allowlist kills the old cardinality
bug). The one warned foot-gun is real but opt-in: `METHOD_*`/`EVENT_*` generic metrics with
`AUTO_DISCOVER_METHODS` can hit 50k–500k series (warned at `metrics.py:534–541`).

---

## (d) Reliability

### D1 — HIGH — The event stream never detects a silently dead TCP connection; `truenas_event_stream_up` stays 1 forever
`runtime.py:2047–2054`, `transport.py:102–105`
After subscribing, the loop only ever calls `recv()` with a 15 s socket timeout;
`WebSocketTimeoutException` is treated as "quiet period" and loops forever. No WebSocket ping is
ever sent, and there is no "no message in N seconds → reconnect" rule — even though
`reporting.realtime` is contractually a ≤ `event_interval` heartbeat, so silence *is* failure.
**Failure scenario:** NAS power-cycles / NAT or firewall drops the idle mapping / cable pull → no
FIN/RST → `recv` times out every 15 s indefinitely. Event metrics correctly expire to NaN
(`_expire_stale_events`), but the stream never reconnects until the process restarts, and
`truenas_event_stream_up{event=...}` **stays 1.0** (it's only set to 0 in the unsubscribe/error
paths, `runtime.py:2087,2102`) — the one metric a dashboard would alert on reports healthy.
Fix: force a reconnect (or send a ping / `core.ping`) when no `collection_update` arrives within
`event_read_timeout_seconds`; the config knob already exists (`config.py:147`) but its value is
neutered by `min(..., event_stale_after_seconds)` at `runtime.py:1996–1999`.

### D2 — MEDIUM — `PROFILE_UNKNOWN` is the v26 profile, not the advertised "common intersection"
`compat_profiles.py:153–164` (`target_version="common-intersection"` but
`reviewed_methods=_V26_METHODS`, which *includes* `V26_ADDED_METHODS`).
**Failure scenario:** a transient `system.version_short` failure on a healthy 25.10 box
(`runtime.py:946–955`) selects "unknown" → that scrape calls v26-only `container.query`/`smb.status`
(fail → collector errors) and **blocks** `virt.instance.query`/`reporting.*graphs` as "removed" →
virt metrics absent for the cycle. Against a genuinely unknown version (24.x, 27.x) the exporter
runs the v26 surface rather than a safe intersection. The docstring and the code disagree; one of
them is wrong.

### D3 — MEDIUM — `compatibility_profile` is racily shared between the scrape and event threads
Both threads run `_bootstrap_connection` (`runtime.py:939–967`; event thread at `runtime.py:2003`)
and assign `self.compatibility_profile`, which the *other* thread consults on every
`_require_profile_method` call mid-cycle. A version-detection hiccup in the event thread can flip
the scrape thread onto the unknown profile halfway through a scrape (amplifying D2). Profile
detection should be per-connection or write-once.

### D4 — MEDIUM — One failed cycle wipes *all* polled metrics (absent-on-failure), including in collector mode
`runtime.py:3124` (reset at cycle start) + `runtime.py:3763–3774` (snapshot published even on
failure). A single connect/auth failure at second 0 of a cycle empties every polled series until
the next successful cycle (≥30 s). `truenas_up=0` does surface it, and absent-is-better-than-stale
is a defensible policy — but resetting *after* a successful connection+auth (or keeping the
previous snapshot on total connection failure, with `truenas_up=0`) would avoid turning a 1-second
network blip into a 30–60 s hole across ~400 series. Partial failure *within* a connected cycle is
handled well: each collector has its own try/except, failures increment
`truenas_collector_errors_total{collector=...}` / `truenas_api_call_success{method=...}=0`, and
other collectors proceed.

### D5 — LOW — `_auto_skipped_methods` is permanent for the process lifetime
`runtime.py:764,1437–1443`. A method that once returned "method not found" (e.g. while the wrong
profile was active during a D2/D3 episode, or before a feature was enabled server-side) is never
retried, even across profile re-detection or a TrueNAS upgrade mid-run.

### D6 — Positive findings (verified, no action)
Timeouts exist on every remote call path: connect timeout (`transport.py:51–55`), per-recv socket
timeout, and a monotonic whole-scrape deadline threaded into `call()` (`transport.py:79–84`).
Reconnect uses exponential backoff 2→120 s with reset-on-success (`runtime.py:2045,2106–2108`) and
**does** re-subscribe all events after reconnect. Auth happens per connection, so session expiry
self-heals. Shutdown handles SIGTERM/SIGINT and joins both threads with bounded timeouts
(`runtime.py:5077–5095`). No fire-and-forget tasks (threaded, not asyncio — the "blocking calls in
the event loop" concern doesn't apply; the two worker threads are the design).

---

## (e) Everything else (conventions, security, oddities)

1. **Bind address is hardcoded to all interfaces** — `make_server("", port, ...)`
   (`http.py:64`); no `EXPORTER_BIND_ADDRESS` env. Fine in a container, surprising on a host
   install: `/metrics` (full system inventory incl. hostnames, dataset names, GPU/PCI info) is
   exposed on every interface unauthenticated.
2. **API key handling is clean** (verified): never logged, not in exception messages, `_LANDING_PAGE`
   static, `main()` even redacts the hostname from its own startup log (`runtime.py:5046–5052`).
   One inconsistency: `LOG.warning(..., exc_info=True)` / `LOG.exception("Scrape failed")`
   (`runtime.py:2105,3764`) print tracebacks whose connection-error messages typically contain the
   TrueNAS host/IP — violating the code's own "no hostname is ever logged" invariant.
3. **TLS**: `TRUENAS_VERIFY_TLS` defaults to true; the false-path sets `CERT_NONE` +
   `check_hostname=False` explicitly (`transport.py:46–50`); custom CA supported. Good.
4. **~50 permanent-NaN scalar series** are always exposed (unlabeled dead gauges can't be
   "absent" in prometheus_client — they render as `NaN`). Harmless to PromQL comparisons but
   noisy, inflates the exposition, and confuses users diffing against the contract. Consider
   registering producerless metrics lazily.
5. **`docs/metrics-contract.json` is generated and CI-enforced** (`scripts/
   generate_metric_contract.py`, `validate.sh` runs `--check`) — but it is a contract of
   *declarations* (`METRIC_SPECS`), not of emissions; nothing in CI fails when a declared metric
   loses its producer. The parity generator does track producer evidence via AST, but its
   field-mapping tables are hand-maintained inside the script ("The mappings below are
   authoritative", `generate_api_exporter_parity.py:1517–1520`) — which is exactly where the A3/A5
   overclaims live.
6. **Non-base units by design**: `truenas_certificate_days_to_expiry` (days; the
   `_timestamp_seconds` twin exists — good), `truenas_audit_retention_days`,
   `truenas_ntp_server_{min,max}_poll_minutes`, dead `truenas_fc_port_speed_gbit`. Tolerable but
   flagged per convention.
7. **Naming/HELP quality otherwise good**: consistent `truenas_` prefix, `_info` pattern used for
   identity (`truenas_host_info`, `truenas_exporter_info`, `truenas_gpu_info`), no client-side
   timestamps anywhere, serials redacted (`DISK_INFO serial="redacted"`, `runtime.py:2975`),
   directory-services fault reason redacted. UUID labels limited to stable 1-series cases
   (`host_id`, `global_id`) with the reboot-scoped `boot_id` correctly converted to a counter.
8. **Dead code**: `_merge_event_snapshot` (`runtime.py:793`) is only called from tests;
   `_collect_smart_test_results` / `_collect_ups_metrics` / `_collect_tn_connect` /
   `_collect_truecommand_status` / `_collect_disk_used_metrics` are documented no-op stubs; the
   vdev walker (A/B above). The 230-line version-history docstring at the top of `runtime.py`
   describes many behaviors (12 default event subscriptions, pool.scan/alert.list events, vdev
   errors) that **no longer exist** — the real default subscriptions are just 4
   (`api_catalog.py:749–754`) — actively misleading for maintainers.
9. **Tests cementing wrong behavior**: `tests/test_reliability.py:22–24` (user%=total,
   idle%=100−total), `tests/test_runtime_api_parity.py:106` (dedup bytes into ratio metric).
   `test_removed_source_suppression.py` is fine — it guards real v26 suppression.
10. **Config foot-gun**: `EVENT_INTERVAL_SECONDS` may equal `EVENT_STALE_AFTER_SECONDS`
    (validation is `>=`, `config.py:109`); at equality every event arrives exactly at expiry and
    event metrics flap present/absent. Staleness should be validated as ≥ 2× interval.
11. `smb.status` info-level strings (`SESSIONS`/`SHARES`/`LOCKS`, `runtime.py:2860`) are
    unverifiable against the committed v26 doc (enum values were lost in doc conversion) — worth a
    live-system check; a wrong literal would fail silently into debug logs.

---

## Answers to the explicit questions

**1. Zero-vs-absent-vs-stale policy.** Intended and mostly implemented policy: *never fabricate.*
Polled metrics are wiped at the start of each cycle (labeled → removed, scalars → NaN,
`runtime.py:778–791`) and only set from successfully parsed documented fields; "API said 0" is
emitted, "API didn't answer" is absent. Event metrics are cached with per-event freshness and
expire to absent after `EVENT_STALE_AFTER_SECONDS` (15 s) — the exporter does **not** serve last
values forever. Counters persist across cycles. Exceptions to the policy: A2 (user%/idle%
fabricated from total), A6 (`job_abortable/transient=0` and `reporting_enabled=0` on partial
failure), A7 (semantic fabrication), and the D4 nuance that a whole-cycle failure converts
*everything* to absent at once.

**2. TrueNAS unreachable at startup.** The exporter starts fine (no API access in `main()`/
`__init__`). In default collector mode `/metrics` serves the initial snapshot: exporter
self-metrics plus `truenas_up 0` after the first failed cycle; all target gauges NaN/absent.
`/healthz` returns 200 (process liveness only); `/readyz` returns 503 until a scrape succeeds
(`runtime.py:884–893`, `http.py:53–57`). Correct behavior for k8s-style probes.

**3. Worst-case series count (100 datasets / 20 disks / 10 VMs), default config.** Roughly
**4,000–4,500 series**: ~25 per-dataset gauges × 100 ≈ 2,500; disks ≈ 20 × (5 realtime + 5 poll +
3 temp-agg) ≈ 260 (25.10 realtime is aggregate-only, so realtime disk I/O may be just 5 series);
`truenas_api_call_{success,duration}` ≈ 2 × ~115 methods ≈ 230; apps/VM/interfaces/alerts/services
a few hundred; ~350 scalar singletons. **Nothing scales per-snapshot** — snapshots contribute
exactly two scalars (count + oldest timestamp). The explosion risk is entirely behind the
default-off `ENABLE_GENERIC_METHOD_METRICS`/`AUTO_DISCOVER_METHODS`/`SCRAPE_ALL_METRICS` flags
(warned in `metrics.py:534`: 50k–500k+).

**4. Contract provenance/enforcement.** `docs/metrics-contract.json` is machine-generated from
`METRIC_SPECS` in `metrics.py` by `scripts/generate_metric_contract.py` and enforced in
`scripts/validate.sh` via `--check` (drift fails validation), alongside the parity, manifest, and
dashboard generators. Caveat in (e)5: it freezes declarations, not emission behavior.

**5. Scrape-timing-dependent values.** No client-side rate computation exists — every `_per_second`
value is pre-computed by TrueNAS (realtime event stream), so Prometheus scrape interval cannot
corrupt values. Two timing couplings to know about: (i) in default collector mode, event-stream
gauges are only re-published into the served snapshot at the end of each poll cycle
(`runtime.py:3767–3774`), so "realtime" CPU/disk/network gauges are effectively sampled at
`SCRAPE_INTERVAL_SECONDS` (30 s) + cycle duration, not at the 2 s event cadence — spikes shorter
than the poll interval are invisible regardless of Prometheus scrape interval; (ii)
`truenas_scrape_duration_seconds`/staleness interact with the fixed 25 s budget: cycles that
overrun lose their tail collectors (C1). `disk.temperature_agg` always uses a fixed 7-day window
independent of any interval.

---

## Suggested priority order

1. D1 (event-stream dead-connection reconnect + honest `event_stream_up`) — silent, permanent data loss.
2. A2 + A1 (stop fabricating `cpu_user_percent`; fix/deprecate `pool_dedup_ratio`) — wrong values on every system.
3. B-row 1–4 (replication/cloudsync/rsync/snapshottask outcome state — the declared-but-dead `truenas_task_state`) — biggest operational blind spot.
4. A3/A5 parity overclaims + realtime pools bytes remap.
5. D2/D3 (unknown-profile semantics + profile race).
6. C1/C2 (batch or parallelize the serial call storm; drop duplicate/count-only round-trips).
