---
title: interface.websocket_local_ip
kind: method
source_rst: _sources/api_methods_interface.websocket_local_ip.rst.txt
source_html: api_methods_interface.websocket_local_ip.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# interface.websocket_local_ip

## Summary

Returns the local ip address for this websocket session.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`

The local IP address for the current websocket session or `null`.
#### Any of

##### Option 1

- Type: const

##### Option 2

- Type: string

##### Option 3

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
