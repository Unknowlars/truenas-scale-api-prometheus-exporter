---
title: interface.websocket_interface
kind: method
source_rst: _sources/api_methods_interface.websocket_interface.rst.txt
source_html: api_methods_interface.websocket_interface.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# interface.websocket_interface

## Summary

Returns the interface this websocket is connected to.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

The interface used for the current websocket connection or `null` if not available.
#### Any of

##### Option 1

- Type: object

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
