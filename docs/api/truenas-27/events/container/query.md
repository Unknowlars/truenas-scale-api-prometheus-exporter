---
title: container.query
kind: event
source_rst: _sources/api_events_container.query.rst.txt
source_html: api_events_container.query.html
required_roles:
  - CONTAINER_READ
---

# container.query

## Summary

Sent on container changes.

## Required Roles

- `CONTAINER_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `ContainerAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `ContainerEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Container ID.

<a id="headingADDED_fields_uuid"></a>
<a id="ADDED_fields_uuid"></a>
##### uuid (required)

- Schema name: `Uuid`
- Type: string

Container UUID (for libvirt).

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Container name.
- Must be at least `1` characters long

<a id="headingADDED_fields_description"></a>
<a id="ADDED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Container description.

<a id="headingADDED_fields_devices"></a>
<a id="ADDED_fields_devices"></a>
##### devices

- Schema name: `Devices`
- Type: array of object
- Default: []

Container's devices.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_devices_items"></a>
###### ContainerDeviceEntry

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_id"></a>
<a id="ADDED_fields_devices_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

<a id="headingADDED_fields_devices_items_attributes"></a>
<a id="ADDED_fields_devices_items_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="ADDED_fields_devices_items_attributes_oneOf"></a>
###### One of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i0"></a>
###### [ContainerFilesystemDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i0)

- Schema name: `ContainerFilesystemDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i0_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for FILESYSTEM devices.
- Specific value: `"FILESYSTEM"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i0_target"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i0_target"></a>
###### target (required)

- Schema name: `Target`
- Type: string

Path inside the container to mount the source at. Must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingADDED_fields_devices_items_attributes_oneOf_i0_source"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

Host path to bind-mount into the container. Must reside within a pool (under `/mnt`) and must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1"></a>
###### [ContainerGPUDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1)

- Schema name: `ContainerGPUDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for GPU devices.
- Specific value: `"GPU"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_gpu_type"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_gpu_type"></a>
###### gpu_type (required)

- Schema name: `Gpu Type`
- Type: enum (of string)

GPU device type.
###### Must be one of:

- "AMD"
- "INTEL"
- "NVIDIA"

<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_pci_address"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_pci_address"></a>
###### pci_address (required)

- Schema name: `Pci Address`
- Type: string

PCI address of the GPU device on the host system.
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2"></a>
###### [ContainerNICDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2)

- Schema name: `ContainerNICDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_type"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_nic_attach"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_mac"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3"></a>
###### [ContainerUSBDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3)

