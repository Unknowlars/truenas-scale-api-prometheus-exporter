---
title: disk.temperature_agg
kind: method
source_rst: _sources/api_methods_disk.temperature_agg.rst.txt
source_html: api_methods_disk.temperature_agg.html
required_roles:
  - REPORTING_READ
---

# disk.temperature_agg

## Summary

Returns min/max/avg temperature for `names` disks over the last `days` days.

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

#### Parameter 1: names

<a id="Call_parameters_items_i0"></a>
#### names

- Schema name: `names`
- Type: array of string

Array of disk names to retrieve temperature aggregates for.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
- Type: string

#### Parameter 2: days

<a id="Call_parameters_items_i1"></a>
#### days

- Schema name: `days`
- Type: integer
- Default: 7

Number of days to aggregate temperature data over.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Object mapping disk names to their aggregated temperature statistics.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `DiskTemperatureAggEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_additionalProperties_min"></a>
<a id="Return_value_additionalProperties_min"></a>
##### min (required)

- Schema name: `Min`

Minimum temperature recorded during the time period or `null`.
<a id="Return_value_additionalProperties_min_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_min_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_min_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_additionalProperties_min_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_min_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_additionalProperties_min_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_additionalProperties_min_anyOf_i2)

- Type: null

<a id="headingReturn_value_additionalProperties_max"></a>
<a id="Return_value_additionalProperties_max"></a>
##### max (required)

- Schema name: `Max`

Maximum temperature recorded during the time period or `null`.
<a id="Return_value_additionalProperties_max_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_max_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_additionalProperties_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_max_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_additionalProperties_max_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_additionalProperties_max_anyOf_i2)

- Type: null

<a id="headingReturn_value_additionalProperties_avg"></a>
<a id="Return_value_additionalProperties_avg"></a>
##### avg (required)

- Schema name: `Avg`

Average temperature during the time period or `null`.
<a id="Return_value_additionalProperties_avg_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_avg_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_avg_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_additionalProperties_avg_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_avg_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_additionalProperties_avg_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_additionalProperties_avg_anyOf_i2)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
