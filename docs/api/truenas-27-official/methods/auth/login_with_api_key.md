---
title: auth.login_with_api_key
kind: method
source_rst: _sources/api_methods_auth.login_with_api_key.rst.txt
source_html: api_methods_auth.login_with_api_key.html
required_roles:
  []
---

# auth.login_with_api_key

## Summary

Authenticate session using API Key.

Deprecated and removed in v27. Use [auth.login_ex](login_ex.md) with `mechanism="API_KEY_PLAIN"` (or `mechanism="SCRAM"` for SCRAM-based authentication).

*DEPRECATED: this method is scheduled to be removed in v27.*

## Required Roles

- None documented.

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: api_key

<a id="Call_parameters_items_i0"></a>
#### api_key

- Schema name: `api_key`
- Type: string

API key for authentication (masked for security).

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if API key login was successful, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
