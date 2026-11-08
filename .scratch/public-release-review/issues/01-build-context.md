# 01-build-context
Status: resolved
Finding IDs: PRR-01
Affected files/symbols: .dockerignore:10; scripts/release.sh:43-53
Blocked by: none
Blocks: final public release acceptance

## Implementation and acceptance
Exclude .env variants and protected secret inputs without excluding required build inputs. Export a context using synthetic .env.production and assert it is absent; verify production/test Docker builds. Preserve dry-run/publish guards.

## Validation
`docker build --tag truenas-scale-api-prometheus-exporter:validate .; ./scripts/validate.sh`

Record exact candidate SHA, commands, results and sanitized evidence. Preserve existing contracts and user changes; do not weaken checks. Full validate required before closure.

## Answer
Reproduced: synthetic `.env.production`, `secrets/api_key`, `synthetic-test.pem` entered a BuildKit `COPY . /ctx` context; nested `tests/nested/.env.local` and `c.key` re-entered via `!tests/**`.
Fix: `.dockerignore` secret block (recursive env/secrets/pem/key/p12/pfx, root `*api_key*`), placed last; `!.env.example` kept for Dockerfile.test; caches/build outputs excluded.
Evidence (local/container): re-export lists only `/ctx/.env.example`; synthetic files deleted. Production and test images build; release.sh dry-run unchanged (no push).
Regression: tests/test_build_context.py (static; skipped inside Dockerfile.test where .dockerignore is absent).
Closeout: docs/reviews/public-release-remediation-2026-11-07.md. Candidate: HEAD 04ca8b1 + uncommitted working tree (no exact SHA). Final ./scripts/validate.sh exit 0, validation_ok, 377 passed, 91.88% coverage.
