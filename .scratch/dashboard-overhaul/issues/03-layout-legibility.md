# 03-layout-legibility
Status: done
Findings: D5 D8 D9 D14 D15
Blocked by: none

Legend formats (Disk Sizes, Tasks by Type, Alert Classes); no truncated titles;
escape `$var` in the classic tip text; RAM excluding ARC (or relaxed
thresholds) — document choice; remove duplicate CPU panel; fix clipped legends,
dim bar-gauge text, empty reservation box, Incus running-state "no time field",
names instead of IDs where a name label exists, MTU unit `none`, datasource
variable label "Datasource".

## Answer
Done 2026-11-07.
- **Legends and labels.** Disk Sizes, Tasks by Type and Alert Classes are now bar gauges with legends. Timeseries legends are lists unless a table fits.
- **Tiles.** `reflow()` caps rows at 8 tiles. `SHORT_TITLES`/`TITLE_LIMITS` shorten titles, and the validator enforces the limits.
- **Text.** The tip text no longer contains `$variables`. MTU uses unit `none` and the datasource label is "Datasource".
- **D14 (owner decision).** Both RAM figures are shown: excl. ARC (thresholded) and incl. ARC (informational).
- **D15.**
  - The duplicate per-core CPU panel is removed.
  - Bar gauges use a fixed row height, explicit text sizes and the theme text colour for values. `topk`/`bottomk` bars are sorted by value; live data showed alphabetical order before.
  - The empty reservation box reads "No datasets have a reservation".
  - Incus running state is a table.
  - Alert services and tasks label numeric IDs honestly ("ID", "Task (name or ID)"); the exporter exports no display name, so this is proposal 2.

Checks: 1600 px renders of every tab (mock 27/25.10 and live) and the light theme on Overview, Incident and Pools.

Limit: bar gauges size the value column from the first value, so a longer later value can lose its first digit (Grafana).
