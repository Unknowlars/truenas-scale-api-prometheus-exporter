---
title: container.query
kind: method
source_rst: _sources/api_methods_container.query.rst.txt
source_html: api_methods_container.query.html
required_roles:
  - CONTAINER_READ
---

# container.query

## Required Roles

- `CONTAINER_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Query options including pagination, ordering, and additional parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### ContainerQueryResultItem

- Schema name: `ContainerQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Container ID.

<a id="headingReturn_value_anyOf_i0_items_uuid"></a>
<a id="Return_value_anyOf_i0_items_uuid"></a>
###### uuid

- Schema name: `Uuid`
- Type: string

Container UUID (for libvirt).

<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Container name.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_description"></a>
<a id="Return_value_anyOf_i0_items_description"></a>
###### description

- Schema name: `Description`
- Type: string

Container description.

<a id="headingReturn_value_anyOf_i0_items_devices"></a>
<a id="Return_value_anyOf_i0_items_devices"></a>
###### devices

- Schema name: `Devices`
- Type: array of object

Container's devices.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_devices_items"></a>
###### ContainerDeviceEntry

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_devices_items_id"></a>
<a id="Return_value_anyOf_i0_items_devices_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i0"></a>
###### [ContainerFilesystemDevice](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i0)

- Schema name: `ContainerFilesystemDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i0_dtype"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for FILESYSTEM devices.
- Specific value: `"FILESYSTEM"`

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i0_target"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i0_target"></a>
###### target (required)

- Schema name: `Target`
- Type: string

Path inside the container to mount the source at. Must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i0_source"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

Host path to bind-mount into the container. Must reside within a pool (under `/mnt`) and must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i1"></a>
###### [ContainerGPUDevice](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i1)

- Schema name: `ContainerGPUDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i1_dtype"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for GPU devices.
- Specific value: `"GPU"`

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i1_gpu_type"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i1_gpu_type"></a>
###### gpu_type (required)

- Schema name: `Gpu Type`
- Type: enum (of string)

GPU device type.
###### Must be one of:

- "AMD"
- "INTEL"
- "NVIDIA"

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i1_pci_address"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i1_pci_address"></a>
###### pci_address (required)

- Schema name: `Pci Address`
- Type: string

PCI address of the GPU device on the host system.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2"></a>
###### [ContainerNICDevice](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2)

- Schema name: `ContainerNICDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_dtype"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_type"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_nic_attach"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_mac"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3"></a>
###### [ContainerUSBDevice](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3)

- Schema name: `ContainerUSBDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_dtype"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_usb_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_device"></a>
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_device_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_devices_items_attributes_oneOf_i3_device_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_devices_items_container"></a>
<a id="Return_value_anyOf_i0_items_devices_items_container"></a>
###### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

<a id="headingReturn_value_anyOf_i0_items_cpuset"></a>
<a id="Return_value_anyOf_i0_items_cpuset"></a>
###### cpuset

- Schema name: `Cpuset`

List of physical CPU numbers that domain process and virtual CPUs can be pinned to by default.
<a id="Return_value_anyOf_i0_items_cpuset_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_cpuset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_cpuset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_cpuset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_cpuset_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_autostart"></a>
<a id="Return_value_anyOf_i0_items_autostart"></a>
###### autostart

- Schema name: `Autostart`
- Type: boolean

Automatically start the container on boot.

<a id="headingReturn_value_anyOf_i0_items_time"></a>
<a id="Return_value_anyOf_i0_items_time"></a>
###### time

- Schema name: `Time`
- Type: enum (of string)

Whether container time should be local time or UTC time.
###### Must be one of:

- "LOCAL"
- "UTC"

<a id="headingReturn_value_anyOf_i0_items_shutdown_timeout"></a>
<a id="Return_value_anyOf_i0_items_shutdown_timeout"></a>
###### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer

How many seconds to wait for container to shut down before killing it.
- Value must be greater or equal to `5` and lesser or equal to `300`

<a id="headingReturn_value_anyOf_i0_items_dataset"></a>
<a id="Return_value_anyOf_i0_items_dataset"></a>
###### dataset

