# T19 — HELP/type/naming corrections batch

- **Priority:** P3
- **Size:** M (five small independent items — do them in order, commit as one task)
- **Depends on:** T03 (dedup HELP is handled there, not here)
- **Review reference:** review-report.md findings A7, A8, A9, A10, A11

Every item below changes HELP text and/or adds an alias metric ⇒ after all items, regenerate
contract + parity + dashboard once (README rule 6) and check the diffs item by item.

## Item 1 — `truenas_network_gateway_reachable` (A7)

`src/truenas_exporter/runtime.py` ~3030–3041, `metrics.py` ~179–180. Value = "a default route
exists", HELP = "gateway is reachable". The honest twin
`truenas_network_default_gateway_configured` already exists and gets the same value.

- Change `NETWORK_GATEWAY_REACHABLE`'s HELP to: "Deprecated alias of
  truenas_network_default_gateway_configured (route presence only — does NOT test
  reachability); will be removed in a future release."
- Keep emitting it (alias policy, `docs/VERSIONING.md`).
- Check the dashboard generator for references; migrate panels to the configured-metric.

## Item 2 — App blkio cumulative bytes exposed as plain gauges (A8)

`metrics.py` ~646–647 (`truenas_app_blkio_{read,write}_bytes`), producer `runtime.py`
~1653–1660; doc `docs/truenas-api/events/app/stats.md` ("Blkio read bytes" — cumulative
container totals).

Constraint: prometheus_client `Counter` cannot `.set()` an externally-sourced total, so a true
Counter type is not implementable here. Required:

- Fix HELP on both to state cumulativeness: "Cumulative block-I/O bytes read by the app's
  containers since container start (counter semantics; use rate()); resets when containers
  restart."
- Do NOT rename (contract), do NOT convert to Counter.
- Note for parity tables: `documented_type_unit` should say cumulative bytes.

## Item 3 — `truenas_smb_open_file_count` counts LOCKS (A9)

`runtime.py` ~2860–2864 maps info level `"LOCKS"` to `SMB_OPEN_FILE_COUNT`. smbstatus locks ≠
open files. Required:

- HELP change (`metrics.py` ~672): "Number of SMB lock records reported by smb.status LOCKS
  (approximates open files)."
- Leave the mapping — there is no better documented source; the doc corpus lost the info_level
  enum values, so also add a code comment noting the literals are unverified against docs and
  validated only by live systems.

## Item 4 — `truenas_snapshot_oldest_timestamp_seconds` HELP lies (A10)

`metrics.py` ~754 says "(0 if no snapshots)"; the code (`runtime.py` ~4475–4483) correctly
leaves it NaN/absent. Fix HELP: "Unix timestamp of the oldest ZFS snapshot; absent when there
are no snapshots." Do not change the code.

## Item 5 — Realtime disk I/O HELP overpromises per-disk labels (A11)

`metrics.py` ~585–589: on 25.10 the realtime `disks` section is aggregate-only, so the only
series is `{disk="total"}` (fixture-proven). Append to each of the five HELP strings:
"…; on systems reporting only aggregate disk stats a single series with disk=\"total\" is
exported."

## Code to read

Only the regions cited per item + `tests/test_phase1_metrics.py` / `tests/test_phase2_events.py`
if any test asserts a HELP string (grep the tests for the metric names first).

## Tests

- Grep tests for asserted HELP text of the touched metrics; update if present.
- Add one registry-render test asserting the new HELP for at least items 1 and 4 (cheap
  contract pinning): render `generate_latest()` and check the `# HELP` lines.

## Verification

```
python3 -m pytest tests/ -q
python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py
./scripts/validate.sh
```

## Definition of done

- All five HELPs truthful; no renames/retypes; dashboard migrated off the deprecated gateway
  metric; generators re-run with reviewed diffs; validate.sh green; TASKS.md updated.

## Outcome

Completed 2026-07-16.

- Updated HELP text for `truenas_network_gateway_reachable`,
  `truenas_app_blkio_read_bytes`, `truenas_app_blkio_write_bytes`,
  `truenas_smb_open_file_count`, `truenas_snapshot_oldest_timestamp_seconds`,
  and the five realtime disk I/O gauges without renaming or retyping any
  metric.
- Kept `truenas_network_gateway_reachable` emitting as a deprecated alias of
  `truenas_network_default_gateway_configured`; the dashboard generator already
  referenced the configured metric, so no dashboard source migration was needed.
- Added the requested `smb.status` info-level comment and parity metadata
  overrides so blkio fields are documented as cumulative bytes and the gateway
  alias remains a boolean 1/0 compatibility metric.
- Added a rendered-registry HELP contract test for the gateway alias and oldest
  snapshot timestamp HELP lines.
- Regenerated `docs/metrics-contract.json`, `docs/api-exporter-parity.json`,
  and `docs/api-exporter-parity.md`. Dashboard generation was run and produced
  no dashboard artifact diff.
- Verification passed:
  `python3 -m pytest tests/ -q` (`233 passed, 4 skipped`);
  `python3 scripts/generate_metric_contract.py`;
  `python3 scripts/generate_api_exporter_parity.py`;
  `python3 scripts/generate_truenas_dashboard.py`;
  `./scripts/validate.sh` (`237 passed`, 91.41% coverage,
  `public_release_audit_ok`, Docker image build, version smoke `5.2.0`,
  `validation_ok`).
