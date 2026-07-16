# 04 — Tests, Fixtures, and Release Plan

## Sanitized fixtures

Add a separate `tests/fixtures/api_26_0_0/` namespace. Fixtures must be small,
synthetic, and free of credentials, hostnames, UUIDs, paths, user names, and
unredacted live responses.

Required fixture categories:

- `system.version_short` for 25.10, 26.0, unknown, malformed, and failed detection;
- VM memory scalar/object results (bytes for both profiles; 25.10.x returns
  bytes on live systems despite the doc saying megabytes);
- v26 structured realtime event data;
- v25 `disls` realtime data and compatibility aliases;
- dataset list/object/nested responses;
- pool scan/expand/status responses;
- nullable app image/application fields;
- removed-method and removed-event profile cases;
- permission-denied and malformed response cases;
- subscription IDs, unsubscribe responses, and reconnect cleanup.

## Focused tests

Add or extend tests for:

- profile normalization and selection;
- unknown-version common-intersection behavior;
- pre-call method/event gating;
- query-limit clamping;
- VM unit conversion and value-magnitude regression;
- removal of stale v25 metrics after selecting v26;
- realtime `disls`/`disks`, CPU, interface, memory, and pool parsing;
- dataset/pool/application shape normalization;
- absent, denied, null, malformed, and non-finite values;
- subscription identifier tracking and clean unsubscribe;
- auth compatibility without secret logging;
- unchanged metric names, types, help text, and labels.
- failed, denied, malformed, empty, and unknown version detection cannot expand
  profile permissions;
- `EXTRA_METHODS`, generic discovery, reporting discovery, count queries, and
  configured `EVENT_SUBSCRIPTIONS` cannot enable v25-only or v26-only
  methods/events outside the selected profile.

## Verification commands

Run focused tests first:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q \
  tests/test_api_catalog.py \
  tests/test_documented_api_shapes.py \
  tests/test_runtime_api_parity.py \
  tests/test_phase2_events.py \
  tests/test_transport.py
```

Then run:

```text
./scripts/validate.sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q
python3 scripts/generate_metric_contract.py --check
python3 scripts/generate_truenas_dashboard.py --check
python3 scripts/validate_dashboard.py
python3 scripts/generate_api_docs_manifest.py --check
python3 scripts/generate_api_exporter_parity.py --check
```

Also run the new target-aware v26 manifest, parity, and diff checks.

## Optional live smoke

Use only a read-only API key and only read-only calls. Verify separately:

- authenticated connection;
- version detection;
- profile selection;
- `system.info`/`pool.query`/`service.query` behavior;
- absence of removed-method calls;
- metrics endpoint and health endpoint.

Do not save responses. Record only redacted summaries and command results.

## Rollout

1. Land documentation provenance and target-aware tooling.
2. Land profiles and pre-call safety gating with no new metrics.
3. Land unit and response normalization.
4. Land removed-source and event lifecycle handling.
5. Land fixtures and regression coverage.
6. Run optional live smoke against both API families.
7. Run the full local validation gate and record evidence.
8. Release one image supporting both profiles.

If v26 validation fails, serve only common metrics and mark v26-specific
sources unavailable. Never fall back to unsafe calls or guessed semantics.
