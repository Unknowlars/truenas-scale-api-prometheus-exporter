# Dashboard overhaul — agent brief
Status: done (closeout: docs/reviews/dashboard-overhaul-2026-11-07.md)

Owner request (2026-11-07): fix every dashboard defect found in live review and
turn **TrueNAS · Mission Control** into a dashboard that makes people say
*"wow"*: immediately readable, beautiful, honest about missing data, and
useful in an incident. This brief is self-contained; read it fully first.

## Read first

1. `AGENTS.md`, then `.agents/skills/truenas-prometheus-exporter/SKILL.md` and
   its `references/validation.md` (dashboard rules).
2. `docs/reviews/dashboard-live-review-2026-11-07.md` — the 15 findings (D1–D15)
   with live root causes. **This is your defect backlog.**
3. `README.md` § Grafana dashboards, and `grafana-dashboard/screenshots/` for the
   current look.
4. Issues in `issues/` here, in order.

## Where things live (do not hand-edit generated JSON)

| File | Role |
|---|---|
| `scripts/generate_truenas_dashboard.py` (≈2,450 lines) | **Source of truth for every query.** Panel helpers (`stat`, `timeseries`, `bargauge`, `state_timeline`, `table`, `text_panel` …) emit the classic `operations-center-dashboard.json` (Grafana schema v1, 19 collapsible rows). |
| `grafana-dashboard/build_mission_control.py` (≈1,060 lines) | Reads the classic JSON and **generates** `truenas-mission-control.json` (schema v2 `dashboard.grafana.app/v2beta1`, 12 tabs, Grafana 13+). Layout, tabs and styling for the flagship live here. |
| `scripts/validate_dashboard.py` | Structural/reference validator (currently: classic 370 panels / 364 metric refs; MC 369 elements). |
| `docs/reviews/truenas27-metric-coverage.md` | Every metric, its HELP, unit, labels and which panels use it. Use it to choose queries. |
| `src/truenas_exporter/metrics.py` | Metric declarations — **read-only for you** (see constraints). |

Fix queries in the classic generator first; Mission Control inherits them.
Put MC-only layout and visual polish in `build_mission_control.py`.

## Hard constraints

- **Do not change exporter metrics** (names, types, HELP, labels) or collectors.
  All D1–D15 fixes are dashboard-side. If a metric gap blocks an idea, write it
  up as a proposal in your closeout; do not implement it.
- Keep both dashboard identities (classic `uid: truenas-operations-center-3`,
  MC `metadata.name: truenas-mission-control`), the `DS_PROMETHEUS` datasource
  variable and the existing template variables, so users' imports and links keep
  working.
- **Never personalize committed dashboards from production data.** The review
  appliance's pool names, app names, disk models, thresholds and so on must not
  appear in JSON. Design for any NAS: 1 pool or 20, 0 apps or 80, HDD or NVMe,
  with or without VMs, IPMI, UPS, HA, or a directory service.
- Missing data stays honest: absent ≠ 0 ≠ healthy. Use `or vector(0)` only
  where absence really means zero (e.g. "critical alerts"). Elsewhere show a
  neutral "N/A" in a neutral colour, never green.
- Support 25.10, 26.0 and 27.0 data shapes. 27 sends only aggregate disk I/O
  (`disk="total"`) and CPU usage without a user/system/idle split; 25.10 sends
  per-disk data and the split. Panels must look intentional in both.
- No hosted CI, no push or publish. Live NAS access only under AGENTS.md rules,
  and only with a key the owner supplies for the session; never store it in
  the repo.
- `./scripts/validate.sh` must pass, and both generators must be byte-stable
  (`--check`).

## Design direction — make it "wow"

Aim for a calm, dense, premium NOC look: dark-first but legible in light theme.
Think "aircraft glass cockpit", not "rainbow of stat tiles".

**1. A real hero.** The Overview tab's top band answers "is my NAS OK?" in under
two seconds: a large health verdict (worst of system state, pool health,
outstanding alerts, scrape freshness), then a 6–8 tile strip with sparklines
(CPU, RAM excluding ARC, pool capacity, hottest disk, network throughput,
outstanding alerts, uptime). Each tile links to its tab.

