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

To destroy snapshots, use :doc:`zfs.resource.snapshot.destroy <api_methods_zfs.resource.snapshot.destroy>` instead.

Invalid input is returned to the client as a JSON-RPC `error` response (code `-32602`, *Invalid params*); each failing condition appears in the error's `data.extra` array with its own `errno`. A validation error is raised when:

- a snapshot path (containing `@`) is supplied (use :doc:`zfs.resource.snapshot.destroy <api_methods_zfs.resource.snapshot.destroy>`) - the resource does not exist (`ENOENT`) - the resource has children and `recursive` is `false` (`EBUSY`) - the resource has snapshots and `recursive` is `false` - the target is the pool's root filesystem - the path is absolute or ends with `/` - the path references a protected internal resource

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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Parameters.
- No Additional Properties
##### path (required)

- Schema name: `Path`
- Type: string

Path of the zfs resource (dataset or volume) to be destroyed. Snapshot paths (containing '@') are not accepted - use `zfs.resource.snapshot.destroy` instead.
- Must be at least `1` characters long

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Recursively destroy all descendants of the resource, including child datasets, snapshots, clones, and holds.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
