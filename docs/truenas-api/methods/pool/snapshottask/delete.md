---
title: pool.snapshottask.delete
kind: method
source_rst: _sources/api_methods_pool.snapshottask.delete.rst.txt
source_html: api_methods_pool.snapshottask.delete.html
required_roles:
  - SNAPSHOT_TASK_WRITE
---

# pool.snapshottask.delete

## Summary

Delete a Periodic Snapshot Task with specific `id`

.. examples(websocket)::

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.snapshottask.delete", "params": [ 1 ] }

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

ID of the periodic snapshot task to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options for controlling task deletion behavior.
- No Additional Properties
##### fixate_removal_date

- Schema name: `Fixate Removal Date`
- Type: boolean
- Default: false

Whether to fix the removal date of existing snapshots when the task is deleted.

### Return value

- Schema name: `Result`
- Type: const

Indicates successful deletion of the periodic snapshot task.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
