---
title: vm.resolution_choices
kind: method
source_rst: _sources/api_methods_vm.resolution_choices.rst.txt
source_html: api_methods_vm.resolution_choices.html
required_roles:
  - READONLY_ADMIN | VM_READ
---

# vm.resolution_choices

## Summary

Retrieve supported resolution choices for VM Display devices.

## Required Roles

- `READONLY_ADMIN | VM_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available display resolutions for virtual machines.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
