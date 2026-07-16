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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: iscsi_extent_create

#### iscsi_extent_create

- Schema name: `iscsi_extent_create`
- Type: object

iSCSI extent configuration data for creation.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI extent.
- Must be at least `1` characters long
- Must be at most `64` characters long

##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "DISK"

Type of the extent storage backend.

##### disk

- Schema name: `Disk`
- Default: null

Disk device to use for the extent or `null` if using a file.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### serial

- Schema name: `Serial`
- Default: null

Serial number for the extent or `null` to auto-generate.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### path

- Schema name: `Path`
- Default: null

File path for file-based extents or `null` if using a disk.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### filesize

- Schema name: `Filesize`
- Default: "0"

Size of the file-based extent in bytes.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: integer

##### blocksize

- Schema name: `Blocksize`
- Type: enum (of integer)
- Default: 512

Block size for the extent in bytes.

##### pblocksize

- Schema name: `Pblocksize`
- Type: boolean
- Default: false

Whether to use physical block size reporting.

##### avail_threshold

- Schema name: `Avail Threshold`
- Default: null

Available space threshold percentage or `null` to disable.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `99`

####### Option 2

- Type: null

##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the extent.

##### insecure_tpc

- Schema name: `Insecure Tpc`
- Type: boolean
- Default: true

Whether to enable insecure Third Party Copy (TPC) operations.

##### xen

- Schema name: `Xen`
- Type: boolean
- Default: false

Whether to enable Xen compatibility mode.

##### rpm

- Schema name: `Rpm`
- Type: enum (of string)
- Default: "SSD"

Reported RPM type for the extent.

##### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Whether the extent is read-only.

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extent is enabled and available for use.

##### product_id

- Schema name: `Product Id`
- Default: null

Product ID string for the extent or `null` for default.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long
- Must be at most `16` characters long

####### Option 2

- Type: null

### Return value

- Schema name: `IscsiExtentEntry`
- Type: object

The created iSCSI extent configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI extent.

#### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI extent.
- Must be at least `1` characters long
- Must be at most `64` characters long

#### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "DISK"

Type of the extent storage backend.

#### disk

- Schema name: `Disk`
- Default: null

Disk device to use for the extent or `null` if using a file.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### serial

- Schema name: `Serial`
- Default: null

Serial number for the extent or `null` to auto-generate.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### path

- Schema name: `Path`
- Default: null

File path for file-based extents or `null` if using a disk.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### filesize

- Schema name: `Filesize`
- Default: "0"

Size of the file-based extent in bytes.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: integer

#### blocksize

- Schema name: `Blocksize`
- Type: enum (of integer)
- Default: 512

Block size for the extent in bytes.

#### pblocksize

- Schema name: `Pblocksize`
- Type: boolean
- Default: false

Whether to use physical block size reporting.

#### avail_threshold

- Schema name: `Avail Threshold`
- Default: null

Available space threshold percentage or `null` to disable.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `99`

###### Option 2

- Type: null

#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the extent.

#### naa (required)

- Schema name: `Naa`
- Type: string

Network Address Authority (NAA) identifier for the extent.
- Must be at most `34` characters long

#### insecure_tpc

- Schema name: `Insecure Tpc`
- Type: boolean
- Default: true

Whether to enable insecure Third Party Copy (TPC) operations.

#### xen

- Schema name: `Xen`
- Type: boolean
- Default: false

Whether to enable Xen compatibility mode.

#### rpm

- Schema name: `Rpm`
- Type: enum (of string)
- Default: "SSD"

Reported RPM type for the extent.

#### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Whether the extent is read-only.

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extent is enabled and available for use.

#### vendor (required)

- Schema name: `Vendor`
- Type: string

Vendor string reported by the extent.

#### product_id

- Schema name: `Product Id`
- Default: null

Product ID string for the extent or `null` for default.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long
- Must be at most `16` characters long

###### Option 2

- Type: null

#### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the iscsi extent is located on a locked dataset. `true`: The extent is in a locked dataset. `false`: The extent is not in a locked dataset. `null`: Lock status is not available because path locking information was not requested.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