- Schema name: `ContainerUSBDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_usb"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_usb_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_device"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_device_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_device_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_container"></a>
<a id="ADDED_fields_devices_items_container"></a>
###### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

<a id="headingADDED_fields_cpuset"></a>
<a id="ADDED_fields_cpuset"></a>
##### cpuset

- Schema name: `Cpuset`
- Default: null

List of physical CPU numbers that domain process and virtual CPUs can be pinned to by default.
<a id="ADDED_fields_cpuset_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_cpuset_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_cpuset_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_cpuset_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_cpuset_anyOf_i1)

- Type: null

<a id="headingADDED_fields_autostart"></a>
<a id="ADDED_fields_autostart"></a>
##### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Automatically start the container on boot.

<a id="headingADDED_fields_time"></a>
<a id="ADDED_fields_time"></a>
##### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Whether container time should be local time or UTC time.
###### Must be one of:

- "LOCAL"
- "UTC"

<a id="headingADDED_fields_shutdown_timeout"></a>
<a id="ADDED_fields_shutdown_timeout"></a>
##### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

How many seconds to wait for container to shut down before killing it.
- Value must be greater or equal to `5` and lesser or equal to `300`

<a id="headingADDED_fields_dataset"></a>
<a id="ADDED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

Which dataset to use as the container root filesystem.

<a id="headingADDED_fields_init"></a>
<a id="ADDED_fields_init"></a>
##### init

- Schema name: `Init`
- Type: string
- Default: "/sbin/init"

"init" process commandline.

<a id="headingADDED_fields_initdir"></a>
<a id="ADDED_fields_initdir"></a>
##### initdir

- Schema name: `Initdir`
- Default: null

"init" process working dir.
<a id="ADDED_fields_initdir_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_initdir_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_initdir_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_initdir_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_initdir_anyOf_i1)

- Type: null

<a id="headingADDED_fields_initenv"></a>
<a id="ADDED_fields_initenv"></a>
##### initenv

- Schema name: `Initenv`
- Type: object
- Default: {}

"init" process environment variables.
<a id="headingADDED_fields_initenv_additionalProperties"></a>
<a id="ADDED_fields_initenv_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

<a id="headingADDED_fields_inituser"></a>
<a id="ADDED_fields_inituser"></a>
##### inituser

- Schema name: `Inituser`
- Default: null

"init" process username.
<a id="ADDED_fields_inituser_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_inituser_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_inituser_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_inituser_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_inituser_anyOf_i1)

- Type: null

<a id="headingADDED_fields_initgroup"></a>
<a id="ADDED_fields_initgroup"></a>
##### initgroup

- Schema name: `Initgroup`
- Default: null

"init" process group.
<a id="ADDED_fields_initgroup_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_initgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_initgroup_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_initgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_initgroup_anyOf_i1)

- Type: null

<a id="headingADDED_fields_idmap"></a>
<a id="ADDED_fields_idmap"></a>
##### idmap

- Schema name: `Idmap`
- Default: {"type": "DEFAULT"}

Idmap configuration for the container There are three two possible values: DEFAULT: This applies the standard TrueNAS idmap namespace configuration. It changes user ID (UID) 0 (root) in the container to UID 2147000001 (truenas*container*unpriv_root). It offsets the other container UIDs by the same amount. For example, UID 1000 in the container becomes UID 2147001001 in the host. ISOLATED: Same as `DEFAULT`, but UID will be calculated as `2147000001 + 65536 * slice`. This will ensure unique ID for each container (provided that the `slice` is also unique). None: The container does not apply any idmap namespace. Container UIDs map directly to host UIDs. For example, UID 0 in the container is UID 0 in the host. WARNING: For security, use the DEFAULT value. Security best practice is to run containers with idmap namespaces.
<a id="ADDED_fields_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_idmap_anyOf_i0)

<a id="ADDED_fields_idmap_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_ADDED_fields_idmap_anyOf_i0_oneOf_i0"></a>
###### [DefaultIdmapConfiguration](#tab-pane_ADDED_fields_idmap_anyOf_i0_oneOf_i0)

- Schema name: `DefaultIdmapConfiguration`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_idmap_anyOf_i0_oneOf_i0_type"></a>
<a id="ADDED_fields_idmap_anyOf_i0_oneOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Configuration type for default ID mapping.
- Specific value: `"DEFAULT"`

<a id="tab-pane_ADDED_fields_idmap_anyOf_i0_oneOf_i1"></a>
###### [IsolatedIdmapConfiguration](#tab-pane_ADDED_fields_idmap_anyOf_i0_oneOf_i1)

- Schema name: `IsolatedIdmapConfiguration`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_idmap_anyOf_i0_oneOf_i1_type"></a>
<a id="ADDED_fields_idmap_anyOf_i0_oneOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Configuration type for isolated ID mapping.
- Specific value: `"ISOLATED"`

<a id="headingADDED_fields_idmap_anyOf_i0_oneOf_i1_slice"></a>
<a id="ADDED_fields_idmap_anyOf_i0_oneOf_i1_slice"></a>
###### slice (required)

- Schema name: `Slice`

`null` when creating means we'll look up an unused slice on backend.
<a id="ADDED_fields_idmap_anyOf_i0_oneOf_i1_slice_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0` and strictly lesser than `1000`

<a id="tab-pane_ADDED_fields_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_idmap_anyOf_i1)

- Type: null

