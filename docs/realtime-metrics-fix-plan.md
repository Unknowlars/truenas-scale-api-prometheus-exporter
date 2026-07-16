# Realtime Metrics Fix Plan — TrueNAS 25.10 `reporting.realtime` Parser

Status: implemented (parser and dashboard fixes complete; hit-ratio and pool-capacity items deferred)
Date: 2026-07-13
Target: TrueNAS SCALE 25.10.3 (compatibility baseline per AGENTS.md: 25.10.2)

This document hands over a completed diagnosis and a set of proposed fixes.
Read AGENTS.md first: only read-only API calls, preserve the Prometheus
metric contract (names, types, help text, label sets), run
`./scripts/validate.sh` before declaring completion, and record verification
evidence in `docs/modernization/README.md`.

Implementation result: the parser now accepts the observed sibling `cpuN`
shape, retains legacy event shapes, implements the documented user/idle CPU
fallbacks, and has fixture coverage for aggregate disk and interface rates.
The CPU dashboard panels now use total and per-core usage. Realtime pool
capacity is intentionally not mapped into polling-owned metrics, and the
existing API-reported ZFS hit-ratio semantics remain unchanged.

---

## 1. Problem statement

The Grafana dashboards show no data for the CPU Breakdown panels
(`truenas_cpu_user_percent`, `truenas_cpu_system_percent`,
`truenas_cpu_iowait_percent`, `truenas_cpu_idle_percent`,
`truenas_cpu_interrupt_percent`) and several other realtime panels
(per-core CPU, CPU temperature, pool realtime I/O). The owner asked whether
collection was disabled in `.env`. It is not — configuration is correct and
complete. The causes are (a) an upstream API change and (b) parser gaps in
the exporter.

## 2. Diagnosis evidence (verified live 2026-07-13)

Environment: exporter container `truenas-exporter` (image
`truenas-scale-api-prometheus-exporter:local`) on the owner's host, TrueNAS
SCALE 25.10.3 at `wss://192.168.0.238:449/api/current`.

Verified facts:

1. **Config is fine.** `ENABLE_EVENT_STREAMS=true`,
   `EVENT_SUBSCRIPTIONS=reporting.realtime,app.stats,virt.instance.metrics`,
   `EVENT_INTERVAL_SECONDS=2`, all `ENABLE_*` collector toggles on.
   `truenas_event_stream_up` = 1 for all three streams;
   `truenas_event_messages_total{event="reporting.realtime"}` advanced 22
   messages in 40 s (~2 s cadence); zero `truenas_collector_errors_total`.
2. **Live payload shape** (captured via `docker exec` using the exporter's
   own `JsonRpcWsClient`, `core.subscribe` on `reporting.realtime`):

   ```json
   {
     "cpu": {
       "cpu":   {"usage": 25.0, "temp": 47.0},
       "cpu0":  {"usage": 18.0, "temp": 47.0},
       "...":   "… cpu1 through cpu15, same shape …"
     },
     "memory": {
       "arc_size": 15965502736,
       "arc_free_memory": 2456612864,
       "arc_available_memory": 1231847552,
       "physical_memory_total": 33564585984,
       "physical_memory_available": 3850489856
     },
     "disks": {
       "read_ops": 0.64, "read_bytes": 10504,
       "write_ops": 175, "write_bytes": 5710878, "busy": 1.67
     },
     "interfaces": {
       "enp8s0": {"link_state": "LINK_STATE_UP", "speed": 1000,
                   "received_bytes_rate": 33830, "sent_bytes_rate": 61204},
       "...": "… one entry per NIC …"
     },
     "pools": {
       "big_data":  {"available": 3188529774592, "used": 8690991542272,
                      "total": 11879521316864},
       "boot-pool": {"...": "same shape"},
       "new_ssd":   {"...": "same shape"}
     },
     "zfs": {
       "demand_data_hits_per_second": 1781,
       "demand_data_hit_percentage": 0,
       "...": "… hit/miss/accesses per second + *_percentage keys …"
     }
   }
   ```

3. **Upstream API removal**: the 25.10 payload has NO user/system/iowait/
   idle/interrupt CPU split anywhere. Only `usage` and `temp` per core and
   in the `cpu.cpu` aggregate.
