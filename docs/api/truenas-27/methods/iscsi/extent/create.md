---
title: iscsi.extent.create
kind: method
source_rst: _sources/api_methods_iscsi.extent.create.rst.txt
source_html: api_methods_iscsi.extent.create.html
required_roles:
  - SHARING_ISCSI_EXTENT_WRITE
---

# iscsi.extent.create

## Summary

Create an iSCSI Extent.

When `type` is set to FILE, attribute `filesize` is used and it represents number of bytes. `filesize` if not zero should be a multiple of `blocksize`. `path` is a required attribute with `type` set as FILE.

With `type` being set to DISK, a valid ZFS volume is required.

`insecure_tpc` when enabled allows an initiator to bypass normal access control and access any scannable target. This allows xcopy operations otherwise blocked by access control.

`xen` is a boolean value which is set to true if Xen is being used as the iSCSI initiator.

`ro` when set to true prevents the initiator from writing to this LUN.

## Required Roles

- `SHARING_ISCSI_EXTENT_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: iscsi_extent_create

<a id="Call_parameters_items_i0"></a>
#### iscsi_extent_create

- Schema name: `iscsi_extent_create`
- Type: object

iSCSI extent configuration data for creation.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI extent.
- Must be at least `1` characters long
- Must be at most `64` characters long

<a id="headingCall_parameters_items_i0_type"></a>
<a id="Call_parameters_items_i0_type"></a>
##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "DISK"

Type of the extent storage backend.
###### Must be one of:

- "DISK"
- "FILE"

<a id="headingCall_parameters_items_i0_disk"></a>
<a id="Call_parameters_items_i0_disk"></a>
##### disk

- Schema name: `Disk`
- Default: null

Disk device to use for the extent or `null` if using a file.
<a id="Call_parameters_items_i0_disk_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_disk_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_disk_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_disk_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_disk_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_serial"></a>
<a id="Call_parameters_items_i0_serial"></a>
##### serial

- Schema name: `Serial`
- Default: null

Serial number for the extent or `null` to auto-generate.
<a id="Call_parameters_items_i0_serial_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_serial_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_serial_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path

- Schema name: `Path`
- Default: null

File path for file-based extents or `null` if using a disk.
<a id="Call_parameters_items_i0_path_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_path_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_path_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_filesize"></a>
<a id="Call_parameters_items_i0_filesize"></a>
##### filesize

- Schema name: `Filesize`
- Default: "0"

Size of the file-based extent in bytes.
<a id="Call_parameters_items_i0_filesize_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_filesize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_filesize_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_filesize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_filesize_anyOf_i1)

- Type: integer

<a id="headingCall_parameters_items_i0_blocksize"></a>
<a id="Call_parameters_items_i0_blocksize"></a>
##### blocksize

- Schema name: `Blocksize`
- Type: enum (of integer)
- Default: 512

Block size for the extent in bytes.
###### Must be one of:

- 512
- 1024
- 2048
- 4096

<a id="headingCall_parameters_items_i0_pblocksize"></a>
<a id="Call_parameters_items_i0_pblocksize"></a>
##### pblocksize

- Schema name: `Pblocksize`
- Type: boolean
- Default: false

Whether to use physical block size reporting.

<a id="headingCall_parameters_items_i0_avail_threshold"></a>
<a id="Call_parameters_items_i0_avail_threshold"></a>
##### avail_threshold

- Schema name: `Avail Threshold`
- Default: null

Available space threshold percentage or `null` to disable.
<a id="Call_parameters_items_i0_avail_threshold_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_avail_threshold_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_avail_threshold_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `99`

<a id="tab-pane_Call_parameters_items_i0_avail_threshold_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_avail_threshold_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_comment"></a>
<a id="Call_parameters_items_i0_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the extent.

<a id="headingCall_parameters_items_i0_insecure_tpc"></a>
<a id="Call_parameters_items_i0_insecure_tpc"></a>
##### insecure_tpc

- Schema name: `Insecure Tpc`
- Type: boolean
- Default: true

Whether to enable insecure Third Party Copy (TPC) operations.

<a id="headingCall_parameters_items_i0_xen"></a>
<a id="Call_parameters_items_i0_xen"></a>
##### xen

- Schema name: `Xen`
- Type: boolean
- Default: false

Whether to enable Xen compatibility mode.

<a id="headingCall_parameters_items_i0_rpm"></a>
<a id="Call_parameters_items_i0_rpm"></a>
##### rpm

- Schema name: `Rpm`
- Type: enum (of string)
- Default: "SSD"

Reported RPM type for the extent.
###### Must be one of:

- "UNKNOWN"
- "SSD"
- "5400"
- "7200"
- "10000"
- "15000"

<a id="headingCall_parameters_items_i0_ro"></a>
<a id="Call_parameters_items_i0_ro"></a>
##### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Whether the extent is read-only.

<a id="headingCall_parameters_items_i0_enabled"></a>
<a id="Call_parameters_items_i0_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extent is enabled and available for use.

<a id="headingCall_parameters_items_i0_product_id"></a>
<a id="Call_parameters_items_i0_product_id"></a>
##### product_id

- Schema name: `Product Id`
- Default: null

Product ID string for the extent or `null` for default.
<a id="Call_parameters_items_i0_product_id_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_product_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_product_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long
- Must be at most `16` characters long

<a id="tab-pane_Call_parameters_items_i0_product_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_product_id_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `iSCSITargetExtentEntry`
- Type: object

The created iSCSI extent configuration.
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