- Schema name: `Dataset`
- Type: string

Which dataset to use as the container root filesystem.

<a id="headingReturn_value_anyOf_i0_items_init"></a>
<a id="Return_value_anyOf_i0_items_init"></a>
###### init

- Schema name: `Init`
- Type: string

"init" process commandline.

<a id="headingReturn_value_anyOf_i0_items_initdir"></a>
<a id="Return_value_anyOf_i0_items_initdir"></a>
###### initdir

- Schema name: `Initdir`

"init" process working dir.
<a id="Return_value_anyOf_i0_items_initdir_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_initdir_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_initdir_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_initdir_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_initdir_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_initenv"></a>
<a id="Return_value_anyOf_i0_items_initenv"></a>
###### initenv

- Schema name: `Initenv`
- Type: object

"init" process environment variables.
<a id="headingReturn_value_anyOf_i0_items_initenv_additionalProperties"></a>
<a id="Return_value_anyOf_i0_items_initenv_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

<a id="headingReturn_value_anyOf_i0_items_inituser"></a>
<a id="Return_value_anyOf_i0_items_inituser"></a>
###### inituser

- Schema name: `Inituser`

"init" process username.
<a id="Return_value_anyOf_i0_items_inituser_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_inituser_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_inituser_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_inituser_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_inituser_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_initgroup"></a>
<a id="Return_value_anyOf_i0_items_initgroup"></a>
###### initgroup

- Schema name: `Initgroup`

"init" process group.
<a id="Return_value_anyOf_i0_items_initgroup_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_initgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_initgroup_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_initgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_initgroup_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_idmap"></a>
<a id="Return_value_anyOf_i0_items_idmap"></a>
###### idmap

- Schema name: `Idmap`

Idmap configuration for the container There are three two possible values: DEFAULT: This applies the standard TrueNAS idmap namespace configuration. It changes user ID (UID) 0 (root) in the container to UID 2147000001 (truenas*container*unpriv_root). It offsets the other container UIDs by the same amount. For example, UID 1000 in the container becomes UID 2147001001 in the host. ISOLATED: Same as `DEFAULT`, but UID will be calculated as `2147000001 + 65536 * slice`. This will ensure unique ID for each container (provided that the `slice` is also unique). None: The container does not apply any idmap namespace. Container UIDs map directly to host UIDs. For example, UID 0 in the container is UID 0 in the host. WARNING: For security, use the DEFAULT value. Security best practice is to run containers with idmap namespaces.
<a id="Return_value_anyOf_i0_items_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i0)

<a id="Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i0"></a>
###### [DefaultIdmapConfiguration](#tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i0)

- Schema name: `DefaultIdmapConfiguration`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i0_type"></a>
<a id="Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Configuration type for default ID mapping.
- Specific value: `"DEFAULT"`

<a id="tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1"></a>
###### [IsolatedIdmapConfiguration](#tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1)

- Schema name: `IsolatedIdmapConfiguration`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1_type"></a>
<a id="Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Configuration type for isolated ID mapping.
- Specific value: `"ISOLATED"`

<a id="headingReturn_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1_slice"></a>
<a id="Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1_slice"></a>
###### slice (required)

- Schema name: `Slice`

`null` when creating means we'll look up an unused slice on backend.
<a id="Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1_slice_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0` and strictly lesser than `1000`

<a id="tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i0_oneOf_i1_slice_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_idmap_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_capabilities_policy"></a>
<a id="Return_value_anyOf_i0_items_capabilities_policy"></a>
###### capabilities_policy

- Schema name: `Capabilities Policy`
- Type: enum (of string)

Default rules for capabilities: either keep the default behavior that is dropping the following capabilities: sys*module, sys*time, mknod, audit*control, mac*admin. Or keep all capabilities, or drop all capabilities.
###### Must be one of:

- "DEFAULT"
- "ALLOW"
- "DENY"

<a id="headingReturn_value_anyOf_i0_items_capabilities_state"></a>
<a id="Return_value_anyOf_i0_items_capabilities_state"></a>
###### capabilities_state

