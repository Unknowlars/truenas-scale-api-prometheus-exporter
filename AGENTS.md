# Repository Agent Rules

## Safety and compatibility

- Treat TrueNAS SCALE 25.10.2 as the authoritative API target.
- Only call methods that are demonstrably read-only. Never add a mutating API
  call to tests, discovery, smoke checks, or collectors.
- Preserve existing Prometheus metric names, types, help text, and label sets.
  New replacements require a compatibility alias and a documented deprecation.
- Never commit API keys, `.env` files, captured credentials, or unredacted live
  API responses.

## Verification

- Run `./scripts/validate.sh` before declaring a task complete.
- Use the optional live smoke test only with a read-only API key.
- Record verification evidence in `docs/modernization/README.md`.

## Hosted automation prohibition

- Do not create GitHub Actions, `.github/workflows`, or other hosted CI/CD
  automation unless the repository owner explicitly reverses this decision.
- Container publication is a deliberate local operation. Release tooling must
  default to dry-run behavior and require an explicit publish flag.

