---
title: pool.snapshottask.run
kind: method
source_rst: _sources/api_methods_pool.snapshottask.run.rst.txt
source_html: api_methods_pool.snapshottask.run.html
required_roles:
  - SNAPSHOT_TASK_WRITE
---

# pool.snapshottask.run

## Summary

Execute a Periodic Snapshot Task of `id`.

## Required Roles

- `SNAPSHOT_TASK_WRITE`

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

ID of the periodic snapshot task to run immediately.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful task execution.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