<a id="headingADDED_fields_capabilities_policy"></a>
<a id="ADDED_fields_capabilities_policy"></a>
##### capabilities_policy

- Schema name: `Capabilities Policy`
- Type: enum (of string)
- Default: "DEFAULT"

Default rules for capabilities: either keep the default behavior that is dropping the following capabilities: sys*module, sys*time, mknod, audit*control, mac*admin. Or keep all capabilities, or drop all capabilities.
###### Must be one of:

- "DEFAULT"
- "ALLOW"
- "DENY"

<a id="headingADDED_fields_capabilities_state"></a>
<a id="ADDED_fields_capabilities_state"></a>
##### capabilities_state

- Schema name: `Capabilities State`
- Type: object
- Default: {}

Enable or disable specific capabilities.
<a id="headingADDED_fields_capabilities_state_additionalProperties"></a>
<a id="ADDED_fields_capabilities_state_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: boolean

<a id="headingADDED_fields_default_network"></a>
<a id="ADDED_fields_default_network"></a>
##### default_network

- Schema name: `Default Network`
- Default: null

The default network bridge this container will use when no NIC devices are explicitly attached. When the container has explicitly configured NIC devices, this is `null` because the NIC configuration is visible in the `devices` list.
<a id="ADDED_fields_default_network_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_default_network_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_default_network_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_default_network_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_default_network_anyOf_i1)

- Type: null

<a id="headingADDED_fields_status"></a>
<a id="ADDED_fields_status"></a>
##### status (required)

- Schema name: `ContainerStatus`
- Type: object

Container state.
- No Additional Properties
<a id="headingADDED_fields_status_state"></a>
<a id="ADDED_fields_status_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Container state.
###### Must be one of:

- "RUNNING"
- "STOPPED"
- "SUSPENDED"

<a id="headingADDED_fields_status_pid"></a>
<a id="ADDED_fields_status_pid"></a>
###### pid (required)

- Schema name: `Pid`

Container host PID (if running). Informational only do not rely on this value to identify the container's init process.
<a id="ADDED_fields_status_pid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_status_pid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_status_pid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_status_pid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_status_pid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_status_domain_state"></a>
<a id="ADDED_fields_status_domain_state"></a>
###### domain_state (required)

- Schema name: `Domain State`

Domain state reported by libvirt.
<a id="ADDED_fields_status_domain_state_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_status_domain_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_status_domain_state_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_status_domain_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_status_domain_state_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `ContainerChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `ContainerEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Container ID.

<a id="headingCHANGED_fields_uuid"></a>
<a id="CHANGED_fields_uuid"></a>
##### uuid (required)

- Schema name: `Uuid`
- Type: string

Container UUID (for libvirt).

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Container name.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Container description.

<a id="headingCHANGED_fields_devices"></a>
<a id="CHANGED_fields_devices"></a>
##### devices

- Schema name: `Devices`
- Type: array of object
- Default: []

Container's devices.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_devices_items"></a>
###### ContainerDeviceEntry

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_id"></a>
<a id="CHANGED_fields_devices_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

<a id="headingCHANGED_fields_devices_items_attributes"></a>
<a id="CHANGED_fields_devices_items_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="CHANGED_fields_devices_items_attributes_oneOf"></a>
###### One of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i0"></a>
###### [ContainerFilesystemDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i0)

- Schema name: `ContainerFilesystemDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i0_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for FILESYSTEM devices.
- Specific value: `"FILESYSTEM"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i0_target"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i0_target"></a>
###### target (required)

- Schema name: `Target`
- Type: string

Path inside the container to mount the source at. Must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i0_source"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

Host path to bind-mount into the container. Must reside within a pool (under `/mnt`) and must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1"></a>
###### [ContainerGPUDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1)

- Schema name: `ContainerGPUDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for GPU devices.
- Specific value: `"GPU"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_gpu_type"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_gpu_type"></a>
###### gpu_type (required)

- Schema name: `Gpu Type`
- Type: enum (of string)

GPU device type.
###### Must be one of:

