---
title: interface.has_pending_changes
kind: method
source_rst: _sources/api_methods_interface.has_pending_changes.rst.txt
source_html: api_methods_interface.has_pending_changes.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.has_pending_changes

## Summary

Return whether there are pending interfaces changes to be applied or not.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Whether there are pending interface changes that need to be committed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
