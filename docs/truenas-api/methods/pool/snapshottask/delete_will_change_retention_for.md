---
title: pool.snapshottask.delete_will_change_retention_for
kind: method
source_rst: _sources/api_methods_pool.snapshottask.delete_will_change_retention_for.rst.txt
source_html: api_methods_pool.snapshottask.delete_will_change_retention_for.html
required_roles:
  - SNAPSHOT_TASK_READ
---

# pool.snapshottask.delete_will_change_retention_for

## Summary

Returns a list of snapshots which will change the retention if periodic snapshot task `id` is deleted.

## Required Roles

- `SNAPSHOT_TASK_READ`

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

ID of the periodic snapshot task to analyze for deletion impact.

### Return value

- Schema name: `Result`
- Type: object

Object mapping retention change types to arrays of snapshots that would be affected by task deletion.
#### Additional Properties

Each additional property must conform to the following schema
- Type: array of string
- No Additional Items

##### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
