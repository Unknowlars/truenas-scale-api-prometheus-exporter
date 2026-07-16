---
title: sharing.smb.delete
kind: method
source_rst: _sources/api_methods_sharing.smb.delete.rst.txt
source_html: api_methods_sharing.smb.delete.html
required_roles:
  - SHARING_SMB_WRITE
---

# sharing.smb.delete

## Summary

Delete SMB Share of `id`. This will forcibly disconnect SMB clients that are accessing the share.

## Required Roles

- `SHARING_SMB_WRITE`

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

ID of the SMB share to delete.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the SMB share is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
