---
title: virt.global.bridge_choices
kind: method
source_rst: _sources/api_methods_virt.global.bridge_choices.rst.txt
source_html: api_methods_virt.global.bridge_choices.html
required_roles:
  - READONLY_ADMIN | VIRT_GLOBAL_READ
---

# virt.global.bridge_choices

## Summary

Bridge choices for virtualization purposes.

Empty means it will be managed/created automatically.

## Required Roles

- `READONLY_ADMIN | VIRT_GLOBAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available network bridge interfaces and their configurations.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
