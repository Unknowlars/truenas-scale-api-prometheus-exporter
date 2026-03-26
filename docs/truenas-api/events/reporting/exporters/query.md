---
title: reporting.exporters.query
kind: event
source_rst: _sources/api_events_reporting.exporters.query.rst.txt
source_html: api_events_reporting.exporters.query.html
required_roles:
  - REPORTING_READ
---

# reporting.exporters.query

## Summary

Sent on reporting.exporters changes.

## Required Roles

- `REPORTING_READ`

## Schema

- Type: object

### ADDED

- Schema name: `ReportingExporterAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `ReportingExporterEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the reporting exporter.

##### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether this exporter is enabled and active.

##### attributes (required)

- Schema name: `Attributes`
- Type: object

Specific attributes for the exporter.
- No Additional Properties
###### exporter_type (required)

- Schema name: `Exporter Type`
- Type: const

Type of exporter - Graphite.

###### destination_ip (required)

- Schema name: `Destination Ip`
- Type: string

IP address of the Graphite server.
- Must be at least `1` characters long

###### destination_port (required)

- Schema name: `Destination Port`
- Type: integer

Port number of the Graphite server.
- Value must be greater or equal to `1` and lesser or equal to `65535`

###### prefix

- Schema name: `Prefix`
- Type: string
- Default: "scale"

Prefix to prepend to all metric names.

###### namespace (required)

- Schema name: `Namespace`
- Type: string

Namespace to organize metrics under.
- Must be at least `1` characters long

###### update_every

- Schema name: `Update Every`
- Type: integer
- Default: 1

Interval in seconds between metric updates.
- Value must be greater or equal to `1`

###### buffer_on_failures

- Schema name: `Buffer On Failures`
- Type: integer
- Default: 10

Number of updates to buffer when Graphite server is unavailable.
- Value must be greater or equal to `1`

###### send_names_instead_of_ids

- Schema name: `Send Names Instead Of Ids`
- Type: boolean
- Default: true

Whether to send human-readable names instead of internal IDs.

###### matching_charts

- Schema name: `Matching Charts`
- Type: string
- Default: "*"

Pattern to match charts for export (supports wildcards).
- Must be at least `1` characters long

##### name (required)

- Schema name: `Name`
- Type: string

User defined name of exporter configuration.

### CHANGED

- Schema name: `ReportingExporterChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `ReportingExporterEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the reporting exporter.

##### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether this exporter is enabled and active.

##### attributes (required)

- Schema name: `Attributes`
- Type: object

Specific attributes for the exporter.
- No Additional Properties
###### exporter_type (required)

- Schema name: `Exporter Type`
- Type: const

Type of exporter - Graphite.

###### destination_ip (required)

- Schema name: `Destination Ip`
- Type: string

IP address of the Graphite server.
- Must be at least `1` characters long

###### destination_port (required)

- Schema name: `Destination Port`
- Type: integer

Port number of the Graphite server.
- Value must be greater or equal to `1` and lesser or equal to `65535`

###### prefix

- Schema name: `Prefix`
- Type: string
- Default: "scale"

Prefix to prepend to all metric names.

###### namespace (required)

- Schema name: `Namespace`
- Type: string

Namespace to organize metrics under.
- Must be at least `1` characters long

###### update_every

- Schema name: `Update Every`
- Type: integer
- Default: 1

Interval in seconds between metric updates.
- Value must be greater or equal to `1`

###### buffer_on_failures

- Schema name: `Buffer On Failures`
- Type: integer
- Default: 10

Number of updates to buffer when Graphite server is unavailable.
- Value must be greater or equal to `1`

###### send_names_instead_of_ids

- Schema name: `Send Names Instead Of Ids`
- Type: boolean
- Default: true

Whether to send human-readable names instead of internal IDs.

###### matching_charts

- Schema name: `Matching Charts`
- Type: string
- Default: "*"

Pattern to match charts for export (supports wildcards).
- Must be at least `1` characters long

##### name (required)

- Schema name: `Name`
- Type: string

User defined name of exporter configuration.

### REMOVED

- Schema name: `ReportingExporterRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
