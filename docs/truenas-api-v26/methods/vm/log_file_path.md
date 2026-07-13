---
title: vm.log_file_path
kind: method
source_rst: _sources/api_methods_vm.log_file_path.rst.txt
source_html: api_methods_vm.log_file_path.html
required_roles:
  - VM_READ
---

# vm.log_file_path

## Summary

Retrieve log file path of `id` VM.

It will return path of the log file if it exists and `null` otherwise.

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

ID of the virtual machine to get log file path for.

### Return value

- Schema name: `Result`

Path to the VM log file. `null` if no log file exists.
#### Any of

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
