# T09 — Re-enable pool vdev read/write/checksum error metrics via `pool.query` topology

- **Priority:** P2
- **Size:** M
- **Depends on:** nothing (coordinate with T15 if both touch the pool.query select — check TASKS.md)
- **Review reference:** review-report.md gap table row "pool.query topology"

## Problem

`truenas_pool_vdev_{read,write,checksum}_errors{pool,vdev}` are declared
(`src/truenas_exporter/metrics.py` ~652–666) and a complete, once-working extraction walker
exists (`_extract_vdev_errors` / `_walk_vdev`, `src/truenas_exporter/runtime.py` ~2818–2844) —
but the pool collector's `select` (`runtime.py` ~3436) does not request `topology`, and a comment
at ~3539 says "Vdev stats fields are opaque in the committed pool.query schema. Legacy vdev error
metrics remain unavailable." The walker is dead code; the most important ZFS health signal
(per-vdev error counters) is not exported.

Doc reality: `docs/truenas-api/methods/pool/query.md` **does** document `topology` ("Physical
topology and structure of the pool including vdevs. `null` if not available.") — the inner vdev
`stats` schema is opaque (typed as object), but the field itself is documented and stable, and
the walker already fails closed on missing/malformed stats.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` ~2818–2844 (walker), ~3431–3541 (pool collector).
- `src/truenas_exporter/metrics.py` ~649–666.
- `docs/truenas-api/methods/pool/query.md` — `topology` section; v26 twin for the same field;
  optionally `docs/truenas-api-v26/methods/zpool/query.md` (explicit topology support — note as
  future option, don't implement).
- `scripts/generate_api_exporter_parity.py` — rows for `POOL_VDEV_*` ("unavailable ... schema
  opaque") — to be updated.
- `tests/test_phase1_metrics.py` for pool-collector test patterns.

## Required behavior

1. Add `"topology"` to the pool.query `select` list (~3436). Note the fallback path
   `_call_query_with_fallback` → bare `pool.query` also returns topology by default.
2. After the scan-block in the pool loop, call
   `self._extract_vdev_errors(pool_name, topology)` when `pool.get("topology")` is a dict.
   Remove the stale comment at ~3539–3540.
3. The walker must stay fail-closed: missing `stats`, missing error keys, non-dict children ⇒ no
   samples, no exceptions. (It already is — verify, don't rewrite.)
4. Cardinality check: `vdev` label uses `name`/`path`/`guid` fallback. `guid` is a stable
   per-vdev identifier (not time-varying) — acceptable per the cardinality rule, but prefer
   `name` when present (already the order). Confirm labels are bounded by (pools × vdevs).
5. Payload-size note: topology adds a few KiB per pool per cycle — acceptable; mention measured
   size in Outcome if you can infer it from fixtures.
6. Naming caveat: these are cumulative-ish counters (reset on scrub/clear) exposed as **gauges
   without `_total`** — that is intentional (they reset via `zpool clear`); the review endorsed
   the existing naming. Do not rename.
7. Update parity tables: `POOL_VDEV_*` become produced, `response_field`
   `topology.<class>[].stats.{read_errors,write_errors,checksum_errors}` with a note that the
   inner schema is opaque in the doc corpus and the extraction fails closed.

## Tests

1. Fake `pool.query` row with a realistic topology (mirror with two child disks, each
   `stats={"read_errors": 0, "write_errors": 3, "checksum_errors": 1}`; include a `cache` class
   vdev) → assert exact samples per (pool, vdev), including the legitimate 0 for read_errors
   (a real 0 from the API is published — that's the policy).
2. Topology null / stats missing / children non-list → no samples, no crash.
3. Depth bomb: nest children 8 deep → recursion stops at depth 5 (existing guard), no crash.

## Verification

```
python3 -m pytest tests/test_phase1_metrics.py tests/test_runtime_api_parity.py -q
python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py
./scripts/validate.sh
```

## Definition of done

- Vdev error gauges emit from documented topology data on both profiles; fail closed on absence;
  parity truthful; validate.sh green; TASKS.md updated (minor-worthy).

## Outcome

Done on 2026-07-16.

- `pool.query` now requests `topology` in the owned pool collector select and calls the existing
  fail-closed vdev walker after scan metrics when `pool.get("topology")` is a dict.
- Re-enabled the existing
  `truenas_pool_vdev_{read,write,checksum}_errors{pool,vdev}` gauges without renaming or
  retyping them; legitimate API zeroes publish, while null topology, missing stats/keys,
  malformed children, and the existing depth guard omit samples without crashing.
- Updated API parity mappings so the three gauges are active dedicated metrics sourced from
  `topology.<class>[].stats.{read_errors,write_errors,checksum_errors}` with the documented
  opaque-inner-schema/fail-closed note.
- Payload-size note: the synthetic mirror-plus-cache topology used by the regression test is
  359 bytes as compact JSON (676 bytes pretty-printed). The checked-in 25.10.2 fixture still has
  `topology: null`, so no live fixture size was available.
- Versioning note: minor-version-worthy because previously declared-but-dead metrics now emit.

Verification:

- `python3 -m pytest tests/test_phase1_metrics.py tests/test_runtime_api_parity.py -q`
  passed: 81 tests.
- `python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py`
  passed.
- `./scripts/validate.sh` exited 0: 206 tests, 91.40% coverage, dashboard/parity/generated
  checks, public release audit, Docker build, and version smoke passed.