4. **Parser gaps** in `src/truenas_exporter/runtime.py::_cache_realtime_event`
   (around lines 1585–1710):
   - Per-core usage: parser searches `cpu_data["per_cpu"]` /
     `cpu_section["per_cpu"]` / `"usage"` — actual data is sibling keys
     `cpu0`…`cpuN`, each `{"usage": float, "temp": float}`. Result:
     `truenas_cpu_core_usage_percent` never populated.
   - CPU temperature: parser searches `temperature`/`temperatures` keys —
     actual data is `temp` inside each `cpuN` entry. Result:
     `truenas_cpu_temperature_celsius` never populated.
   - `disks` aggregate section (read/write ops/bytes, busy) is not parsed —
     `truenas_disk_busy_percent` / read/write rate gauges stay empty even
     though the API sends them every 2 s.
   - `interfaces` per-NIC rates (`received_bytes_rate`, `sent_bytes_rate`,
     `link_state`, `speed`) — check whether
     `truenas_network_rx/tx_bytes_per_second` (see `NETWORK_RX_BYTES_RATE`
     in `src/truenas_exporter/metrics.py`) is wired to this shape.
   - `pools` realtime capacity (used/available/total per pool) is not
     parsed; note the payload has no realtime pool read/write I/O anymore,
     so `POOL_REALTIME_READ/WRITE_BYTES` cannot be populated from this
     event on 25.10.
5. **Memory split removal**: payload has only `physical_memory_total` and
   `physical_memory_available` (plus ARC values). `free`, `cached`,
   `buffers`, and all swap values are gone from the event —
   `truenas_memory_physical_free/cached/buffers_bytes` and
   `truenas_memory_swap_*` stay NaN on 25.10. (Swap may be obtainable from
   a documented read-only method; investigate separately.)
6. **TrueNAS-side bug**: `zfs.demand_data_hit_percentage` reports `0` while
   `demand_data_hits_per_second` = 1781. The exporter faithfully copies the
   bogus 0 into `truenas_zfs_demand_data_hit_ratio`. Hit ratios should be
   derived from hits/misses instead (the Mission Control dashboard already
   does this at query time; fixing it in the exporter must respect the
   deprecation/alias policy since the metric semantics would change).

Reproduce the payload capture (read-only):

```bash
docker exec -i truenas-exporter python - <<'EOF'
from truenas_exporter.transport import JsonRpcWsClient
from truenas_exporter.config import load_config
import json
cfg = load_config()
with JsonRpcWsClient(ws_url=cfg.ws_url, timeout_seconds=20,
                     verify_tls=cfg.verify_tls, ca_file=cfg.ca_file) as c:
    c.authenticate(cfg.api_key)
    c.call("core.subscribe", ["reporting.realtime"])
    while True:
        msg = c.recv_json()
        if msg.get("method") == "collection_update":
            print(json.dumps(msg["params"]["fields"], indent=1)[:4000])
            break
EOF
```

## 3. Proposed fixes (in priority order)

### Fix 1 — Parse the 25.10 realtime payload shape (exporter code)

In `_cache_realtime_event`:

1. **Per-core CPU usage**: iterate `cpu_section` keys matching
   `^cpu\d+$`; emit `truenas_cpu_core_usage_percent{core="cpuN"}` from each
   entry's `usage`. Keep the existing `per_cpu` lookups as fallbacks for
   older payloads — additive parsing only, never remove existing paths.
   Check the existing label name for `CPU_CORE_USAGE_PERCENT` in
   `metrics.py` and keep it unchanged.
2. **CPU temperature**: from the same `cpuN` entries' `temp` field, emit
   `truenas_cpu_temperature_celsius{...}` (verify declared label set; keep
   it). The aggregate `cpu.cpu.temp` can also feed a sensible series if the
   label set allows it.
3. **Disks aggregate**: map `disks.read_ops`, `read_bytes`, `write_ops`,
   `write_bytes`, `busy` to the declared `DISK_READ_OPS_RATE`,
   `DISK_READ_BYTES_RATE`, `DISK_WRITE_OPS_RATE`, `DISK_WRITE_BYTES_RATE`,
   `DISK_BUSY_PERCENT` gauges. Check their declared label sets first — if
   they were declared per-disk and the 25.10 payload is aggregate-only,
   follow the compatibility rules (do not silently change a labeled metric
   to unlabeled; an aggregate may need the documented alias/deprecation
   path or a fixed label value; propose before implementing).
4. **Interfaces**: map per-NIC `received_bytes_rate`/`sent_bytes_rate` to
   the declared network rate gauges if their label sets match (`interface`
   label expected).
