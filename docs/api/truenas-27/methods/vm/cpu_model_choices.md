---
title: vm.cpu_model_choices
kind: method
source_rst: _sources/api_methods_vm.cpu_model_choices.rst.txt
source_html: api_methods_vm.cpu_model_choices.html
required_roles:
  - READONLY_ADMIN
  - VM_READ
---

# vm.cpu_model_choices

## Summary

Retrieve CPU Model choices which can be used with a VM guest to emulate the CPU in the guest.

## Required Roles

- `READONLY_ADMIN`
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

- Schema name: `VMCpuModelChoicesResult`
- Type: object

VMCpuModelChoicesResult return fields.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
