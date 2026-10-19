---
title: zfs.resource.destroy
kind: method
source_rst: _sources/api_methods_zfs.resource.destroy.rst.txt
source_html: api_methods_zfs.resource.destroy.html
required_roles:
  - ZFS_RESOURCE_DELETE
---

# zfs.resource.destroy

## Summary

Destroy a ZFS resource (filesystem or volume).

This method provides an interface for destroying ZFS datasets and volumes with support for recursive deletion.

NOTE: To destroy snapshots, use `zfs.resource.snapshot.destroy`.

Args: data (dict): Dictionary containing destruction parameters: - path (str): Path of the ZFS resource to destroy. Must be in the form 'pool/name' or 'pool/zvol'. Snapshot paths (containing '@') are not accepted - use `zfs.resource.snapshot.destroy` instead. Cannot be an absolute path or end with a forward slash. - recursive (bool, optional): If True, recursively destroy all descendants including their snapshots, clones, and holds. Default: False.

Returns: None: On successful destruction.

Raises: ValidationError: Raised in the following cases: - Snapshot path provided (use zfs.resource.snapshot.destroy) - Resource does not exist (ENOENT) - Resource has children and recursive=False (EBUSY) - Resource has snapshots and recursive=False - Attempting to destroy root filesystem - Path is absolute (starts with /) - Path ends with forward slash - Path references protected internal resources

Examples: # Destroy a simple filesystem destroy({"path": "tank/temp"})

# Recursively destroy filesystem and all descendants destroy({"path": "tank/parent", "recursive": True})

Notes: - Root filesystem destruction is not allowed for safety - Protected system paths cannot be destroyed via API - Datasets with snapshots require recursive=True - To destroy snapshots, use `zfs.resource.snapshot.destroy`

## Required Roles

- `ZFS_RESOURCE_DELETE`

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

Parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Path of the zfs resource (dataset or volume) to be destroyed. Must be of the form 'pool/name'. It cannot be an absolute path or end with '/'. Snapshot paths (containing '@') are not accepted. One must use `zfs.resource.snapshot.destroy` instead.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_recursive"></a>
<a id="Call_parameters_items_i0_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Recursively destroy all descendants of the resource, including child datasets, snapshots, clones, and holds.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