5. **Pools realtime capacity**: payload `pools.<name>.{used,available,total}`
   could refresh existing pool capacity gauges between full scrape cycles —
   only do this if it does not fight the polling collector (same metric
   updated from two sources needs a single owner; otherwise skip).
6. **CPU split metrics** (`user/system/iowait/idle/interrupt`): cannot be
   restored on 25.10. Options: leave NaN as-is (current behavior), or
   implement the fallback the help text already promises for
   `truenas_cpu_user_percent` ("falls back to total CPU usage when user
   split is unavailable") — if implementing, apply it exactly as the help
   text describes and leave the others NaN.

Constraints: metric names/types/help/labels are a locked contract
(AGENTS.md, `docs/metrics-contract.json`, and the parity documents under
`docs/`). Purely additive parsing that populates already-declared metrics is
safe. Anything that changes semantics or labels needs the alias +
deprecation route. Add fixture-based unit tests with the payload shape from
section 2 (do NOT commit real captured responses; synthesize equivalent
fixtures). Update `docs/metrics-contract.json` only via its generator if
availability states change.

### Fix 2 — Hit-ratio metrics derived from counters (exporter, optional)

`truenas_zfs_*_hit_ratio` currently mirrors the broken `*_percentage` API
fields. Consider computing ratio = hits / (hits + misses) when the
percentage field is 0-while-hits-nonzero, or documenting the metrics as
unreliable on 25.10. Semantics change → requires the compatibility/alias
policy; dashboards already work around it, so this is lower priority.

### Fix 3 — `.env` additions (owner action, no code)

```dotenv
SCRAPE_ALL_METRICS=true             # extra reviewed read-only telemetry methods
DATASET_SNAPSHOT_FALLBACK_LIMIT=100 # populates per-dataset snapshot counts
```

Then `docker compose up -d` (or restart the container). Leave
`AUTO_DISCOVER_METHODS`, `ENABLE_GENERIC_METHOD_METRICS`,
`ENABLE_GENERIC_EVENT_METRICS` **off** — documented 50k–500k+ series risk.
`ENABLE_FILESYSTEM_LISTDIR` optional, niche value.

### Fix 4 — Dashboard follow-up (after Fix 1 ships)

In `grafana-dashboard/` (regenerate via `build_mission_control.py`; panel
queries are harvested from `operations-center-dashboard.json`, so fix
queries there first):

1. Replace the "CPU Breakdown" mode-split chart with per-core usage
   (`truenas_cpu_core_usage_percent`) + total (`truenas_cpu_usage_percent`);
   the mode-split metrics are permanently empty on 25.10.
2. "Per-Core CPU Usage" and "CPU Temperature per Core" panels will revive
   automatically once samples exist — delete
   `grafana-dashboard/.metric-names-cache.json` and rerun the builder so
   dead-panel relocation re-evaluates.
3. If Fix 3 is applied, "Dataset Snapshot Counts" revives the same way.
4. Re-import: delete the old dashboard in Grafana, import the regenerated
   `truenas-mission-control.json` (same `metadata.name` keeps the URL).

## 4. Verification checklist for the implementing agent

- [x] Unit tests with a synthesized 25.10-shaped realtime fixture cover every
      newly parsed field (per-core usage, temp, disks, interfaces).
- [x] `./scripts/validate.sh` passes (includes coverage gate, metric
      contract, dashboard validation).
- [ ] Live (read-only): `curl http://<host>:9108/metrics` shows samples for
      `truenas_cpu_core_usage_percent`, `truenas_cpu_temperature_celsius`,
      and disk/interface rate gauges within ~2 event intervals of startup.
- [x] No metric name/type/help/label change without alias + deprecation
      documentation.
- [x] Evidence recorded in `docs/modernization/README.md` (dated entry).
- [x] No captured live API responses, hostnames, or keys committed.

## 5. Related context

- `README.md` → "Metric behavior notes" documents the NaN flapping and the
  dashboard-side workarounds shipped on 2026-07-13.
- `docs/modernization/README.md` → 2026-07-13 live-observation entry
  (NaN realtime gauges, broken hit ratios, NaN snapshot timestamp).
- The NaN "flapping" seen on dashboards is the staleness expiry
  (`EVENT_STALE_AFTER_SECONDS=15`) interacting with fields that are never
  present; fields that ARE present update every ~2 s and stay fresh.
