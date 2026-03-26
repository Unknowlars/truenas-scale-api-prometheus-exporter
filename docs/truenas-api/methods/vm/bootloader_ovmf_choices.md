---
title: vm.bootloader_ovmf_choices
kind: method
source_rst: _sources/api_methods_vm.bootloader_ovmf_choices.rst.txt
source_html: api_methods_vm.bootloader_ovmf_choices.html
required_roles:
  - READONLY_ADMIN | VM_READ
---

# vm.bootloader_ovmf_choices

## Summary

Retrieve bootloader ovmf choices

## Required Roles

- `READONLY_ADMIN | VM_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `VMBootloaderOvmfChoicesResult`
- Type: object

VMBootloaderOvmfChoicesResult return fields.
#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
