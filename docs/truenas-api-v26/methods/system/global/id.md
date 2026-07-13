---
title: system.global.id
kind: method
source_rst: _sources/api_methods_system.global.id.rst.txt
source_html: api_methods_system.global.id.html
required_roles:
  - READONLY_ADMIN
---

# system.global.id

## Summary

Retrieve a 128 bit hexadecimal UUID value unique for each TrueNAS system.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: string

Unique system identifier.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
