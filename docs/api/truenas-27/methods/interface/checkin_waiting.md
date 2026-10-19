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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

Number of seconds left to wait or `null` if not waiting.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
