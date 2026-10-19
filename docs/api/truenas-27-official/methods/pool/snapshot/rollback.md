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

## Summary

Roll the dataset of snapshot `id` back to the state captured by that snapshot.

.. warning::

This operation is destructive. Any data written to the dataset after the snapshot was taken is permanently lost. Snapshots more recent than `id` must also be destroyed for the rollback to proceed; use the `recursive`, `recursive_clones`, or `recursive_rollback` options to control how newer snapshots and their clones are handled. A hold on a newer snapshot, or a clone that cannot be destroyed, is reported as a JSON-RPC `error` response (code `-32001`, *Method call error*, errno `EBUSY`); release a hold with [pool.snapshot.release](release.md) first.

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
