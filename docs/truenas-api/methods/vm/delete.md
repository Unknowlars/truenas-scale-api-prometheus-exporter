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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the virtual machine to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {"zvols": false, "force": false}

Options controlling the VM deletion process.
- No Additional Properties
##### zvols

- Schema name: `Zvols`
- Type: boolean
- Default: false

Delete associated ZFS volumes when deleting the VM.

##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force deletion even if the VM is currently running.

### Return value

- Schema name: `Result`
- Type: boolean

Whether the virtual machine was successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
