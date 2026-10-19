---
title: vm.device.passthrough_device
kind: method
source_rst: _sources/api_methods_vm.device.passthrough_device.rst.txt
source_html: api_methods_vm.device.passthrough_device.html
required_roles:
  - VM_DEVICE_READ
---

# vm.device.passthrough_device

## Summary

Retrieve details about `device` PCI device.

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

PCI device identifier to get passthrough information for.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `VMDevicePassthroughDevice`
- Type: object

Detailed information about the specified PCI passthrough device.
- No Additional Properties
<a id="headingReturn_value_capability"></a>
<a id="Return_value_capability"></a>
#### capability (required)

- Schema name: `VMDeviceCapability`
- Type: object

PCI device capability information.
- No Additional Properties
<a id="headingReturn_value_capability_class"></a>
<a id="Return_value_capability_class"></a>
##### class (required)

- Schema name: `Class`

PCI device class identifier. `null` if not available.
<a id="Return_value_capability_class_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_class_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_class_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_class_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_class_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_domain"></a>
<a id="Return_value_capability_domain"></a>
##### domain (required)

- Schema name: `Domain`

PCI domain number. `null` if not available.
<a id="Return_value_capability_domain_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_domain_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_domain_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_domain_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_domain_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_bus"></a>
<a id="Return_value_capability_bus"></a>
##### bus (required)

- Schema name: `Bus`

PCI bus number. `null` if not available.
<a id="Return_value_capability_bus_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_bus_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_bus_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_bus_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_bus_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_slot"></a>
<a id="Return_value_capability_slot"></a>
##### slot (required)

- Schema name: `Slot`

PCI slot number. `null` if not available.
<a id="Return_value_capability_slot_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_slot_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_slot_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_slot_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_slot_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_function"></a>
<a id="Return_value_capability_function"></a>
##### function (required)

- Schema name: `Function`

PCI function number. `null` if not available.
<a id="Return_value_capability_function_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_function_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_function_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_function_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_function_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_product"></a>
<a id="Return_value_capability_product"></a>
##### product (required)

- Schema name: `Product`

Product name of the PCI device. `null` if not available.
<a id="Return_value_capability_product_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_product_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_product_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_product_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_product_anyOf_i1)

- Type: null

<a id="headingReturn_value_capability_vendor"></a>
<a id="Return_value_capability_vendor"></a>
##### vendor (required)

- Schema name: `Vendor`

Vendor name of the PCI device. `null` if not available.
<a id="Return_value_capability_vendor_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_capability_vendor_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_capability_vendor_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_capability_vendor_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_capability_vendor_anyOf_i1)

- Type: null

<a id="headingReturn_value_controller_type"></a>
<a id="Return_value_controller_type"></a>
#### controller_type (required)

- Schema name: `Controller Type`

Type of controller this device provides. `null` if not a controller.
<a id="Return_value_controller_type_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_controller_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_controller_type_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_controller_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_controller_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_iommu_group"></a>
<a id="Return_value_iommu_group"></a>
#### iommu_group

- Default: null

IOMMU group information for device isolation. `null` if IOMMU not available.
<a id="Return_value_iommu_group_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_iommu_group_anyOf_i0"></a>
###### [VMDeviceIOMMUGroup](#tab-pane_Return_value_iommu_group_anyOf_i0)

- Schema name: `VMDeviceIOMMUGroup`
- Type: object
- No Additional Properties
<a id="headingReturn_value_iommu_group_anyOf_i0_number"></a>
<a id="Return_value_iommu_group_anyOf_i0_number"></a>
###### number (required)

- Schema name: `Number`
- Type: integer

IOMMU group number for device isolation.

<a id="headingReturn_value_iommu_group_anyOf_i0_addresses"></a>
<a id="Return_value_iommu_group_anyOf_i0_addresses"></a>
###### addresses (required)

- Schema name: `Addresses`
- Type: array of object

Array of PCI addresses in this IOMMU group.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_iommu_group_anyOf_i0_addresses_items"></a>
###### VMDeviceIOMMUGroupAddress

- Schema name: `VMDeviceIOMMUGroupAddress`
- Type: object
- No Additional Properties
<a id="headingReturn_value_iommu_group_anyOf_i0_addresses_items_domain"></a>
<a id="Return_value_iommu_group_anyOf_i0_addresses_items_domain"></a>
###### domain (required)

- Schema name: `Domain`
- Type: string

PCI domain number for this IOMMU group address.

<a id="headingReturn_value_iommu_group_anyOf_i0_addresses_items_bus"></a>
<a id="Return_value_iommu_group_anyOf_i0_addresses_items_bus"></a>
###### bus (required)

- Schema name: `Bus`
- Type: string

PCI bus number for this IOMMU group address.

<a id="headingReturn_value_iommu_group_anyOf_i0_addresses_items_slot"></a>
<a id="Return_value_iommu_group_anyOf_i0_addresses_items_slot"></a>
###### slot (required)

- Schema name: `Slot`
- Type: string

PCI slot number for this IOMMU group address.

<a id="headingReturn_value_iommu_group_anyOf_i0_addresses_items_function"></a>
<a id="Return_value_iommu_group_anyOf_i0_addresses_items_function"></a>
###### function (required)

- Schema name: `Function`
- Type: string

PCI function number for this IOMMU group address.

<a id="tab-pane_Return_value_iommu_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_iommu_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_available"></a>
<a id="Return_value_available"></a>
#### available (required)

- Schema name: `Available`
- Type: boolean

Whether the device is available for passthrough to virtual machines.

<a id="headingReturn_value_drivers"></a>
<a id="Return_value_drivers"></a>
#### drivers (required)

- Schema name: `Drivers`
- Type: array of string

Array of kernel drivers currently bound to this device.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_drivers_items"></a>
- Type: string

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

<a id="headingReturn_value_reset_mechanism_defined"></a>
<a id="Return_value_reset_mechanism_defined"></a>
#### reset_mechanism_defined (required)

- Schema name: `Reset Mechanism Defined`
- Type: boolean

Whether the device supports proper reset mechanisms for passthrough.

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the PCI device.

<a id="headingReturn_value_critical"></a>
<a id="Return_value_critical"></a>
#### critical (required)

- Schema name: `Critical`
- Type: boolean

Whether this device is critical to host system operation.

<a id="headingReturn_value_device_path"></a>
<a id="Return_value_device_path"></a>
#### device_path (required)

- Schema name: `Device Path`

Device filesystem path. `null` if not available.
<a id="Return_value_device_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_device_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_device_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_device_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_device_path_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
