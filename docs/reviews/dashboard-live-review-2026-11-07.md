# Live dashboard review — 2026-11-07

Evidence type: **live**. Owner's `27.0.0-RC.1` appliance, owner-authorized
FULL_ADMIN key (least privilege unconfirmed). Stack: exporter `:validate`
image (hardened), Prometheus v3.5.0, Grafana 13.0.1 with image renderer, all
bound to localhost. Both dashboards were imported unchanged. Every Mission
Control tab and the expanded classic Operations Center were rendered after
about 30 minutes of data. No dashboard JSON was changed by this review.

Related: [remediation closeout](public-release-remediation-2026-11-07.md).

## Verdict

Both dashboards load and render on Grafana 13 with no query errors, and most
panels show correct live values (cross-checked against the API: pool sizes and
free space, memory, app counts, certificate expiry after the LIVE-01 fix).
Several panels are misleading or broken. None needs an exporter metric
contract change; all are dashboard fixes.

## Findings

Severity is the dashboard-user impact.

| # | Sev | Dashboard / panel | Observation | Cause | Suggested fix |
|---|---|---|---|---|---|
| D1 | High | Both: Overview "Active Alerts", "Total Alerts", classic "A…" | Red **6**, but 5 of the 6 alerts are dismissed; only 1 INFO is outstanding | `truenas_alert_count` counts everything `alert.list` returns, dismissed included (HELP says "active", which is imprecise) | Query `truenas_alert_count - truenas_alert_dismissed_count`. Keep the metric; clarify its HELP only through the alias/deprecation process |
| D2 | High | Classic "Data Hit %"; MC Exporter tab "Data IO Hit", "Meta IO Hit", "Advanced ZFS Ratios" | Red **0%** while the hit rate is about 100% | Upstream: RC.1 `reporting.realtime` sends `demand_data_hit_percentage: 0` with 272/272 hits (verified on the raw event). Exporter is faithful | Compute from rates: `hits_per_second / accesses_per_second`, as the MC Overview tile already does. Report upstream |
| D3 | Med | Security "Dir Svc OK" (twice) | Red **Down** when directory services are intentionally disabled | `healthy{service="none"} = 0` is shown as a failure | Show "Disabled" when `status="DISABLED"`; colour red only for FAULTED |
| D4 | Med | State timelines: link state, service runtime, SMB encryption, boot scan/status, API method success | The value label reads **"-∞+"** | Missing value mappings / threshold display | Add 0/1 → Down/Up mappings; API Method Success has too many rows to read and needs a table or top-N |
| D5 | Med | MC Disks "Disk Sizes", Alerts "Tasks by Type", "Alert Classes" | Raw series names overlap the bars and axes | Missing `legendFormat` / bar-chart label field | Set `legendFormat` (`{{disk}}`, `{{task_type}}`, `{{klass}}`) |
| D6 | Med | "Avg Busy", per-disk busy and IO panels on 27 | "No data" (Avg Busy on green) | 27 sends only the aggregate `disk="total"`; panels filter `disk!="total"` (documented in HELP) | Fall back to `disk="total"` when per-disk series are absent |
| D7 | Med | Stat tiles with no value: Critical, API Errors, Scanning Now, Update Avail, Reboot Reason, Cloud Bkp On, Pwd Min Len, Pwd History, Pwd Min Age, Update DL, Checkin Wait, IPMI tiles, Incus Vols | "No data" or empty coloured tiles, often green, which reads as healthy | Absent series (e.g. no critical alerts, IPMI not present, password policy NaN) | Use `or vector(0)` only where absence really means zero; otherwise set a neutral no-value colour with "N/A" text |
| D8 | Low | MC Shares top row, classic System Overview row | Titles truncated to "S…", "R…", "N…" | 12 tiles per row | Fewer tiles per row or shorter titles |
| D9 | Low | Classic header "Tip" text panel | Reads "start with `.*`, then narrow by `.*`…" | Grafana interpolates `$instance` etc. in the text panel | Escape the variable names in the text |
| D10 | Low | Pool Scan Progress | new_ssd shows **101.4%**; axis 99.8–101.6% | Upstream `scan.percentage` = 101.39 for a FINISHED scrub (verified); exporter faithful | Clamp the display at 100% (`clamp_max`) and fix the axis to 0–100 |
| D11 | Low | "CPU Time Breakdown" | Always empty on 27 | 27 realtime sends usage only (split deliberately NaN) | Hide on 27 or add a "not provided by 27" description |
| D12 | Low | "Dataset Snapshot Counts" | Shows 2 snapshots; the NAS has 20 | On 27 the per-dataset count costs one call each, capped by `DATASET_SNAPSHOT_FALLBACK_LIMIT=25` (69 datasets) | Say in the panel description that it is partial; owner may raise the limit |
| D13 | Low | Disk temperature sde | **0 °C** | TrueNAS reports `0.0` for this USB disk; exporter keeps a reported zero | Treat ≤0 °C as "no sensor" in the panels |
| D14 | Low | RAM Used % (yellow/red thresholds) | 86% warning, but about 11.7 GiB of it is reclaimable ARC | Used includes ARC | Show used excluding ARC, or relax the thresholds |
| D15 | Low | Cosmetics | Duplicate "CPU Usage" / "Per-Core CPU Usage"; legend tables clipped; dim bar-gauge text; empty "Datasets with Reservations" box; "Incus Instance Running State" errors with "Data does not have a time field"; "Alert Services"/"Task Enablement" show IDs, not names; MTU shown as "1.50 K"; datasource variable labelled `DS_PROMETHEUS` | — | Address in the generator / Operations Center source (Mission Control is generated from it) |

Exporter observation (not a dashboard defect): `failover.reboot.info` is the
slowest call (about 4 s per cycle) on this non-HA system. It may be worth
profile-gating to HA systems.

## Not covered

Interaction (variable filtering, drill-down links, tab navigation by click),
light theme, mobile widths, 25.10/26.0 appliances, long-range (days) panels.