- "AMD"
- "INTEL"
- "NVIDIA"

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_pci_address"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_pci_address"></a>
###### pci_address (required)

- Schema name: `Pci Address`
- Type: string

PCI address of the GPU device on the host system.
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2"></a>
###### [ContainerNICDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2)

- Schema name: `ContainerNICDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_type"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_nic_attach"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_mac"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3"></a>
###### [ContainerUSBDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3)

- Schema name: `ContainerUSBDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_usb"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_usb_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_usb_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_device"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_device_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_device_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_container"></a>
<a id="CHANGED_fields_devices_items_container"></a>
###### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

<a id="headingCHANGED_fields_cpuset"></a>
<a id="CHANGED_fields_cpuset"></a>
##### cpuset

- Schema name: `Cpuset`
- Default: null

List of physical CPU numbers that domain process and virtual CPUs can be pinned to by default.
<a id="CHANGED_fields_cpuset_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_cpuset_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_cpuset_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_cpuset_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_cpuset_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_autostart"></a>
<a id="CHANGED_fields_autostart"></a>
##### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Automatically start the container on boot.

<a id="headingCHANGED_fields_time"></a>
<a id="CHANGED_fields_time"></a>
##### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Whether container time should be local time or UTC time.
###### Must be one of:

- "LOCAL"
- "UTC"

<a id="headingCHANGED_fields_shutdown_timeout"></a>
<a id="CHANGED_fields_shutdown_timeout"></a>
##### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

How many seconds to wait for container to shut down before killing it.
- Value must be greater or equal to `5` and lesser or equal to `300`

<a id="headingCHANGED_fields_dataset"></a>
<a id="CHANGED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

Which dataset to use as the container root filesystem.

<a id="headingCHANGED_fields_init"></a>
<a id="CHANGED_fields_init"></a>
##### init

- Schema name: `Init`
- Type: string
- Default: "/sbin/init"

"init" process commandline.

<a id="headingCHANGED_fields_initdir"></a>
<a id="CHANGED_fields_initdir"></a>
##### initdir

- Schema name: `Initdir`
- Default: null

"init" process working dir.
<a id="CHANGED_fields_initdir_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_initdir_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_initdir_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_initdir_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_initdir_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_initenv"></a>
<a id="CHANGED_fields_initenv"></a>
##### initenv

- Schema name: `Initenv`
- Type: object
- Default: {}

"init" process environment variables.
<a id="headingCHANGED_fields_initenv_additionalProperties"></a>
<a id="CHANGED_fields_initenv_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

<a id="headingCHANGED_fields_inituser"></a>
<a id="CHANGED_fields_inituser"></a>
##### inituser

- Schema name: `Inituser`
- Default: null

"init" process username.
<a id="CHANGED_fields_inituser_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_inituser_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_inituser_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_inituser_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_inituser_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_initgroup"></a>
<a id="CHANGED_fields_initgroup"></a>
##### initgroup

- Schema name: `Initgroup`
- Default: null

"init" process group.
<a id="CHANGED_fields_initgroup_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_initgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_initgroup_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_initgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_initgroup_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_idmap"></a>
<a id="CHANGED_fields_idmap"></a>
##### idmap

- Schema name: `Idmap`
- Default: {"type": "DEFAULT"}

Idmap configuration for the container There are three two possible values: DEFAULT: This applies the standard TrueNAS idmap namespace configuration. It changes user ID (UID) 0 (root) in the container to UID 2147000001 (truenas*container*unpriv_root). It offsets the other container UIDs by the same amount. For example, UID 1000 in the container becomes UID 2147001001 in the host. ISOLATED: Same as `DEFAULT`, but UID will be calculated as `2147000001 + 65536 * slice`. This will ensure unique ID for each container (provided that the `slice` is also unique). None: The container does not apply any idmap namespace. Container UIDs map directly to host UIDs. For example, UID 0 in the container is UID 0 in the host. WARNING: For security, use the DEFAULT value. Security best practice is to run containers with idmap namespaces.
<a id="CHANGED_fields_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_idmap_anyOf_i0)

