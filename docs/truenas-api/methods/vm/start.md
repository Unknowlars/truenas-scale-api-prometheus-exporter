---
title: vm.start
kind: method
source_rst: _sources/api_methods_vm.start.rst.txt
source_html: api_methods_vm.start.html
required_roles:
  - VM_WRITE
---

# vm.start

## Summary

Start a VM.

options.overcommit defaults to false, meaning VMs are not allowed to start if there is not enough available memory to hold all configured VMs. If true, VM starts even if there is not enough memory for all configured VMs.

Error codes:

ENOMEM(12): not enough free memory to run the VM without overcommit

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

ID of the virtual machine to start.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {"overcommit": false}

Options controlling the VM start process.
- No Additional Properties
##### overcommit

- Schema name: `Overcommit`
- Type: boolean
- Default: false

Whether to allow memory overcommitment when starting the VM.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful VM start initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
