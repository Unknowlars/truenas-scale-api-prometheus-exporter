---
title: pool.dataset.rename
kind: method
source_rst: _sources/api_methods_pool.dataset.rename.rst.txt
source_html: api_methods_pool.dataset.rename.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.rename

## Summary

Rename a zfs resource (filesystem, snapshot, or zvolume) of `id`.

No safety checks are performed when renaming ZFS resources. If the dataset is in use by services such as SMB, iSCSI, snapshot tasks, replication, or cloud sync, renaming may cause disruptions or service failures.

Proceed only if you are certain the ZFS resource is not in use and fully understand the risks. Set Force to continue.

NOTE: The "recursive" option is only valid for renaming snapshots. If True, and a snapshot is given, the snapshot will be renamed recursively for all children. For example: dozer/a@now, dozer/a/b@now will be renamed to dozer/a@new dozer/a/b@new. Renaming snapshots IS NOT recommended and can cause disruptions or service failures all the same.

## Required Roles

- `DATASET_WRITE`

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

The current dataset ID (full path) to rename.
- Must be at least `1` characters long

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

The rename operation options including the new name and safety flags.
- No Additional Properties
<a id="headingCall_parameters_items_i1_new_name"></a>
<a id="Call_parameters_items_i1_new_name"></a>
##### new_name (required)

- Schema name: `New Name`
- Type: string

The new name for the dataset.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_recursive"></a>
<a id="Call_parameters_items_i1_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively rename snapshots.

<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

This operation does not check whether the dataset is currently in use. Renaming an active dataset may disrupt SMB shares, iSCSI targets, snapshots, replication, and other services. Set Force only if you understand and accept the risks.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful dataset rename.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
