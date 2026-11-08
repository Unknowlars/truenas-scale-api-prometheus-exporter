# 02-no-data-and-state
Status: done
Findings: D4 D7 D11
Blocked by: none

- One shared no-value style in both generators: text "N/A", neutral grey.
- `or vector(0)` only where absence means zero (critical alerts, API errors,
  active scans); list each choice in Answer.
- Value mappings on every state_timeline/stat (0/1 → Down/Up, Disabled, Not
  present). No "-∞+" anywhere.
- CPU split (D11): show only when series exist, otherwise a one-line note
  "Not reported by TrueNAS 27".
Acceptance: render against an **empty Prometheus** shows no green/red tiles.

## Answer
Done 2026-11-07.
- **Shared no-value style.** `neutral_base()`, `NA_MAPPINGS` and `NO_VALUE="N/A"` live in the classic generator. Every stat, bar gauge and gauge gets a grey base step, so Grafana's "No data" colour is neutral, plus `noValue` and null/NaN → N/A. Mission Control reuses the same helpers. The validator enforces the neutral base.
- **`or vector(0)` choices.** Absence-means-zero is gated on the exporter being up, as `ZERO_IF_UP = or on() (0 * max(truenas_up == 1))`. It is used for: critical and warning alerts, running services, scanning now, enabled tasks, enabled cloud backups, update available, reboot reason, API and collector errors (1h), and the Incident counters. A bare `vector(0)` survives only as a subtrahend fallback (dismissed alerts, ARC size). A test enforces this.
- **Mappings.** Every stat has value and N/A mappings (Disabled, Not present, None). Grafana 13.0.1 state timelines ignore value mappings; I verified this with four variants. The remaining three timelines therefore colour by thresholds from the 0/1 mapping, hide the "-∞+" labels and legend, and name the colour key in their descriptions. Current-state panels became tables or `textMode: name` stats (SMB encryption, boot scan state/status, API method success, Incus running state).
- **D11.** The CPU split queries `>= 0`. When empty, the panel reads "Not reported by TrueNAS 27 (usage only)"; on the 25.10 mock it shows data.

Check: an empty-Prometheus render of all 13 MC tabs and 19 classic rows, plus a pixel scan, found no green or red value tile. The only colour left is the gauge threshold scale and the tab emoji. See `grafana-dashboard/screenshots/*-empty.png`.
