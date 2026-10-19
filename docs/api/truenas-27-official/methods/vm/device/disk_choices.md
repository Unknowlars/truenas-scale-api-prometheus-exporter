---
title: vm.device.disk_choices
kind: method
source_rst: _sources/api_methods_vm.device.disk_choices.rst.txt
source_html: api_methods_vm.device.disk_choices.html
required_roles:
  - READONLY_ADMIN
  - VM_DEVICE_READ
---

# vm.device.disk_choices

## Summary

Returns disk choices for device type "DISK".

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

- Schema name: `VMDeviceDiskChoices`
- Type: object

Available disk devices and storage volumes for VM attachment.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
