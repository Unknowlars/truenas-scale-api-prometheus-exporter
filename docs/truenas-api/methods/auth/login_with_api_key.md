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

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: api_key

#### api_key

- Schema name: `api_key`
- Type: string

API key for authentication (masked for security).

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if API key login was successful, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
