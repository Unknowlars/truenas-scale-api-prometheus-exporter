---
title: reporting.exporters.create
kind: method
source_rst: _sources/api_methods_reporting.exporters.create.rst.txt
source_html: api_methods_reporting.exporters.create.html
required_roles:
  - REPORTING_WRITE
---

# reporting.exporters.create

## Summary

Create a specific reporting exporter configuration containing required details for exporting reporting metrics.

## Required Roles

- `REPORTING_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: reporting_exporter_create

#### reporting_exporter_create

- Schema name: `reporting_exporter_create`
- Type: object

ReportingExportsCreateArgs parameters.
- No Additional Properties
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

### Return value

- Schema name: `ReportingExporterEntry`
- Type: object

The newly created reporting exporter configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the reporting exporter.

#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether this exporter is enabled and active.

#### attributes (required)

- Schema name: `Attributes`
- Type: object

Specific attributes for the exporter.
- No Additional Properties
##### exporter_type (required)

- Schema name: `Exporter Type`
- Type: const

Type of exporter - Graphite.

##### destination_ip (required)

- Schema name: `Destination Ip`
- Type: string

IP address of the Graphite server.
- Must be at least `1` characters long

##### destination_port (required)

- Schema name: `Destination Port`
- Type: integer

Port number of the Graphite server.
- Value must be greater or equal to `1` and lesser or equal to `65535`

##### prefix

- Schema name: `Prefix`
- Type: string
- Default: "scale"

Prefix to prepend to all metric names.

##### namespace (required)

- Schema name: `Namespace`
- Type: string

Namespace to organize metrics under.
- Must be at least `1` characters long

##### update_every

- Schema name: `Update Every`
- Type: integer
- Default: 1

Interval in seconds between metric updates.
- Value must be greater or equal to `1`

##### buffer_on_failures

- Schema name: `Buffer On Failures`
- Type: integer
- Default: 10

Number of updates to buffer when Graphite server is unavailable.
- Value must be greater or equal to `1`

##### send_names_instead_of_ids

- Schema name: `Send Names Instead Of Ids`
- Type: boolean
- Default: true

Whether to send human-readable names instead of internal IDs.

##### matching_charts

- Schema name: `Matching Charts`
- Type: string
- Default: "*"

Pattern to match charts for export (supports wildcards).
- Must be at least `1` characters long

#### name (required)

- Schema name: `Name`
- Type: string

User defined name of exporter configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
