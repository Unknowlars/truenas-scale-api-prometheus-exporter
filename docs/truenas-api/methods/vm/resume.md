---
title: vm.resume
kind: method
source_rst: _sources/api_methods_vm.resume.rst.txt
source_html: api_methods_vm.resume.html
required_roles:
  - VM_WRITE
---

# vm.resume

## Summary

Resume suspended `id` VM.

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

ID of the virtual machine to resume from suspended state.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful VM resume initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
