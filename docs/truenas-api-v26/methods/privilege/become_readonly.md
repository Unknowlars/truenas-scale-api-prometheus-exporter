---
title: privilege.become_readonly
kind: method
source_rst: _sources/api_methods_privilege.become_readonly.rst.txt
source_html: api_methods_privilege.become_readonly.html
required_roles:
  - READONLY_ADMIN
---

# privilege.become_readonly

## Summary

Reduce the privileges of the current user credentials to `READONLY_ADMINS`. This action prevents the session from making configuration changes. It also redacts sensitive data in API output.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
