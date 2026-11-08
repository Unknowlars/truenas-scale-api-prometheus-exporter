# Dashboard overhaul closeout (2026-11-07)

Scope: fix live-review findings D1–D15
([dashboard-live-review-2026-11-07.md](dashboard-live-review-2026-11-07.md))
and redesign **TrueNAS · Mission Control**. Brief and per-issue answers:
`.scratch/dashboard-overhaul/` (spec plus issues 01–06).

## Evidence types

| Kind | What was used | Committed? |
|---|---|---|
| **Mocked** | `.scratch/dashboard-overhaul/tools/mock_exporter.py`: a synthetic exporter built from `docs/metrics-contract.json` with fictional names (host `nas-demo`, pools `tank`/`flash`, generic app names). It has two profiles: `27` (aggregate `disk="total"` I/O, CPU split NaN, no pool realtime I/O) and `25.10` (per-disk I/O, CPU split). It deliberately reproduces D1, D2, D3, D10, D12 and D13. Six hours of history are backfilled with `promtool tsdb create-blocks-from openmetrics`. | All screenshots in this doc and in `grafana-dashboard/screenshots/` |
| **Empty** | Prometheus with no scrape targets (`mock_stack.sh empty`) | `*-empty.png` |
| **Live** | Owner's 27.0.0-RC.1 NAS, owner-supplied session key (mode 600, outside the repo), exporter `:validate` image, Prometheus v3.5.0, Grafana 13.0.1, all on localhost-only ports | **No**. Renders and responses stayed in the session scratchpad; only the non-sensitive conclusions below are recorded. |

Tools: Grafana 13.0.1, grafana-image-renderer `latest` (sha256:a7970b826f6e…),
Prometheus v3.5.0 (and promtool from that image), Python 3.12.3. The renders
are 1600 px wide; the committed copies are trimmed and quantized.

## Result

- **D1–D15:** all fixed, or justified where Grafana itself limits the fix (see the table).
- **Mission Control:** a new hero Overview ("Is my NAS OK?" verdict plus the health checks behind it), a new **Incident** tab, per-pool cards repeated by `$pool`, question-led titles, drill-down links, one semantic palette, and feature sections that collapse when unused.
- **Missing data:** an empty Prometheus renders **no green or red value tile** in any of the 13 Mission Control tabs or the 19 classic rows. Every value reads grey **N/A**. The only coloured pixels left are the gauge threshold scale and the tab emoji.
- **PromQL:** 0 errors on mock 27, mock 25.10 and live. Every empty query is classified (below).
- **Validation:** `./scripts/validate.sh` exits 0 with `validation_ok` (400 tests, 91.88 % coverage). Both generators pass `--check`.

| Count | Before | After |
|---|---|---|
| Classic panels (`validate_dashboard.py`) | 370 | 367 |
| Classic metric references | 364 | 356 (the 8 unreliable `*_ratio` metrics removed, D2) |
| Mission Control elements | 369 | 379 |
| Mission Control tabs | 12 | 13 (+ 🚑 Incident) |

The UIDs (`truenas-operations-center-3`, `truenas-mission-control`), the
`DS_PROMETHEUS` variable and all template variables are unchanged. No
exporter metric, collector, HELP text or label changed.

## Owner decisions

1. **RAM vs ARC (D14): show both.** "RAM excl. ARC" = (used − ARC) ÷ total, with thresholds at 80/92 %. "RAM incl. ARC" is informational, with no thresholds. Both appear in the Mission Control hero, Compute and the classic Memory row.
2. **Incident tab: added.** It holds outstanding/critical alerts, bad pools, enabled-but-stopped services, failing API calls, collector errors, data age and the realtime stream, plus a "What needs attention right now?" table, a "What changed in this time range?" table and error/poll trends.

## Design decisions (made autonomously)

