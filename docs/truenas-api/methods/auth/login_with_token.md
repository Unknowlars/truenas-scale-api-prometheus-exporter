---
title: auth.login_with_token
kind: method
source_rst: _sources/api_methods_auth.login_with_token.rst.txt
source_html: api_methods_auth.login_with_token.html
required_roles:
  []
---

# auth.login_with_token

## Summary

Authenticate session using token generated with `auth.generate_token`.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: token

#### token

- Schema name: `token`
- Type: string

Authentication token (masked for security).

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if token login was successful, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
