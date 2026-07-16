---
title: vm.get_vmemory_in_use
kind: method
source_rst: _sources/api_methods_vm.get_vmemory_in_use.rst.txt
source_html: api_methods_vm.get_vmemory_in_use.html
required_roles:
  - VM_READ
---

# vm.get_vmemory_in_use

## Summary

The total amount of virtual memory in MB used by guests

Returns a dict with the following information: RNP - Running but not provisioned PRD - Provisioned but not running RPRD - Running and provisioned

## Required Roles

- `VM_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `VMGetVmemoryInUseResult`
- Type: object

VMGetVmemoryInUseResult return fields.
- No Additional Properties
#### RNP (required)

- Schema name: `Rnp`
- Type: integer

Running but not provisioned

#### PRD (required)

- Schema name: `Prd`
- Type: integer

Provisioned but not running

#### RPRD (required)

- Schema name: `Rprd`
- Type: integer

Running and provisioned

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
