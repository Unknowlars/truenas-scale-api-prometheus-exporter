---
title: truenas.is_eula_accepted
kind: method
source_rst: _sources/api_methods_truenas.is_eula_accepted.rst.txt
source_html: api_methods_truenas.is_eula_accepted.html
required_roles:
  - READONLY_ADMIN
---

# truenas.is_eula_accepted

## Summary

Returns whether the EULA is accepted or not.

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
- Type: boolean

Whether the End User License Agreement has been formally accepted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