**2. One semantic colour system** used everywhere (define it once in the
generators):
- OK green, warn amber, critical red, info blue, and **neutral grey for
  N/A/disabled/not present**.
- Intentionally disabled features (directory services, FTP, IPMI absent) are
  grey "Disabled"/"Not present", never red.
- Thresholds sit on meaningful values, with units in base form.

**3. Every panel answers a question.** Titles are questions or nouns a user
cares about ("Which pool fills first?", "Hottest disks"), and descriptions
explain the source and caveats (e.g. "27.x reports aggregate disk I/O only").
Remove duplicates (CPU Usage vs Per-Core CPU Usage).

**4. Capacity storytelling.** Per-pool used % with a `predict_linear`
"days until full" estimate, capacity trend, fragmentation, and scrub age
against schedule. Datasets: top consumers, quota pressure, snapshot space.

**5. Readable at a glance.**
- No truncated titles: at most 6–8 tiles per row, or shorter titles.
- Legends as tables only when they fit, otherwise hidden with tooltips.
- Value mappings on every state panel (fixes "-∞+").
- Clamp percentages to 0–100.
- Gradient bar gauges with readable text contrast.

**6. Graceful variability.** Repeat rows/panels by `$pool`/`$disk` where useful,
and collapse or hide sections when their feature is absent (no VMs → compact
"No VMs configured" note, not six empty panels).

**7. Navigation.** Cross-tab links, data links from tables to the matching tab
filtered by the variable, and a "← Operations Center (classic)" link.

**8. Polish.**
- Consistent panel heights on a 24-column rhythm.
- Sparklines on stats.
- `cursorSync` crosshair (already on).
- Sensible default time range and refresh.
- Light theme check.
- No panel taller than its content.

Stretch (only after D1–D15 are closed and validated): an "Incident" tab that
puts errors, alerts, failing services, scrape health and recent changes on one
screen.

## Known live facts (27.0.0-RC.1) to design around

- Dismissed alerts are included in `truenas_alert_count`; use
  `truenas_alert_count - truenas_alert_dismissed_count` for outstanding alerts (D1).
- Upstream RC.1 sends ZFS `*_hit_percentage = 0`; compute ratios from
  `*_hits_per_second / *_accesses_per_second` (D2).
- `pool_scan_percent` can exceed 100 upstream (101.39 seen); clamp it (D10).
- A disk temperature of 0 °C means no sensor (D13).
- `DATASET_SNAPSHOT_FALLBACK_LIMIT` (default 25) caps per-dataset snapshot
  counts on 27; label the panel as partial (D12).

## Review loop (tools in `tools/`)

`tools/README.md` brings up exporter + Prometheus + Grafana 13.0.1 + image
renderer on localhost, provisions both dashboards, renders every MC tab to PNG
and evaluates every dashboard query against Prometheus. Iterate:

1. Edit the generator(s), then run `python3 scripts/generate_truenas_dashboard.py && python3 grafana-dashboard/build_mission_control.py`.
2. Re-import, then run `tools/render_tabs.sh`, and look at every PNG (Read the images).
3. Run `python3 -I tools/eval_queries.py <dashboard.json>…`: there must be 0 errors and every empty query must be explainable.
4. Run `./scripts/validate.sh`.

Without a live NAS you can still do a lot: point the exporter at the mocked
fixtures or just render against an empty Prometheus to check no-data behaviour
(every panel should then read N/A/neutral, never green or red).

## Acceptance

- [ ] D1–D15 each fixed, or explicitly justified, in the issue Answer sections.
- [ ] Screenshot set of every MC tab and the expanded classic dashboard
      (dark + one light) saved under `grafana-dashboard/screenshots/` and
      **sanitized**: render against fixture/mock data, or blur hostnames, pool
      names, disk serials and app names. No private live labels committed.
- [ ] 0 PromQL errors; empty queries classified.
- [ ] Empty Prometheus renders no green or red "No data" tiles.
- [ ] `./scripts/validate.sh` passes; both generators `--check` clean;
      `validate_dashboard.py` counts updated deliberately.
- [ ] README dashboard section and screenshots updated; evidence entry in
      `docs/modernization/README.md` with tool versions and limits.
- [ ] Closeout doc `docs/reviews/dashboard-overhaul-<date>.md` with
      before/after, decisions, and any metric proposals.
