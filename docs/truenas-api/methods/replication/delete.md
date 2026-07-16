---
title: replication.delete
kind: method
source_rst: _sources/api_methods_replication.delete.rst.txt
source_html: api_methods_replication.delete.html
required_roles:
  - REPLICATION_TASK_WRITE
---

# replication.delete

## Summary

Delete a Replication Task with specific `id`

## Required Roles

- `REPLICATION_TASK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the replication task to delete.

### Return value

- Schema name: `Result`
- Type: boolean

Whether the replication task was successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
