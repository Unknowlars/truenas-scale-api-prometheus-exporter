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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of string

Array of available snapshot naming schema patterns.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
