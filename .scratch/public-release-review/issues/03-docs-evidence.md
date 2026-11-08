# 03-docs-evidence
Status: resolved
Finding IDs: PRR-03 PRR-04 PRR-05
Affected files/symbols: README.md:101-106; CONTRIBUTING.md; SECURITY.md:6; docs/truenas27-migration.md; docs/modernization/01-reliability.md; .scratch/truenas27-live-validation/report.md; tests/test_truenas27.py:279-335
Blocked by: none
Blocks: final public release acceptance

## Implementation and acceptance
Correct local environment startup instructions and version support matrix. Qualify historical live/readiness evidence. Add success then failed poll then readiness expiry regression; verify active subscription versus expired data. Do not redefine existing metric semantics. Copy instructions in clean synthetic environment and confirm configuration reaches a local mock endpoint.

## Validation
`python3 -m pytest -q tests/test_truenas27.py tests/test_event_stream_liveness.py; ./scripts/validate.sh`

Record exact candidate SHA, commands, results and sanitized evidence. Preserve existing contracts and user changes; do not weaken checks. Full validate required before closure.

## Answer
PRR-03: README local Python now exports TRUENAS_WS_URL/TRUENAS_API_KEY_FILE; states .env is not loaded; CONTRIBUTING clarified. Verified by running copied steps under `env -i` in a fresh venv against a local listener: received `GET /api/current HTTP/1.1`; key file mode 600 (synthetic key, no NAS).
PRR-04: README badge/quick start/evidence table and SECURITY.md name 27.0 primary, 25.10/26.0 retained; migration doc dated update citing historical 27.0.0-RC.1 live run.
PRR-05: dated corrections appended to docs/modernization/01-reliability.md and .scratch/truenas27-live-validation/report.md; README readiness/event_stream_up wording. tests/test_readiness_lifetimes.py: success->failed->expiry->recovery and active-subscription-with-expired-data (mocked). Semantics unchanged.
Focused: pytest test_truenas27/test_event_stream_liveness/test_readiness_lifetimes 58 passed.
Closeout: docs/reviews/public-release-remediation-2026-11-07.md. Candidate: HEAD 04ca8b1 + uncommitted working tree (no exact SHA). Final ./scripts/validate.sh exit 0, validation_ok, 377 passed, 91.88% coverage.
