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

ID of the periodic snapshot task to analyze for deletion impact.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Object mapping retention change types to arrays of snapshots that would be affected by task deletion.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: array of string
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_additionalProperties_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
