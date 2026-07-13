---
title: failover.sync_from_peer
kind: method
source_rst: _sources/api_methods_failover.sync_from_peer.rst.txt
source_html: api_methods_failover.sync_from_peer.html
required_roles:
  - FAILOVER_WRITE
---

# failover.sync_from_peer

## Summary

Sync database and files from the other controller.

## Required Roles

- `FAILOVER_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the sync from peer operation is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
