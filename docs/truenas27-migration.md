# Upgrading to the TrueNAS 27 release candidate

Candidate: **5.2.0rc1**. The checkout previously identified5.2.0 as unreleased;
no public releases or tags were returned during discovery. This is an additive
candidate, not a published production release.

## Configuration and compatibility

Use your existing WebSocket URL, read-only API key, and collector/default mode.
For the supported modern authentication mechanism add `TRUENAS_USERNAME` with
the key owner's username. This selects `auth.login_ex(API_KEY_PLAIN)` and requires
`response_type=SUCCESS`. An unset username keeps the legacy key-only mechanism;
a rejected modern login never silently falls back. Prefer TLS with certificate
verification and a custom CA when required. Existing explicit ws:// setups are
still supported. `TRUENAS_API_KEY_FILE` uses a mounted local secret when the
inline API-key setting is empty; container users must mount that file read-only.

27.0.x now selects a dedicated profile.25.10.x and26.0.x retain their own profiles,
including existing unit and event compatibility. Unknown releases remain
conservative and do not imply supported27 behavior. Versioned local and official
27.0.0 documentation differ; the matrix records both sources independently.

No pre-existing metric name, type, HELP or label set is intentionally changed.
Removed/unsupported calls are suppressed, keeping their historical metric
declarations without inventing replacement values. A successful empty list is
different from a malformed response or failed query. Required domain failures
mark `truenas_up=0` while unrelated domains continue; API/collector diagnostics
identify the failure. Authentication/connection failure and time budgets remain
cycle-level failures. Snapshot TTL enforcement also applies during blocked polls.

Generic extraction remains disabled by default. If enabled, `MAX_GENERIC_SERIES`
defaults to10000 per polling generation and10000 across all retained generic
events. Broad dictionaries may now be truncated. `truenas_generic_series{source}`
reports retained series; `truenas_generic_series_limit_hits_total{source}` counts
pruned extraction branches, not every possible descendant sample. The only
source values are `method` and `event`. Dedicated telemetry is outside these limits.

## Dashboards

Both Operations Center and Mission Control remain supported with their existing
identities. Edit the classic generator, then regenerate Mission Control. The
default build never probes an exporter and never reads the old names cache.
For a private system-specific layout supply `--metric-names /private/names.json`
explicitly; do not commit installation-specific generated output. Both default
outputs are covered by deterministic checks and metric/reference validation.
Browser/Grafana acceptance is separate from these structural checks.

On 27 the dashboards follow the 27 data shapes:
- Disk panels fall back to the aggregate `disk="total"` series.
- CPU Time Breakdown reads "Not reported by TrueNAS 27".
- Pool read/write rates are not sent by 27, so I/O is shown from disks.
- ZFS hit percentages are computed from hit/access rates, because the
  upstream percentage reads 0.
- "Alerts" means outstanding alerts (dismissed alerts excluded).

See `docs/reviews/dashboard-overhaul-2026-11-07.md`.

## Verification and release

Run `./scripts/validate.sh`, optionally `./scripts/test_python_matrix.sh`, runtime
dependency and image vulnerability audits, and the bounded read-only live smoke.
Live operations are owner-authorized, but require a verified read-only key and
must not save unredacted operational responses. The supplied local key's legacy
login returned false during discovery; exact appliance release and live metric
correctness remain unverified until authentication succeeds.

*Update (2026-11-07, PRR-04):* the paragraph above records the initial
discovery state. A later owner-authorized read-only run on 2026-10-21
authenticated to `27.0.0-RC.1` and selected the 27.0 profile (see
`docs/modernization/README.md`). That is historical RC evidence only; GA 27.0,
26.0 and current least-privilege acceptance remain unconfirmed.

The owner authorizes use of real server data for confirmation, not configuration
changes or disruptive operations. Never grant write/admin privileges for metrics.

`./scripts/release.sh` remains a dry run without `--publish`. Prereleases do not
tag `latest`; publication additionally requires explicit owner authorization,
a clean worktree and exact version tag. No tag, push, release or deployment is
part of this migration implementation.
