---
title: vm.delete
kind: method
source_rst: _sources/api_methods_vm.delete.rst.txt
source_html: api_methods_vm.delete.html
required_roles:
  - VM_WRITE
---

# vm.delete

## Summary

Delete a VM.

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

ID of the virtual machine to delete.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {"zvols": false, "force": false}

Options controlling the VM deletion process.
- No Additional Properties
<a id="headingCall_parameters_items_i1_zvols"></a>
<a id="Call_parameters_items_i1_zvols"></a>
##### zvols

- Schema name: `Zvols`
- Type: boolean
- Default: false

Delete associated ZFS volumes when deleting the VM.

<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force deletion even if the VM is currently running.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
