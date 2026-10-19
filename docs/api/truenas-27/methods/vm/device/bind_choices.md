---
title: vm.device.bind_choices
kind: method
source_rst: _sources/api_methods_vm.device.bind_choices.rst.txt
source_html: api_methods_vm.device.bind_choices.html
required_roles:
  - READONLY_ADMIN
  - VM_DEVICE_READ
---

# vm.device.bind_choices

## Summary

Available choices for Bind attribute.

## Required Roles

- `READONLY_ADMIN`
- `VM_DEVICE_READ`

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

- Schema name: `VMDeviceBindChoicesResult`
- Type: object

VMDeviceBindChoicesResult return fields.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
