---
title: reporting.get_data
kind: method
source_rst: _sources/api_methods_reporting.get_data.rst.txt
source_html: api_methods_reporting.get_data.html
required_roles:
  - REPORTING_READ
---

# reporting.get_data

## Summary

Get reporting data for given graphs.

List of possible graphs can be retrieved using [reporting.graphs](graphs.md) call.

For the time period of the graph either `unit` and `page` OR `start` and `end` should be used, not both.

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

#### Parameter 1: graphs

<a id="Call_parameters_items_i0"></a>
#### graphs

- Schema name: `graphs`
- Type: array of object

Array of graph identifiers specifying which metrics to retrieve.
- Must contain a minimum of `1` items
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
##### GraphIdentifier

- Schema name: `GraphIdentifier`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_items_name"></a>
<a id="Call_parameters_items_i0_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: enum (of string)

Type of performance metric to retrieve. `cpu`: CPU usage statistics `cputemp`: CPU temperature readings `disk`: Disk I/O statistics `interface`: Network interface statistics `load`: System load averages `processes`: Process count and statistics `memory`: Memory usage statistics `uptime`: System uptime `arcsize`: ZFS ARC cache size `disktemp`: Disk temperature readings `upscharge`: UPS battery charge level `upsruntime`: UPS estimated runtime `upsvoltage`: UPS voltage readings `upscurrent`: UPS current readings `upsfrequency`: UPS frequency readings `upsload`: UPS load percentage `upstemperature`: UPS temperature readings
###### Must be one of:

- "cpu"
- "cputemp"
- "disk"
- "interface"
- "load"
- "processes"
- "memory"
- "uptime"
- "arcsize"
- "disktemp"
- "upscharge"
- "upsruntime"
- "upsvoltage"
- "upscurrent"
- "upsfrequency"
- "upsload"
- "upstemperature"

<a id="headingCall_parameters_items_i0_items_identifier"></a>
<a id="Call_parameters_items_i0_items_identifier"></a>
###### identifier

- Schema name: `Identifier`
- Default: null

Specific instance identifier for the metric (e.g., device name, interface name). `null` for system-wide metrics.
<a id="Call_parameters_items_i0_items_identifier_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_items_identifier_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_items_identifier_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_items_identifier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_items_identifier_anyOf_i1)

- Type: null

#### Parameter 2: query

<a id="Call_parameters_items_i1"></a>
#### query

- Schema name: `query`
- Type: object

Query parameters for filtering and formatting the returned data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_unit"></a>
<a id="Call_parameters_items_i1_unit"></a>
##### unit

- Schema name: `Unit`
- Default: null

Time unit for data aggregation. `null` for default aggregation.
<a id="Call_parameters_items_i1_unit_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_unit_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="tab-pane_Call_parameters_items_i1_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_unit_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_page"></a>
<a id="Call_parameters_items_i1_page"></a>
##### page

- Schema name: `Page`
- Type: integer
- Default: 1

Page number for paginated results.
- Value must be greater or equal to `1`

<a id="headingCall_parameters_items_i1_aggregate"></a>
<a id="Call_parameters_items_i1_aggregate"></a>
##### aggregate

- Schema name: `Aggregate`
- Type: boolean
- Default: true

Whether to return aggregated data or raw data points.

<a id="headingCall_parameters_items_i1_start"></a>
<a id="Call_parameters_items_i1_start"></a>
##### start

- Schema name: `Start`
- Default: null

Start timestamp for the data range. `null` for default start time.
<a id="Call_parameters_items_i1_start_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_start_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_start_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0`

<a id="tab-pane_Call_parameters_items_i1_start_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_start_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_end"></a>
<a id="Call_parameters_items_i1_end"></a>
##### end

- Schema name: `End`
- Default: null

End timestamp for the data range. `null` for current time.
<a id="Call_parameters_items_i1_end_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_end_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_end_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0`

<a id="tab-pane_Call_parameters_items_i1_end_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_end_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of performance data responses for each requested graph.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### ReportingGetDataResponse

- Schema name: `ReportingGetDataResponse`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the performance metric.
- Must be at least `1` characters long

<a id="headingReturn_value_items_identifier"></a>
<a id="Return_value_items_identifier"></a>
##### identifier (required)

- Schema name: `Identifier`

Specific instance identifier for the metric. `null` for system-wide metrics.
<a id="Return_value_items_identifier_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_identifier_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_identifier_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_identifier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_identifier_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_data"></a>
<a id="Return_value_items_data"></a>
##### data (required)

- Schema name: `Data`
- Type: array

Array of time-series data points for the requested time period.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_data_items"></a>
- Type: object

<a id="headingReturn_value_items_aggregations"></a>
<a id="Return_value_items_aggregations"></a>
##### aggregations (required)

Statistical aggregations of the data over the time period.
<a id="Return_value_items_aggregations_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_aggregations_anyOf_i0"></a>
###### [Aggregations](#tab-pane_Return_value_items_aggregations_anyOf_i0)

- Schema name: `Aggregations`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_aggregations_anyOf_i0_min"></a>
<a id="Return_value_items_aggregations_anyOf_i0_min"></a>
###### min (required)

- Schema name: `Min`
- Type: object

Minimum values for each data series over the time period.

<a id="headingReturn_value_items_aggregations_anyOf_i0_mean"></a>
<a id="Return_value_items_aggregations_anyOf_i0_mean"></a>
###### mean (required)

- Schema name: `Mean`
- Type: object

Average values for each data series over the time period.

<a id="headingReturn_value_items_aggregations_anyOf_i0_max"></a>
<a id="Return_value_items_aggregations_anyOf_i0_max"></a>
###### max (required)

- Schema name: `Max`
- Type: object

Maximum values for each data series over the time period.

<a id="tab-pane_Return_value_items_aggregations_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_aggregations_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_start"></a>
<a id="Return_value_items_start"></a>
##### start (required)

- Schema name: `Start`
- Type: integer

Actual start timestamp of the returned data.
- Value must be strictly greater than `0`

<a id="headingReturn_value_items_end"></a>
<a id="Return_value_items_end"></a>
##### end (required)

- Schema name: `End`
- Type: integer

Actual end timestamp of the returned data.
- Value must be strictly greater than `0`

<a id="headingReturn_value_items_legend"></a>
<a id="Return_value_items_legend"></a>
##### legend (required)

- Schema name: `Legend`
- Type: array of string

Array of labels describing each data series in the results.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_legend_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
