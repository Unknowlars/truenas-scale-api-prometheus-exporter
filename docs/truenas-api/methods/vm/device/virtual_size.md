---
title: vm.device.virtual_size
kind: method
source_rst: _sources/api_methods_vm.device.virtual_size.rst.txt
source_html: api_methods_vm.device.virtual_size.html
required_roles:
  - VM_DEVICE_READ
---

# vm.device.virtual_size

## Summary

Get the virtual size of a disk image using qemu-img info.

Args: file_path: Absolute path to the disk image file

Returns: Virtual size in bytes (int)

Raise: ValidationError if any failure occurs

## Required Roles

- `VM_DEVICE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vm_virtual_size

#### vm_virtual_size

- Schema name: `vm_virtual_size`
- Type: object

VMDeviceVirtualSizeArgs parameters.
- No Additional Properties
##### path (required)

- Schema name: `Path`
- Type: string

Absolute path to the disk image.

### Return value

- Schema name: `Result`
- Type: integer

The virtual size of the disk image in bytes.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
