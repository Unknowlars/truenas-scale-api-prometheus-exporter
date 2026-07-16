---
title: vm.get_memory_usage
kind: method
source_rst: _sources/api_methods_vm.get_memory_usage.rst.txt
source_html: api_methods_vm.get_memory_usage.html
required_roles:
  - VM_READ
---

# vm.get_memory_usage

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

ID of the virtual machine to get memory usage for.

### Return value

- Schema name: `Result`
- Type: integer

Current memory usage of the virtual machine in bytes.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
