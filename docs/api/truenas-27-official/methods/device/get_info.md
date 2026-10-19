---
title: device.get_info
kind: method
source_rst: _sources/api_methods_device.get_info.rst.txt
source_html: api_methods_device.get_info.html
required_roles:
  - READONLY_ADMIN
---

# device.get_info

## Summary

Get info for `type` device.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`

Device information query parameters specifying type and options.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [DeviceGetInfoDisk](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Schema name: `DeviceGetInfoDisk`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_anyOf_i0_type"></a>
<a id="Call_parameters_items_i0_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Get disk info.
- Specific value: `"DISK"`

<a id="headingCall_parameters_items_i0_anyOf_i0_get_partitions"></a>
<a id="Call_parameters_items_i0_anyOf_i0_get_partitions"></a>
###### get_partitions

- Schema name: `Get Partitions`
- Type: boolean
- Default: false

If set, query partition information for the disks. **NOTE: This can be expensive on systems with a large number of disks present.**

<a id="headingCall_parameters_items_i0_anyOf_i0_serials_only"></a>
<a id="Call_parameters_items_i0_anyOf_i0_serials_only"></a>
###### serials_only

- Schema name: `Serials Only`
- Type: boolean
- Default: false

If set, query *ONLY* serial information for the disks (overrides `get_partitions`).

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [DeviceGetInfoOther](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Schema name: `DeviceGetInfoOther`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_anyOf_i1_type"></a>
<a id="Call_parameters_items_i0_anyOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Get info for either serial devices or GPUs.
###### Must be one of:

- "SERIAL"
- "GPU"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

Return an object if `type="DISK"` or an array otherwise.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: object
<a id="headingReturn_value_anyOf_i0_additionalProperties"></a>
<a id="Return_value_anyOf_i0_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: object
<a id="headingReturn_value_anyOf_i1_additionalProperties"></a>
<a id="Return_value_anyOf_i1_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: object

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### SerialInfo

- Schema name: `SerialInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_name"></a>
<a id="Return_value_anyOf_i2_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Device name for the serial port.

<a id="headingReturn_value_anyOf_i2_items_location"></a>
<a id="Return_value_anyOf_i2_items_location"></a>
###### location (required)

- Schema name: `Location`
- Type: string

Physical location or path of the serial device.

<a id="headingReturn_value_anyOf_i2_items_drivername"></a>
<a id="Return_value_anyOf_i2_items_drivername"></a>
###### drivername (required)

- Schema name: `Drivername`
- Type: string

Name of the kernel driver handling this serial device.

<a id="headingReturn_value_anyOf_i2_items_start"></a>
<a id="Return_value_anyOf_i2_items_start"></a>
###### start (required)

- Schema name: `Start`
- Type: string

Starting address or identifier for the serial device.

<a id="headingReturn_value_anyOf_i2_items_size"></a>
<a id="Return_value_anyOf_i2_items_size"></a>
###### size (required)

- Schema name: `Size`
- Type: integer

Size or capacity information for the serial device.

<a id="headingReturn_value_anyOf_i2_items_description"></a>
<a id="Return_value_anyOf_i2_items_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the serial device.

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [Option 4](#tab-pane_Return_value_anyOf_i3)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_items"></a>
###### GPUInfo

- Schema name: `GPUInfo`
- Type: object
<a id="headingReturn_value_anyOf_i3_items_addr"></a>
<a id="Return_value_anyOf_i3_items_addr"></a>
###### addr (required)

- Schema name: `GPUInfoAddr`
- Type: object

PCI address information for the GPU.
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_items_addr_pci_slot"></a>
<a id="Return_value_anyOf_i3_items_addr_pci_slot"></a>
###### pci_slot (required)

- Schema name: `Pci Slot`
- Type: string

PCI slot identifier for the GPU.

<a id="headingReturn_value_anyOf_i3_items_addr_domain"></a>
<a id="Return_value_anyOf_i3_items_addr_domain"></a>
###### domain (required)

- Schema name: `Domain`
- Type: string

PCI domain number.

<a id="headingReturn_value_anyOf_i3_items_addr_bus"></a>
<a id="Return_value_anyOf_i3_items_addr_bus"></a>
###### bus (required)

- Schema name: `Bus`
- Type: string

PCI bus number.

<a id="headingReturn_value_anyOf_i3_items_addr_slot"></a>
<a id="Return_value_anyOf_i3_items_addr_slot"></a>
###### slot (required)

- Schema name: `Slot`
- Type: string

PCI slot number.

<a id="headingReturn_value_anyOf_i3_items_description"></a>
<a id="Return_value_anyOf_i3_items_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the GPU.

<a id="headingReturn_value_anyOf_i3_items_devices"></a>
<a id="Return_value_anyOf_i3_items_devices"></a>
###### devices (required)

- Schema name: `Devices`
- Type: array of object

Array of PCI devices associated with this GPU.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_items_devices_items"></a>
###### GPUInfoDevice

- Schema name: `GPUInfoDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_items_devices_items_pci_id"></a>
<a id="Return_value_anyOf_i3_items_devices_items_pci_id"></a>
###### pci_id (required)

- Schema name: `Pci Id`
- Type: string

PCI device identifier.

<a id="headingReturn_value_anyOf_i3_items_devices_items_pci_slot"></a>
<a id="Return_value_anyOf_i3_items_devices_items_pci_slot"></a>
###### pci_slot (required)

- Schema name: `Pci Slot`
- Type: string

PCI slot location.

<a id="headingReturn_value_anyOf_i3_items_devices_items_vm_pci_slot"></a>
<a id="Return_value_anyOf_i3_items_devices_items_vm_pci_slot"></a>
###### vm_pci_slot (required)

- Schema name: `Vm Pci Slot`
- Type: string

Virtual machine PCI slot mapping.

<a id="headingReturn_value_anyOf_i3_items_vendor"></a>
<a id="Return_value_anyOf_i3_items_vendor"></a>
###### vendor (required)

- Schema name: `Vendor`

GPU vendor name or `null` if unknown.
<a id="Return_value_anyOf_i3_items_vendor_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_items_vendor_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_items_vendor_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_items_vendor_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_items_vendor_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_items_available_to_host"></a>
<a id="Return_value_anyOf_i3_items_available_to_host"></a>
###### available_to_host (required)

- Schema name: `Available To Host`
- Type: boolean

Whether the GPU is available for use by the host system.

<a id="headingReturn_value_anyOf_i3_items_uses_system_critical_devices"></a>
<a id="Return_value_anyOf_i3_items_uses_system_critical_devices"></a>
###### uses_system_critical_devices (required)

- Schema name: `Uses System Critical Devices`
- Type: boolean

Whether the GPU uses devices critical for system operation.

<a id="headingReturn_value_anyOf_i3_items_critical_reason"></a>
<a id="Return_value_anyOf_i3_items_critical_reason"></a>
###### critical_reason (required)

- Schema name: `Critical Reason`

Reason why GPU is considered critical or `null` if not critical.
<a id="Return_value_anyOf_i3_items_critical_reason_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_items_critical_reason_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_items_critical_reason_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_items_critical_reason_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_items_critical_reason_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_items_additionalProperties"></a>
<a id="Return_value_anyOf_i3_items_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
