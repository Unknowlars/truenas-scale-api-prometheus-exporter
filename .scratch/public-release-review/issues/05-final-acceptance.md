# 05-final-acceptance
Status: claimed
Finding IDs: PRR-U2 PRR-U3
Affected files/symbols: scripts/validate.sh; scripts/live_smoke.py; scripts/test_python_matrix.sh; Dockerfile; dashboards; docs/modernization/README.md
Blocked by: 01,02,03,04
Blocks: final public release acceptance

## Implementation and acceptance
Run full gate from isolated clean candidate, runtime/build/image audits and supported platforms/Python matrix. Confirm read-only key and exact appliance version before bounded live calls. Verify TLS/least privilege, repeated polling/events/expiry/reconnect and representative metric values; evaluate PromQL and browser no-data behavior. Retain sanitized summaries only. Record unavailable gates UNCONFIRMED. Owner explicitly accepts supported-version claims before release.

## Validation
`./scripts/validate.sh; ./scripts/test_python_matrix.sh; python3 scripts/live_smoke.py (only with verified read-only key)`

Record exact candidate SHA, commands, results and sanitized evidence. Preserve existing contracts and user changes; do not weaken checks. Full validate required before closure.

## Answer
Done: validate.sh exit 0; test_python_matrix.sh 3.12/3.13/3.14 375 passed 2 skipped (amd64, container); Trivy 0.72.0 on :validate: 51 HIGH / 0 CRITICAL all Debian base OS, 2 fixable (apt, libapt-pkg 3.0.4), 0 in Python packages; release.sh dry-run; git diff --check.
LIVE (2026-11-07, 27.0.0-RC.1, owner-authorized FULL_ADMIN key): smoke pass; hardened container ready, values cross-checked, outage/expiry/reconnect verified via local proxy; dashboard PromQL 0 errors, empty panels classified; found and fixed LIVE-01 certificate `until` ctime parsing (tests/test_certificate_until_formats.py). Details in the closeout doc.
BLOCKED: arm64 (no builder). UNCONFIRMED: least privilege (key is FULL_ADMIN), GA/25.10/26 appliances, TLS verification, browser visual check, long soak.
UNCONFIRMED: clean checkout of exact committed SHA/tag; owner acceptance of supported-version claims.
Stays open until those gates and issue 04 close.
Closeout: docs/reviews/public-release-remediation-2026-11-07.md. Candidate: HEAD 04ca8b1 + uncommitted working tree (no exact SHA). Final ./scripts/validate.sh exit 0, validation_ok, 388 passed, 91.88% coverage.
