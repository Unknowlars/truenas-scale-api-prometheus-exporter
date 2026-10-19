---
title: auth.mechanism_choices
kind: method
source_rst: _sources/api_methods_auth.mechanism_choices.rst.txt
source_html: api_methods_auth.mechanism_choices.html
required_roles:
  - READONLY_ADMIN
---

# auth.mechanism_choices

## Summary

Get the list of authentication mechanisms available for [auth.login_ex](login_ex.md).

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
- Type: array of string

Array of available authentication mechanisms.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
