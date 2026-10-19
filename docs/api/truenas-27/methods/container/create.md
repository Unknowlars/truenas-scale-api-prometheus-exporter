---
title: container.create
kind: method
source_rst: _sources/api_methods_container.create.rst.txt
source_html: api_methods_container.create.html
required_roles:
  - CONTAINER_WRITE
---

# container.create

## Summary

Create a Container.

This method is a job.

## Required Roles

- `CONTAINER_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: container_create

<a id="Call_parameters_items_i0"></a>
#### container_create

- Schema name: `container_create`
- Type: object

ContainerCreateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_uuid"></a>
<a id="Call_parameters_items_i0_uuid"></a>
##### uuid

- Schema name: `Uuid`
- Default: null

Container UUID (for libvirt). Auto-generated if not provided.
<a id="Call_parameters_items_i0_uuid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_uuid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_uuid_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_uuid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_uuid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Container name.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_description"></a>
<a id="Call_parameters_items_i0_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Container description.

<a id="headingCall_parameters_items_i0_cpuset"></a>
<a id="Call_parameters_items_i0_cpuset"></a>
##### cpuset

- Schema name: `Cpuset`
- Default: null

List of physical CPU numbers that domain process and virtual CPUs can be pinned to by default.
<a id="Call_parameters_items_i0_cpuset_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_cpuset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_cpuset_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_cpuset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_cpuset_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_autostart"></a>
<a id="Call_parameters_items_i0_autostart"></a>
##### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Automatically start the container on boot.

<a id="headingCall_parameters_items_i0_time"></a>
<a id="Call_parameters_items_i0_time"></a>
##### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Whether container time should be local time or UTC time.
###### Must be one of:

- "LOCAL"
- "UTC"

<a id="headingCall_parameters_items_i0_shutdown_timeout"></a>
<a id="Call_parameters_items_i0_shutdown_timeout"></a>
##### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

How many seconds to wait for container to shut down before killing it.
- Value must be greater or equal to `5` and lesser or equal to `300`

<a id="headingCall_parameters_items_i0_init"></a>
<a id="Call_parameters_items_i0_init"></a>
##### init

- Schema name: `Init`
- Type: string
- Default: "/sbin/init"

"init" process commandline.

<a id="headingCall_parameters_items_i0_initdir"></a>
<a id="Call_parameters_items_i0_initdir"></a>
##### initdir

- Schema name: `Initdir`
- Default: null

"init" process working dir.
<a id="Call_parameters_items_i0_initdir_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_initdir_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_initdir_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_initdir_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_initdir_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_initenv"></a>
<a id="Call_parameters_items_i0_initenv"></a>
##### initenv

- Schema name: `Initenv`
- Type: object
- Default: {}

"init" process environment variables.
<a id="headingCall_parameters_items_i0_initenv_additionalProperties"></a>
<a id="Call_parameters_items_i0_initenv_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

<a id="headingCall_parameters_items_i0_inituser"></a>
<a id="Call_parameters_items_i0_inituser"></a>
##### inituser

- Schema name: `Inituser`
- Default: null

"init" process username.
<a id="Call_parameters_items_i0_inituser_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_inituser_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_inituser_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_inituser_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_inituser_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_initgroup"></a>
<a id="Call_parameters_items_i0_initgroup"></a>
##### initgroup

- Schema name: `Initgroup`
- Default: null

"init" process group.
<a id="Call_parameters_items_i0_initgroup_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_initgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_initgroup_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_initgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_initgroup_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_idmap"></a>
<a id="Call_parameters_items_i0_idmap"></a>
##### idmap

- Schema name: `Idmap`
- Default: {"type": "DEFAULT"}

Idmap configuration for the container There are three two possible values: DEFAULT: This applies the standard TrueNAS idmap namespace configuration. It changes user ID (UID) 0 (root) in the container to UID 2147000001 (truenas*container*unpriv_root). It offsets the other container UIDs by the same amount. For example, UID 1000 in the container becomes UID 2147001001 in the host. ISOLATED: Same as `DEFAULT`, but UID will be calculated as `2147000001 + 65536 * slice`. This will ensure unique ID for each container (provided that the `slice` is also unique). None: The container does not apply any idmap namespace. Container UIDs map directly to host UIDs. For example, UID 0 in the container is UID 0 in the host. WARNING: For security, use the DEFAULT value. Security best practice is to run containers with idmap namespaces.
<a id="Call_parameters_items_i0_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_idmap_anyOf_i0)

<a id="Call_parameters_items_i0_idmap_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i0"></a>
###### [DefaultIdmapConfiguration](#tab-pane_Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i0)

- Schema name: `DefaultIdmapConfiguration`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_idmap_anyOf_i0_oneOf_i0_type"></a>
<a id="Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Configuration type for default ID mapping.
- Specific value: `"DEFAULT"`

<a id="tab-pane_Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i1"></a>
###### [IsolatedIdmapConfiguration](#tab-pane_Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i1)

- Schema name: `IsolatedIdmapConfiguration`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_idmap_anyOf_i0_oneOf_i1_type"></a>
<a id="Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Configuration type for isolated ID mapping.
- Specific value: `"ISOLATED"`

<a id="headingCall_parameters_items_i0_idmap_anyOf_i0_oneOf_i1_slice"></a>
<a id="Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i1_slice"></a>
###### slice (required)

- Schema name: `Slice`

`null` when creating means we'll look up an unused slice on backend.
<a id="Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i1_slice_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0` and strictly lesser than `1000`

