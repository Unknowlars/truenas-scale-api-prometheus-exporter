---
title: system.security.info.fips_enabled
kind: method
source_rst: _sources/api_methods_system.security.info.fips_enabled.rst.txt
source_html: api_methods_system.security.info.fips_enabled.html
required_roles:
  - SYSTEM_SECURITY_READ
---

# system.security.info.fips_enabled

## Summary

Returns a boolean identifying whether FIPS mode has been enabled on this system

## Required Roles

- `SYSTEM_SECURITY_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Whether FIPS mode is currently enabled on this system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
