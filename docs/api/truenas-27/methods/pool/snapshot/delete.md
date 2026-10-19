---
title: pool.snapshot.delete
kind: method
source_rst: _sources/api_methods_pool.snapshot.delete.rst.txt
source_html: api_methods_pool.snapshot.delete.html
required_roles:
  - SNAPSHOT_DELETE
---

# pool.snapshot.delete

## Required Roles

- `SNAPSHOT_DELETE`

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
- Type: string

ID of the snapshot to delete.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for controlling snapshot deletion behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_defer"></a>
<a id="Call_parameters_items_i1_defer"></a>
##### defer

- Schema name: `Defer`
- Type: boolean
- Default: false

Defer deletion of the snapshot.

<a id="headingCall_parameters_items_i1_recursive"></a>
<a id="Call_parameters_items_i1_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively delete child snapshots.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Indicates successful snapshot deletion.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
