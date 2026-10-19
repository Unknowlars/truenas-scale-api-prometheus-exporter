---
title: disk.get_instance
kind: method
source_rst: _sources/api_methods_disk.get_instance.rst.txt
source_html: api_methods_disk.get_instance.html
required_roles:
  - DISK_READ
---

# disk.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `DISK_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: string

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
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

- Schema name: `DiskEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_identifier"></a>
<a id="Return_value_identifier"></a>
#### identifier (required)

- Schema name: `Identifier`
- Type: string

Unique identifier for the disk device.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

System name of the disk device.

<a id="headingReturn_value_subsystem"></a>
<a id="Return_value_subsystem"></a>
#### subsystem (required)

- Schema name: `Subsystem`
- Type: string

Storage subsystem type.
Examples:

```json
"SCSI"
```
Examples:

```json
"ATA"
```

<a id="headingReturn_value_number"></a>
<a id="Return_value_number"></a>
#### number (required)

- Schema name: `Number`
- Type: integer

Numeric identifier assigned to the disk.

<a id="headingReturn_value_serial"></a>
<a id="Return_value_serial"></a>
#### serial (required)

- Schema name: `Serial`
- Type: string

Manufacturer serial number of the disk.

<a id="headingReturn_value_lunid"></a>
<a id="Return_value_lunid"></a>
#### lunid (required)

- Schema name: `Lunid`

Logical unit number identifier or `null` if not applicable.
<a id="Return_value_lunid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_lunid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_lunid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_lunid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_lunid_anyOf_i1)

- Type: null

<a id="headingReturn_value_size"></a>
<a id="Return_value_size"></a>
#### size (required)

- Schema name: `Size`

Total size of the disk in bytes. `null` if not available.
<a id="Return_value_size_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the disk device.

<a id="headingReturn_value_transfermode"></a>
<a id="Return_value_transfermode"></a>
#### transfermode (required)

- Schema name: `Transfermode`
- Type: string

Data transfer mode and capabilities of the disk.

<a id="headingReturn_value_hddstandby"></a>
<a id="Return_value_hddstandby"></a>
#### hddstandby (required)

- Schema name: `Hddstandby`
- Type: enum (of string)

Hard disk standby timer in minutes or `ALWAYS ON` to disable standby.
##### Must be one of:

- "ALWAYS ON"
- "5"
- "10"
- "20"
- "30"
- "60"
- "120"
- "180"
- "240"
- "300"
- "330"

<a id="headingReturn_value_advpowermgmt"></a>
<a id="Return_value_advpowermgmt"></a>
#### advpowermgmt (required)

- Schema name: `Advpowermgmt`
- Type: enum (of string)

Advanced power management level or `DISABLED` to turn off power management.
##### Must be one of:

- "DISABLED"
- "1"
- "64"
- "127"
- "128"
- "192"
- "254"

<a id="headingReturn_value_expiretime"></a>
<a id="Return_value_expiretime"></a>
#### expiretime (required)

- Schema name: `Expiretime`

Expiration timestamp for disk data or `null` if not applicable.
<a id="Return_value_expiretime_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_expiretime_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_expiretime_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_expiretime_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_expiretime_anyOf_i1)

- Type: null

<a id="headingReturn_value_model"></a>
<a id="Return_value_model"></a>
#### model (required)

- Schema name: `Model`

Manufacturer model name/number of the disk. `null` if not available.
<a id="Return_value_model_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_model_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_model_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_model_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_model_anyOf_i1)

- Type: null

<a id="headingReturn_value_rotationrate"></a>
<a id="Return_value_rotationrate"></a>
#### rotationrate (required)

- Schema name: `Rotationrate`

Disk rotation speed in RPM or `null` for SSDs and unknown devices.
<a id="Return_value_rotationrate_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_rotationrate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_rotationrate_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_rotationrate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_rotationrate_anyOf_i1)

- Type: null

<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type (required)

- Schema name: `Type`

Disk type classification or `null` if not determined.
<a id="Return_value_type_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_type_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_zfs_guid"></a>
<a id="Return_value_zfs_guid"></a>
#### zfs_guid (required)

- Schema name: `Zfs Guid`

ZFS globally unique identifier for this disk or `null` if not used in ZFS.
<a id="Return_value_zfs_guid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_zfs_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_zfs_guid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_zfs_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_zfs_guid_anyOf_i1)

- Type: null

<a id="headingReturn_value_bus"></a>
<a id="Return_value_bus"></a>
#### bus (required)

- Schema name: `Bus`
- Type: string

System bus type the disk is connected to.

<a id="headingReturn_value_devname"></a>
<a id="Return_value_devname"></a>
#### devname (required)

- Schema name: `Devname`
- Type: string

Device name in the operating system.
Examples:

```json
"/dev/sda"
```

<a id="headingReturn_value_enclosure"></a>
<a id="Return_value_enclosure"></a>
#### enclosure (required)

Physical enclosure information or `null` if not in an enclosure.
<a id="Return_value_enclosure_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_enclosure_anyOf_i0"></a>
###### [DiskEntryEnclosure](#tab-pane_Return_value_enclosure_anyOf_i0)

- Schema name: `DiskEntryEnclosure`
- Type: object
- No Additional Properties
<a id="headingReturn_value_enclosure_anyOf_i0_number"></a>
<a id="Return_value_enclosure_anyOf_i0_number"></a>
###### number (required)

- Schema name: `Number`
- Type: integer

Enclosure number where the disk is located.

<a id="headingReturn_value_enclosure_anyOf_i0_slot"></a>
<a id="Return_value_enclosure_anyOf_i0_slot"></a>
###### slot (required)

- Schema name: `Slot`
- Type: integer

Physical slot position within the enclosure.

<a id="tab-pane_Return_value_enclosure_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_enclosure_anyOf_i1)

- Type: null

<a id="headingReturn_value_pool"></a>
<a id="Return_value_pool"></a>
#### pool (required)

- Schema name: `Pool`

Name of the storage pool this disk belongs to. `null` if not part of any pool.
<a id="Return_value_pool_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_pool_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pool_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_pool_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pool_anyOf_i1)

- Type: null

<a id="headingReturn_value_passwd"></a>
<a id="Return_value_passwd"></a>
#### passwd

- Schema name: `Passwd`
- Type: string

Disk encryption password (masked for security).

<a id="headingReturn_value_kmip_uid"></a>
<a id="Return_value_kmip_uid"></a>
#### kmip_uid

- Schema name: `Kmip Uid`

KMIP (Key Management Interoperability Protocol) unique identifier or `null`.
<a id="Return_value_kmip_uid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_kmip_uid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_kmip_uid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_kmip_uid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_kmip_uid_anyOf_i1)

- Type: null

<a id="headingReturn_value_sed"></a>
<a id="Return_value_sed"></a>
#### sed (required)

- Schema name: `Sed`

Whether the disk is SED (Self-Encrypting Drive) capable. `null` if not yet determined.
<a id="Return_value_sed_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sed_anyOf_i1)

- Type: null

<a id="headingReturn_value_sed_status"></a>
<a id="Return_value_sed_status"></a>
#### sed_status

- Schema name: `Sed Status`

SED Status of the disk. `null` if not yet determined.
<a id="Return_value_sed_status_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_sed_status_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sed_status_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_sed_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sed_status_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
