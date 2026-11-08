# Grafana dashboards

## Ownership
`scripts/generate_truenas_dashboard.py` owns every query and the shared
helpers: the palette, `neutral_base`, `NA_MAPPINGS`, `ZERO_IF_UP`,
`OUTSTANDING_ALERTS`, `rate_pct`, `disk_sel`, `DISK_TEMP`, `RAM_*`,
`DIRSVC_*` and `DAYS_UNTIL_FULL`.

`grafana-dashboard/build_mission_control.py` imports that module and owns
the Mission Control layout: the hero verdict and health checks, the Incident
tab, the `$pool` repeat, question titles, drill-down links and collapsed
feature rows.

Regenerate both dashboards and never hand-edit the JSON. Keep the UIDs, the
`DS_PROMETHEUS` variable and the template variables unchanged.

## Honest missing data (validator-enforced)
- Grafana paints "No data" in the **base threshold colour**. Every stat,
  bar gauge and gauge therefore starts with the neutral grey base, plus
  `noValue` N/A and null/NaN → N/A mappings. Absent means grey, never green
  or red.
- `or vector(0)` is never a result. Use `ZERO_IF_UP` (zero only while
  `truenas_up == 1`) when absence really means zero. A bare `vector(0)` is
  allowed only as a subtrahend fallback.
- Disabled or absent features read grey ("Disabled", "None",
  "Not present"); only real faults are red.
- Tile titles must fit their width (`TITLE_LIMITS`; w=3 takes about 11
  characters at 1600 px). Use at most 8 tiles per row.

## Upstream data quirks the panels must absorb
- `truenas_alert_count` includes dismissed alerts. Outstanding is
  `alert_count - alert_dismissed_count`. The by-level and by-class counts
  include dismissed alerts too.
- 27.0 RC.1 sends `*_hit_percentage` = 0. Derive every ZFS % from the rate
  pairs; the validator rejects `*_hit|miss_ratio|percentage`.
- `pool_scan_percent` can exceed 100: clamp it. A disk temperature of 0 °C
  means no sensor: filter `> 0`.
- 27 sends aggregate disk I/O (`disk="total"`). Use `disk_sel()` to prefer
  per-disk series and fall back to the total.
- 27 sends no CPU user/system split (NaN) and no pool realtime read/write
  rates (see diagnostics). Say so in `noValue` text and descriptions.

## Grafana 13.0.1 behaviour (verify on upgrade)
- State timelines ignore value mappings and print threshold labels
  ("-∞+"). Colour them by thresholds, hide the values and legend, or use a
  table or a `textMode: name` stat for the current state.
- Bars render in frame order: wrap `topk`/`bottomk` in
  `sort_desc`/`sort` on an instant query.
- Bar gauges need about 30–36 px per row when the name is on top. The value
  column is sized from the first value.
- Rows cannot be hidden based on data: collapse feature sections instead.
- The renderer caps very tall pages: render classic rows one at a time.

## Review loop
`.scratch/dashboard-overhaul/tools/`:
- `mock_stack.sh up 27|25.10|empty` starts a synthetic, contract-derived
  exporter with fictional names and 6 h of history backfilled through
  promtool.
- `render_tabs.sh` renders every Mission Control tab and every classic row
  (set `THEME=light` for light theme, `GRAFANA=` for another stack).
- `eval_queries.py` checks every query against Prometheus (`PROM=`).

Look at every PNG, aim for 0 PromQL errors and classify every empty query.
For a live render use a separate stack on other ports with an owner key kept
outside the repo. Commit only mock or empty renders.
