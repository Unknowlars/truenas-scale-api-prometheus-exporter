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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the virtual machine to clone.

#### Parameter 2: name

#### name

- Schema name: `name`
- Default: null

Name for the cloned virtual machine. `null` to auto-generate.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: boolean

Whether the virtual machine was successfully cloned.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
