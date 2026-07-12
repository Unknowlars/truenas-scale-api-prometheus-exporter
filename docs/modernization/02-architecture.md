# Phase 2: Architecture and Collector Convergence

## Tasks

- [x] Add package metadata and a `src/truenas_exporter` package.
- [x] Separate configuration, transport, method safety, metrics, events,
  collection, HTTP serving, and CLI startup.
- [x] Replace private prometheus-client attribute access with owned metric specs.
- [x] Make collectors produce fresh snapshots and publish them atomically.
- [x] Export operational counters from the same registry as collector metrics.
- [x] Add a generated metric-contract manifest and compatibility test.
- [x] Reach dedicated-metric and dashboard parity with legacy mode.
- [x] Make collector mode the default only after parity; retain legacy mode for
  one compatibility release.
- [ ] Raise total branch coverage from 78% to the 85% completion target with
  fixture-driven domain branch tests.

## Acceptance

- Contract comparison reports no removed or changed metrics or labels.
- Collector mode exposes API errors, collector errors, exporter info, event
  counters, and all dashboard dependencies.
- The root `truenas_exporter.py` remains a working compatibility launcher.

## Current migration boundary

Configuration, transport, method-safety policy, metric declarations, event
metadata, fixture-friendly collection parsers, HTTP serving, CLI, and versioning
are separate modules. `TrueNASCollector` exposes the last complete background
snapshot; the duplicate partial collector and `FullParityCollector` bridge have
been removed. Legacy mode remains available for this compatibility release.

## Completed convergence queue

The midway review ([05-handover.md](05-handover.md)) confirmed that
`FullParityCollector` is the wrong convergence point: it runs the full API
scrape inside every `/metrics` request on a single-threaded server and yields
the mutable global registry. The unregistered `TrueNASCollector` snapshot
design (`runtime.py:6279`) is the correct mechanism — collect into immutable
metric families under the lock, expose outside it.

1. **Atomic snapshot exposition — complete.** Collector mode runs a background
   single-flight scrape and serves only the last complete snapshot.
2. **Collector convergence — complete.** `TrueNASCollector` has full parity;
   the partial scraper, `FullParityCollector`, and hand-maintained metric tuples
   are removed.
3. **Single event sink — complete.** Both modes write the shared event cache;
   legacy mode projects that cache into the default registry.
4. **Package boundaries — complete.** Event metadata, pure collection parsers,
   HTTP serving, and method-safety policy live in dedicated modules. Further
   domain-parser extraction continues alongside coverage work.
5. **Owned metric specs — complete.** Metric names, types, help, and labels are
   owned metadata, and the contract generator consumes those specs directly.
6. **Default flip — complete.** Collector mode is the default, legacy remains
   available for this compatibility release, and migration notes are published.
