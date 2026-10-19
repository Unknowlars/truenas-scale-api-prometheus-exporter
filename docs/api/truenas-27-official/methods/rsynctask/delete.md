---
title: rsynctask.delete
kind: method
source_rst: _sources/api_methods_rsynctask.delete.rst.txt
source_html: api_methods_rsynctask.delete.html
required_roles:
  - SNAPSHOT_TASK_WRITE
---

# rsynctask.delete

## Summary

Delete Rsync Task of `id`.

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

ID of the rsync task to delete.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Whether the rsync task was successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
