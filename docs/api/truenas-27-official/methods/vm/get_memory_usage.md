---
title: vm.get_memory_usage
kind: method
source_rst: _sources/api_methods_vm.get_memory_usage.rst.txt
source_html: api_methods_vm.get_memory_usage.html
required_roles:
  - VM_READ
---

# vm.get_memory_usage

## Summary

Get the memory usage of a given VM.

## Required Roles

- `VM_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the virtual machine to get memory usage for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: integer

Current memory usage of the virtual machine in bytes.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
