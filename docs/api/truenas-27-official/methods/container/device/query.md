---
title: container.device.query
kind: method
source_rst: _sources/api_methods_container.device.query.rst.txt
source_html: api_methods_container.device.query.html
required_roles:
  - CONTAINER_DEVICE_READ
---

# container.device.query

## Required Roles

- `CONTAINER_DEVICE_READ`

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
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

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
###### ContainerDeviceEntry

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

<a id="headingReturn_value_anyOf_i0_items_attributes"></a>
<a id="Return_value_anyOf_i0_items_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="Return_value_anyOf_i0_items_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0"></a>
###### [ContainerFilesystemDevice](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i0)

- Schema name: `ContainerFilesystemDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i0_dtype"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for FILESYSTEM devices.
- Specific value: `"FILESYSTEM"`

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i0_target"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i0_target"></a>
###### target (required)

- Schema name: `Target`
- Type: string

Path inside the container to mount the source at. Must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i0_source"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

Host path to bind-mount into the container. Must reside within a pool (under `/mnt`) and must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i1"></a>
###### [ContainerGPUDevice](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i1)

- Schema name: `ContainerGPUDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i1_dtype"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for GPU devices.
- Specific value: `"GPU"`

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i1_gpu_type"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i1_gpu_type"></a>
###### gpu_type (required)

- Schema name: `Gpu Type`
- Type: enum (of string)

GPU device type.
###### Must be one of:

- "AMD"
- "INTEL"
- "NVIDIA"

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i1_pci_address"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i1_pci_address"></a>
###### pci_address (required)

- Schema name: `Pci Address`
- Type: string

PCI address of the GPU device on the host system.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2"></a>
###### [ContainerNICDevice](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2)

- Schema name: `ContainerNICDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i2_dtype"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i2_type"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i2_nic_attach"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i2_mac"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3"></a>
###### [ContainerUSBDevice](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3)

- Schema name: `ContainerUSBDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i3_dtype"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i3_usb"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i3_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i3_usb_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i3_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i3_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3_usb_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_attributes_oneOf_i3_device"></a>
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i3_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="Return_value_anyOf_i0_items_attributes_oneOf_i3_device_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_attributes_oneOf_i3_device_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_container"></a>
<a id="Return_value_anyOf_i0_items_container"></a>
###### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [ContainerDeviceEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

<a id="headingReturn_value_anyOf_i1_attributes"></a>
<a id="Return_value_anyOf_i1_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="Return_value_anyOf_i1_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i1_attributes_oneOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_attributes_oneOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_attributes_oneOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_attributes_oneOf_i1)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_attributes_oneOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i1_attributes_oneOf_i2)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_attributes_oneOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_anyOf_i1_attributes_oneOf_i3)

- Type: object

<a id="headingReturn_value_anyOf_i1_container"></a>
<a id="Return_value_anyOf_i1_container"></a>
###### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### ContainerDeviceQueryResultItem

- Schema name: `ContainerDeviceQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

<a id="headingReturn_value_anyOf_i2_items_attributes"></a>
<a id="Return_value_anyOf_i2_items_attributes"></a>
###### attributes

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="Return_value_anyOf_i2_items_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i0"></a>
###### [ContainerFilesystemDevice](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i0)

- Schema name: `ContainerFilesystemDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i0_dtype"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for FILESYSTEM devices.
- Specific value: `"FILESYSTEM"`

<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i0_target"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i0_target"></a>
###### target (required)

- Schema name: `Target`
- Type: string

Path inside the container to mount the source at. Must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i0_source"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

Host path to bind-mount into the container. Must reside within a pool (under `/mnt`) and must not contain braces.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i1"></a>
###### [ContainerGPUDevice](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i1)

- Schema name: `ContainerGPUDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i1_dtype"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for GPU devices.
- Specific value: `"GPU"`

<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i1_gpu_type"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i1_gpu_type"></a>
###### gpu_type (required)

- Schema name: `Gpu Type`
- Type: enum (of string)

GPU device type.
###### Must be one of:

- "AMD"
- "INTEL"
- "NVIDIA"

<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i1_pci_address"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i1_pci_address"></a>
###### pci_address (required)

- Schema name: `Pci Address`
- Type: string

PCI address of the GPU device on the host system.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i2"></a>
###### [ContainerNICDevice](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i2)

- Schema name: `ContainerNICDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i2_dtype"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i2_type"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i2_nic_attach"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i2_mac"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i3"></a>
###### [ContainerUSBDevice](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i3)

- Schema name: `ContainerUSBDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i3_dtype"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i3_usb"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i3_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i3_usb_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i3_usb_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i3_usb_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i3_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i3_usb_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_attributes_oneOf_i3_device"></a>
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i3_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="Return_value_anyOf_i2_items_attributes_oneOf_i3_device_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i3_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i3_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i3_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_attributes_oneOf_i3_device_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_container"></a>
<a id="Return_value_anyOf_i2_items_container"></a>
###### container

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [ContainerDeviceQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `ContainerDeviceQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

<a id="headingReturn_value_anyOf_i3_attributes"></a>
<a id="Return_value_anyOf_i3_attributes"></a>
###### attributes

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="Return_value_anyOf_i3_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i3_attributes_oneOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_attributes_oneOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_attributes_oneOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_attributes_oneOf_i1)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_attributes_oneOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i3_attributes_oneOf_i2)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_attributes_oneOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_anyOf_i3_attributes_oneOf_i3)

- Type: object

<a id="headingReturn_value_anyOf_i3_container"></a>
<a id="Return_value_anyOf_i3_container"></a>
###### container

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
