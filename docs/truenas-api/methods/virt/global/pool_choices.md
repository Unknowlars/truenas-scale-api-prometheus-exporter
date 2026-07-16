---
title: virt.global.pool_choices
kind: method
source_rst: _sources/api_methods_virt.global.pool_choices.rst.txt
source_html: api_methods_virt.global.pool_choices.html
required_roles:
  - READONLY_ADMIN | VIRT_GLOBAL_READ
---

# virt.global.pool_choices

## Summary

Pool choices for virtualization purposes.

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

Object of available ZFS pools that can be used for virtualization storage.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
