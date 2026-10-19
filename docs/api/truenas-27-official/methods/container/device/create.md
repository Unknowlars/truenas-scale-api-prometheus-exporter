---
title: container.device.create
kind: method
source_rst: _sources/api_methods_container.device.create.rst.txt
source_html: api_methods_container.device.create.html
required_roles:
  - CONTAINER_DEVICE_WRITE
---

# container.device.create

## Summary

Create a new device for the container of id `container`.

## Required Roles

- `CONTAINER_DEVICE_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: container_device_create

<a id="Call_parameters_items_i0"></a>
#### container_device_create

- Schema name: `container_device_create`
- Type: object

ContainerDeviceCreateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes"></a>
<a id="Call_parameters_items_i0_attributes"></a>
##### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="Call_parameters_items_i0_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i0"></a>
###### [ContainerFilesystemDevice](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i0)

- Schema name: `ContainerFilesystemDevice`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i0_dtype"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for FILESYSTEM devices.
- Specific value: `"FILESYSTEM"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i0_target"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i0_target"></a>
###### target (required)

- Schema name: `Target`
- Type: string

Path inside the container to mount the source at. Must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i0_source"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

Host path to bind-mount into the container. Must reside within a pool (under `/mnt`) and must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i1"></a>
###### [ContainerGPUDevice](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i1)

- Schema name: `ContainerGPUDevice`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i1_dtype"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for GPU devices.
- Specific value: `"GPU"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i1_gpu_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i1_gpu_type"></a>
###### gpu_type (required)

- Schema name: `Gpu Type`
- Type: enum (of string)

GPU device type.
###### Must be one of:

- "AMD"
- "INTEL"
- "NVIDIA"

<a id="headingCall_parameters_items_i0_attributes_oneOf_i1_pci_address"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i1_pci_address"></a>
###### pci_address (required)

- Schema name: `Pci Address`
- Type: string

PCI address of the GPU device on the host system.
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i2"></a>
###### [ContainerNICDevice](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i2)

- Schema name: `ContainerNICDevice`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i2_dtype"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingCall_parameters_items_i0_attributes_oneOf_i2_type"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingCall_parameters_items_i0_attributes_oneOf_i2_nic_attach"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="Call_parameters_items_i0_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_attributes_oneOf_i2_mac"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="Call_parameters_items_i0_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i3"></a>
###### [ContainerUSBDevice](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i3)

- Schema name: `ContainerUSBDevice`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i3_dtype"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingCall_parameters_items_i0_attributes_oneOf_i3_usb"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i3_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="Call_parameters_items_i0_attributes_oneOf_i3_usb_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_usb_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_attributes_oneOf_i3_device"></a>
<a id="Call_parameters_items_i0_attributes_oneOf_i3_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="Call_parameters_items_i0_attributes_oneOf_i3_device_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_attributes_oneOf_i3_device_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_container"></a>
<a id="Call_parameters_items_i0_container"></a>
##### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ContainerDeviceEntry`
- Type: object

The newly created container device configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

<a id="headingReturn_value_attributes"></a>
<a id="Return_value_attributes"></a>
#### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="Return_value_attributes_oneOf"></a>
##### One of

<a id="tab-pane_Return_value_attributes_oneOf_i0"></a>
###### [ContainerFilesystemDevice](#tab-pane_Return_value_attributes_oneOf_i0)

- Schema name: `ContainerFilesystemDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i0_dtype"></a>
<a id="Return_value_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for FILESYSTEM devices.
- Specific value: `"FILESYSTEM"`

<a id="headingReturn_value_attributes_oneOf_i0_target"></a>
<a id="Return_value_attributes_oneOf_i0_target"></a>
###### target (required)

- Schema name: `Target`
- Type: string

Path inside the container to mount the source at. Must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i0_source"></a>
<a id="Return_value_attributes_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

Host path to bind-mount into the container. Must reside within a pool (under `/mnt`) and must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i1"></a>
###### [ContainerGPUDevice](#tab-pane_Return_value_attributes_oneOf_i1)

- Schema name: `ContainerGPUDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i1_dtype"></a>
<a id="Return_value_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for GPU devices.
- Specific value: `"GPU"`

<a id="headingReturn_value_attributes_oneOf_i1_gpu_type"></a>
<a id="Return_value_attributes_oneOf_i1_gpu_type"></a>
###### gpu_type (required)

- Schema name: `Gpu Type`
- Type: enum (of string)

GPU device type.
###### Must be one of:

- "AMD"
- "INTEL"
- "NVIDIA"

<a id="headingReturn_value_attributes_oneOf_i1_pci_address"></a>
<a id="Return_value_attributes_oneOf_i1_pci_address"></a>
###### pci_address (required)

- Schema name: `Pci Address`
- Type: string

PCI address of the GPU device on the host system.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i2"></a>
###### [ContainerNICDevice](#tab-pane_Return_value_attributes_oneOf_i2)

- Schema name: `ContainerNICDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i2_dtype"></a>
<a id="Return_value_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingReturn_value_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="Return_value_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingReturn_value_attributes_oneOf_i2_type"></a>
<a id="Return_value_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingReturn_value_attributes_oneOf_i2_nic_attach"></a>
<a id="Return_value_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="Return_value_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingReturn_value_attributes_oneOf_i2_mac"></a>
<a id="Return_value_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="Return_value_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_attributes_oneOf_i3"></a>
###### [ContainerUSBDevice](#tab-pane_Return_value_attributes_oneOf_i3)

- Schema name: `ContainerUSBDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i3_dtype"></a>
<a id="Return_value_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingReturn_value_attributes_oneOf_i3_usb"></a>
<a id="Return_value_attributes_oneOf_i3_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="Return_value_attributes_oneOf_i3_usb_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i3_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_Return_value_attributes_oneOf_i3_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingReturn_value_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
<a id="Return_value_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingReturn_value_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
<a id="Return_value_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i3_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i3_usb_anyOf_i1)

- Type: null

<a id="headingReturn_value_attributes_oneOf_i3_device"></a>
<a id="Return_value_attributes_oneOf_i3_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="Return_value_attributes_oneOf_i3_device_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_attributes_oneOf_i3_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_attributes_oneOf_i3_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_attributes_oneOf_i3_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_attributes_oneOf_i3_device_anyOf_i1)

- Type: null

<a id="headingReturn_value_container"></a>
<a id="Return_value_container"></a>
#### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
