---
title: pool.snapshot.rollback
kind: method
source_rst: _sources/api_methods_pool.snapshot.rollback.rst.txt
source_html: api_methods_pool.snapshot.rollback.html
required_roles:
  - POOL_WRITE
  - SNAPSHOT_WRITE
---

# pool.snapshot.rollback

## Required Roles

- `POOL_WRITE`
- `SNAPSHOT_WRITE`

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

ID of the snapshot to rollback to.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for controlling snapshot rollback behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_recursive"></a>
<a id="Call_parameters_items_i1_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Destroy any snapshots and bookmarks more recent than the one specified.

<a id="headingCall_parameters_items_i1_recursive_clones"></a>
<a id="Call_parameters_items_i1_recursive_clones"></a>
##### recursive_clones

- Schema name: `Recursive Clones`
- Type: boolean
- Default: false

Just like `recursive`, but also destroy any clones.

<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force unmount of any clones.

<a id="headingCall_parameters_items_i1_recursive_rollback"></a>
<a id="Call_parameters_items_i1_recursive_rollback"></a>
##### recursive_rollback

- Schema name: `Recursive Rollback`
- Type: boolean
- Default: false

Do a complete recursive rollback of each child snapshot for `id`. If any child does not have specified snapshot, this operation will fail.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful snapshot rollback.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
