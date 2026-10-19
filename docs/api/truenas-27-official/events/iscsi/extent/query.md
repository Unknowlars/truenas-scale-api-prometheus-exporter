---
title: iscsi.extent.query
kind: event
source_rst: _sources/api_events_iscsi.extent.query.rst.txt
source_html: api_events_iscsi.extent.query.html
required_roles:
  - SHARING_ISCSI_EXTENT_READ
---

# iscsi.extent.query

## Summary

Sent on iscsi.extent changes.

## Required Roles

- `SHARING_ISCSI_EXTENT_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `iSCSITargetExtentAddedEvent`
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

- Schema name: `iSCSITargetExtentEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI extent.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI extent.
- Must be at least `1` characters long
- Must be at most `64` characters long

<a id="headingADDED_fields_type"></a>
<a id="ADDED_fields_type"></a>
##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "DISK"

Type of the extent storage backend.
###### Must be one of:

- "DISK"
- "FILE"

<a id="headingADDED_fields_disk"></a>
<a id="ADDED_fields_disk"></a>
##### disk

- Schema name: `Disk`
- Default: null

Disk device to use for the extent or `null` if using a file.
<a id="ADDED_fields_disk_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_disk_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_disk_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_disk_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_disk_anyOf_i1)

- Type: null

<a id="headingADDED_fields_serial"></a>
<a id="ADDED_fields_serial"></a>
##### serial

- Schema name: `Serial`
- Default: null

Serial number for the extent or `null` to auto-generate.
<a id="ADDED_fields_serial_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_serial_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_serial_anyOf_i1)

- Type: null

<a id="headingADDED_fields_path"></a>
<a id="ADDED_fields_path"></a>
##### path

- Schema name: `Path`
- Default: null

File path for file-based extents or `null` if using a disk.
<a id="ADDED_fields_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_dataset"></a>
<a id="ADDED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing the file-based extent (e.g., 'tank/iscsi'). Returns `null` for non-FILE extent types (DISK, ZVOL) or if the FILE path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "path".
<a id="ADDED_fields_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_dataset_anyOf_i1)

- Type: null

<a id="headingADDED_fields_relative_path"></a>
<a id="ADDED_fields_relative_path"></a>
##### relative_path (required)

- Schema name: `Relative Path`

The path of the file-based extent relative to the dataset mountpoint (e.g., 'extents/lun0.img'). An empty string indicates the file is at the dataset root. Returns `null` for non-FILE types or if the path cannot be resolved yet. This is a read-only field automatically populated from "path".
<a id="ADDED_fields_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_relative_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_filesize"></a>
<a id="ADDED_fields_filesize"></a>
##### filesize

- Schema name: `Filesize`
- Default: "0"

Size of the file-based extent in bytes. If non-zero, must be a multiple of `blocksize`.
<a id="ADDED_fields_filesize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_filesize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_filesize_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_filesize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_filesize_anyOf_i1)

- Type: integer

<a id="headingADDED_fields_blocksize"></a>
<a id="ADDED_fields_blocksize"></a>
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

<a id="headingADDED_fields_pblocksize"></a>
<a id="ADDED_fields_pblocksize"></a>
##### pblocksize

- Schema name: `Pblocksize`
- Type: boolean
- Default: false

Whether to use physical block size reporting.

<a id="headingADDED_fields_avail_threshold"></a>
<a id="ADDED_fields_avail_threshold"></a>
##### avail_threshold

- Schema name: `Avail Threshold`
- Default: null

Available space threshold percentage or `null` to disable.
<a id="ADDED_fields_avail_threshold_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_avail_threshold_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_avail_threshold_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `99`

<a id="tab-pane_ADDED_fields_avail_threshold_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_avail_threshold_anyOf_i1)

- Type: null

<a id="headingADDED_fields_comment"></a>
<a id="ADDED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the extent.

<a id="headingADDED_fields_naa"></a>
<a id="ADDED_fields_naa"></a>
##### naa (required)

- Schema name: `Naa`
- Type: string

Network Address Authority (NAA) identifier for the extent.
- Must be at most `34` characters long

<a id="headingADDED_fields_insecure_tpc"></a>
<a id="ADDED_fields_insecure_tpc"></a>
##### insecure_tpc

- Schema name: `Insecure Tpc`
- Type: boolean
- Default: true

Whether to allow initiators to bypass normal access control for XCOPY (Third Party Copy) operations. Disable if XCOPY cross-target access is not required.

<a id="headingADDED_fields_xen"></a>
<a id="ADDED_fields_xen"></a>
##### xen

- Schema name: `Xen`
- Type: boolean
- Default: false

Whether to enable Xen compatibility mode. Set to `true` when Xen is the iSCSI initiator.

<a id="headingADDED_fields_rpm"></a>
<a id="ADDED_fields_rpm"></a>
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

<a id="headingADDED_fields_ro"></a>
<a id="ADDED_fields_ro"></a>
##### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Whether the extent is read-only.

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extent is enabled and available for use.

<a id="headingADDED_fields_vendor"></a>
<a id="ADDED_fields_vendor"></a>
##### vendor (required)

- Schema name: `Vendor`
- Type: string

Vendor string reported by the extent.

<a id="headingADDED_fields_product_id"></a>
<a id="ADDED_fields_product_id"></a>
##### product_id

- Schema name: `Product Id`
- Default: null

Product ID string for the extent or `null` for default.
<a id="ADDED_fields_product_id_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_product_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_product_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long
- Must be at most `16` characters long

<a id="tab-pane_ADDED_fields_product_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_product_id_anyOf_i1)

