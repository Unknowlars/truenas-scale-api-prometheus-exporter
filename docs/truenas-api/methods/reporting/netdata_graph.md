---
title: reporting.netdata_graph
kind: method
source_rst: _sources/api_methods_reporting.netdata_graph.rst.txt
source_html: api_methods_reporting.netdata_graph.html
required_roles:
  - REPORTING_READ
---

# reporting.netdata_graph

## Summary

Get reporting data for `name` graph.

## Required Roles

- `REPORTING_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: str

#### str

- Schema name: `str`
- Type: string

String identifier for the specific graph to retrieve.
- Must be at least `1` characters long

#### Parameter 2: query

#### query

- Schema name: `query`
- Type: object

Query parameters for filtering and formatting the returned data.
- No Additional Properties
##### unit

- Schema name: `Unit`
- Default: null

Time unit for data aggregation. `null` for default aggregation.
###### Any of

####### Option 1

- Type: enum (of string)

####### Option 2

- Type: null

##### page

- Schema name: `Page`
- Type: integer
- Default: 1

Page number for paginated results.
- Value must be greater or equal to `1`

##### aggregate

- Schema name: `Aggregate`
- Type: boolean
- Default: true

Whether to return aggregated data or raw data points.

##### start

- Schema name: `Start`
- Default: null

Start timestamp for the data range. `null` for default start time.
###### Any of

####### Option 1

- Type: integer
- Value must be strictly greater than `0`

####### Option 2

- Type: null

##### end

- Schema name: `End`
- Default: null

End timestamp for the data range. `null` for current time.
###### Any of

####### Option 1

- Type: integer
- Value must be strictly greater than `0`

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: array of object

Array of performance data responses for each requested graph.
- No Additional Items

#### Each item of this array must be:

#### ReportingGetDataResponse

- Schema name: `ReportingGetDataResponse`
- Type: object
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Name of the performance metric.
- Must be at least `1` characters long

##### identifier (required)

- Schema name: `Identifier`

Specific instance identifier for the metric. `null` for system-wide metrics.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### data (required)

- Schema name: `Data`
- Type: array

Array of time-series data points for the requested time period.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### aggregations (required)

- Schema name: `Aggregations`
- Type: object

Statistical aggregations of the data over the time period.
- No Additional Properties
###### min (required)

- Schema name: `Min`
- Type: object

Minimum values for each data series over the time period.

###### mean (required)

- Schema name: `Mean`
- Type: object

Average values for each data series over the time period.

###### max (required)

- Schema name: `Max`
- Type: object

Maximum values for each data series over the time period.

##### start (required)

- Schema name: `Start`
- Type: integer

Actual start timestamp of the returned data.
- Value must be strictly greater than `0`

##### end (required)

- Schema name: `End`
- Type: integer

Actual end timestamp of the returned data.
- Value must be strictly greater than `0`

##### legend (required)

- Schema name: `Legend`
- Type: array of string

Array of labels describing each data series in the results.
- No Additional Items

###### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