- **One palette.** It is defined once in `scripts/generate_truenas_dashboard.py`: OK `#37A85B`, warn `#E8A33D`, critical `#E0464E`, info `#3D8BEA`, neutral `#7B828C`, accent `#9E6CDB`. `finalize()` rewrites Grafana colour names in both dashboards, and Mission Control imports the module.
- **Honest no-data.** Grafana paints "No data" with the *base threshold colour*, which is why an empty tile showed red or green. Every stat, bar gauge and gauge now has a neutral base step, `noValue: "N/A"`, and null/NaN → N/A mappings. The validator enforces this.
- **When absence means zero.** `or vector(0)` is never a result on its own. "Absence means zero" is written `… or on() (0 * max(truenas_up == 1))`, so it reads 0 only while the exporter is up and N/A otherwise. It is used for: critical/warning alerts, running services, scanning now, enabled tasks, enabled cloud backups, update available, reboot reason, API/collector errors (1h), and the Incident counters. `vector(0)` remains only as a subtrahend fallback (dismissed alerts, ARC size).
- **Health verdict.** It takes the worst of eight 0/1/2 checks, each listed in "Health checks". Thresholds: pool 80/90 %, disk 45/55 °C, data age 5/15 min. The data-age bands were widened from 2/10 min after live data showed a normal 25–56 s age with 30 s polling plus about 10 s of collection.
- **Feature-absent sections.** VMs show a "what is configured?" strip ("None" in grey) with the details collapsed. Hardware & IPMI; NVMe-oF/FC/HA; audit and directory services; and system configuration are collapsed rows whose titles say they read N/A when absent. The whole row cannot be hidden at runtime (Grafana has no data-driven row visibility), so it collapses instead.
- **State timelines.** Grafana 13.0.1 ignores value mappings, both value and range types, in state timelines and prints threshold ranges ("-∞+", "1+"). I verified this with four variants. The remaining three timelines colour by thresholds built from the 0/1 mapping, hide the misleading labels and legend, and name the colour key in the description. Where the current state matters, a table or a `textMode: name` stat replaces the timeline (SMB encryption, boot scan state/status, API method success, Incus running state).
- **Bar gauges.** Fixed 30–36 px rows with the name on top and explicit text sizes. `topk`/`bottomk` are wrapped in `sort_desc`/`sort` on instant queries, because the live check showed bars ordered alphabetically, not by value.

## Per-finding resolution

| # | Resolution | Verified |
|---|---|---|
| D1 | All "alerts" tiles and the verdict use `clamp_min(sum(alert_count) − (sum(dismissed) or vector(0)), 0)`. "Dismissed" stays a separate tile, and Alert Count Over Time shows outstanding, dismissed and all. The validator requires this expression. | Mock 4/3 → **1**; live 6/5 → **1** |
| D2 | Every ARC/L2ARC % comes from rates: `100 * sum(hits/s) / (sum(accesses/s) > 0)`. A zero denominator gives N/A. The validator rejects `*_hit_ratio`, `*_miss_ratio` and `*_hit_percentage`. | Mock 98.5 %; live 99.7 % (was 0 %) |
| D3 | A single "Directory Svc" state: DISABLED = grey "Disabled", HEALTHY green, JOINING/LEAVING amber, FAULTED red. The status table maps colours, and Dir Faults 0 = "None". | Mock and live: grey Disabled |
| D4 | No "-∞+" anywhere (see State timelines above). Every stat has value and N/A mappings. API Method Success is now a table with failures first. | Mock render |
| D5 | Disk Sizes, Tasks by Type and Alert Classes are now bar gauges with `{{disk}}`, `{{task_type}}` and `{{klass}}` legends. | Mock render |
| D6 | Disk panels use `x{disk!="total"} or (x{disk="total"} unless on(instance) x{disk!="total"})`, with descriptions explaining the 27 aggregate behaviour. Overview "Storage throughput" uses the same fallback. | Mock 27: "total"; mock 25.10: per-disk; live: total |
| D7 | Neutral base plus N/A everywhere, and gated zeroes (above). | Empty-Prometheus renders, pixel check |
| D8 | At most 8 tiles per row (`reflow()`). Titles are shortened to fit (`TITLE_LIMITS`, enforced by the validator). | 1600 px renders |
| D9 | The tip text no longer contains `$variables` (it names the pickers). | Classic render |
| D10 | `clamp_max(pool_scan_percent, 100)`, axis 0–100. Boot scan % is clamped too. | Mock 101.39 → 100 %; live 101.39 → 100 % |
| D11 | CPU Time Breakdown queries `>= 0`. With no data it shows "Not reported by TrueNAS 27 (usage only)"; it is half width, and the duplicate panel was removed. | Mock 27 note; mock 25.10 data |
| D12 | The Dataset Snapshot Counts description states the 27 fallback limit (`DATASET_SNAPSHOT_FALLBACK_LIMIT`, default 25) and points to the total. | Description |
| D13 | Every disk-temperature query filters `> 0`, including the inventory and peak aggregate. | Mock and live: the 0 °C USB disk is excluded |
| D14 | Both figures shown (owner decision). | Mock and live |
| D15 | Duplicate per-core CPU panel removed. Legends are lists unless they fit. Bar-gauge text is readable. The empty reservation box reads "No datasets have a reservation". Incus running state is a table. Alert services lead with type and label the numeric `name` as "ID", and tasks show "Task (name or ID)" (no name label exists; see proposal 2). MTU unit is `none`, and the datasource variable label is "Datasource". | Mock and live renders |

