---
title: support.is_available
kind: method
source_rst: _sources/api_methods_support.is_available.rst.txt
source_html: api_methods_support.is_available.html
required_roles:
  - SUPPORT_READ
---

# support.is_available

## Summary

Returns whether Proactive Support is available for the current license.

## Required Roles

- `SUPPORT_READ`

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
- Type: boolean

Whether support functionality is available on this system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
