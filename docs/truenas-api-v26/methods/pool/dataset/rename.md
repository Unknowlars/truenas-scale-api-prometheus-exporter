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

Rename a ZFS resource (filesystem, snapshot, or zvolume) identified by `id`.

.. warning::

No safety checks are performed when renaming ZFS resources. If the resource is in use by services such as SMB, iSCSI, snapshot tasks, replication, or cloud sync, renaming may cause disruptions or service failures. Proceed only if you are certain the resource is not in use and fully understand the risks; set `force` to continue.

The `recursive` option is only valid for renaming snapshots. If `true`, and a snapshot is given, the snapshot is renamed recursively for all children -- for example, `dozer/a@now` and `dozer/a/b@now` are renamed to `dozer/a@new` and `dozer/a/b@new`. Renaming snapshots is likewise not recommended.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

The current dataset ID (full path) to rename.
- Must be at least `1` characters long

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

The rename operation options including the new name and safety flags.
- No Additional Properties
##### new_name (required)

- Schema name: `New Name`
- Type: string

The new name for the dataset.
- Must be at least `1` characters long

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively rename snapshots.

##### force

- Schema name: `Force`
- Type: boolean
- Default: false

This operation does not check whether the dataset is currently in use. Renaming an active dataset may disrupt SMB shares, iSCSI targets, snapshots, replication, and other services. Set Force only if you understand and accept the risks.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful dataset rename.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
