---
title: nfs.client_count
kind: method
source_rst: _sources/api_methods_nfs.client_count.rst.txt
source_html: api_methods_nfs.client_count.html
required_roles:
  - SHARING_NFS_READ
---

# nfs.client_count

## Summary

Return currently connected clients count. Count may not be accurate if NFSv3 protocol is in use due to potentially stale rmtab entries.

## Required Roles

- `SHARING_NFS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: integer

Current number of connected NFS clients.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
