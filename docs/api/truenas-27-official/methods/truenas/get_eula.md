---
title: truenas.get_eula
kind: method
source_rst: _sources/api_methods_truenas.get_eula.rst.txt
source_html: api_methods_truenas.get_eula.html
required_roles:
  - READONLY_ADMIN
---

# truenas.get_eula

## Summary

Returns the TrueNAS End-User License Agreement (EULA).

## Required Roles

- `READONLY_ADMIN`

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

Full text of the End User License Agreement. `null` if no EULA is required.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