<a id="CHANGED_fields_idmap_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_CHANGED_fields_idmap_anyOf_i0_oneOf_i0"></a>
###### [DefaultIdmapConfiguration](#tab-pane_CHANGED_fields_idmap_anyOf_i0_oneOf_i0)

- Schema name: `DefaultIdmapConfiguration`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_idmap_anyOf_i0_oneOf_i0_type"></a>
<a id="CHANGED_fields_idmap_anyOf_i0_oneOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Configuration type for default ID mapping.
- Specific value: `"DEFAULT"`

<a id="tab-pane_CHANGED_fields_idmap_anyOf_i0_oneOf_i1"></a>
###### [IsolatedIdmapConfiguration](#tab-pane_CHANGED_fields_idmap_anyOf_i0_oneOf_i1)

- Schema name: `IsolatedIdmapConfiguration`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_idmap_anyOf_i0_oneOf_i1_type"></a>
<a id="CHANGED_fields_idmap_anyOf_i0_oneOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Configuration type for isolated ID mapping.
- Specific value: `"ISOLATED"`

<a id="headingCHANGED_fields_idmap_anyOf_i0_oneOf_i1_slice"></a>
<a id="CHANGED_fields_idmap_anyOf_i0_oneOf_i1_slice"></a>
###### slice (required)

- Schema name: `Slice`

`null` when creating means we'll look up an unused slice on backend.
<a id="CHANGED_fields_idmap_anyOf_i0_oneOf_i1_slice_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0` and strictly lesser than `1000`

<a id="tab-pane_CHANGED_fields_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_idmap_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_capabilities_policy"></a>
<a id="CHANGED_fields_capabilities_policy"></a>
##### capabilities_policy

- Schema name: `Capabilities Policy`
- Type: enum (of string)
- Default: "DEFAULT"

Default rules for capabilities: either keep the default behavior that is dropping the following capabilities: sys*module, sys*time, mknod, audit*control, mac*admin. Or keep all capabilities, or drop all capabilities.
###### Must be one of:

- "DEFAULT"
- "ALLOW"
- "DENY"

<a id="headingCHANGED_fields_capabilities_state"></a>
<a id="CHANGED_fields_capabilities_state"></a>
##### capabilities_state

- Schema name: `Capabilities State`
- Type: object
- Default: {}

Enable or disable specific capabilities.
<a id="headingCHANGED_fields_capabilities_state_additionalProperties"></a>
<a id="CHANGED_fields_capabilities_state_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: boolean

<a id="headingCHANGED_fields_default_network"></a>
<a id="CHANGED_fields_default_network"></a>
##### default_network

- Schema name: `Default Network`
- Default: null

The default network bridge this container will use when no NIC devices are explicitly attached. When the container has explicitly configured NIC devices, this is `null` because the NIC configuration is visible in the `devices` list.
<a id="CHANGED_fields_default_network_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_default_network_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_default_network_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_default_network_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_default_network_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_status"></a>
<a id="CHANGED_fields_status"></a>
##### status (required)

- Schema name: `ContainerStatus`
- Type: object

Container state.
- No Additional Properties
<a id="headingCHANGED_fields_status_state"></a>
<a id="CHANGED_fields_status_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Container state.
###### Must be one of:

- "RUNNING"
- "STOPPED"
- "SUSPENDED"

<a id="headingCHANGED_fields_status_pid"></a>
<a id="CHANGED_fields_status_pid"></a>
###### pid (required)

- Schema name: `Pid`

Container host PID (if running). Informational only do not rely on this value to identify the container's init process.
<a id="CHANGED_fields_status_pid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_pid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_status_pid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_status_pid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_pid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_status_domain_state"></a>
<a id="CHANGED_fields_status_domain_state"></a>
###### domain_state (required)

- Schema name: `Domain State`

Domain state reported by libvirt.
<a id="CHANGED_fields_status_domain_state_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_domain_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_status_domain_state_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_status_domain_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_domain_state_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `ContainerRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
