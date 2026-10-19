---
title: vm.device.usb_passthrough_choices
kind: method
source_rst: _sources/api_methods_vm.device.usb_passthrough_choices.rst.txt
source_html: api_methods_vm.device.usb_passthrough_choices.html
required_roles:
  - READONLY_ADMIN
  - VM_DEVICE_READ
---

# vm.device.usb_passthrough_choices

## Summary

Available choices for USB passthrough devices.

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

- Schema name: `USBPassthroughInfo`
- Type: object

Object of available USB devices for passthrough with their detailed information.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `USBPassthroughDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_additionalProperties_capability"></a>
<a id="Return_value_additionalProperties_capability"></a>
##### capability (required)

- Schema name: `USBCapability`
- Type: object

USB device capability and identification information.
- No Additional Properties
<a id="headingReturn_value_additionalProperties_capability_product"></a>
<a id="Return_value_additionalProperties_capability_product"></a>
###### product (required)

- Schema name: `Product`

USB product name. `null` if not available.
<a id="Return_value_additionalProperties_capability_product_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_capability_product_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_capability_product_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_capability_product_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_capability_product_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_capability_product_id"></a>
<a id="Return_value_additionalProperties_capability_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`

USB product identifier. `null` if not available.
<a id="Return_value_additionalProperties_capability_product_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_capability_product_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_capability_product_id_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_capability_product_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_capability_product_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_capability_vendor"></a>
<a id="Return_value_additionalProperties_capability_vendor"></a>
###### vendor (required)

- Schema name: `Vendor`

USB vendor name. `null` if not available.
<a id="Return_value_additionalProperties_capability_vendor_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_capability_vendor_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_capability_vendor_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_capability_vendor_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_capability_vendor_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_capability_vendor_id"></a>
<a id="Return_value_additionalProperties_capability_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`

USB vendor identifier. `null` if not available.
<a id="Return_value_additionalProperties_capability_vendor_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_capability_vendor_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_capability_vendor_id_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_capability_vendor_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_capability_vendor_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_capability_bus"></a>
<a id="Return_value_additionalProperties_capability_bus"></a>
###### bus (required)

- Schema name: `Bus`

USB bus number. `null` if not available.
<a id="Return_value_additionalProperties_capability_bus_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_capability_bus_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_capability_bus_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_capability_bus_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_capability_bus_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_capability_device"></a>
<a id="Return_value_additionalProperties_capability_device"></a>
###### device (required)

- Schema name: `Device`

USB device number on bus. `null` if not available.
<a id="Return_value_additionalProperties_capability_device_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_capability_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_capability_device_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_capability_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_capability_device_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_available"></a>
<a id="Return_value_additionalProperties_available"></a>
##### available (required)

- Schema name: `Available`
- Type: boolean

Whether the USB device is available for passthrough to virtual machines.

<a id="headingReturn_value_additionalProperties_error"></a>
<a id="Return_value_additionalProperties_error"></a>
##### error (required)

- Schema name: `Error`

Error message if the device cannot be used for passthrough. `null` if no error.
<a id="Return_value_additionalProperties_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_description"></a>
<a id="Return_value_additionalProperties_description"></a>
##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the USB device.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
