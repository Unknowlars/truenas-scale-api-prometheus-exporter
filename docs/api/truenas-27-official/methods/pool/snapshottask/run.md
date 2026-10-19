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

Returns a `EEXIST` error code if the snapshot already existed (i.e. because the task already ran on schedule).

This method is a job.

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

ID of the periodic snapshot task to run immediately.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful task execution.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
