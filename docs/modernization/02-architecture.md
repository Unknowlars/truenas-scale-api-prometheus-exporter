# Phase 2: Architecture and Collector Convergence

## Tasks

- [x] Add package metadata and a `src/truenas_exporter` package.
- [ ] Separate configuration, transport, method safety, metrics, events,
  collection, HTTP serving, and CLI startup.
- [ ] Replace private prometheus-client attribute access with owned metric specs.
- [x] Make collectors produce fresh snapshots and publish them atomically.
- [x] Export operational counters from the same registry as collector metrics.
- [x] Add a generated metric-contract manifest and compatibility test.
- [x] Reach dedicated-metric and dashboard parity with legacy mode.
- [x] Make collector mode the default only after parity; retain legacy mode for
  one compatibility release.

## Acceptance

- Contract comparison reports no removed or changed metrics or labels.
- Collector mode exposes API errors, collector errors, exporter info, event
  counters, and all dashboard dependencies.
- The root `truenas_exporter.py` remains a working compatibility launcher.

## Current migration boundary

Configuration, transport, metric declarations, CLI, and versioning are separate
modules. Collector mode exposes the complete metric contract through
`FullParityCollector`, but non-core domains still call the legacy coordinator.
The remaining tasks intentionally remove that bridge before changing the
default mode in a later compatibility release.

## Remaining work queue (recommended order)

The midway review ([05-handover.md](05-handover.md)) confirmed that
`FullParityCollector` is the wrong convergence point: it runs the full API
scrape inside every `/metrics` request on a single-threaded server and yields
the mutable global registry. The unregistered `TrueNASCollector` snapshot
design (`runtime.py:6279`) is the correct mechanism — collect into immutable
metric families under the lock, expose outside it.

1. **Atomic snapshot exposition.** Run `scrape_once` on a background interval
   loop in collector mode too; have the registered collector serve the last
   complete snapshot (single-flight, no per-request scrape). This also fixes
   handover findings 1 (healthcheck blocking) and 6 (readiness deadlock).
2. **Generalize `TrueNASCollector` to full parity and delete
   `FullParityCollector`.** Derive the collector metric sets from the metric
   declarations instead of the hand-maintained
   `_COLLECTOR_SCALAR_METRICS`/`_COLLECTOR_SERIES_METRICS` tuples; remove the
   duplicated `collect_collector_snapshot` extraction path so exactly one
   extraction pipeline exists.
3. **Single event sink.** Collapse the `_is_collector_mode()` branches at
   every event write site: always write the `_collector_event_*` cache dicts;
   legacy mode publishes the cache to the default registry via the existing
   `_publish_cached_events_to_default_registry`.
4. **Decompose `runtime.py`** into events, domain collection, HTTP serving,
   and method-safety modules, extracting domain parsers as pure functions
   over fixture payloads (this is where coverage rises toward 85%; raise the
   `--cov-fail-under` gate in `scripts/validate.sh` as it does).
5. **Owned metric specs.** Replace `metric._name` / `._documentation` /
   `._labelnames` access with a spec dataclass; derive the contract manifest
   from the specs instead of ast-parsing `metrics.py`.
6. **Default flip.** Make collector mode the default, retain legacy for one
   compatibility release, and write CHANGELOG/README migration notes
   (entrypoint change, strict config validation).
