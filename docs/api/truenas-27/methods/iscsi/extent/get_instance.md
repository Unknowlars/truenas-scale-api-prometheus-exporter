---
title: iscsi.extent.get_instance
kind: method
source_rst: _sources/api_methods_iscsi.extent.get_instance.rst.txt
source_html: api_methods_iscsi.extent.get_instance.html
required_roles:
  - SHARING_ISCSI_EXTENT_READ
---

# iscsi.extent.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `SHARING_ISCSI_EXTENT_READ`

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
- Type: integer

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

- Schema name: `iSCSITargetExtentEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI extent.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI extent.
- Must be at least `1` characters long
- Must be at most `64` characters long

<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "DISK"

Type of the extent storage backend.
##### Must be one of:

- "DISK"
- "FILE"

<a id="headingReturn_value_disk"></a>
<a id="Return_value_disk"></a>
#### disk

- Schema name: `Disk`
- Default: null

Disk device to use for the extent or `null` if using a file.
<a id="Return_value_disk_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_disk_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_disk_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_disk_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_disk_anyOf_i1)

- Type: null

<a id="headingReturn_value_serial"></a>
<a id="Return_value_serial"></a>
#### serial

- Schema name: `Serial`
- Default: null

Serial number for the extent or `null` to auto-generate.
<a id="Return_value_serial_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_serial_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_serial_anyOf_i1)

- Type: null

<a id="headingReturn_value_path"></a>
<a id="Return_value_path"></a>
#### path

- Schema name: `Path`
- Default: null

File path for file-based extents or `null` if using a disk.
<a id="Return_value_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing the file-based extent (e.g., 'tank/iscsi'). Returns `null` for non-FILE extent types (DISK, ZVOL) or if the FILE path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "path".
<a id="Return_value_dataset_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_relative_path"></a>
<a id="Return_value_relative_path"></a>
#### relative_path (required)

- Schema name: `Relative Path`

The path of the file-based extent relative to the dataset mountpoint (e.g., 'extents/lun0.img'). An empty string indicates the file is at the dataset root. Returns `null` for non-FILE types or if the path cannot be resolved yet. This is a read-only field automatically populated from "path".
<a id="Return_value_relative_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_filesize"></a>
<a id="Return_value_filesize"></a>
#### filesize

- Schema name: `Filesize`
- Default: "0"

Size of the file-based extent in bytes.
<a id="Return_value_filesize_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_filesize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_filesize_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_filesize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_filesize_anyOf_i1)

- Type: integer

<a id="headingReturn_value_blocksize"></a>
<a id="Return_value_blocksize"></a>
#### blocksize

- Schema name: `Blocksize`
- Type: enum (of integer)
- Default: 512

Block size for the extent in bytes.
##### Must be one of:

- 512
- 1024
- 2048
- 4096

<a id="headingReturn_value_pblocksize"></a>
<a id="Return_value_pblocksize"></a>
#### pblocksize

- Schema name: `Pblocksize`
- Type: boolean
- Default: false

Whether to use physical block size reporting.

<a id="headingReturn_value_avail_threshold"></a>
<a id="Return_value_avail_threshold"></a>
#### avail_threshold

- Schema name: `Avail Threshold`
- Default: null

Available space threshold percentage or `null` to disable.
<a id="Return_value_avail_threshold_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_avail_threshold_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_avail_threshold_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `99`

<a id="tab-pane_Return_value_avail_threshold_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_avail_threshold_anyOf_i1)

- Type: null

<a id="headingReturn_value_comment"></a>
<a id="Return_value_comment"></a>
#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the extent.

<a id="headingReturn_value_naa"></a>
<a id="Return_value_naa"></a>
#### naa (required)

- Schema name: `Naa`
- Type: string

Network Address Authority (NAA) identifier for the extent.
- Must be at most `34` characters long

<a id="headingReturn_value_insecure_tpc"></a>
<a id="Return_value_insecure_tpc"></a>
#### insecure_tpc

- Schema name: `Insecure Tpc`
- Type: boolean
- Default: true

Whether to enable insecure Third Party Copy (TPC) operations.

<a id="headingReturn_value_xen"></a>
<a id="Return_value_xen"></a>
#### xen

- Schema name: `Xen`
- Type: boolean
- Default: false

Whether to enable Xen compatibility mode.

<a id="headingReturn_value_rpm"></a>
<a id="Return_value_rpm"></a>
#### rpm

- Schema name: `Rpm`
- Type: enum (of string)
- Default: "SSD"

Reported RPM type for the extent.
##### Must be one of:

- "UNKNOWN"
- "SSD"
- "5400"
- "7200"
- "10000"
- "15000"

<a id="headingReturn_value_ro"></a>
<a id="Return_value_ro"></a>
#### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Whether the extent is read-only.

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extent is enabled and available for use.

<a id="headingReturn_value_vendor"></a>
<a id="Return_value_vendor"></a>
#### vendor (required)

- Schema name: `Vendor`
- Type: string

Vendor string reported by the extent.

<a id="headingReturn_value_product_id"></a>
<a id="Return_value_product_id"></a>
#### product_id

- Schema name: `Product Id`
- Default: null

Product ID string for the extent or `null` for default.
<a id="Return_value_product_id_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_product_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_product_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long
- Must be at most `16` characters long

<a id="tab-pane_Return_value_product_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_product_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_locked"></a>
<a id="Return_value_locked"></a>
#### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the iscsi extent is located on a locked dataset. `true`: The extent is in a locked dataset. `false`: The extent is not in a locked dataset. `null`: Lock status is not available because path locking information was not requested.
<a id="Return_value_locked_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_locked_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
