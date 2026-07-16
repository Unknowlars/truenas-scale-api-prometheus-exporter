---
title: auth.logout
kind: method
source_rst: _sources/api_methods_auth.logout.rst.txt
source_html: api_methods_auth.logout.html
required_roles:
  []
---

# auth.logout

## Summary

Deauthenticates an app and if a token exists, removes that from the session.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when logout is successful.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