- Type: null

<a id="headingADDED_fields_locked"></a>
<a id="ADDED_fields_locked"></a>
##### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the iscsi extent is located on a locked dataset. `true`: The extent is in a locked dataset. `false`: The extent is not in a locked dataset. `null`: Lock status is not available because path locking information was not requested.
<a id="ADDED_fields_locked_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_locked_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `iSCSITargetExtentChangedEvent`
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

- Schema name: `iSCSITargetExtentEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI extent.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI extent.
- Must be at least `1` characters long
- Must be at most `64` characters long

<a id="headingCHANGED_fields_type"></a>
<a id="CHANGED_fields_type"></a>
##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "DISK"

Type of the extent storage backend.
###### Must be one of:

- "DISK"
- "FILE"

<a id="headingCHANGED_fields_disk"></a>
<a id="CHANGED_fields_disk"></a>
##### disk

- Schema name: `Disk`
- Default: null

Disk device to use for the extent or `null` if using a file.
<a id="CHANGED_fields_disk_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_disk_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_disk_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_disk_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_disk_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_serial"></a>
<a id="CHANGED_fields_serial"></a>
##### serial

- Schema name: `Serial`
- Default: null

Serial number for the extent or `null` to auto-generate.
<a id="CHANGED_fields_serial_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_serial_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_serial_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_path"></a>
<a id="CHANGED_fields_path"></a>
##### path

- Schema name: `Path`
- Default: null

File path for file-based extents or `null` if using a disk.
<a id="CHANGED_fields_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_dataset"></a>
<a id="CHANGED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing the file-based extent (e.g., 'tank/iscsi'). Returns `null` for non-FILE extent types (DISK, ZVOL) or if the FILE path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "path".
<a id="CHANGED_fields_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_dataset_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_relative_path"></a>
<a id="CHANGED_fields_relative_path"></a>
##### relative_path (required)

- Schema name: `Relative Path`

The path of the file-based extent relative to the dataset mountpoint (e.g., 'extents/lun0.img'). An empty string indicates the file is at the dataset root. Returns `null` for non-FILE types or if the path cannot be resolved yet. This is a read-only field automatically populated from "path".
<a id="CHANGED_fields_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_relative_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_filesize"></a>
<a id="CHANGED_fields_filesize"></a>
##### filesize

- Schema name: `Filesize`
- Default: "0"

Size of the file-based extent in bytes. If non-zero, must be a multiple of `blocksize`.
<a id="CHANGED_fields_filesize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_filesize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_filesize_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_filesize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_filesize_anyOf_i1)

- Type: integer

<a id="headingCHANGED_fields_blocksize"></a>
<a id="CHANGED_fields_blocksize"></a>
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

<a id="headingCHANGED_fields_pblocksize"></a>
<a id="CHANGED_fields_pblocksize"></a>
##### pblocksize

- Schema name: `Pblocksize`
- Type: boolean
- Default: false

Whether to use physical block size reporting.

<a id="headingCHANGED_fields_avail_threshold"></a>
<a id="CHANGED_fields_avail_threshold"></a>
##### avail_threshold

- Schema name: `Avail Threshold`
- Default: null

Available space threshold percentage or `null` to disable.
<a id="CHANGED_fields_avail_threshold_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_avail_threshold_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_avail_threshold_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `99`

<a id="tab-pane_CHANGED_fields_avail_threshold_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_avail_threshold_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_comment"></a>
<a id="CHANGED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the extent.

<a id="headingCHANGED_fields_naa"></a>
<a id="CHANGED_fields_naa"></a>
##### naa (required)

- Schema name: `Naa`
- Type: string

Network Address Authority (NAA) identifier for the extent.
- Must be at most `34` characters long

<a id="headingCHANGED_fields_insecure_tpc"></a>
<a id="CHANGED_fields_insecure_tpc"></a>
##### insecure_tpc

- Schema name: `Insecure Tpc`
- Type: boolean
- Default: true

Whether to allow initiators to bypass normal access control for XCOPY (Third Party Copy) operations. Disable if XCOPY cross-target access is not required.

<a id="headingCHANGED_fields_xen"></a>
<a id="CHANGED_fields_xen"></a>
##### xen

- Schema name: `Xen`
- Type: boolean
- Default: false

Whether to enable Xen compatibility mode. Set to `true` when Xen is the iSCSI initiator.

<a id="headingCHANGED_fields_rpm"></a>
<a id="CHANGED_fields_rpm"></a>
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

<a id="headingCHANGED_fields_ro"></a>
<a id="CHANGED_fields_ro"></a>
##### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Whether the extent is read-only.

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extent is enabled and available for use.

<a id="headingCHANGED_fields_vendor"></a>
<a id="CHANGED_fields_vendor"></a>
##### vendor (required)

- Schema name: `Vendor`
- Type: string

Vendor string reported by the extent.

<a id="headingCHANGED_fields_product_id"></a>
<a id="CHANGED_fields_product_id"></a>
##### product_id

- Schema name: `Product Id`
- Default: null

Product ID string for the extent or `null` for default.
<a id="CHANGED_fields_product_id_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_product_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_product_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long
- Must be at most `16` characters long

<a id="tab-pane_CHANGED_fields_product_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_product_id_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_locked"></a>
<a id="CHANGED_fields_locked"></a>
##### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the iscsi extent is located on a locked dataset. `true`: The extent is in a locked dataset. `false`: The extent is not in a locked dataset. `null`: Lock status is not available because path locking information was not requested.
<a id="CHANGED_fields_locked_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_locked_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `iSCSITargetExtentRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
