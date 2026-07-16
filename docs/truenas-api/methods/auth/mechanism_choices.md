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

Get list of available authentication mechanisms available for auth.login_ex

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of string

Array of available authentication mechanisms.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
