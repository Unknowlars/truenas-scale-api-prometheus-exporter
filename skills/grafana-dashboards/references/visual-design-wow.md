# Visual Design & Wow-Factor Recipes

How to make Grafana dashboards look deliberately designed, impressive in demos,
and pleasant to live in — without sacrificing operational honesty.

Read this together with `design-patterns.md` (layout/hierarchy) before building
any new dashboard. This file contains the concrete JSON/fieldConfig recipes.

**Golden rule: wow through clarity and craft, not decoration.** Every visual
choice must either (a) speed up comprehension, or (b) be neutral to it. Nothing
may distort it.

---

## The five-second test

When the dashboard loads, a first-time viewer should within five seconds:

1. Know what system this is about (title, intro text, section icons).
2. See whether it is healthy (hero KPI band with background colors).
3. Feel that someone designed it (consistent colors, aligned grid, varied but
   intentional panel types, no default-gray sameness).

If the top of the dashboard is a wall of identical thin-line charts with
auto-assigned colors, it fails the test.

---

## Hero KPI band (the opening statement)

Full-width row of 4–8 stats, `h=4`, threshold-colored backgrounds, sparkline
where a trend exists.

```json
{
  "type": "stat",
  "title": "Success Rate",
  "gridPos": {"x": 0, "y": 1, "w": 4, "h": 4},
  "fieldConfig": {
    "defaults": {
      "unit": "percent",
      "decimals": 1,
      "min": 0, "max": 100,
      "thresholds": {"mode": "absolute", "steps": [
        {"color": "red", "value": null},
        {"color": "#E0B400", "value": 90},
        {"color": "green", "value": 98}
      ]}
    }
  },
  "options": {
    "colorMode": "background_solid",
    "graphMode": "area",
    "textMode": "auto",
    "justifyMode": "center",
    "percentChangeColorMode": "standard",
    "showPercentChange": true
  }
}
```

Recipe notes:

- **`textMode` trap**: `"value_and_name"` prints the *field name*, and for a
  Prometheus query with an empty `legendFormat` the field name is the raw
  PromQL expression — the tile renders the query text in tiny letters.
  Use `"auto"` (the panel title already labels the tile), or set a
  `legendFormat`/`displayName` if the name must appear inside the tile.

- `colorMode`: `"background_solid"` for a bold flat tile; `"background"` for a
  gradient tile; `"value"` when a colored background would be too loud (e.g. a
  dashboard with many stats).
- `graphMode: "area"` gives the sparkline. Use `"none"` for instant-only values.
- `showPercentChange: true` adds a delta vs the previous period — cheap wow,
  real information. Only when the underlying query makes the comparison
  meaningful.
- Keep the hero band to one visual grammar: same height, same colorMode, same
  text mode. Uniformity here reads as design.
- 4–8 tiles max. Nine or more stops being a headline.

---

## Time series with depth

Default flat lines look unfinished. Give trends body:

```json
"fieldConfig": {
  "defaults": {
    "custom": {
      "drawStyle": "line",
      "lineInterpolation": "smooth",
      "lineWidth": 2,
      "fillOpacity": 15,
      "gradientMode": "opacity",
      "showPoints": "never",
      "pointSize": 5,
      "spanNulls": false,
      "axisSoftMin": 0
    },
    "color": {"mode": "palette-classic-by-name"}
  }
}
```

- `gradientMode: "opacity"` = fill fades toward zero. The single best
  low-effort visual upgrade for any timeseries.
- `gradientMode: "scheme"` + `color.mode: "continuous-GrYlRd"` (or another
  continuous scheme) makes a single-series hero chart shift color with value —
  striking for latency or saturation. Use only on single-series panels and only
  when the color scale maps to severity correctly.
- `lineInterpolation: "smooth"` for continuous signals (rates, latency,
  utilization). Keep `"linear"` or `"stepAfter"` for counts, states, and
  anything where smoothing could hide a spike. Never smooth error-rate panels
  used for incident response.
- `axisSoftMin: 0` keeps area fills grounded without clipping negative data.
- Thresholds as area or dashed line context:

```json
"custom": {"thresholdsStyle": {"mode": "dashed+area"}},
"thresholds": {"mode": "absolute", "steps": [
  {"color": "transparent", "value": null},
  {"color": "red", "value": 500}
]}
```

  This paints the SLO/limit directly on the chart — operators love it, demos
  love it, and it is honest.

---

## Stacked composition (volume + mix in one panel)

```json
"custom": {
  "stacking": {"mode": "normal", "group": "A"},
  "fillOpacity": 60,
  "lineWidth": 1,
  "gradientMode": "none"
}
```

