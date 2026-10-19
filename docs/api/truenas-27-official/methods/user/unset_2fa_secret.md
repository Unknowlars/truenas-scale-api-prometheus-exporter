---
title: user.unset_2fa_secret
kind: method
source_rst: _sources/api_methods_user.unset_2fa_secret.rst.txt
source_html: api_methods_user.unset_2fa_secret.html
required_roles:
  - ACCOUNT_WRITE
---

# user.unset_2fa_secret

## Summary

Unset two-factor authentication secret for `username`.

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

#### Parameter 1: username

<a id="Call_parameters_items_i0"></a>
#### username

- Schema name: `username`
- Type: string

Username to disable two-factor authentication for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful two-factor authentication removal.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
