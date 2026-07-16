# Phase 4: Local Validation and Manual Release

## Tasks

- [x] Add one local validation command for lint, types, tests, generated assets,
  Compose, container build, and security checks.
- [x] Add local Python 3.12, 3.13, and 3.14 container test commands.
- [x] Add a fake JSON-RPC transport and black-box HTTP tests.
- [x] Add optional read-only live smoke validation with redacted output.
- [x] Add a dry-run-by-default manual release tool with explicit publication.
- [x] Generate local SBOM/provenance data for release images where supported.
- [x] Keep `.github/workflows` absent.

## Acceptance

- `./scripts/validate.sh` passes from a clean checkout with documented prerequisites.
- Publishing cannot occur without an explicit flag and clean version/tag checks.
- Live validation is never required for the deterministic local test suite.
