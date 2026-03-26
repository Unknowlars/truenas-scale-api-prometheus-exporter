---
title: system.general.ui_address_choices
kind: method
source_rst: _sources/api_methods_system.general.ui_address_choices.rst.txt
source_html: api_methods_system.general.ui_address_choices.html
required_roles:
  - READONLY_ADMIN | SYSTEM_GENERAL_READ
---

# system.general.ui_address_choices

## Summary

Returns network interfaces that have statically configured IPv4 address(es). These addresses can be used to bind the UI server.

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

Object of available IPv4 addresses and their interface names for UI binding.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
