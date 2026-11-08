# 04-version-variability
Status: done
Findings: D6 D12
Blocked by: none

- Disk panels: prefer per-disk series, fall back to `disk="total"` (e.g.
  `x{disk!="total"} or x{disk="total"}`), with descriptions stating 27 behavior.
- Snapshot count panel described as partial when the fallback limit applies.
- Feature-absent sections (VMs, Incus, IPMI, UPS, HA, NVMe-oF, directory
  services) collapse to a compact note instead of empty panels.
Verify with 25.10 fixture shapes (`tests/fixtures/`) and 27 live/mocked shapes.

## Answer
Done 2026-11-07.
- **Disk I/O.** `disk_sel()` = `x{disk!="total"} or (x{disk="total"} unless on(instance) x{disk!="total"})`. It is used for disk throughput, IOPS, busy and Avg Busy, and for the Overview "Storage throughput". Descriptions state the 27 aggregate behaviour.
- **Snapshot counts.** The panel description explains the `DATASET_SNAPSHOT_FALLBACK_LIMIT` partial count on 27.
- **Feature-absent sections.** Grafana cannot hide rows from data, so MC shows a presence strip for VMs ("None" in grey) with the details collapsed. Hardware & IPMI, NVMe-oF/FC/HA, audit/directory and configuration are collapsed rows whose titles say they read N/A when absent.
- **27-only gaps (live-verified).** Pool realtime read/write are absent on 27: Overview uses disk I/O instead and the classic panel says "Not reported by TrueNAS 27". `virt.instance.metrics` is down on 27, so the Incident "Realtime" tile watches `reporting.realtime`.

Checks:
- `tools/mock_exporter.py` profiles 27 and 25.10 reproduce the fixture shapes: aggregate total vs per-disk, CPU split NaN vs present.
- Renders confirm "total" on 27 and per-disk on 25.10, and the CPU note on 27.
- `eval_queries.py` reports 0 errors on both profiles and live.

Limit: 25.10 and 26.0 are mock-only; no live 25.10/26.0 appliance was available.
