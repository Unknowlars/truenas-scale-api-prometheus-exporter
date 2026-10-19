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

ID of the virtual machine to suspend.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful VM suspend initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
