---
title: zfs.resource.snapshot.rollback
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.rollback.rst.txt
source_html: api_methods_zfs.resource.snapshot.rollback.html
required_roles:
  - SNAPSHOT_WRITE
---

# zfs.resource.snapshot.rollback

## Summary

Rollback a ZFS dataset to a snapshot.

WARNING: This is a destructive change. All data written since the target snapshot was taken will be discarded.

Args: data: Rollback parameters containing: - path: Snapshot path to rollback to (e.g., 'pool/dataset@snapshot'). - recursive: Destroy any snapshots and bookmarks more recent than the one specified. - recursive_clones: Like recursive, but also destroy any clones. - force: Force unmount of any clones. - recursive_rollback: Do a complete recursive rollback of each child snapshot.

Returns: None on success.

Raises: ValidationError: If snapshot not found or rollback fails.

Examples: # Basic rollback rollback({"path": "tank/data@backup"})

# Rollback destroying more recent snapshots rollback({"path": "tank/data@backup", "recursive": True})

# Rollback all child datasets rollback({"path": "tank@backup", "recursive_rollback": True})

## Required Roles

- `SNAPSHOT_WRITE`

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

Rollback parameters for rolling back to ZFS snapshots.
- No Additional Properties
<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Snapshot path to rollback to (e.g., 'pool/dataset@snapshot').
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_recursive"></a>
<a id="Call_parameters_items_i0_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Destroy any snapshots and bookmarks more recent than the one specified.

<a id="headingCall_parameters_items_i0_recursive_clones"></a>
<a id="Call_parameters_items_i0_recursive_clones"></a>
##### recursive_clones

- Schema name: `Recursive Clones`
- Type: boolean
- Default: false

Like recursive, but also destroy any clones.

<a id="headingCall_parameters_items_i0_force"></a>
<a id="Call_parameters_items_i0_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force unmount of any clones.

<a id="headingCall_parameters_items_i0_recursive_rollback"></a>
<a id="Call_parameters_items_i0_recursive_rollback"></a>
##### recursive_rollback

- Schema name: `Recursive Rollback`
- Type: boolean
- Default: false

Do a complete recursive rollback of each child snapshot. Fails if any child lacks the snapshot.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
