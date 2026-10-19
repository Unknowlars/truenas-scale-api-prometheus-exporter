---
title: auth.generate_onetime_password
kind: method
source_rst: _sources/api_methods_auth.generate_onetime_password.rst.txt
source_html: api_methods_auth.generate_onetime_password.html
required_roles:
  - ACCOUNT_WRITE
---

# auth.generate_onetime_password

## Summary

Generate a password for the specified username that may be used only a single time to authenticate to TrueNAS. This may be used by server administrators to allow users authenticate and then set a proper password and two-factor authentication token.

## Required Roles

- `ACCOUNT_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: generate_single_use_password

<a id="Call_parameters_items_i0"></a>
#### generate_single_use_password

- Schema name: `generate_single_use_password`
- Type: object

AuthGenerateOnetimePasswordArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_username"></a>
<a id="Call_parameters_items_i0_username"></a>
##### username (required)

- Schema name: `Username`
- Type: string

Username to generate a one-time password for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: string

Generated one-time password for the specified user.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
