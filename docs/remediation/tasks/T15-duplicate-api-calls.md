# T15 — Deduplicate per-cycle API calls

- **Priority:** P2 (performance)
- **Size:** M — mechanical but touches many collectors; keep each change minimal
- **Depends on:** nothing (coordinate with T09 which adds `topology` to the pool.query select)
- **Review reference:** review-report.md findings C1/C2

## Problem

With default config the scrape cycle makes ~120–130 **serial** WebSocket round-trips every 30 s.
A meaningful chunk is redundant:

1. `disk.query` called twice with different selects:
   `src/truenas_exporter/runtime.py` ~3544 (main disk pass: `name, identifier, size, pool` +
   `extra.pools`) and ~2952 (`_collect_disk_extended_metrics`: `name, identifier, type,
   rotationrate, model, bus`).
2. `service.query` called three times: main pass ~3638, `_query_service_enable_map(("ssh",
   "ftp", "snmp"))` ~4577, `_query_service_enable_map(("netdata", "reporting"))` ~4803.
3. `vm.query` full list fetched (~2273) and then unused when
   `ENABLE_GENERIC_METHOD_METRICS=false` (the default) — only the separate count matters.
4. ~15 collectors run a list query **plus** a separate `{"count": true}` query for the same
   method (datasets ~2465+2525, replication/cloudsync/rsync/snapshottask ~2640–2684, scrub
   ~4416+4428, cloud_backup ~4508+4520, cronjob ~4540+4552, boot envs ~3882+3893, virt
   instances ~4035+4044, app/vm counts ~2276/2298).

## Code to read (only this)

The regions listed above, plus `_call_query_with_fallback` (~1053) and `_query_count` (~1069).

## Required behavior

Apply exactly these four changes — resist broader refactors:

1. **Single `disk.query`:** merge the selects into the main disk pass
   (`name, identifier, size, pool, type, rotationrate, model, bus` + `extra.pools`) and have
   `_collect_disk_extended_metrics` consume the rows via the `cache` dict (it already receives
   `client`; change its signature to accept the disk list or stash the result in
   `result_cache["disk.query"]` — the result_cache plumbing already exists in `scrape_once`).
   Keep both metric groups' behavior byte-identical.
2. **Single `service.query`:** fetch once in the main pass with
   `select: ["service", "enable", "state"]`, store in the cache; make
   `_query_service_enable_map` read from the cached rows instead of re-querying (keep the method
   as the parser, add a cache parameter). The `extra: {"include_state": ...}` difference:
   the main pass already requests state — a superset is fine for the enable-map consumers.
3. **Drop the wasted `vm.query` list** when generic metrics are disabled: only fetch the list
   when `self.config.enable_generic_method_metrics` is true; the count query stays
   unconditional.
4. **List+count pairs:** where the list was fetched with `limit=L` and `len(items) < L`, use
   `len(items)` as the total and skip the count round-trip; only issue the count query when
   `len(items) == L` (truncation possible). Implement once as a small helper, e.g.
   `def _count_or_len(client, method, items, limit) -> int`, and apply it to the ~10 dedicated
   collectors listed above. Do NOT touch count-only collectors (they have no list — the count
   query is already optimal, as their comments state).

Explicit non-goals (leave for future work, don't do here): parallelizing calls, `core.bulk`,
connection reuse across cycles, changing `pool.snapshot.query`/`disk.temperature_agg` (that's
T16).

## Compatibility rules

- Zero metric-visible changes intended. The wire-level select for `disk.query` grows — that's
  covered by the documented field set (verify each added field exists in
  `docs/truenas-api/methods/disk/query.md`; they all do — `type`, `rotationrate`, `model`,
  `bus` are in the extended collector today).
- `scripts/generate_api_exporter_parity.py` embeds wire-shape evidence strings
  (`_auto_params_evidence`, `_wire_shape`) — regenerate parity and check the diff only reflects
  your intended select/count changes.

## Tests

Use the `RecordingClient` pattern (`tests/test_removed_source_suppression.py`):

1. Full `scrape_once` against a recording fake with default config → assert `disk.query` appears
   **once**, `service.query` **once**, `vm.query` only as a count query.
2. Count-skip helper: list shorter than limit → no count call; list length == limit → count call
   issued and its value used.
3. Golden behavior: for one representative collector (e.g. cronjob), assert the emitted metrics
   are identical before/after (write the assertion against current expected values).

## Verification

```
python3 -m pytest tests/ -q
python3 scripts/generate_api_exporter_parity.py
./scripts/validate.sh
```

Record in Outcome: measured call count per cycle before/after (the RecordingClient gives you the
number — expect roughly −20 to −30 calls).

## Definition of done

- Call count reduced with byte-identical metric output; no collector behavior change under
  failure; parity regenerated; validate.sh green; TASKS.md updated with before/after call counts.

## Outcome

Implemented T15-only per-cycle API call deduplication with no metric or config
contract changes:

- `disk.query` now uses one merged selected read per scrape
  (`name`, `identifier`, `size`, `pool`, `type`, `rotationrate`, `model`,
  `bus` plus `extra.pools`) shared through `result_cache` by the main disk pass
  and extended disk metrics.
- `service.query` now uses one selected read per scrape
  (`service`, `enable`, `state`) shared by the main service pass, protocol
  config metrics, and reporting-enabled parsing.
- `vm.query` count remains unconditional, but the VM list fetch now runs only
  when generic method metrics are enabled.
- Added `_count_or_len` and applied it to the T15-listed list+count collectors:
  dataset, replication, cloudsync, rsynctask, snapshottask, boot environment,
  virt/container instance, app, scrub task, cloud backup, and cronjob. Count-only
  collectors, `pool.snapshot.query`, and `disk.temperature_agg` were not changed.

Measured with the same default-config synthetic `RecordingClient` scrape against
the T14 baseline (`337d99efa55306ba8e3a39ca3a143a1e7f0bb563`) and this change:

- Before: 128 JSON-RPC calls per cycle; `disk.query` 2, `service.query` 3,
  `vm.query` list + count.
- After: 117 JSON-RPC calls per cycle; `disk.query` 1, `service.query` 1,
  `vm.query` count only.

Tests added/updated:

- Added `tests/test_t15_duplicate_api_calls.py` for full-scrape call-shape
  recording, `_count_or_len` short/limit behavior, and representative cronjob
  metric output.
- Updated existing T15-owned collector tests that previously asserted the old
  redundant count query behavior.

Verification:

- `python3 -m pytest tests/ -q` -> `219 passed, 2 skipped`.
- `python3 scripts/generate_api_exporter_parity.py` -> regenerated parity
  artifacts with the merged disk select and list/count evidence updates.
- `./scripts/validate.sh` -> exit 0; ruff, mypy, pytest+coverage
  (`221 passed`, 91.38% coverage), dashboard validation, generated checks,
  `public_release_audit_ok`, Docker image build, container version smoke
  `5.2.0`, and `validation_ok`.
