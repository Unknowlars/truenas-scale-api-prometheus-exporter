# T03 — `truenas_pool_dedup_ratio` reports DDT bytes under a ratio name

- **Priority:** P1
- **Size:** S
- **Depends on:** nothing
- **Review reference:** review-report.md finding A1

## Problem

`runtime.py` (~lines 3483–3490) reads `pool.query`'s `dedup_table_size` — documented as *"Size of
the deduplication table in bytes"* (`docs/truenas-api/methods/pool/query.md`, dedup_table_size
section) — and writes the same value into **both**:

- `truenas_pool_dedup_table_size_bytes` (correct), and
- `truenas_pool_dedup_ratio`, whose HELP says *"Pool deduplication ratio (1.0 means no dedup
  savings)"* (`metrics.py:128`).

A pool with a 1 GiB DDT reports `truenas_pool_dedup_ratio ≈ 1.07e9`. Any alert built from the
HELP text is nonsense. `tests/test_runtime_api_parity.py:106` cements this by feeding
`dedup_table_size = {"parsed": 1048576}` and (directly or indirectly) accepting the aliasing.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` ~3431–3540 (the pool.query collector block).
- `src/truenas_exporter/metrics.py` lines ~128–130 (POOL_DEDUP_RATIO, POOL_DEDUP_TABLE_SIZE_BYTES).
- `docs/truenas-api/methods/pool/query.md` — `dedup_table_size` / `dedup_table_quota` sections.
- `tests/test_runtime_api_parity.py` around line 106.
- `docs/VERSIONING.md` (12 lines that matter: alias policy).
- Parity generator note: `scripts/generate_api_exporter_parity.py` — the metric already carries a
  "deprecated compatibility" disposition and an explanatory note; you will update that note.

## Required behavior

Decision (already made — implement, don't relitigate): **stop emitting a value for
`truenas_pool_dedup_ratio`** and fix its HELP; keep the declaration for one release.

1. In the pool collector, delete the `POOL_DEDUP_RATIO...set(dedup)` line. Keep
   `POOL_DEDUP_TABLE_SIZE_BYTES` exactly as is.
2. In `metrics.py`, keep `POOL_DEDUP_RATIO` **declared** (contract/alias rule) but change HELP to
   state the truth, e.g.: `"Deprecated: no documented ratio source in TrueNAS 25.10/26.0; always
   absent. Use truenas_pool_dedup_table_size_bytes for DDT size."`
3. Check whether `pool.query` (both doc corpora) or `zpool.query` (v26) exposes an actual
   dedupratio property. 25.10 `pool.query` does **not**. If you find a documented real ratio
   source on v26 (`docs/truenas-api-v26/methods/zpool/query.md` properties), do *not* implement
   it here — note it in TASKS.md "Discovered" for T21.
4. Update the parity generator's hand-maintained note for `POOL_DEDUP_RATIO` so the regenerated
   parity report reflects "declared, intentionally absent" rather than "deprecated compatibility
   (emits bytes)".
5. Ensure `POOL_DEDUP_RATIO` is not referenced by the Grafana dashboard generator; if it is,
   switch the panel to the bytes metric via the generator.

## Compatibility rules that apply

- `docs/VERSIONING.md`: a corrected replacement must keep the previous metric as an alias for one
  release. Keeping the declaration (absent-valued) satisfies "retain the metric"; document the
  migration in HELP and in your Outcome note. Removing the *series values* of a metric whose
  values were garbage is a fix, not a contract break — say so explicitly in the commit message.

## Tests

1. **Update** `tests/test_runtime_api_parity.py` (~line 106 area): with `dedup_table_size`
   present, assert `truenas_pool_dedup_table_size_bytes{pool=...}` is set and
   `truenas_pool_dedup_ratio` has **no samples** for that pool.
2. Keep/extend a case where `dedup_table_size` is null → both absent (no fabricated 0).

## Verification

```
python3 -m pytest tests/test_runtime_api_parity.py tests/test_phase1_metrics.py -q
python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py
./scripts/validate.sh
```

## Definition of done

- `truenas_pool_dedup_ratio` never carries a byte count; HELP tells the truth; bytes metric
  unchanged; contract/parity/dashboard regenerated; validate.sh green; TASKS.md updated.

## Outcome

Completed 2026-07-16.

- Stopped writing `pool.query.dedup_table_size` bytes into `truenas_pool_dedup_ratio`; the metric remains declared as an absent deprecated compatibility metric for one release.
- Kept `truenas_pool_dedup_table_size_bytes` unchanged as the DDT size metric and updated the ratio metric HELP/parity note to document the migration.
- Confirmed the checked 25.10 `pool.query`, v26 `pool.query`, and v26 `zpool.query` docs do not expose a documented dedup ratio source; the dashboard generator already references the bytes metric, not the ratio metric.
- Updated `tests/test_runtime_api_parity.py` to assert DDT bytes are exported only through `truenas_pool_dedup_table_size_bytes`, and that null DDT size leaves both metrics absent.
- Regenerated `docs/metrics-contract.json`, `docs/api-exporter-parity.md`, and `docs/api-exporter-parity.json`; dashboard generation produced no tracked dashboard diff.
- Verification: `python3 -m pytest tests/test_runtime_api_parity.py tests/test_phase1_metrics.py -q` (`70 passed`); `python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py`; `./scripts/validate.sh` (`validation_ok`, `191 passed`, 90.55% coverage, Docker image build and version smoke `5.2.0`).
