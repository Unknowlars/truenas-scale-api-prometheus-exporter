# Bounded read-only live validation

Status: resolved

Confirm authentication, exact version and effective permissions. Then run the
five-method smoke and sequential five-minute exporter sessions with current and
historical settings. Report failures rather than fixing behavior.

## Answer

Modern and legacy authentication succeed with the new key. The server reports
27.0.0-RC.1 and selects the 27.0 profile. The owner explicitly authorized the
wildcard-access key after disclosure; every actual RPC remained read-only.

The five-method smoke and both five-minute sessions completed. Sixteen polling
cycles were up/ready; HTTP scrapes caused no NAS calls. Events/subscriptions
reconnected after a locally closed socket. The packaged Python 3.14.6 runtime
also completed two bounded checks. Across the checks, 512 source/metric
comparisons matched and 16 SMB1 comparisons failed.

The focused packaged HTTP check confirmed that continuous fresh events are not
republished into collector snapshots: CPU becomes NaN after the snapshot TTL
while the newest event is <2 seconds old. See `../report.md` and
`../evidence.json`. No NAS configuration changes or deployment occurred.
