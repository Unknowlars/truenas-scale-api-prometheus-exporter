---
title: iscsi.portal.delete
kind: method
source_rst: _sources/api_methods_iscsi.portal.delete.rst.txt
source_html: api_methods_iscsi.portal.delete.html
required_roles:
  - SHARING_ISCSI_PORTAL_WRITE
---

# iscsi.portal.delete

## Summary

Delete iSCSI Portal `id`.

## Required Roles

- `SHARING_ISCSI_PORTAL_WRITE`

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

ID of the iSCSI portal to delete.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the iSCSI portal is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
