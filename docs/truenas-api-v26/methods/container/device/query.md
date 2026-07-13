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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

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
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### ContainerDeviceEntry

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
####### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

####### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

####### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

##### ContainerDeviceEntry

- Schema name: `ContainerFilesystemDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for FILESYSTEM devices.

###### target (required)

- Schema name: `Target`
- Type: string

Target must not contain braces.
- Must be at least `1` characters long

###### source (required)

- Schema name: `Source`
- Type: string

Source must not contain braces, and not start with /mnt/.
- Must be at least `1` characters long

##### Option 3

- Schema name: `ContainerGPUDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for GPU devices.

###### gpu_type (required)

- Schema name: `Gpu Type`
- Type: enum (of string)

GPU device type.

###### pci_address (required)

- Schema name: `Pci Address`
- Type: string

PCI address of the GPU device on the host system.
- Must be at least `1` characters long

##### Option 4

- Schema name: `ContainerNICDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.

###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.

###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### Option 5

- Type: string

##### ContainerFilesystemDevice

- Type: null

##### ContainerGPUDevice

- Type: string

##### ContainerNICDevice

- Type: null

##### ContainerUSBDevice

- Schema name: `ContainerUSBDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.

###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
####### Any of

######## USBAttributes

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
######### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must be at least `1` characters long

######### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must be at least `1` characters long

######## Option 2

- Type: null

###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

##### Option 1

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must be at least `1` characters long

###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### USBAttributes

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

###### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

##### Option 2

- Type: object

##### Option 1

- Type: object

##### Option 2

- Type: object

##### Option 1

- Type: object

##### Option 2

- Type: array of object
- No Additional Items

###### Each item of this array must be:

- Type: object

##### Option 3

- Type: object

##### Option 4

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
