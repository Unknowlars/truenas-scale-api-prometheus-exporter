---
title: failover.sync_to_peer
kind: method
source_rst: _sources/api_methods_failover.sync_to_peer.rst.txt
source_html: api_methods_failover.sync_to_peer.html
required_roles:
  - FAILOVER_WRITE
---

# failover.sync_to_peer

## Summary

Sync database and files to the other controller.

## Required Roles

- `FAILOVER_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`
- Type: object
- Default: {"reboot": false}

Options for syncing configuration to the peer node.
- No Additional Properties
##### reboot

- Schema name: `Reboot`
- Type: boolean
- Default: false

Reboot the other controller.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the sync to peer operation is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
