---
title: interface.rollback
kind: method
source_rst: _sources/api_methods_interface.rollback.rst.txt
source_html: api_methods_interface.rollback.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.rollback

## Summary

Rollback pending interfaces changes.

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
- Type: null

No return value for successful rollback operation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
