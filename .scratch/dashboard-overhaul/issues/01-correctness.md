# 01-correctness
Status: done
Findings: D1 D2 D3 D10 D13
Blocked by: none

Fix panels that tell the user something false:
- D1: outstanding alerts = `truenas_alert_count - truenas_alert_dismissed_count`
  (Overview, Alerts tab, classic System Overview). Keep a separate "dismissed" tile.
- D2: every ZFS hit/miss % from rates (`hits/accesses`), never `*_hit_percentage`
  / `*_hit_ratio` (upstream RC.1 sends 0). Guard divide-by-zero → N/A.
- D3: directory service shows grey "Disabled" for `status="DISABLED"`, red only
  for FAULTED.
- D10: `clamp_max(...,100)` and axis 0–100 for scan progress.
- D13: disk temperature ≤ 0 → N/A (filter `> 0`).
Tests: extend `scripts/validate_dashboard.py` with rules that reject
`*_hit_percentage` / `*_hit_ratio` in panel queries and require the D1
expression. Do not weaken existing checks.

## Answer
Done 2026-11-07. Changes are in `scripts/generate_truenas_dashboard.py`; Mission Control inherits them.
- **D1.** `OUTSTANDING_ALERTS` = `clamp_min(sum(alert_count) - (sum(alert_dismissed_count) or on() vector(0)), 0)`. It drives classic Overview "Alerts", the Alerts row "Outstanding", Alert Count Over Time (outstanding/dismissed/all), the MC hero tile, the verdict and Incident. "Dismissed" stays a separate tile.
- **D2.** `rate_pct()` computes `100 * sum(hits/s) / (sum(accesses/s) > 0)`. Every data, meta, L2ARC, I/O-hit and miss % uses it, and a zero denominator gives N/A. The stale MC `_patch_hit_pct` was removed.
- **D3.** `DIRSVC_STATE` maps DISABLED → grey "Disabled", HEALTHY green, JOINING/LEAVING amber, FAULTED red. It is used in Security and in Audit; the status table gets coloured text, and Dir Faults 0 reads "None".
- **D10.** `clamp_max(pool_scan_percent, 100)` with a 0–100 axis; boot scan % is clamped too.
- **D13.** `DISK_TEMP` adds `> 0` to every disk-temperature query, including the inventory and peak aggregate.

Checks:
- `scripts/validate_dashboard.py` has new rules: it rejects `truenas_zfs_*_(hit|miss)_(ratio|percentage)` and requires the D1 expression. Existing checks are unchanged.
- `tests/test_dashboard_overhaul.py` covers the rules and the committed JSON.
- Mock renders show 1 outstanding (4 total, 3 dismissed), ARC 98.5 %, grey Disabled, scan 100 % and the 0 °C USB disk excluded.
- Live 27.0.0-RC.1 shows 1 outstanding (6 total, 5 dismissed) and ARC hit 99.7 %.

Limits: `alert_count_by_level` and `alert_count_by_class` still include dismissed alerts, so the Critical/Warning tiles can overcount. See exporter proposal 1 in the closeout.
