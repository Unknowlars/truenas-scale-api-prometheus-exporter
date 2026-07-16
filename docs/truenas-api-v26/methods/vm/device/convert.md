---
title: vm.device.convert
kind: method
source_rst: _sources/api_methods_vm.device.convert.rst.txt
source_html: api_methods_vm.device.convert.html
required_roles:
  - VM_DEVICE_WRITE
---

# vm.device.convert

## Summary

Convert between disk images and ZFS volumes. Supported disk image formats are qcow2, qed, raw, vdi, vhdx, and vmdk. The conversion direction is determined automatically based on file extension.

This method is a job.

## Required Roles

- `VM_DEVICE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vm_convert

#### vm_convert

- Schema name: `vm_convert`
- Type: object

VMDeviceConvertArgs parameters.
- No Additional Properties
##### source (required)

- Schema name: `Source`
- Type: string

Source path for the conversion (disk image file or ZFS volume).
- Must be at least `1` characters long

##### destination (required)

- Schema name: `Destination`
- Type: string

Destination path for the conversion (disk image file or ZFS volume).
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: boolean

Whether the conversion operation was successful.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
