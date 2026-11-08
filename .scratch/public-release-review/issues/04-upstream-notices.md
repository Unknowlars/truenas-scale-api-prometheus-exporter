# 04-upstream-notices
Status: claimed
Finding IDs: PRR-U1
Affected files/symbols: LICENSE; docs/api; docs/truenas-api; docs/truenas-api-v26
Blocked by: none
Blocks: final public release acceptance

## Implementation and acceptance
Find authoritative upstream redistribution terms for each included snapshot. Record URLs/access dates and required notices; obtain owner decision if unavailable. Do not assert legal violation from missing evidence. Acceptance: documented provenance and required notices or owner-approved removal plan, with regeneration impacts checked.

## Validation
`python3 scripts/public_release_audit.py; ./scripts/validate.sh`

Record exact candidate SHA, commands, results and sanitized evidence. Preserve existing contracts and user changes; do not weaken checks. Full validate required before closure.

## Answer
Primary sources (2026-11-07): api.truenas.com/v27.0 and /v25.10 show "© Copyright 2026, iXsystems, Inc. dba TrueNAS." with no license/terms; /v26.0 is an empty listing; truenas/middleware repo is LGPL-3.0 but coverage of published docs is not established. No legal conclusion drawn.
Added root NOTICE (attribution, MIT does not apply, source record) and link in docs/api/README.md. Snapshot READMEs left unchanged: their hashes are pinned by manifests (an attempted edit failed validate and was reverted), so regeneration is unaffected.
python3 scripts/public_release_audit.py passes inside validate.
Remains open: OWNER DECISION — obtain iXsystems terms/permission, or exclude snapshots from the public release.
Closeout: docs/reviews/public-release-remediation-2026-11-07.md. Candidate: HEAD 04ca8b1 + uncommitted working tree (no exact SHA). Final ./scripts/validate.sh exit 0, validation_ok, 377 passed, 91.88% coverage.