## Before and after (mock data, dark theme)

Before = the committed dashboards at HEAD (`04ca8b1`) rendered against the same
mock. Full-resolution after-images, including light-theme and empty-Prometheus
variants, are in `grafana-dashboard/screenshots/`.

| Tab | Before | After |
|---|---|---|
| Overview | ![](dashboard-overhaul-2026-11-07/before/mc-00-overview.png) | ![](dashboard-overhaul-2026-11-07/after/mc-00-overview.png) |
| Incident (new) | — | ![](dashboard-overhaul-2026-11-07/after/mc-01-incident.png) |
| Compute | ![](dashboard-overhaul-2026-11-07/before/mc-01-compute.png) | ![](dashboard-overhaul-2026-11-07/after/mc-02-compute.png) |
| Pools & ZFS | ![](dashboard-overhaul-2026-11-07/before/mc-02-pools-zfs.png) | ![](dashboard-overhaul-2026-11-07/after/mc-03-pools-zfs.png) |
| Datasets | ![](dashboard-overhaul-2026-11-07/before/mc-03-datasets.png) | ![](dashboard-overhaul-2026-11-07/after/mc-04-datasets.png) |
| Disks & Hardware | ![](dashboard-overhaul-2026-11-07/before/mc-04-disks-hardware.png) | ![](dashboard-overhaul-2026-11-07/after/mc-05-disks-hardware.png) |
| Network | ![](dashboard-overhaul-2026-11-07/before/mc-05-network.png) | ![](dashboard-overhaul-2026-11-07/after/mc-06-network.png) |
| Shares & Protocols | ![](dashboard-overhaul-2026-11-07/before/mc-06-shares-protocols.png) | ![](dashboard-overhaul-2026-11-07/after/mc-07-shares-protocols.png) |
| Apps & Docker | ![](dashboard-overhaul-2026-11-07/before/mc-07-apps-docker.png) | ![](dashboard-overhaul-2026-11-07/after/mc-08-apps-docker.png) |
| VMs & Virt | ![](dashboard-overhaul-2026-11-07/before/mc-08-vms-virt.png) | ![](dashboard-overhaul-2026-11-07/after/mc-09-vms-virt.png) |
| Alerts & Jobs | ![](dashboard-overhaul-2026-11-07/before/mc-09-alerts-jobs.png) | ![](dashboard-overhaul-2026-11-07/after/mc-10-alerts-jobs.png) |
| Security & Audit | ![](dashboard-overhaul-2026-11-07/before/mc-10-security-audit.png) | ![](dashboard-overhaul-2026-11-07/after/mc-11-security-audit.png) |
| Exporter & Config | ![](dashboard-overhaul-2026-11-07/before/mc-11-exporter-config.png) | ![](dashboard-overhaul-2026-11-07/after/mc-12-exporter-config.png) |
| Classic (top) | ![](dashboard-overhaul-2026-11-07/before/classic-top.png) | ![](dashboard-overhaul-2026-11-07/after/classic-00-system-overview.png) |

## Empty-query classification

Results from `eval_queries.py`, where `$var` = `.*` and `$__range` = 6h:

| Target | Data / empty / errors |
|---|---|
| Mock 27 | classic 359/58/0; MC 394/63/0 |
| Mock 25.10 | classic 371/46/0; MC 405/50/0 |
| Live 27.0.0-RC.1 | classic 372/45/0; MC 408/47/0 |

Every empty query falls into one of these classes:

