---
title: system.state
kind: method
source_rst: _sources/api_methods_system.state.rst.txt
source_html: api_methods_system.state.html
required_roles:
  - SYSTEM_GENERAL_READ
---

# system.state

## Summary

Returns the current system state.

## Required Roles

- `SYSTEM_GENERAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: enum (of string)

Current system state indicating boot status or shutdown process.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
