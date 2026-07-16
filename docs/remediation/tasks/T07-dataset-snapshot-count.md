# T07 — Make `truenas_dataset_snapshot_count` actually emit

- **Priority:** P1
- **Size:** S
- **Depends on:** nothing
- **Review reference:** review-report.md finding A5

## Problem

With default configuration the metric never emits:

- `pool.dataset.query` (25.10 doc: `docs/truenas-api/methods/pool/dataset/query.md`) documents
  **no** `snapshot_count` field, and the collector's `select`/`extra.properties` lists
  (`src/truenas_exporter/runtime.py` ~2465–2516) don't request one.
- The per-dataset fallback `pool.dataset.snapshot_count` is gated on
  `DATASET_SNAPSHOT_FALLBACK_LIMIT`, whose default is `0` (`config.py:152`) — disabled.

So `snap_count` is always `None` (`runtime.py` ~2562–2570) and the series is absent for every
dataset, while `docs/api-exporter-parity.json` marks the metric "active dedicated".

## Code to read (only this)

- `src/truenas_exporter/runtime.py` — `_collect_dataset_metrics` (~2461–2604).
- `src/truenas_exporter/config.py` — `dataset_snapshot_fallback_limit` (~152).
- `docs/truenas-api/methods/pool/dataset/query.md` and the v26 twin — search for
  `snapshot_count` and for the `extra` parameter schema.
- `scripts/generate_api_exporter_parity.py` — the mapping row for `DATASET_SNAPSHOT_COUNT`.
- `tests/test_phase1_metrics.py` / `tests/test_documented_api_shapes.py` for patterns.

## Required behavior

Investigate, then implement **one** of these, in order of preference:

1. **Preferred:** TrueNAS middleware supports `extra: {"snapshot_count": true}` on
   `pool.dataset.query` (returns a `snapshot_count` int per dataset) even though the committed
   doc corpus doesn't spell it out. Check both doc corpora for any mention (also
   `pool/dataset/details.md`). If a doc file supports it (even the v26 one), add it to the
   query's `extra` and read the field via the existing `snap_count` path. Document in the parity
   mapping note which corpus documents it.
2. **If the field is genuinely undocumented in both corpora:** this repo's convention is to not
   rely on undocumented behavior. In that case:
   a. Change the `DATASET_SNAPSHOT_FALLBACK_LIMIT` default from `0` to a bounded sensible value
      (e.g. `25`) so the per-dataset `pool.dataset.snapshot_count` fallback (which IS documented —
      verify `docs/truenas-api/methods/pool/dataset/snapshot_count.md` exists) covers the first N
      datasets, and
   b. Update the parity mapping so the metric's row states the real coverage ("first N datasets
      by query order via pool.dataset.snapshot_count; requires fallback limit > 0").
   Also update `README`/env-var docs if the repo documents `DATASET_SNAPSHOT_FALLBACK_LIMIT`
   (grep the repo root README and `.env.example`).
3. Whatever path you take, the parity report must stop claiming "active dedicated" for a metric
   that default config cannot emit — or the default config must actually emit it.

Cost note: option 2 adds up to N API round-trips per cycle. Keep N ≤ 25 by default and honor
`max_entity_calls` as the code already does.

## Compatibility rules

- No renames/retypes. A changed config default is minor-worthy; note in TASKS.md.

## Tests

1. Fake client returning dataset rows with the chosen mechanism (extra-field or fallback calls)
   → `truenas_dataset_snapshot_count{dataset=...}` emits the right values.
2. Mechanism unavailable (field missing / fallback errors) → series absent, no fabricated 0,
   other dataset metrics unaffected.
3. If option 2: assert the number of `pool.dataset.snapshot_count` calls is capped by the limit
   (RecordingClient pattern from `tests/test_removed_source_suppression.py`).

## Verification

```
python3 -m pytest tests/test_phase1_metrics.py tests/test_documented_api_shapes.py -q
python3 scripts/generate_api_exporter_parity.py
./scripts/validate.sh
```

## Definition of done

- Default config emits the metric (or parity/docs stop claiming it does, with the fallback path
  made usable and documented). Tests prove emission and absence paths. validate.sh green.
  TASKS.md updated.

## Outcome

- 2026-07-16: Neither the 25.10.2 nor v26 `pool.dataset.query` docs, nor their
  `pool/dataset/details.md` files, document `extra.snapshot_count`. Both corpora
  document read-only `pool.dataset.snapshot_count` returning an integer.
- Implemented the documented fallback path by changing the default
  `DATASET_SNAPSHOT_FALLBACK_LIMIT` from `0` to `25`; the existing runtime cap
  still honors `min(DATASET_SNAPSHOT_FALLBACK_LIMIT, MAX_ENTITY_CALLS)`.
- Updated README and `.env.example` defaults, and regenerated parity artifacts
  so `truenas_dataset_snapshot_count` maps to the bounded
  `pool.dataset.snapshot_count` fallback instead of an undocumented
  `pool.dataset.query` field.
- Added regression coverage for default config, successful fallback emission,
  fallback failure leaving the series absent while other dataset metrics emit,
  disabled fallback behavior, and fallback call capping.
- Verification passed:
  `python3 -m pytest tests/test_phase1_metrics.py tests/test_documented_api_shapes.py -q`
  (`55 passed`), `python3 scripts/generate_api_exporter_parity.py`, and
  `./scripts/validate.sh` (`validation_ok`, `202 passed`, 90.77% coverage,
  Docker image build passed).
