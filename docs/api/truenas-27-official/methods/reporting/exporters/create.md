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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: reporting_exporter_create

<a id="Call_parameters_items_i0"></a>
#### reporting_exporter_create

- Schema name: `reporting_exporter_create`
- Type: object

ReportingExportsCreateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_enabled"></a>
<a id="Call_parameters_items_i0_enabled"></a>
##### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether this exporter is enabled and active.

<a id="headingCall_parameters_items_i0_attributes"></a>
<a id="Call_parameters_items_i0_attributes"></a>
##### attributes (required)

- Schema name: `GraphiteExporter`
- Type: object

Specific attributes for the exporter.
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_exporter_type"></a>
<a id="Call_parameters_items_i0_attributes_exporter_type"></a>
###### exporter_type (required)

- Schema name: `Exporter Type`
- Type: const

Type of exporter - Graphite.
- Specific value: `"GRAPHITE"`

<a id="headingCall_parameters_items_i0_attributes_destination_ip"></a>
<a id="Call_parameters_items_i0_attributes_destination_ip"></a>
###### destination_ip (required)

- Schema name: `Destination Ip`
- Type: string

IP address of the Graphite server.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_destination_port"></a>
<a id="Call_parameters_items_i0_attributes_destination_port"></a>
###### destination_port (required)

- Schema name: `Destination Port`
- Type: integer

Port number of the Graphite server.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingCall_parameters_items_i0_attributes_prefix"></a>
<a id="Call_parameters_items_i0_attributes_prefix"></a>
###### prefix

- Schema name: `Prefix`
- Type: string
- Default: "scale"

Prefix to prepend to all metric names.

<a id="headingCall_parameters_items_i0_attributes_namespace"></a>
<a id="Call_parameters_items_i0_attributes_namespace"></a>
###### namespace (required)

- Schema name: `Namespace`
- Type: string

Namespace to organize metrics under.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_update_every"></a>
<a id="Call_parameters_items_i0_attributes_update_every"></a>
###### update_every

- Schema name: `Update Every`
- Type: integer
- Default: 1

Interval in seconds between metric updates.
- Value must be greater or equal to `1`

<a id="headingCall_parameters_items_i0_attributes_buffer_on_failures"></a>
<a id="Call_parameters_items_i0_attributes_buffer_on_failures"></a>
###### buffer_on_failures

- Schema name: `Buffer On Failures`
- Type: integer
- Default: 10

Number of updates to buffer when Graphite server is unavailable.
- Value must be greater or equal to `1`

<a id="headingCall_parameters_items_i0_attributes_send_names_instead_of_ids"></a>
<a id="Call_parameters_items_i0_attributes_send_names_instead_of_ids"></a>
###### send_names_instead_of_ids

- Schema name: `Send Names Instead Of Ids`
- Type: boolean
- Default: true

Whether to send human-readable names instead of internal IDs.

<a id="headingCall_parameters_items_i0_attributes_matching_charts"></a>
<a id="Call_parameters_items_i0_attributes_matching_charts"></a>
###### matching_charts

- Schema name: `Matching Charts`
- Type: string
- Default: "*"

Pattern to match charts for export (supports wildcards).
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

User defined name of exporter configuration.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ReportingExportsEntry`
- Type: object

The newly created reporting exporter configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the reporting exporter.

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether this exporter is enabled and active.

<a id="headingReturn_value_attributes"></a>
<a id="Return_value_attributes"></a>
#### attributes (required)

- Schema name: `GraphiteExporter`
- Type: object

Specific attributes for the exporter.
- No Additional Properties
<a id="headingReturn_value_attributes_exporter_type"></a>
<a id="Return_value_attributes_exporter_type"></a>
##### exporter_type (required)

- Schema name: `Exporter Type`
- Type: const

Type of exporter - Graphite.
- Specific value: `"GRAPHITE"`

<a id="headingReturn_value_attributes_destination_ip"></a>
<a id="Return_value_attributes_destination_ip"></a>
##### destination_ip (required)

- Schema name: `Destination Ip`
- Type: string

IP address of the Graphite server.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_destination_port"></a>
<a id="Return_value_attributes_destination_port"></a>
##### destination_port (required)

- Schema name: `Destination Port`
- Type: integer

Port number of the Graphite server.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingReturn_value_attributes_prefix"></a>
<a id="Return_value_attributes_prefix"></a>
##### prefix

- Schema name: `Prefix`
- Type: string
- Default: "scale"

Prefix to prepend to all metric names.

<a id="headingReturn_value_attributes_namespace"></a>
<a id="Return_value_attributes_namespace"></a>
##### namespace (required)

- Schema name: `Namespace`
- Type: string

Namespace to organize metrics under.
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_update_every"></a>
<a id="Return_value_attributes_update_every"></a>
##### update_every

- Schema name: `Update Every`
- Type: integer
- Default: 1

Interval in seconds between metric updates.
- Value must be greater or equal to `1`

<a id="headingReturn_value_attributes_buffer_on_failures"></a>
<a id="Return_value_attributes_buffer_on_failures"></a>
##### buffer_on_failures

- Schema name: `Buffer On Failures`
- Type: integer
- Default: 10

Number of updates to buffer when Graphite server is unavailable.
- Value must be greater or equal to `1`

<a id="headingReturn_value_attributes_send_names_instead_of_ids"></a>
<a id="Return_value_attributes_send_names_instead_of_ids"></a>
##### send_names_instead_of_ids

- Schema name: `Send Names Instead Of Ids`
- Type: boolean
- Default: true

Whether to send human-readable names instead of internal IDs.

<a id="headingReturn_value_attributes_matching_charts"></a>
<a id="Return_value_attributes_matching_charts"></a>
##### matching_charts

- Schema name: `Matching Charts`
- Type: string
- Default: "*"

Pattern to match charts for export (supports wildcards).
- Must be at least `1` characters long

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

User defined name of exporter configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
