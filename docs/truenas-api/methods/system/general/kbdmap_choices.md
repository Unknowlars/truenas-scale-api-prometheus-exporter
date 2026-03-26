---
title: system.general.kbdmap_choices
kind: method
source_rst: _sources/api_methods_system.general.kbdmap_choices.rst.txt
source_html: api_methods_system.general.kbdmap_choices.html
required_roles:
  - READONLY_ADMIN | SYSTEM_GENERAL_READ
---

# system.general.kbdmap_choices

## Summary

Returns keyboard map choices.

## Required Roles

- `READONLY_ADMIN | SYSTEM_GENERAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available keyboard layout codes and their descriptive names.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
