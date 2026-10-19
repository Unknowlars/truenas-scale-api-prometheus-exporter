---
title: system.advanced.sed_global_password_is_set
kind: method
source_rst: _sources/api_methods_system.advanced.sed_global_password_is_set.rst.txt
source_html: api_methods_system.advanced.sed_global_password_is_set.html
required_roles:
  - SYSTEM_ADVANCED_READ
---

# system.advanced.sed_global_password_is_set

## Summary

Returns a boolean identifying whether or not a global SED password has been set

## Required Roles

- `SYSTEM_ADVANCED_READ`

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

Whether a SED global password has been configured.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
