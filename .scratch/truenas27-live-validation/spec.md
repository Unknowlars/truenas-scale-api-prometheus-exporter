# SCALE 27 live validation

Status: resolved

Validate modernization changes from `de0e18b` through `a1a5526` against local
checks and the owner-authorized SCALE 27 server. Test and report only; do not
change exporter behavior. Preserve the pre-existing untracked gap analysis.

Use only bounded, documented read-only RPCs and reviewed subscriptions. Keep
credentials and raw production responses out of files and output. Verify modern
authentication with the owner-confirmed username and inspect key privileges. Compare
current defaults and the supplied historical settings in sequential five-minute
sessions, subject to authentication, safety and permission gates.

Record sanitized final evidence in `docs/modernization/README.md`. No deployment,
publication, commit, push, hosted automation or NAS configuration changes.

## Owner clarification during execution

The permission probe returned a wildcard method/resource allowlist. After this
was disclosed, the owner explicitly instructed continued use of the supplied
key. This supersedes the read-only-key prerequisite for this validation run;
every actual operation must still be read-only and bounded. Least-privilege
compatibility remains unverified.

## Work

- 01: Local validation, Python matrix, dependency audit, metric contracts.
- 02: Authentication, permission gate, live smoke and exporter checks.
- 03: Evidence report, limitations and final worktree review.