Use for build results, HTTP status classes, log levels. Pin semantic colors
(see below). `"percent"` stacking answers "what share", `"normal"` answers
"how much" — pick per question, and say which in the panel description.

---

## Semantic color identity

One accent palette per dashboard; semantic colors pinned everywhere.

```json
"overrides": [
  {"matcher": {"id": "byName", "options": "success"},
   "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "#1A9E3A"}}]},
  {"matcher": {"id": "byName", "options": "failed"},
   "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "#F2495C"}}]},
  {"matcher": {"id": "byRegexp", "options": "/5\\d\\d/"},
   "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "#F2495C"}}]}
]
```

Rules:

- Reuse the same override list across all panels in the dashboard (define once
  in the builder script).
- Red/orange/yellow are reserved for severity. Never use them decoratively.
- For non-semantic multi-series panels, `palette-classic-by-name` keeps a
  series the same color in every panel that shows it — cross-panel consistency
  reads as polish.
- Both Grafana themes exist: check that fixed colors keep contrast in light
  *and* dark theme when the org uses both. The named Grafana colors
  (`green`, `red`, `orange`, `yellow`, `blue`, `purple`) are theme-aware and
  safer than raw hex when in doubt.
- Grafana 13.1's **panel style presets** apply curated color/threshold/display
  combos in one click in the editor (timeseries, stat, gauge, bar gauge, bar
  chart). When users edit in the UI, point them there and to **copy/paste panel
  styles** for consistency; when generating JSON, emulate the same discipline.

---

## Value mappings — turn numbers into words

Raw `0`/`1` states are hostile. Map them:

```json
"mappings": [
  {"type": "value", "options": {
    "1": {"text": "🟢 Online", "color": "green", "index": 0},
    "0": {"text": "🔴 Down",  "color": "red",   "index": 1}
  }},
  {"type": "special", "options": {"match": "null",
    "result": {"text": "⚪ No data", "color": "text", "index": 2}}}
]
```

- Great in stats, tables (with `cellOptions: {"type": "color-background"}`),
  and state timelines.
- Range mappings work for scores: `0–70 → "Needs attention"`,
  `70–90 → "OK"`, `90–100 → "Excellent"`.
- **Not every 0/1 metric is a health signal.** `0 → red` is only correct when
  0 is actually bad ("exporter down"). For neutral facts — no GPU installed,
  no ECC RAM, rate-limit error *absent*, dataset not readonly — a red tile
  (or a table full of red cells) is alarmist noise that trains operators to
  ignore red. Map neutral facts to gray/dim text, map *absence of a problem*
  to green, and reserve red for states someone should act on. Check the
  polarity: "Error present: No" must be green, never red.
- **NaN needs a mapping too.** Exporters that emit NaN (or stop emitting a
  series) produce giant "NaN" stat tiles. Add a special mapping
  (`"special": {"match": "nan"}` → `"n/a"`, gray) and/or `noValue: "n/a"` to
  every stat whose source can go missing.
- Emoji: one per mapping/row-title maximum, always paired with text and color,
  never the only signal (accessibility). Skip emoji entirely for formal
  executive/compliance dashboards unless the org's culture clearly welcomes it.

---

## Gauges, bar gauges, and rankings

- Bar gauge with `displayMode: "gradient"` (or `"lcd"` for a retro segmented
  look) + threshold colors is the best-looking Top-N ranking Grafana has.
  Horizontal orientation, sorted desc, N ≤ 10.
- **Threshold colors only where thresholds mean something.** A default
  green→yellow→red scheme on a *size ranking* (top datasets by bytes, top
  apps by memory) paints the biggest item red as if it were a problem — and
  on an "available space" ranking it colors the *most* free space red, the
  exact inverse of the truth. For neutral rankings set
  `color: {"mode": "continuous-blues"}` (any single-hue continuous scheme);
  for "higher is better" data use `continuous-RdYlGr`; keep threshold colors
  for utilization-percentage bars where red genuinely means full.
- Radial gauge: set honest `min`/`max` (real capacity, not a flattering
  number) and `showThresholdMarkers: true`.
- Table cell polish: `color-background` cells for status columns, `gauge` cells
  (`"type": "gauge", "mode": "gradient"`) for utilization columns, data links
  on the name column. A table with three styled columns beats five extra
  panels.

---

## State timelines and heatmaps — the underused stunners

- **State timeline**: one row per entity, color bands over time. Instantly
  shows maintenance windows, flapping, incident spans. Pair with value
  mappings. Almost always the most-praised panel in a review.
