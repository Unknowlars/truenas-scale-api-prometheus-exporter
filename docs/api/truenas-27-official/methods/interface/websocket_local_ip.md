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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

The local IP address for the current websocket session or `null`.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