<a id="tab-pane_Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i1)

- Type: null

<a id="tab-pane_Call_parameters_items_i0_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_idmap_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_capabilities_policy"></a>
<a id="Call_parameters_items_i0_capabilities_policy"></a>
##### capabilities_policy

- Schema name: `Capabilities Policy`
- Type: enum (of string)
- Default: "DEFAULT"

Default rules for capabilities: either keep the default behavior that is dropping the following capabilities: sys*module, sys*time, mknod, audit*control, mac*admin. Or keep all capabilities, or drop all capabilities.
###### Must be one of:

- "DEFAULT"
- "ALLOW"
- "DENY"

<a id="headingCall_parameters_items_i0_capabilities_state"></a>
<a id="Call_parameters_items_i0_capabilities_state"></a>
##### capabilities_state

- Schema name: `Capabilities State`
- Type: object
- Default: {}

Enable or disable specific capabilities.
<a id="headingCall_parameters_items_i0_capabilities_state_additionalProperties"></a>
<a id="Call_parameters_items_i0_capabilities_state_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: boolean

<a id="headingCall_parameters_items_i0_pool"></a>
<a id="Call_parameters_items_i0_pool"></a>
##### pool

- Schema name: `Pool`
- Default: null

Pool to use for this container. Leave it null to use container preferred pool instead.
<a id="Call_parameters_items_i0_pool_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_pool_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_pool_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_pool_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_pool_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_image"></a>
<a id="Call_parameters_items_i0_image"></a>
##### image (required)

- Schema name: `ContainerCreateImage`
- Type: object

Image to use for container creation.
- No Additional Properties
<a id="headingCall_parameters_items_i0_image_name"></a>
<a id="Call_parameters_items_i0_image_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Image name. Use `container.image.query_registry` to list all available images.

<a id="headingCall_parameters_items_i0_image_version"></a>
<a id="Call_parameters_items_i0_image_version"></a>
###### version (required)

- Schema name: `Version`
- Type: string

Image version. Use `container.image.query_registry` to list all available images.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ContainerEntry`
- Type: object

Newly created container.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Container ID.

<a id="headingReturn_value_uuid"></a>
<a id="Return_value_uuid"></a>
#### uuid (required)

- Schema name: `Uuid`
- Type: string

Container UUID (for libvirt).

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Container name.
- Must be at least `1` characters long

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description

- Schema name: `Description`
- Type: string
- Default: ""

Container description.

<a id="headingReturn_value_devices"></a>
<a id="Return_value_devices"></a>
#### devices

- Schema name: `Devices`
- Type: array of object
- Default: []

Container's devices.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_devices_items"></a>
##### ContainerDeviceEntry

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_id"></a>
<a id="Return_value_devices_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

<a id="headingReturn_value_devices_items_attributes"></a>
<a id="Return_value_devices_items_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="Return_value_devices_items_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i0"></a>
###### [ContainerFilesystemDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i0)

- Schema name: `ContainerFilesystemDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i0_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for FILESYSTEM devices.
- Specific value: `"FILESYSTEM"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i0_target"></a>
<a id="Return_value_devices_items_attributes_oneOf_i0_target"></a>
###### target (required)

- Schema name: `Target`
- Type: string

Path inside the container to mount the source at. Must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingReturn_value_devices_items_attributes_oneOf_i0_source"></a>
<a id="Return_value_devices_items_attributes_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

Host path to bind-mount into the container. Must reside within a pool (under `/mnt`) and must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i1"></a>
###### [ContainerGPUDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i1)

- Schema name: `ContainerGPUDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i1_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for GPU devices.
- Specific value: `"GPU"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i1_gpu_type"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_gpu_type"></a>
###### gpu_type (required)

- Schema name: `Gpu Type`
- Type: enum (of string)

GPU device type.
###### Must be one of:

- "AMD"
- "INTEL"
- "NVIDIA"

<a id="headingReturn_value_devices_items_attributes_oneOf_i1_pci_address"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_pci_address"></a>
###### pci_address (required)

- Schema name: `Pci Address`
- Type: string

PCI address of the GPU device on the host system.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i2"></a>
###### [ContainerNICDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i2)

- Schema name: `ContainerNICDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i2_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="Return_value_devices_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingReturn_value_devices_items_attributes_oneOf_i2_type"></a>
<a id="Return_value_devices_items_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingReturn_value_devices_items_attributes_oneOf_i2_nic_attach"></a>
<a id="Return_value_devices_items_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="Return_value_devices_items_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i2_mac"></a>
<a id="Return_value_devices_items_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="Return_value_devices_items_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i3"></a>
###### [ContainerUSBDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i3)

