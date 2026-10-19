---
title: zfs.resource.snapshot.rename
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.rename.rst.txt
source_html: api_methods_zfs.resource.snapshot.rename.html
required_roles:
  - SNAPSHOT_WRITE
---

# zfs.resource.snapshot.rename

## Summary

Rename a ZFS snapshot.

Args: data: Rename parameters containing: - current_name: Current snapshot path (e.g., 'pool/dataset@old_name'). - new_name: New snapshot path (e.g., 'pool/dataset@new_name'). - recursive: Recursively rename matching snapshots in child datasets.

Returns: None on success.

Raises: ValidationError: If snapshot not found, new name already exists, or invalid paths.

Examples: # Rename a single snapshot rename({"current_name": "tank/data@old", "new_name": "tank/data@new"})

# Rename recursively (all matching child snapshots) rename({ "current_name": "tank@old", "new_name": "tank@new", "recursive": True })

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

Rename parameters for renaming ZFS snapshots.
- No Additional Properties
<a id="headingCall_parameters_items_i0_current_name"></a>
<a id="Call_parameters_items_i0_current_name"></a>
##### current_name (required)

- Schema name: `Current Name`
- Type: string

Current snapshot path (e.g., 'pool/dataset@old_name').
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_new_name"></a>
<a id="Call_parameters_items_i0_new_name"></a>
##### new_name (required)

- Schema name: `New Name`
- Type: string

New snapshot path (e.g., 'pool/dataset@new_name').
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_recursive"></a>
<a id="Call_parameters_items_i0_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Recursively rename matching snapshots in child datasets.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
