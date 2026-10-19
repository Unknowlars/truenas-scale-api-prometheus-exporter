---
title: vm.bootloader_options
kind: method
source_rst: _sources/api_methods_vm.bootloader_options.rst.txt
source_html: api_methods_vm.bootloader_options.html
required_roles:
  - VM_READ
---

# vm.bootloader_options

## Summary

Supported motherboard firmware options.

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

- Schema name: `VMBootloaderOptionsResult`
- Type: object

VMBootloaderOptionsResult return fields.
- No Additional Properties
<a id="headingReturn_value_UEFI"></a>
<a id="Return_value_UEFI"></a>
#### UEFI

- Schema name: `Uefi`
- Type: const
- Default: "UEFI"

Modern UEFI firmware with secure boot support.
- Specific value: `"UEFI"`

<a id="headingReturn_value_UEFI_CSM"></a>
<a id="Return_value_UEFI_CSM"></a>
#### UEFI_CSM

- Schema name: `Uefi Csm`
- Type: const
- Default: "Legacy BIOS"

UEFI with Compatibility Support Module for legacy BIOS compatibility.
- Specific value: `"Legacy BIOS"`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
