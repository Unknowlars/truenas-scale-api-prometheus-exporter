---
title: reporting.update
kind: method
source_rst: _sources/api_methods_reporting.update.rst.txt
source_html: api_methods_reporting.update.html
required_roles:
  - REPORTING_WRITE
---

# reporting.update

## Summary

Update reporting configuration settings.

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

#### Parameter 1: reporting_update

<a id="Call_parameters_items_i0"></a>
#### reporting_update

- Schema name: `reporting_update`
- Type: object

ReportingUpdateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_tier0_days"></a>
<a id="Call_parameters_items_i0_tier0_days"></a>
##### tier0_days

- Schema name: `Tier0 Days`
- Type: integer

Number of days to keep high-resolution reporting data.
- Value must be greater or equal to `1`

<a id="headingCall_parameters_items_i0_tier1_days"></a>
<a id="Call_parameters_items_i0_tier1_days"></a>
##### tier1_days

- Schema name: `Tier1 Days`
- Type: integer

Number of days to keep lower-resolution aggregated reporting data.
- Value must be greater or equal to `1`

<a id="headingCall_parameters_items_i0_tier1_update_interval"></a>
<a id="Call_parameters_items_i0_tier1_update_interval"></a>
##### tier1_update_interval

- Schema name: `Tier1 Update Interval`
- Type: integer

Interval in seconds for updating aggregated tier1 data.
- Value must be greater or equal to `1`

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ReportingEntry`
- Type: object

The updated reporting configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the reporting configuration.

<a id="headingReturn_value_tier0_days"></a>
<a id="Return_value_tier0_days"></a>
#### tier0_days (required)

- Schema name: `Tier0 Days`
- Type: integer

Number of days to keep high-resolution reporting data.
- Value must be greater or equal to `1`

<a id="headingReturn_value_tier1_days"></a>
<a id="Return_value_tier1_days"></a>
#### tier1_days (required)

- Schema name: `Tier1 Days`
- Type: integer

Number of days to keep lower-resolution aggregated reporting data.
- Value must be greater or equal to `1`

<a id="headingReturn_value_tier1_update_interval"></a>
<a id="Return_value_tier1_update_interval"></a>
#### tier1_update_interval (required)

- Schema name: `Tier1 Update Interval`
- Type: integer

Interval in seconds for updating aggregated tier1 data.
- Value must be greater or equal to `1`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
