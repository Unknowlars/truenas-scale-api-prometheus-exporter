---
title: pool.snapshot.rename
kind: method
source_rst: _sources/api_methods_pool.snapshot.rename.rst.txt
source_html: api_methods_pool.snapshot.rename.html
required_roles:
  - SNAPSHOT_WRITE
---

# pool.snapshot.rename

## Summary

Rename a snapshot `id` to `new_name`.

No safety checks are performed when renaming ZFS resources. If the dataset is in use by services such as SMB, iSCSI, snapshot tasks, replication, or cloud sync, renaming may cause disruptions or service failures.

Proceed only if you are certain the ZFS resource is not in use and fully understand the risks. Set Force to continue.

## Required Roles

- `SNAPSHOT_WRITE`

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

Current ID of the snapshot to rename.
- Must be at least `1` characters long

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

The rename operation options including the new name and force flag.
- No Additional Properties
##### new_name (required)

- Schema name: `New Name`
- Type: string

The new name for the snapshot.
- Must be at least `1` characters long

##### force

- Schema name: `Force`
- Type: boolean
- Default: false

This operation does not check whether the dataset is currently in use. Renaming an active dataset may disrupt SMB shares, iSCSI targets, snapshots, replication, and other services. Set Force only if you understand and accept the risks.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful snapshot rename.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
