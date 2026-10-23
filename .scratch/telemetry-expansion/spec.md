# Bounded TrueNAS telemetry expansion

The owner requests as much useful read-only TrueNAS telemetry as practical,
starting with the gaps identified against the pinned 27 API documentation.
Expand typed metrics rather than arbitrary response extraction. Preserve all
420 existing metric contracts, polling/event snapshot behavior, API budgets,
privacy, and 25.10/26.0 compatibility.

Implement and verify pool scan details, dataset accounting, SED status, UPS
reporting, cloud backup outcomes, and 27-only tiering where the documented
schemas and release source establish meaningful fields and units. Prefer
existing projected responses; isolate optional unsupported sources. No raw
response captures, credential values, mutating RPCs, or new arbitrary labels.

Verification uses the existing runtime/transport and public metric snapshot
boundaries, synthetic fixtures, then bounded read-only live checks. Complete
the repository validation gate, record official/mocked/live evidence separately,
and rebuild/recreate only the already authorized local test exporter. Do not
publish images, push, or change NAS configuration.
