---
title: reporting.exporters.get_instance
kind: method
source_rst: _sources/api_methods_reporting.exporters.get_instance.rst.txt
source_html: api_methods_reporting.exporters.get_instance.html
required_roles:
  - REPORTING_READ
---

# reporting.exporters.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `REPORTING_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ReportingExportsEntry`
- Type: object
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
