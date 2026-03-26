---
title: reporting.config
kind: method
source_rst: _sources/api_methods_reporting.config.rst.txt
source_html: api_methods_reporting.config.html
required_roles:
  - REPORTING_READ
---

# reporting.config

## Required Roles

- `REPORTING_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `ReportingEntry`
- Type: object
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