- **Feature absent**, so the panel reads N/A by design: IPMI, UPS, HA/failover, FC, NVMe-oF, JBOF, GPU details, KMIP (22 on the mock; 1 on live).
- **Event-only:** no running jobs, no API errors, no pool expansion or active scan, no generic-series limit hits (11–13).
- **Not sent by 27.0:** CPU user/system split; pool realtime read/write rates (7–8; live-verified).
- **Filtered by design:** "only problems / only changes / only growing pools / only reservations / L2ARC", plus policy fields that are unset (10–15).
- **27 aggregate I/O:** the per-disk busy/throughput/IOPS columns in Disk Inventory (5).
- **No Prometheus alerting rules:** the classic `ALERTS{}` annotation (1).
- **Live only:** no API key with an expiry (1). `truenas_dataset_encrypted`, `truenas_dataset_key_loaded` and `truenas_dataset_locked` are absent from the live exporter output (3; see proposal 3).

## Remaining limits

- **Grafana-side:**
  - The state-timeline value mappings issue (above) is a Grafana 13.0.1 behaviour; recheck on upgrade.
  - Bar gauges size the value column from the first value, so a longer later value ("632.0 MiB") can lose its first digit.
  - With no data, gauges still draw their threshold scale.
  - Grafana cannot hide a row based on data, so absent features collapse rather than disappear.
- **Interaction:** tile links, data links (`dtab` and `var-*`) and `$pool` repeats were rendered but not click-tested in a browser. Mobile widths were not checked. The light theme was checked on Overview, Incident and Pools only.
- **Live coverage:** live checks covered about one hour of data on one 27.0.0-RC.1 system. "Days until full" needs days of history to be meaningful; it is projected from a 7-day `deriv`. 25.10/26.0 coverage is mock-only (fixture shapes), not live.
- **Repo assets:** `.github/images/*` (the README hero image) predates this work and was not regenerated. The README gallery now points at the new mock screenshots.

## Proposed exporter metric changes (write-up only, not implemented)

1. **Outstanding alerts.**
   - Add `truenas_alert_outstanding_count` (non-dismissed) and a `dismissed="true|false"` dimension, or a non-dismissed variant, for `alert_count_by_level` and `alert_count_by_class`.
   - Clarify the `truenas_alert_count` HELP through the alias/deprecation process.
   - Why: the Critical/Warning tiles and the verdict's critical path currently cannot exclude dismissed alerts.
2. **Display names.** `alertservice_enabled`, `cronjob_enabled` and snapshot-task `task_enabled` carry numeric IDs in `name`. Proposal: a low-cardinality info metric such as `truenas_task_info{task_type,id,description}` and `truenas_alertservice_info{id,name,type}`.
3. **Dataset encryption on 27.** `encrypted`, `key_loaded` and `locked` are not returned by the live 27.0.0-RC.1 `pool.dataset.query` as currently projected. Check the 27 projection (read-only) and either restore the fields or document the gap in the profile.
4. **Profile-removed subscriptions.** The 27.0 profile suppresses `virt.instance.metrics` (`container.metrics` replaces it), yet `truenas_event_stream_up{event="virt.instance.metrics"}` is still emitted as 0. Stop emitting `event_stream_up` for events the active profile removed, so "stream up" covers only valid subscriptions. Incident therefore watches `reporting.realtime` only.
5. **27 pool I/O.** `truenas_pool_realtime_{read,write}_bytes_per_second` are absent on 27. State this in HELP or the profile docs, or derive per-pool I/O from a documented 27 source if one exists.
6. **Snapshot-count completeness.** Add `truenas_dataset_snapshot_count_partial` (1 when `DATASET_SNAPSHOT_FALLBACK_LIMIT` truncated the per-dataset counts), so panels can flag partial data automatically instead of only describing it (D12).
7. **Deprecate the `*_hit_ratio` / `*_miss_ratio` ZFS gauges** in favour of the documented rate pairs, through the alias/deprecation process. The dashboards no longer query them (D2).
8. **Disk temperature sensor presence.** Optionally add `truenas_disk_temperature_sensor_present` so 0 °C need not be inferred as "no sensor" (D13).
9. **Collection cost.** `failover.reboot.info` is the slowest call (about 4 s) on non-HA systems; profile-gate it to HA (carried over from the live review).
