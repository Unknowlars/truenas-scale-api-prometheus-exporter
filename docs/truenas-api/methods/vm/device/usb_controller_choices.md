---
title: vm.device.usb_controller_choices
kind: method
source_rst: _sources/api_methods_vm.device.usb_controller_choices.rst.txt
source_html: api_methods_vm.device.usb_controller_choices.html
required_roles:
  - READONLY_ADMIN | VM_DEVICE_READ
---

# vm.device.usb_controller_choices

## Summary

Retrieve USB controller type choices

## Required Roles

- `READONLY_ADMIN | VM_DEVICE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `VMDeviceUsbControllerChoicesResult`
- Type: object

VMDeviceUsbControllerChoicesResult return fields.
#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
