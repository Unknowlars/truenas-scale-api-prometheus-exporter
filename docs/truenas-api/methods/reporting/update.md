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

`tier1_days` can be set to specify for how many days we want to store reporting history which in netdata terms specifies the number of days netdata should be storing data in tier1 storage.

## Required Roles

- `REPORTING_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: reporting_update

#### reporting_update

- Schema name: `reporting_update`
- Type: object

ReportingUpdateArgs parameters.
- No Additional Properties
##### tier0_days

- Schema name: `Tier0 Days`
- Type: integer

Number of days to keep high-resolution reporting data.
- Value must be greater or equal to `1`

##### tier1_days

- Schema name: `Tier1 Days`
- Type: integer

Number of days to keep lower-resolution aggregated reporting data.
- Value must be greater or equal to `1`

##### tier1_update_interval

- Schema name: `Tier1 Update Interval`
- Type: integer

Interval in seconds for updating aggregated tier1 data.
- Value must be greater or equal to `1`

### Return value

- Schema name: `ReportingEntry`
- Type: object

The updated reporting configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the reporting configuration.

#### tier0_days (required)

- Schema name: `Tier0 Days`
- Type: integer

Number of days to keep high-resolution reporting data.
- Value must be greater or equal to `1`

#### tier1_days (required)

- Schema name: `Tier1 Days`
- Type: integer

Number of days to keep lower-resolution aggregated reporting data.
- Value must be greater or equal to `1`

#### tier1_update_interval (required)

- Schema name: `Tier1 Update Interval`
- Type: integer

Interval in seconds for updating aggregated tier1 data.
- Value must be greater or equal to `1`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
