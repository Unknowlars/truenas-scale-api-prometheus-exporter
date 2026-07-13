---
title: user.has_local_administrator_set_up
kind: method
source_rst: _sources/api_methods_user.has_local_administrator_set_up.rst.txt
source_html: api_methods_user.has_local_administrator_set_up.html
required_roles:
  []
---

# user.has_local_administrator_set_up

## Summary

Return whether a local administrator with a valid password exists.

This is used when the system is installed without a password and must be set on first use/login.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Whether a local administrator account has been configured on this system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
