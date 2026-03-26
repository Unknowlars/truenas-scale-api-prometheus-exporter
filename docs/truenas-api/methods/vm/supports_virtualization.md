---
title: vm.supports_virtualization
kind: method
source_rst: _sources/api_methods_vm.supports_virtualization.rst.txt
source_html: api_methods_vm.supports_virtualization.html
required_roles:
  - VM_READ
---

# vm.supports_virtualization

## Summary

Returns "true" if system supports virtualization, "false" otherwise

## Required Roles

- `VM_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Whether the host system supports hardware virtualization (VT-x/AMD-V).

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
