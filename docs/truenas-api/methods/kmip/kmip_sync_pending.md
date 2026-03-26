---
title: kmip.kmip_sync_pending
kind: method
source_rst: _sources/api_methods_kmip.kmip_sync_pending.rst.txt
source_html: api_methods_kmip.kmip_sync_pending.html
required_roles:
  - KMIP_READ
---

# kmip.kmip_sync_pending

## Summary

Returns true or false based on if there are keys which are to be synced from local database to remote KMIP server or vice versa.

## Required Roles

- `KMIP_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if there are keys pending synchronization with the KMIP server.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
