---
title: vm.get_console
kind: method
source_rst: _sources/api_methods_vm.get_console.rst.txt
source_html: api_methods_vm.get_console.html
required_roles:
  - VM_READ
---

# vm.get_console

## Summary

Get the console device from a given guest.

## Required Roles

- `VM_READ`

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

ID of the virtual machine to get console connection information for.

### Return value

- Schema name: `Result`
- Type: string

Console connection string or command for accessing the VM console.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
