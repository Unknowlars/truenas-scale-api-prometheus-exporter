---
title: vm.suspend
kind: method
source_rst: _sources/api_methods_vm.suspend.rst.txt
source_html: api_methods_vm.suspend.html
required_roles:
  - VM_WRITE
---

# vm.suspend

## Summary

Suspend `id` VM.

## Required Roles

- `VM_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the virtual machine to suspend.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful VM suspend initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
