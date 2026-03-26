---
title: interface.checkin_waiting
kind: method
source_rst: _sources/api_methods_interface.checkin_waiting.rst.txt
source_html: api_methods_interface.checkin_waiting.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.checkin_waiting

## Summary

Returns whether we are waiting for the user to check in the applied network changes before they are rolled back.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`

Number of seconds left to wait or `null` if not waiting.
#### Any of

##### Option 1

- Type: integer

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
