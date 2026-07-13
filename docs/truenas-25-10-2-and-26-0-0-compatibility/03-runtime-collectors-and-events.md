# 03 — Runtime Collectors and Events Plan

## Goal

Preserve the existing metric contract while making collection correct for both
documented API shapes.

## VM units

The current runtime multiplies both VM memory methods by `1024**2`. Change this
to profile-owned normalization:

- 25.10.2: interpret the documented result as MB and convert to bytes;
- 26.0.0: interpret the documented result as bytes and do not multiply;
- malformed, negative, null, or non-finite values: omit the sample.

Review `vm.query` memory fields separately. The v26 documentation describes
VM allocation fields in MiB; do not map them to existing byte metrics until the
exact field owner and current collector behavior are proven.

## Response normalization

Keep normalization bounded and additive:

- realtime disks: accept both `disls` and `disks`;
- CPU: accept aggregate and `cpuN` entries, with nullable temperatures;
- interfaces: prefer per-second fields and use documented cumulative/fallback
  fields only where the existing parser already supports them;
- datasets: accept only documented list/object/nested forms and preserve the
  dataset identity label;
- pools: normalize structured scan, expansion, capacity, and status objects;
- application fields: accept nullable v26 fields without inventing strings;
- malformed or unknown structures: omit affected samples and increment the
  existing collector diagnostic.

Do not recursively flatten new opaque v26 objects into production metrics.

## Removed-source behavior

For v26, suppress and clear stale data for:

- Incus/legacy `virt.instance.*` and `virt.volume.*` collectors/events;
- `nvmet.global.sessions`;
- optional plural reporting graph discovery;
- `pool.is_upgraded` and `pool.ddt_prefetch`.

Do not substitute `container.*` for VM/virt metrics. Do not create zero-valued
compatibility series. Existing metric declarations remain present but emit
NaN/absent according to current exporter reset behavior.

`app.image.query` remains eligible and requires only the v26 schema/permission
fixture review; it must not be suppressed merely because it appeared in the
original draft's removal list.

## Event subscriptions

Effective defaults:

| Profile | Default subscriptions |
| --- | --- |
| 25.10 | `reporting.realtime`, `app.stats`, `virt.instance.metrics` |
| 26.0 | `reporting.realtime`, `app.stats` |
| unknown | only the common reviewed subscriptions |

Do not enable `container.metrics` by default. Its payload, required role,
cardinality, and semantic relationship to existing metrics are not sufficient
for first-release production use.

Track the string returned by `core.subscribe`, and call `core.unsubscribe` for
each successfully tracked subscription during clean shutdown and before
reconnect. Unknown/invalid subscription responses must not be treated as
success. Preserve reconnect backoff, stale expiry, and event-up diagnostics.

User-configured subscriptions that are not allowed by the selected profile are
skipped with a redacted diagnostic and marked unavailable; they must not be
sent to TrueNAS.

## Metrics and dashboards

No new metrics or dashboard panels are part of this compatibility slice. Keep
the metric contract and dashboards unchanged. Candidate v26 metrics require a
separate proposal with role, response, cardinality, semantics, fixtures, and
dashboard acceptance evidence.
