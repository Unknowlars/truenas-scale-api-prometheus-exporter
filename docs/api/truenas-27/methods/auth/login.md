---
title: auth.login
kind: method
source_rst: _sources/api_methods_auth.login.rst.txt
source_html: api_methods_auth.login.html
required_roles:
  []
---

# auth.login

## Summary

Authenticate session using username and password. `otp_token` must be specified if two factor authentication is enabled.

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

#### Parameter 1: username

<a id="Call_parameters_items_i0"></a>
#### username

- Schema name: `username`
- Type: string

Username for authentication.

#### Parameter 2: password

<a id="Call_parameters_items_i1"></a>
#### password

- Schema name: `password`
- Type: string

Password for authentication.

#### Parameter 3: otp_token

<a id="Call_parameters_items_i2"></a>
#### otp_token

- Schema name: `otp_token`
- Default: null

One-time password token for two-factor authentication or `null`.
<a id="Call_parameters_items_i2_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i2_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i2_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i2_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i2_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if login was successful, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
