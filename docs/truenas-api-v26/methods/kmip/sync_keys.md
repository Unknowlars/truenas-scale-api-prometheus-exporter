---
title: kmip.sync_keys
kind: method
source_rst: _sources/api_methods_kmip.sync_keys.rst.txt
source_html: api_methods_kmip.sync_keys.html
required_roles:
  - KMIP_WRITE
---

# kmip.sync_keys

## Summary

Sync ZFS/SED keys between KMIP Server and TN database.

## Required Roles

- `KMIP_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when key synchronization with the KMIP server completes.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