- Schema name: `Capabilities State`
- Type: object

Enable or disable specific capabilities.
<a id="headingReturn_value_anyOf_i0_items_capabilities_state_additionalProperties"></a>
<a id="Return_value_anyOf_i0_items_capabilities_state_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: boolean

<a id="headingReturn_value_anyOf_i0_items_default_network"></a>
<a id="Return_value_anyOf_i0_items_default_network"></a>
###### default_network

- Schema name: `Default Network`

The default network bridge this container will use when no NIC devices are explicitly attached. When the container has explicitly configured NIC devices, this is `null` because the NIC configuration is visible in the `devices` list.
<a id="Return_value_anyOf_i0_items_default_network_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_default_network_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_default_network_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_default_network_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_default_network_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_status"></a>
<a id="Return_value_anyOf_i0_items_status"></a>
###### status

- Schema name: `ContainerStatus`
- Type: object

Container state.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_status_state"></a>
<a id="Return_value_anyOf_i0_items_status_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Container state.
###### Must be one of:

- "RUNNING"
- "STOPPED"
- "SUSPENDED"

<a id="headingReturn_value_anyOf_i0_items_status_pid"></a>
<a id="Return_value_anyOf_i0_items_status_pid"></a>
###### pid (required)

- Schema name: `Pid`

Container host PID (if running). Informational only do not rely on this value to identify the container's init process.
<a id="Return_value_anyOf_i0_items_status_pid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_status_pid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_status_pid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_status_pid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_status_pid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_status_domain_state"></a>
<a id="Return_value_anyOf_i0_items_status_domain_state"></a>
###### domain_state (required)

- Schema name: `Domain State`

Domain state reported by libvirt.
<a id="Return_value_anyOf_i0_items_status_domain_state_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_status_domain_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_status_domain_state_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_status_domain_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_status_domain_state_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [ContainerQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `ContainerQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Container ID.

<a id="headingReturn_value_anyOf_i1_uuid"></a>
<a id="Return_value_anyOf_i1_uuid"></a>
###### uuid

- Schema name: `Uuid`
- Type: string

Container UUID (for libvirt).

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name

- Schema name: `Name`
- Type: string

Container name.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_description"></a>
<a id="Return_value_anyOf_i1_description"></a>
###### description

- Schema name: `Description`
- Type: string

Container description.

<a id="headingReturn_value_anyOf_i1_devices"></a>
<a id="Return_value_anyOf_i1_devices"></a>
###### devices

- Schema name: `Devices`
- Type: array

Container's devices.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_devices_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i1_cpuset"></a>
<a id="Return_value_anyOf_i1_cpuset"></a>
###### cpuset

- Schema name: `Cpuset`

List of physical CPU numbers that domain process and virtual CPUs can be pinned to by default.
<a id="Return_value_anyOf_i1_cpuset_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_cpuset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_cpuset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_cpuset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_cpuset_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_autostart"></a>
<a id="Return_value_anyOf_i1_autostart"></a>
###### autostart

- Schema name: `Autostart`
- Type: boolean

Automatically start the container on boot.

<a id="headingReturn_value_anyOf_i1_time"></a>
<a id="Return_value_anyOf_i1_time"></a>
###### time

- Schema name: `Time`
- Type: enum (of string)

Whether container time should be local time or UTC time.
###### Must be one of:

- "LOCAL"
- "UTC"

<a id="headingReturn_value_anyOf_i1_shutdown_timeout"></a>
<a id="Return_value_anyOf_i1_shutdown_timeout"></a>
###### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer

How many seconds to wait for container to shut down before killing it.
- Value must be greater or equal to `5` and lesser or equal to `300`

<a id="headingReturn_value_anyOf_i1_dataset"></a>
<a id="Return_value_anyOf_i1_dataset"></a>
###### dataset

- Schema name: `Dataset`
- Type: string

Which dataset to use as the container root filesystem.

<a id="headingReturn_value_anyOf_i1_init"></a>
<a id="Return_value_anyOf_i1_init"></a>
###### init

