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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vm_convert

<a id="Call_parameters_items_i0"></a>
#### vm_convert

- Schema name: `vm_convert`
- Type: object

VMDeviceConvertArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_source"></a>
<a id="Call_parameters_items_i0_source"></a>
##### source (required)

- Schema name: `Source`
- Type: string

Source path for the conversion (disk image file or ZFS volume).
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_destination"></a>
<a id="Call_parameters_items_i0_destination"></a>
##### destination (required)

- Schema name: `Destination`
- Type: string

Destination path for the conversion (disk image file or ZFS volume).
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Whether the conversion operation was successful.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
