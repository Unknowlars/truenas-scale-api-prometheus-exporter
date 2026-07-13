---
title: interface.checkin
kind: method
source_rst: _sources/api_methods_interface.checkin.rst.txt
source_html: api_methods_interface.checkin.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.checkin

## Summary

If this method is called after interface changes have been committed and within the checkin timeout, then the task that automatically rolls back any interface changes is cancelled and the in-memory snapshot of database tables for the various interface tables will be cleared. The idea is that the end-user has verified the changes work as intended and need to be committed permanently.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: null

No return value for successful checkin operation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
