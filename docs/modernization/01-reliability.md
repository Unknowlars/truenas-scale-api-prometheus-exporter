# Phase 1: Production Reliability

## Tasks

- [x] Preserve numeric zero and boolean false values in all fallback parsing.
- [x] Expire stale event-derived series after a configurable freshness window.
- [x] Add a total scrape budget without changing the socket timeout contract.
- [x] Separate liveness (`/healthz`) from readiness (`/readyz`).
- [x] Validate ports, URLs, intervals, limits, timeouts, and mode at startup.
- [x] Support API-key files and custom CA files without removing env support.
- [x] Add graceful signal-driven shutdown for HTTP and event workers.
- [x] Define core versus optional collector failure behavior.
- [x] Add regression coverage for zero values, expiry, recovery, and invalid config.

## Acceptance

- A 50-to-0 event transition exports zero rather than retaining 50.
- Event series disappear after their TTL while stream health reports down.
- Invalid configuration fails before threads or sockets start.
- `/healthz` remains liveness-only; `/readyz` reflects scrape freshness.

> **Correction (2026-11-07, PRR-05).** The second and fourth bullets above are
> retained as originally written but overstate the implemented contract.
> `truenas_event_stream_up` means the subscription is active (its HELP text);
> event values expire to NaN/absent after their TTL independently, so an
> active subscription can coexist with expired data. `/readyz` reflects the
> age of the last *successful* poll cycle, so a later failed cycle sets
> `truenas_up=0` without immediately clearing readiness. Both lifetimes are
> pinned by `tests/test_readiness_lifetimes.py`; neither metric was redefined.
