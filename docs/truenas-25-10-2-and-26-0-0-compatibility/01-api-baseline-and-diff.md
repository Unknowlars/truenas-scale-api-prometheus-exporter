# 01 — API Baseline and Diff Plan

## Goal

Turn the checked-in 25.10.2 and v26.0.0 documentation into independently
verifiable, reproducible inputs for runtime safety decisions.

## Current evidence

- 25.10.2 has `docs/truenas-api/MANIFEST.json`, generated Markdown, parity JSON,
  and parity Markdown.
- The v26 corpus is under `docs/truenas-api-v26.0.0/truenas-v26.0.0-docs/` and
  contains HTML plus `_sources/*.rst.txt`, but lacks equivalent manifest and
  parity artifacts.
- The current generator uses the hard-coded `TRUENAS_API_VERSION = "25.10.2"`
  and writes only to `docs/truenas-api`.

## Required implementation

1. Add target metadata for `25.10.2` and `26.0.0` without changing the current
   25.10.2 output.
2. Extend conversion and manifest tooling with an explicit target/source/output
   selection. Never infer a target from an arbitrary directory name.
3. Generate and check:
   - `docs/truenas-api/MANIFEST.json` for 25.10.2;
   - `docs/truenas-api-v26.0.0/MANIFEST.json` for v26;
   - separate v26 parity JSON and Markdown artifacts;
   - a machine-readable and human-readable API compatibility diff.
4. Validate the title/version markers in v26 HTML and the source tree before
   accepting the corpus.
5. Record source provenance, file counts, per-file hashes, aggregate hashes,
   generator version, and generation command in the v26 manifest.
6. Add checks proving one target cannot overwrite another target's artifacts.

## Diff rules

Compare method and event leaf names, required roles, call parameters, return
shapes, documented limits, and deprecation/removal notes. Classify each item:

- common and unchanged;
- common with schema change;
- added in v26;
- removed in v26;
- renamed or split;
- present but unsafe for exporter use;
- present but deferred for semantic/cardinality review.

The diff must explicitly capture these exporter-relevant cases:

| Surface | v26 decision |
| --- | --- |
| `vm.get_available_memory` | Keep; bytes require profile conversion |
| `vm.get_vmemory_in_use` | Keep; bytes require profile conversion |
| `virt.instance.query`, `virt.volume.query` | Suppress; no v26 equivalent approved |
| `virt.instance.metrics` | Suppress; removed event |
| `nvmet.global.sessions` | Suppress for v26.0.0; no approved equivalent |
| `app.image.query` | Keep after schema/permission review; it is not removed |
| `reporting.graphs`, `reporting.netdata_graphs` | Suppress optional calls; v26 has singular methods with different call shape |
| `pool.is_upgraded`, `pool.ddt_prefetch` | Keep blocked/suppressed; officially removed in v26 |
| `container.*`, `smb.status`, `zpool.query`, `failover.status`, `zfs.tier.*` | Inventory only; no first-release metric mapping |

## Tests and acceptance

- Both target manifests pass `--check` independently.
- Existing 25.10.2 aggregate hash and generated files remain unchanged.
- v26 method/event counts are derived by tooling, not hand-entered constants.
- The diff identifies every current exporter method/event that is absent or
  schema-changed in v26.
- No API key, hostname, live response, or generated credential is committed.
