---
title: vm.device.iommu_enabled
kind: method
source_rst: _sources/api_methods_vm.device.iommu_enabled.rst.txt
source_html: api_methods_vm.device.iommu_enabled.html
required_roles:
  - VM_DEVICE_READ
---

# vm.device.iommu_enabled

## Summary

Returns "true" if iommu is enabled, "false" otherwise

## Required Roles

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

- Schema name: `Result`
- Type: boolean

Whether IOMMU (Input-Output Memory Management Unit) is enabled on the system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
