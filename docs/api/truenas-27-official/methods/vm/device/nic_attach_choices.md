---
title: vm.device.nic_attach_choices
kind: method
source_rst: _sources/api_methods_vm.device.nic_attach_choices.rst.txt
source_html: api_methods_vm.device.nic_attach_choices.html
required_roles:
  - READONLY_ADMIN
  - VM_DEVICE_READ
---

# vm.device.nic_attach_choices

## Summary

Available choices for NIC Attach attribute.

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

- Schema name: `VMDeviceNicAttachChoicesResult`
- Type: object

VMDeviceNicAttachChoicesResult return fields.
- No Additional Properties
<a id="headingReturn_value_BRIDGE"></a>
<a id="Return_value_BRIDGE"></a>
#### BRIDGE (required)

- Schema name: `Bridge`
- Type: array of string

Available bridge interfaces for NIC attachment.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_BRIDGE_items"></a>
- Type: string

<a id="headingReturn_value_MACVLAN"></a>
<a id="Return_value_MACVLAN"></a>
#### MACVLAN (required)

- Schema name: `Macvlan`
- Type: array of string

Available parent interfaces for creating MACVLAN NIC devices.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_MACVLAN_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
