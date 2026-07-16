---
title: system.advanced.nvidia_present
kind: method
source_rst: _sources/api_methods_system.advanced.nvidia_present.rst.txt
source_html: api_methods_system.advanced.nvidia_present.html
required_roles:
  - SYSTEM_ADVANCED_READ
---

# system.advanced.nvidia_present

## Summary

Returns whether a non-isolated NVIDIA GPU is present in the system.

## Required Roles

- `SYSTEM_ADVANCED_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Whether a non-isolated NVIDIA GPU is present in the system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
