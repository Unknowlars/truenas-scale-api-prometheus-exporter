---
title: iscsi.target.delete
kind: method
source_rst: _sources/api_methods_iscsi.target.delete.rst.txt
source_html: api_methods_iscsi.target.delete.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# iscsi.target.delete

## Summary

Delete iSCSI Target of `id`.

Deleting an iSCSI Target makes sure we delete all Associated Targets which use `id` iSCSI Target.

## Required Roles

- `SHARING_ISCSI_TARGET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the iSCSI target to delete.

#### Parameter 2: force

#### force

- Schema name: `force`
- Type: boolean
- Default: false

Whether to force deletion even if the target is in use.

#### Parameter 3: delete_extents

#### delete_extents

- Schema name: `delete_extents`
- Type: boolean
- Default: false

Whether to also delete associated extents.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the iSCSI target is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
