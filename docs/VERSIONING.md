# Versioning and Compatibility

Exporter releases use semantic versioning.

- Patch releases fix behavior without changing metric contracts.
- Minor releases may add metrics, collectors, configuration, or endpoints.
- Major releases may change runtime architecture or remove previously
  deprecated configuration.

Prometheus metric names, types, help text, and labels are compatibility
contracts independent of package versioning. A corrected replacement metric
must retain the previous metric as a compatibility alias for at least one
release and document the migration.

Collector mode becomes the default only after it matches the committed metric
contract and bundled dashboard. Legacy mode remains available for one
compatibility release after that switch.

