---
title: replication.list_naming_schemas
kind: method
source_rst: _sources/api_methods_replication.list_naming_schemas.rst.txt
source_html: api_methods_replication.list_naming_schemas.html
required_roles:
  - REPLICATION_TASK_WRITE
---

# replication.list_naming_schemas

## Summary

List all naming schemas used in periodic snapshot and replication tasks.

## Required Roles

- `REPLICATION_TASK_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of string

Array of available snapshot naming schema patterns.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