- Schema name: `Init`
- Type: string

"init" process commandline.

<a id="headingReturn_value_anyOf_i1_initdir"></a>
<a id="Return_value_anyOf_i1_initdir"></a>
###### initdir

- Schema name: `Initdir`

"init" process working dir.
<a id="Return_value_anyOf_i1_initdir_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_initdir_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_initdir_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_initdir_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_initdir_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_initenv"></a>
<a id="Return_value_anyOf_i1_initenv"></a>
###### initenv

- Schema name: `Initenv`
- Type: object

"init" process environment variables.
<a id="headingReturn_value_anyOf_i1_initenv_additionalProperties"></a>
<a id="Return_value_anyOf_i1_initenv_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

<a id="headingReturn_value_anyOf_i1_inituser"></a>
<a id="Return_value_anyOf_i1_inituser"></a>
###### inituser

- Schema name: `Inituser`

"init" process username.
<a id="Return_value_anyOf_i1_inituser_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_inituser_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_inituser_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_inituser_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_inituser_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_initgroup"></a>
<a id="Return_value_anyOf_i1_initgroup"></a>
###### initgroup

- Schema name: `Initgroup`

"init" process group.
<a id="Return_value_anyOf_i1_initgroup_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_initgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_initgroup_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_initgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_initgroup_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_idmap"></a>
<a id="Return_value_anyOf_i1_idmap"></a>
###### idmap

- Schema name: `Idmap`

Idmap configuration for the container There are three two possible values: DEFAULT: This applies the standard TrueNAS idmap namespace configuration. It changes user ID (UID) 0 (root) in the container to UID 2147000001 (truenas*container*unpriv_root). It offsets the other container UIDs by the same amount. For example, UID 1000 in the container becomes UID 2147001001 in the host. ISOLATED: Same as `DEFAULT`, but UID will be calculated as `2147000001 + 65536 * slice`. This will ensure unique ID for each container (provided that the `slice` is also unique). None: The container does not apply any idmap namespace. Container UIDs map directly to host UIDs. For example, UID 0 in the container is UID 0 in the host. WARNING: For security, use the DEFAULT value. Security best practice is to run containers with idmap namespaces.
<a id="Return_value_anyOf_i1_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_idmap_anyOf_i0)

<a id="Return_value_anyOf_i1_idmap_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i1_idmap_anyOf_i0_oneOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_idmap_anyOf_i0_oneOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_idmap_anyOf_i0_oneOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_idmap_anyOf_i0_oneOf_i1)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_idmap_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_capabilities_policy"></a>
<a id="Return_value_anyOf_i1_capabilities_policy"></a>
###### capabilities_policy

- Schema name: `Capabilities Policy`
- Type: enum (of string)

Default rules for capabilities: either keep the default behavior that is dropping the following capabilities: sys*module, sys*time, mknod, audit*control, mac*admin. Or keep all capabilities, or drop all capabilities.
###### Must be one of:

- "DEFAULT"
- "ALLOW"
- "DENY"

<a id="headingReturn_value_anyOf_i1_capabilities_state"></a>
<a id="Return_value_anyOf_i1_capabilities_state"></a>
###### capabilities_state

- Schema name: `Capabilities State`
- Type: object

Enable or disable specific capabilities.
<a id="headingReturn_value_anyOf_i1_capabilities_state_additionalProperties"></a>
<a id="Return_value_anyOf_i1_capabilities_state_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: boolean

<a id="headingReturn_value_anyOf_i1_default_network"></a>
<a id="Return_value_anyOf_i1_default_network"></a>
###### default_network

- Schema name: `Default Network`

The default network bridge this container will use when no NIC devices are explicitly attached. When the container has explicitly configured NIC devices, this is `null` because the NIC configuration is visible in the `devices` list.
<a id="Return_value_anyOf_i1_default_network_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_default_network_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_default_network_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_default_network_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_default_network_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_status"></a>
<a id="Return_value_anyOf_i1_status"></a>
###### status

- Type: object

Container state.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
