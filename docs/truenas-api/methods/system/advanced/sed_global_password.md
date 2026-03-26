---
title: system.advanced.sed_global_password
kind: method
source_rst: _sources/api_methods_system.advanced.sed_global_password.rst.txt
source_html: api_methods_system.advanced.sed_global_password.html
required_roles:
  - SYSTEM_ADVANCED_READ
---

# system.advanced.sed_global_password

## Summary

Returns configured global SED password in clear-text if one is configured, otherwise an empty string

## Required Roles

- `SYSTEM_ADVANCED_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: string

Current SED global password (masked for security).

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
