# TrueNAS 25.10.2 and 26.0.0 Compatibility

Status: COMPAT-01A through COMPAT-08 complete. Operator documentation and
handoff evidence (COMPAT-07) and the full validation/release gate (COMPAT-08)
are recorded in `docs/modernization/README.md` and the
[task board](05-agent-task-board.md).

This package is the implementation handoff for supporting the exporter against
the pinned TrueNAS SCALE 25.10.2 contract and the validated TrueNAS API
v26.0.0 contract.

## Objective

Deliver one read-only exporter image that automatically supports both API
families while preserving every existing Prometheus metric name, type, help
text, and label set.

The first compatibility release maintains existing metrics only. New v26-only
metrics are deferred until their API safety, schema, permissions, cardinality,
metric contract, fixture, and dashboard impact are separately approved.

## Authoritative constraints

- 25.10.2 remains the authoritative baseline for existing behavior.
- Only demonstrably read-only API methods and events may be used.
- Removed, denied, malformed, or semantically ambiguous data is unavailable;
  it is never converted into a fabricated zero.
- No operator-managed API-version toggle is required or recommended.
- Unknown API versions use a conservative common profile.
- No GitHub Actions, hosted CI, or automatic publication is added.
- Release tooling remains dry-run by default.

## Research corrections

The original discovery draft is retained as historical evidence, but these
decisions supersede ambiguous or incorrect draft statements:

- `app.image.query` exists in the v26.0.0 documentation and remains a possible
  read-only source after review.
- The v26 corpus removes the old `virt.instance.*`, `virt.volume.*`, and
  `virt.global.*` surfaces used by the current exporter, including the
  `virt.instance.metrics` event.
- `nvmet.global.sessions` is absent from the pinned v26.0.0 corpus but is
  still served by live 26.0.0-BETA.2, so the exporter keeps only the bounded
  count source enabled under v26/unknown.
- v26 documents `reporting.graph` and `reporting.netdata_graph`; the current
  optional generic collector calls `reporting.graphs` and
  `reporting.netdata_graphs`. They are not interchangeable without bounded
  graph selection and semantic review.
- `vm.get_available_memory` and `vm.get_vmemory_in_use` are documented as
  bytes in v26. The pinned 25.10.2 documentation says "megabytes", but a live
  25.10.3 system returns raw bytes (16.2 GiB observed on a 31.3 GiB host,
  2026-07-13). Both profiles therefore treat these methods as bytes; the earlier
  25.10 MiB assumption inflated `truenas_vm_available_memory_bytes` by 1024².
- `core.subscribe` returns a subscription identifier and `core.unsubscribe`
  accepts it.

## Operator behavior summary

The exporter automatically selects a compatibility profile by calling
`system.version_short` once after authentication for each scrape or event
connection. `25.10.*` selects the `25.10` profile, `26.0.*` selects the `26.0`
profile, and malformed, failed, denied, or unexpected detection selects the
`unknown` profile. The `unknown` profile is fail-closed and uses only the
reviewed common method/event intersection. There is no operator-managed version
toggle.

The pinned 26.0.0 diff removes these current exporter sources; the `26.0` and
`unknown` profiles suppress them before transport:

- `virt.instance.query`
- `virt.volume.query`
- `reporting.graphs`
- `reporting.netdata_graphs`
- `virt.instance.metrics`

Metric declarations are preserved. If a source is removed, denied, absent,
malformed, stale, or has no safe semantic equivalent in the selected profile,
the existing unavailable behavior applies: samples are absent or `NaN`; zero is
not emitted as a substitute.

Default event subscriptions are profile-aware. `25.10` uses
`reporting.realtime`, `app.stats`, and `virt.instance.metrics`; `26.0` and
`unknown` use `reporting.realtime`, `app.stats`, and `container.metrics`. The
event loop requires a valid string ID from `core.subscribe`, treats invalid IDs
as failures, and calls `core.unsubscribe` for tracked IDs during clean shutdown
and reconnect cleanup.

`app.image.query` remains eligible for reviewed count use. `pool.is_upgraded`
remains blocked because it requires a pool id, and `pool.ddt_prefetch` remains
prohibited because it is action-like and unsuitable for Prometheus collection.

Official references: [TrueNAS 26 API changes](https://www.truenas.com/docs/scale/26/gettingstarted/versionnotes/), [v26 API documentation](https://api.truenas.com/v26.0/), [v26 authentication method](https://api.truenas.com/v26.0/api_methods_auth.login_ex.html), [v26 VM memory method](https://api.truenas.com/v26.0/api_methods_vm.get_available_memory.html), and [v26 subscription method](https://api.truenas.com/v26.0/api_methods_core.subscribe.html).

## Document map

| Document | Purpose | Primary implementers |
| --- | --- | --- |
| [01 — API baseline and diff](01-api-baseline-and-diff.md) | Pin provenance, manifests, target-aware generators, and exact method/event diff | Documentation/tooling agent |
| [02 — Runtime profile and safety](02-runtime-profile-and-safety.md) | Define profile interfaces, version detection, method gating, and unknown-version policy | Runtime/catalog agent |
| [03 — Collectors and events](03-runtime-collectors-and-events.md) | Implement units, normalizers, removed-source handling, and event lifecycle | Runtime/events agent |
| [04 — Tests and release](04-tests-fixtures-and-release.md) | Define fixtures, regression tests, validation, smoke tests, and rollout evidence | Test/release agent |
| [05 — Agent task board](05-agent-task-board.md) | Dependency-ordered, isolated coding tasks and acceptance criteria | All agents |

## Dependency order

```text
API provenance and diff
          |
          v
Profile and safety interfaces
       /       \
      v         v
Collectors   Event lifecycle
       \       /
        v     v
   Fixtures and regression tests
              |
              v
     Full validation and release evidence
```

## Definition of done

Compatibility is complete only when both profiles pass sanitized fixtures, all
existing metric contracts are unchanged, v26 removed methods are absent from
transport traces, the target-aware generated artifacts pass, the local
`./scripts/validate.sh` gate passes, and verification evidence is recorded in
`docs/modernization/README.md`.
