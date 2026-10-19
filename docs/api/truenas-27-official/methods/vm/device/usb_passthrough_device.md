---
title: vm.device.usb_passthrough_device
kind: method
source_rst: _sources/api_methods_vm.device.usb_passthrough_device.rst.txt
source_html: api_methods_vm.device.usb_passthrough_device.html
required_roles:
  - VM_DEVICE_READ
---

# vm.device.usb_passthrough_device

## Summary

Retrieve details about `device` USB device.

## Required Roles

- `VM_DEVICE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: device

<a id="Call_parameters_items_i0"></a>
#### device

- Schema name: `device`
- Type: string

USB device identifier to get passthrough information for.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `USBPassthroughDevice`
- Type: object

Detailed information about the specified USB passthrough device.
- No Additional Properties
<a id="headingReturn_value_capability"></a>
<a id="Return_value_capability"></a>
#### capability (required)

- Schema name: `USBCapability`
- Type: object

USB device capability and identification information.
- No Additional Properties
<a id="headingReturn_value_capability_product"></a>
<a id="Return_value_capability_product"></a>
##### product (required)

- Schema name: `Product`

USB product name. `null` if not available.
<a id="Return_value_capability_product_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_product_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_product_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_product_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_product_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_product_id"></a>
<a id="Return_value_capability_product_id"></a>
##### product_id (required)

- Schema name: `Product Id`

USB product identifier. `null` if not available.
<a id="Return_value_capability_product_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_product_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_product_id_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_product_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_product_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_vendor"></a>
<a id="Return_value_capability_vendor"></a>
##### vendor (required)

- Schema name: `Vendor`

USB vendor name. `null` if not available.
<a id="Return_value_capability_vendor_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_vendor_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_vendor_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_vendor_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_vendor_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_vendor_id"></a>
<a id="Return_value_capability_vendor_id"></a>
##### vendor_id (required)

- Schema name: `Vendor Id`

USB vendor identifier. `null` if not available.
<a id="Return_value_capability_vendor_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_vendor_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_vendor_id_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_vendor_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_vendor_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_bus"></a>
<a id="Return_value_capability_bus"></a>
##### bus (required)

- Schema name: `Bus`

USB bus number. `null` if not available.
<a id="Return_value_capability_bus_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_bus_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_bus_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_bus_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_bus_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_device"></a>
<a id="Return_value_capability_device"></a>
##### device (required)

- Schema name: `Device`

USB device number on bus. `null` if not available.
<a id="Return_value_capability_device_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_device_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_device_anyOf_i1)

- Type: null

<a id="headingReturn_value_available"></a>
<a id="Return_value_available"></a>
#### available (required)

- Schema name: `Available`
- Type: boolean

Whether the USB device is available for passthrough to virtual machines.

<a id="headingReturn_value_error"></a>
<a id="Return_value_error"></a>
#### error (required)

- Schema name: `Error`

Error message if the device cannot be used for passthrough. `null` if no error.
<a id="Return_value_error_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the USB device.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
