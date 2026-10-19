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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `ReportingExportsAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `ReportingExportsEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the reporting exporter.

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether this exporter is enabled and active.

<a id="headingADDED_fields_attributes"></a>
<a id="ADDED_fields_attributes"></a>
##### attributes (required)

- Schema name: `GraphiteExporter`
- Type: object

Specific attributes for the exporter.
- No Additional Properties
<a id="headingADDED_fields_attributes_exporter_type"></a>
<a id="ADDED_fields_attributes_exporter_type"></a>
###### exporter_type (required)

- Schema name: `Exporter Type`
- Type: const

Type of exporter - Graphite.
- Specific value: `"GRAPHITE"`

<a id="headingADDED_fields_attributes_destination_ip"></a>
<a id="ADDED_fields_attributes_destination_ip"></a>
###### destination_ip (required)

- Schema name: `Destination Ip`
- Type: string

IP address of the Graphite server.
- Must be at least `1` characters long

<a id="headingADDED_fields_attributes_destination_port"></a>
<a id="ADDED_fields_attributes_destination_port"></a>
###### destination_port (required)

- Schema name: `Destination Port`
- Type: integer

Port number of the Graphite server.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingADDED_fields_attributes_prefix"></a>
<a id="ADDED_fields_attributes_prefix"></a>
###### prefix

- Schema name: `Prefix`
- Type: string
- Default: "scale"

Prefix to prepend to all metric names.

<a id="headingADDED_fields_attributes_namespace"></a>
<a id="ADDED_fields_attributes_namespace"></a>
###### namespace (required)

- Schema name: `Namespace`
- Type: string

Namespace to organize metrics under.
- Must be at least `1` characters long

<a id="headingADDED_fields_attributes_update_every"></a>
<a id="ADDED_fields_attributes_update_every"></a>
###### update_every

- Schema name: `Update Every`
- Type: integer
- Default: 1

Interval in seconds between metric updates.
- Value must be greater or equal to `1`

<a id="headingADDED_fields_attributes_buffer_on_failures"></a>
<a id="ADDED_fields_attributes_buffer_on_failures"></a>
###### buffer_on_failures

- Schema name: `Buffer On Failures`
- Type: integer
- Default: 10

Number of updates to buffer when Graphite server is unavailable.
- Value must be greater or equal to `1`

<a id="headingADDED_fields_attributes_send_names_instead_of_ids"></a>
<a id="ADDED_fields_attributes_send_names_instead_of_ids"></a>
###### send_names_instead_of_ids

- Schema name: `Send Names Instead Of Ids`
- Type: boolean
- Default: true

Whether to send human-readable names instead of internal IDs.

<a id="headingADDED_fields_attributes_matching_charts"></a>
<a id="ADDED_fields_attributes_matching_charts"></a>
###### matching_charts

- Schema name: `Matching Charts`
- Type: string
- Default: "*"

Pattern to match charts for export (supports wildcards).
- Must be at least `1` characters long

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

User defined name of exporter configuration.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `ReportingExportsChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `ReportingExportsEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the reporting exporter.

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether this exporter is enabled and active.

<a id="headingCHANGED_fields_attributes"></a>
<a id="CHANGED_fields_attributes"></a>
##### attributes (required)

- Schema name: `GraphiteExporter`
- Type: object

Specific attributes for the exporter.
- No Additional Properties
<a id="headingCHANGED_fields_attributes_exporter_type"></a>
<a id="CHANGED_fields_attributes_exporter_type"></a>
###### exporter_type (required)

- Schema name: `Exporter Type`
- Type: const

Type of exporter - Graphite.
- Specific value: `"GRAPHITE"`

<a id="headingCHANGED_fields_attributes_destination_ip"></a>
<a id="CHANGED_fields_attributes_destination_ip"></a>
###### destination_ip (required)

- Schema name: `Destination Ip`
- Type: string

IP address of the Graphite server.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_attributes_destination_port"></a>
<a id="CHANGED_fields_attributes_destination_port"></a>
###### destination_port (required)

- Schema name: `Destination Port`
- Type: integer

Port number of the Graphite server.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingCHANGED_fields_attributes_prefix"></a>
<a id="CHANGED_fields_attributes_prefix"></a>
###### prefix

- Schema name: `Prefix`
- Type: string
- Default: "scale"

Prefix to prepend to all metric names.

<a id="headingCHANGED_fields_attributes_namespace"></a>
<a id="CHANGED_fields_attributes_namespace"></a>
###### namespace (required)

- Schema name: `Namespace`
- Type: string

Namespace to organize metrics under.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_attributes_update_every"></a>
<a id="CHANGED_fields_attributes_update_every"></a>
###### update_every

- Schema name: `Update Every`
- Type: integer
- Default: 1

Interval in seconds between metric updates.
- Value must be greater or equal to `1`

<a id="headingCHANGED_fields_attributes_buffer_on_failures"></a>
<a id="CHANGED_fields_attributes_buffer_on_failures"></a>
###### buffer_on_failures

- Schema name: `Buffer On Failures`
- Type: integer
- Default: 10

Number of updates to buffer when Graphite server is unavailable.
- Value must be greater or equal to `1`

<a id="headingCHANGED_fields_attributes_send_names_instead_of_ids"></a>
<a id="CHANGED_fields_attributes_send_names_instead_of_ids"></a>
###### send_names_instead_of_ids

- Schema name: `Send Names Instead Of Ids`
- Type: boolean
- Default: true

Whether to send human-readable names instead of internal IDs.

<a id="headingCHANGED_fields_attributes_matching_charts"></a>
<a id="CHANGED_fields_attributes_matching_charts"></a>
###### matching_charts

- Schema name: `Matching Charts`
- Type: string
- Default: "*"

Pattern to match charts for export (supports wildcards).
- Must be at least `1` characters long

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

User defined name of exporter configuration.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `ReportingExportsRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
