---
title: sharing.nfs.delete
kind: method
source_rst: _sources/api_methods_sharing.nfs.delete.rst.txt
source_html: api_methods_sharing.nfs.delete.html
required_roles:
  - SHARING_NFS_WRITE
---

# sharing.nfs.delete

## Summary

Delete NFS Share of `id`.

## Required Roles

- `SHARING_NFS_WRITE`

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

ID of the NFS share to delete.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the NFS share is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
