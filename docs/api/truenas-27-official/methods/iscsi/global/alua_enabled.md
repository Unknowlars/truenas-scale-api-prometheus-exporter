---
title: iscsi.global.alua_enabled
kind: method
source_rst: _sources/api_methods_iscsi.global.alua_enabled.rst.txt
source_html: api_methods_iscsi.global.alua_enabled.html
required_roles:
  - SHARING_ISCSI_GLOBAL_READ
---

# iscsi.global.alua_enabled

## Summary

Returns whether iSCSI ALUA is enabled or not.

## Required Roles

- `SHARING_ISCSI_GLOBAL_READ`

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

Returns `true` if ALUA is enabled, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
