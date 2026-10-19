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

Delete a Periodic Snapshot Task with specific `id`.

## Required Roles

- `SNAPSHOT_TASK_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the periodic snapshot task to delete.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for controlling task deletion behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_fixate_removal_date"></a>
<a id="Call_parameters_items_i1_fixate_removal_date"></a>
##### fixate_removal_date

- Schema name: `Fixate Removal Date`
- Type: boolean
- Default: false

Whether to fix the removal date of existing snapshots when the task is deleted.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Indicates successful deletion of the periodic snapshot task.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