- Schema name: `ContainerUSBDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i3_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i3_usb"></a>
<a id="Return_value_devices_items_attributes_oneOf_i3_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="Return_value_devices_items_attributes_oneOf_i3_usb_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i3_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_Return_value_devices_items_attributes_oneOf_i3_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
<a id="Return_value_devices_items_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingReturn_value_devices_items_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
<a id="Return_value_devices_items_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i3_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i3_usb_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i3_device"></a>
<a id="Return_value_devices_items_attributes_oneOf_i3_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="Return_value_devices_items_attributes_oneOf_i3_device_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i3_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i3_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i3_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i3_device_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_container"></a>
<a id="Return_value_devices_items_container"></a>
###### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

<a id="headingReturn_value_cpuset"></a>
<a id="Return_value_cpuset"></a>
#### cpuset

- Schema name: `Cpuset`
- Default: null

List of physical CPU numbers that domain process and virtual CPUs can be pinned to by default.
<a id="Return_value_cpuset_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_cpuset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_cpuset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_cpuset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_cpuset_anyOf_i1)

- Type: null

<a id="headingReturn_value_autostart"></a>
<a id="Return_value_autostart"></a>
#### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Automatically start the container on boot.

<a id="headingReturn_value_time"></a>
<a id="Return_value_time"></a>
#### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Whether container time should be local time or UTC time.
##### Must be one of:

- "LOCAL"
- "UTC"

<a id="headingReturn_value_shutdown_timeout"></a>
<a id="Return_value_shutdown_timeout"></a>
#### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

How many seconds to wait for container to shut down before killing it.
- Value must be greater or equal to `5` and lesser or equal to `300`

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`
- Type: string

Which dataset to use as the container root filesystem.

<a id="headingReturn_value_init"></a>
<a id="Return_value_init"></a>
#### init

- Schema name: `Init`
- Type: string
- Default: "/sbin/init"

"init" process commandline.

<a id="headingReturn_value_initdir"></a>
<a id="Return_value_initdir"></a>
#### initdir

- Schema name: `Initdir`
- Default: null

"init" process working dir.
<a id="Return_value_initdir_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_initdir_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_initdir_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_initdir_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_initdir_anyOf_i1)

- Type: null

<a id="headingReturn_value_initenv"></a>
<a id="Return_value_initenv"></a>
#### initenv

- Schema name: `Initenv`
- Type: object
- Default: {}

"init" process environment variables.
<a id="headingReturn_value_initenv_additionalProperties"></a>
<a id="Return_value_initenv_additionalProperties"></a>
##### Additional Properties

Each additional property must conform to the following schema
- Type: string

<a id="headingReturn_value_inituser"></a>
<a id="Return_value_inituser"></a>
#### inituser

- Schema name: `Inituser`
- Default: null

"init" process username.
<a id="Return_value_inituser_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_inituser_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_inituser_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_inituser_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_inituser_anyOf_i1)

- Type: null

<a id="headingReturn_value_initgroup"></a>
<a id="Return_value_initgroup"></a>
#### initgroup

- Schema name: `Initgroup`
- Default: null

"init" process group.
<a id="Return_value_initgroup_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_initgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_initgroup_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_initgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_initgroup_anyOf_i1)

- Type: null

<a id="headingReturn_value_idmap"></a>
<a id="Return_value_idmap"></a>
#### idmap

- Schema name: `Idmap`
- Default: {"type": "DEFAULT"}

