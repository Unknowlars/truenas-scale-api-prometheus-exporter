---
title: user.get_next_uid
kind: method
source_rst: _sources/api_methods_user.get_next_uid.rst.txt
source_html: api_methods_user.get_next_uid.html
required_roles:
  - ACCOUNT_READ
---

# user.get_next_uid

## Summary

Get the next available/free uid.

## Required Roles

- `ACCOUNT_READ`

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
- Type: integer

Next available UID for creating a new local user account.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
