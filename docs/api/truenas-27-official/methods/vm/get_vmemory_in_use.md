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

Return the total amount of virtual memory, in bytes, used by guests.

## Required Roles

- `VM_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `VMGetVmemoryInUseResult`
- Type: object

VMGetVmemoryInUseResult return fields.
- No Additional Properties
<a id="headingReturn_value_RNP"></a>
<a id="Return_value_RNP"></a>
#### RNP (required)

- Schema name: `Rnp`
- Type: integer

Running but not provisioned, in bytes

<a id="headingReturn_value_PRD"></a>
<a id="Return_value_PRD"></a>
#### PRD (required)

- Schema name: `Prd`
- Type: integer

Provisioned but not running, in bytes

<a id="headingReturn_value_RPRD"></a>
<a id="Return_value_RPRD"></a>
#### RPRD (required)

- Schema name: `Rprd`
- Type: integer

Running and provisioned, in bytes

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
