---
title: system.boot_id
kind: method
source_rst: _sources/api_methods_system.boot_id.rst.txt
source_html: api_methods_system.boot_id.html
required_roles:
  []
---

# system.boot_id

## Summary

Returns a unique boot identifier.

It is supposed to be unique every system boot.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: string

Unique identifier for the current system boot session.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
