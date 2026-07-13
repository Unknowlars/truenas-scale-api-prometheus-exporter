---
title: vm.device.disk_choices
kind: method
source_rst: _sources/api_methods_vm.device.disk_choices.rst.txt
source_html: api_methods_vm.device.disk_choices.html
required_roles:
  - READONLY_ADMIN | VM_DEVICE_READ
---

# vm.device.disk_choices

## Summary

Returns disk choices for device type "DISK".

## Required Roles

- `READONLY_ADMIN | VM_DEVICE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `VMDeviceDiskChoices`
- Type: object

Available disk devices and storage volumes for VM attachment.
#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
