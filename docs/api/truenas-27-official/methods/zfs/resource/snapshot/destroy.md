---
title: zfs.resource.snapshot.destroy
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.destroy.rst.txt
source_html: api_methods_zfs.resource.snapshot.destroy.html
required_roles:
  - SNAPSHOT_DELETE
---

# zfs.resource.snapshot.destroy

## Summary

Destroy ZFS snapshots.

A validation error is raised when:

- the snapshot does not exist (`ENOENT`)

- it has dependent clones and `defer` is `false` (`EBUSY`)

- it has active holds (`EBUSY`)

- a protected path is targeted without `bypass` (`EACCES`)

Examples:

Destroy a single snapshot:

.. code:: json

{"path": "tank/data@backup"}

Destroy matching snapshots in child datasets:

.. code:: json

{"path": "tank@backup", "recursive": true}

Defer destruction if the snapshot is in use:

.. code:: json

{"path": "tank/data@snap", "defer": true}

Destroy all snapshots of a dataset:

.. code:: json

{"path": "tank/data", "all_snapshots": true}

Destroy all snapshots of a dataset and its children:

.. code:: json

{"path": "tank", "all_snapshots": true, "recursive": true}

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

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Destroy parameters for removing ZFS snapshots.
- No Additional Properties
<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Path to destroy. Either a snapshot path (e.g., 'pool/dataset@snapshot') or a dataset path when all_snapshots=True (e.g., 'pool/dataset').
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_recursive"></a>
<a id="Call_parameters_items_i0_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Recursively destroy matching snapshots in child datasets.

<a id="headingCall_parameters_items_i0_all_snapshots"></a>
<a id="Call_parameters_items_i0_all_snapshots"></a>
##### all_snapshots

- Schema name: `All Snapshots`
- Type: boolean
- Default: false

If True, path should be a dataset path and all its snapshots will be destroyed.

<a id="headingCall_parameters_items_i0_defer"></a>
<a id="Call_parameters_items_i0_defer"></a>
##### defer

- Schema name: `Defer`
- Type: boolean
- Default: false

Defer destruction if snapshot is in use (e.g., has clones).

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
