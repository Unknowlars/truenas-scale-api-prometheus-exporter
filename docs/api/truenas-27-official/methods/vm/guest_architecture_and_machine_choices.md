---
title: vm.guest_architecture_and_machine_choices
kind: method
source_rst: _sources/api_methods_vm.guest_architecture_and_machine_choices.rst.txt
source_html: api_methods_vm.guest_architecture_and_machine_choices.html
required_roles:
  - READONLY_ADMIN
  - VM_READ
---

# vm.guest_architecture_and_machine_choices

## Summary

Retrieve choices for supported guest architecture types and machine choices.

Keys in the response would be supported guest architecture(s) on the host and their respective values would be supported machine type(s) for the specific architecture on the host.

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

- Schema name: `VMGuestArchitectureAndMachineChoicesResult`
- Type: object

VMGuestArchitectureAndMachineChoicesResult return fields.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
