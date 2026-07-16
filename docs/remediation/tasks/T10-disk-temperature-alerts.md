# T10 — Wire `disk.temperature_alerts` → `truenas_disk_temperature_alert_count`

- **Priority:** P2
- **Size:** S
- **Depends on:** nothing
- **Review reference:** review-report.md gap table row "disk.temperature_alerts"

## Problem

`truenas_disk_temperature_alert_count{disk}` is declared (`src/truenas_exporter/metrics.py`
~169) and cleared each cycle, but no collector calls `disk.temperature_alerts`. The method is
documented in both corpora (`docs/truenas-api/methods/disk/temperature_alerts.md`, v26 twin),
requires the disk-name list as a mandatory parameter (which is why auto-discovery correctly
blocks it — `method_safety.py` REQUIRES_ENTITY_PARAM), and the disk collector already has the
name list and calls the sibling `disk.temperature_agg(disk_names, 7)` at
`src/truenas_exporter/runtime.py` ~3571.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` — the disk block of `scrape_once` (~3542–3596).
- `docs/truenas-api/methods/disk/temperature_alerts.md` (+ v26 twin) — exact params and return
  shape. Confirm the return: expected to be a list of alert objects (or per-disk mapping) —
  design the parse from the documented shape, not from assumption.
- `src/truenas_exporter/method_safety.py` — confirm `disk.temperature_alerts` stays in
  `REQUIRES_ENTITY_PARAM` (it must — the dedicated call passes params; auto-discovery must not).
- `scripts/generate_api_exporter_parity.py` — row for `DISK_TEMP_ALERT_COUNT`.

## Required behavior

1. After the `disk.temperature_agg` call, when `disk_names` is non-empty, call
   `self._call(client, "disk.temperature_alerts", [disk_names])` (match the documented signature
   exactly — check whether it takes `(names)` or `(names, days)` in the doc; use the documented
   default for any optional arg).
2. Aggregate alert rows per disk and set `DISK_TEMP_ALERT_COUNT.labels(disk=...)`.
   Disks present in `disk_names` but with zero alert rows: publish `0` **only if** the API's
   return shape distinguishes "queried, no alerts" (e.g. it returns an entry/empty-list per
   requested disk or the call succeeded for the whole set — in that case a real 0 is the correct
   published value for every queried disk). If the return is a bare list of alerts, a successful
   call still means "0 alerts" for every disk not mentioned — publish 0 for all queried disks on
   success, nothing on failure.
3. Wrap in try/except → `LOG.debug` + absent on failure (match sibling collectors); never let it
   break the rest of the disk block.
4. Update the parity mapping: `DISK_TEMP_ALERT_COUNT` from "unavailable" to produced with the
   documented method + field.

## Compatibility rules

- Fills an already-declared contract; minor-worthy. Regenerate contract/parity/dashboard.

## Tests

1. Fake client: temperature_alerts returns alert rows for `sda` (2 rows), none for `sdb` →
   `{disk="sda"} == 2`, `{disk="sdb"} == 0` (both disks were queried and the call succeeded).
2. Call raises → no `truenas_disk_temperature_alert_count` samples; disk size/temperature
   metrics from the same block unaffected.
3. Empty disk list → method not called at all (RecordingClient assertion).

## Verification

```
python3 -m pytest tests/test_phase1_metrics.py -q
python3 scripts/generate_api_exporter_parity.py
./scripts/validate.sh
```

## Definition of done

- Metric emits per queried disk on success, absent on failure; auto-discovery still blocked from
  calling the method bare; parity truthful; validate.sh green; TASKS.md updated.

## Outcome

_(fill in when done)_
