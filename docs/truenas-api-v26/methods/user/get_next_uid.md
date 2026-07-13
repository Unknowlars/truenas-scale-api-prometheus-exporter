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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: integer

Next available UID for creating a new local user account.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
