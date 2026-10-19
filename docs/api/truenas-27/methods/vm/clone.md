---
title: vm.clone
kind: method
source_rst: _sources/api_methods_vm.clone.rst.txt
source_html: api_methods_vm.clone.html
required_roles:
  - VM_WRITE
---

# vm.clone

## Summary

Clone the VM `id`.

`name` is an optional parameter for the cloned VM. If not provided it will append the next number available to the VM name.

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

ID of the virtual machine to clone.

#### Parameter 2: name

<a id="Call_parameters_items_i1"></a>
#### name

- Schema name: `name`
- Default: null

Name for the cloned virtual machine. `null` to auto-generate.
<a id="Call_parameters_items_i1_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Whether the virtual machine was successfully cloned.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