Idmap configuration for the container There are three two possible values: DEFAULT: This applies the standard TrueNAS idmap namespace configuration. It changes user ID (UID) 0 (root) in the container to UID 2147000001 (truenas*container*unpriv_root). It offsets the other container UIDs by the same amount. For example, UID 1000 in the container becomes UID 2147001001 in the host. ISOLATED: Same as `DEFAULT`, but UID will be calculated as `2147000001 + 65536 * slice`. This will ensure unique ID for each container (provided that the `slice` is also unique). None: The container does not apply any idmap namespace. Container UIDs map directly to host UIDs. For example, UID 0 in the container is UID 0 in the host. WARNING: For security, use the DEFAULT value. Security best practice is to run containers with idmap namespaces.
<a id="Return_value_idmap_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_idmap_anyOf_i0)

<a id="Return_value_idmap_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_idmap_anyOf_i0_oneOf_i0"></a>
###### [DefaultIdmapConfiguration](#tab-pane_Return_value_idmap_anyOf_i0_oneOf_i0)

- Schema name: `DefaultIdmapConfiguration`
- Type: object
- No Additional Properties
<a id="headingReturn_value_idmap_anyOf_i0_oneOf_i0_type"></a>
<a id="Return_value_idmap_anyOf_i0_oneOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Configuration type for default ID mapping.
- Specific value: `"DEFAULT"`

<a id="tab-pane_Return_value_idmap_anyOf_i0_oneOf_i1"></a>
###### [IsolatedIdmapConfiguration](#tab-pane_Return_value_idmap_anyOf_i0_oneOf_i1)

- Schema name: `IsolatedIdmapConfiguration`
- Type: object
- No Additional Properties
<a id="headingReturn_value_idmap_anyOf_i0_oneOf_i1_type"></a>
<a id="Return_value_idmap_anyOf_i0_oneOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Configuration type for isolated ID mapping.
- Specific value: `"ISOLATED"`

<a id="headingReturn_value_idmap_anyOf_i0_oneOf_i1_slice"></a>
<a id="Return_value_idmap_anyOf_i0_oneOf_i1_slice"></a>
###### slice (required)

- Schema name: `Slice`

`null` when creating means we'll look up an unused slice on backend.
<a id="Return_value_idmap_anyOf_i0_oneOf_i1_slice_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0` and strictly lesser than `1000`

<a id="tab-pane_Return_value_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_idmap_anyOf_i1)

- Type: null

<a id="headingReturn_value_capabilities_policy"></a>
<a id="Return_value_capabilities_policy"></a>
#### capabilities_policy

- Schema name: `Capabilities Policy`
- Type: enum (of string)
- Default: "DEFAULT"

Default rules for capabilities: either keep the default behavior that is dropping the following capabilities: sys*module, sys*time, mknod, audit*control, mac*admin. Or keep all capabilities, or drop all capabilities.
##### Must be one of:

- "DEFAULT"
- "ALLOW"
- "DENY"

<a id="headingReturn_value_capabilities_state"></a>
<a id="Return_value_capabilities_state"></a>
#### capabilities_state

- Schema name: `Capabilities State`
- Type: object
- Default: {}

Enable or disable specific capabilities.
<a id="headingReturn_value_capabilities_state_additionalProperties"></a>
<a id="Return_value_capabilities_state_additionalProperties"></a>
##### Additional Properties

Each additional property must conform to the following schema
- Type: boolean

<a id="headingReturn_value_default_network"></a>
<a id="Return_value_default_network"></a>
#### default_network

- Schema name: `Default Network`
- Default: null

The default network bridge this container will use when no NIC devices are explicitly attached. When the container has explicitly configured NIC devices, this is `null` because the NIC configuration is visible in the `devices` list.
<a id="Return_value_default_network_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_default_network_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_default_network_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_default_network_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_default_network_anyOf_i1)

- Type: null

<a id="headingReturn_value_status"></a>
<a id="Return_value_status"></a>
#### status (required)

- Schema name: `ContainerStatus`
- Type: object

Container state.
- No Additional Properties
<a id="headingReturn_value_status_state"></a>
<a id="Return_value_status_state"></a>
##### state (required)

- Schema name: `State`
- Type: enum (of string)

Container state.
###### Must be one of:

- "RUNNING"
- "STOPPED"
- "SUSPENDED"

<a id="headingReturn_value_status_pid"></a>
<a id="Return_value_status_pid"></a>
##### pid (required)

- Schema name: `Pid`

Container host PID (if running). Informational only do not rely on this value to identify the container's init process.
<a id="Return_value_status_pid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_status_pid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_status_pid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_status_pid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_status_pid_anyOf_i1)

- Type: null

<a id="headingReturn_value_status_domain_state"></a>
<a id="Return_value_status_domain_state"></a>
##### domain_state (required)

- Schema name: `Domain State`

Domain state reported by libvirt.
<a id="Return_value_status_domain_state_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_status_domain_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_status_domain_state_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_status_domain_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_status_domain_state_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
