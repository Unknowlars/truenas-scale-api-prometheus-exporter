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

Destroy a ZFS resource (filesystem or volume), optionally recursing into its descendants.

To destroy snapshots, use [zfs.resource.snapshot.destroy](snapshot/destroy.md) instead.

.. warning::

The shares, tasks, iSCSI extents, NVMe-oF namespaces, VM devices and apps that use the resource or any of its descendants are deleted before it is destroyed, once the request has passed validation.

A validation error is raised when:

- a snapshot path (containing `@`) is supplied (use [zfs.resource.snapshot.destroy](snapshot/destroy.md)) - the resource does not exist (`ENOENT`) - the resource has children and `recursive` is `false` (`EBUSY`) - the resource has snapshots and `recursive` is `false` - the target is the pool's root filesystem - the path is absolute or ends with `/` - the path references a protected internal resource

Examples:

Destroy a single filesystem:

.. code:: json

{"path": "tank/temp"}

Recursively destroy a filesystem and all of its descendants:

.. code:: json

{"path": "tank/parent", "recursive": true}

.. note::

- Root filesystem destruction is not allowed for safety

- Protected system paths cannot be destroyed via API

- Datasets with snapshots require `recursive` to be `true`

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

Path of the zfs resource (dataset or volume) to be destroyed. Snapshot paths (containing '@') are not accepted - use `zfs.resource.snapshot.destroy` instead.
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