- **Heatmap**: latency buckets over time (`le` histogram data). Use a
  continuous color scheme (`Spectral`, `Turbo`) and log-scale Y when buckets
  are exponential. One good heatmap replaces three percentile lines and looks
  dramatically better.
- **Histogram**: distribution shape (durations, ages, sizes). Reveals
  bimodality that averages hide — visual *and* analytical win.

---

## Canvas and geomap — use sparingly, land heavily

- **Geomap**: if data has real coordinates (sites, PoPs, regions), a geomap
  with threshold-colored markers is the single biggest wow panel available.
  Never fake coordinates.
- **Canvas**: freeform layouts (rack diagrams, flow schematics with live
  metric elements). High effort, high payoff for NOC/lobby screens. Keep
  element metric bindings simple; canvas is hard to maintain as code — prefer
  it for hand-curated flagship dashboards, not generated fleets.

---

## Text panels as design elements

- Dashboard intro panel (w=24, h=3): one bold sentence on purpose + audience,
  a tip line for variables, links to runbook/source. Markdown, restrained.
- Section intros for complex tabs.
- Keep total text panels ≤ 1 per section. Text is seasoning.

---

## Annotations = storytelling

Deployment/incident/maintenance annotations turn a chart into a narrative
("latency dropped right after this deploy"). For demos, ensure at least the
built-in annotations layer is on and one meaningful annotation query exists
(deploys from Loki, releases from Prometheus, or Grafana alert annotations).
Cheap, honest, impressive.

---

## Presentation & demo mode

When the goal is a wall screen or a live demo:

- **Kiosk mode** (`?kiosk` or the TV toggle) hides chrome.
- **Playlists** rotate a curated dashboard set for NOC/lobby displays.
- Set `refresh` appropriate to the story: `5s`–`10s` for a live demo feels
  alive; don't ship that to production if queries are expensive.
- Default time range should show interesting data. `now-6h` on a system that
  only has activity 9–17 makes a demo look dead; pick the range that tells the
  story.
- Shared crosshair (`graphTooltip: 1`) makes multi-panel correlation feel
  magical during walkthroughs.

---

## "No data" panels kill the five-second test

A full-coverage dashboard generated from an exporter's complete metric set
will contain panels for metrics the target system never emits (no L2ARC, no
VMs, no IPMI, no GPU…). Walls of "No data" read as *broken*, not thorough.

- **Detect against the live system**: scrape the exporter, collect metric
  names that have at least one sample (NaN counts as present), and treat a
  panel as dead only when *every* metric it queries has zero samples.
- **Relocate, don't delete**: move dead panels into one collapsed row per
  section/tab titled "🚫 Not collected on this system". Coverage is
  preserved for other deployments; the visible layout stays honest.
- **Exempt conditionally-emitted metrics**: running-job progress, error
  counters, expiring-certificate gauges are empty *by design* most of the
  time and must stay visible — operators need them exactly when they start
  returning data. Keep an explicit allowlist of such metric prefixes.
- **One scrape is not the truth**: collectors report intermittently; union
  metric names across multiple scrapes (cache names between builder runs)
  before declaring a panel dead.

---

## Anti-patterns — what "wow" is NOT

- Rainbow palettes on severity data.
- Decorative thresholds that don't map to real limits.
- Gauge max chosen to make utilization look low.
- Smoothing/`spanNulls: true` that hides spikes or gaps operators must see.
- 3+ emoji per panel, or emoji as the only status signal.
- Pie charts with 10+ slices because "donuts look nice".
- Every panel a different style — polish comes from *consistency* plus a few
  deliberate accents, not from maximal variety.
- Animation/refresh so fast it distracts or hammers the datasource.

---

## Pre-flight visual checklist (run before returning any new dashboard)

- [ ] Hero KPI band present, uniform, threshold-colored.
- [ ] One color identity; semantic colors pinned via shared overrides.
- [ ] Timeseries have fillOpacity + gradientMode; smoothing only where honest.
- [ ] At least 3 distinct panel types beyond timeseries+stat, each chosen for
      the question it answers (state timeline / heatmap / bar gauge / histogram
      / donut / table-with-styled-cells).
- [ ] Value mappings on all state/boolean fields; real units everywhere.
- [ ] SLO/limit thresholds painted on the relevant charts.
- [ ] Intro text panel + section structure for anything non-trivial.
- [ ] Annotations layer meaningful (deploys/alerts) where data exists.
- [ ] Nothing on the anti-pattern list above.
- [ ] Still passes the operational checks in SKILL.md (grid valid, queries
      correct, budgets respected) — beauty never overrides correctness.
