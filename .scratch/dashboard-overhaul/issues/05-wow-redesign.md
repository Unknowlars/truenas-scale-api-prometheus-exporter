# 05-wow-redesign
Status: done
Blocked by: 01 02 03 04

Implement spec "Design direction" items 1–8 in Mission Control
(`build_mission_control.py`), keeping the classic dashboard functional and
query-identical where shared. Hero health verdict + sparkline strip, semantic
palette, question-led titles, capacity "days until full", repeat-by-variable
where useful, cross-tab/data links, consistent grid rhythm, light-theme pass.
Show before/after screenshots per tab in the closeout. Stretch: Incident tab.

## Answer
Done 2026-11-07 in `grafana-dashboard/build_mission_control.py`; the classic dashboard is still query-identical where shared.
1. **Hero.** "Is my NAS OK?" verdict (worst of 8 checks) plus a Health checks table that explains it. Eight linked sparkline tiles: CPU, RAM excl. ARC, fullest pool, hottest disk, network, outstanding alerts, ARC hit, uptime.
2. **Palette.** One semantic palette, defined in the classic generator and imported by MC; `finalize()` maps colour names.
3. **Titles.** Question-led titles (`QUESTION_TITLES`) and source/caveat descriptions.
4. **Capacity.** "Which pool fills first?", "Days until full" (7-day `deriv`), growth trend and fragmentation, plus dataset top consumers and snapshot space.
5. **Readability.** Per-pool cards repeated by `$pool`; feature-absent sections collapse.
6. **Navigation.** Tile links to tabs (`dtab`), table drill-down links (Pool/Disk/App/Dataset → tab with `var-*`), and "← Operations Center (classic)".
7. **Polish.** 4/8-unit grid rhythm, light theme checked, crosshair sync kept.
8. **Stretch.** 🚑 Incident tab (owner approved): failing-now table, changed-in-range table, error rates and poll time.

Before/after per tab: `docs/reviews/dashboard-overhaul-2026-11-07.md`.

Limits: links and repeats were rendered but not click-tested in a browser; mobile widths were not checked.
