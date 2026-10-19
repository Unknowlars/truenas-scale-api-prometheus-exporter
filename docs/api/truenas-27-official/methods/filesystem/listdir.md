---
title: filesystem.listdir
kind: method
source_rst: _sources/api_methods_filesystem.listdir.rst.txt
source_html: api_methods_filesystem.listdir.html
required_roles:
  - FILESYSTEM_ATTRS_READ
---

# filesystem.listdir

## Summary

Get the contents of a directory.

The select option may be used to optimize listdir performance. Metadata-related fields that are not selected will not be retrieved from the filesystem.

For example {"select": ["path", "type"]} will avoid querying an xattr list and ZFS attributes for files in a directory.

## Required Roles

- `FILESYSTEM_ATTRS_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: path

<a id="Call_parameters_items_i0"></a>
#### path

- Schema name: `path`
- Type: string

Directory path to list contents of.
- Must be at least `1` characters long

#### Parameter 2: query_filters

<a id="Call_parameters_items_i1"></a>
#### query_filters

- Schema name: `query_filters`
- Type: array
- Default: []

Query filters to apply to the directory listing.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i1_items"></a>
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

#### Parameter 3: query_options

<a id="Call_parameters_items_i2"></a>
#### query_options

- Schema name: `query_options`
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

Query options for sorting and pagination.
- No Additional Properties
<a id="headingCall_parameters_items_i2_extra"></a>
<a id="Call_parameters_items_i2_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i2_order_by"></a>
<a id="Call_parameters_items_i2_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i2_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i2_select"></a>
<a id="Call_parameters_items_i2_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i2_select_items"></a>
<a id="Call_parameters_items_i2_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i2_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i2_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i2_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i2_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i2_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i2_count"></a>
<a id="Call_parameters_items_i2_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i2_get"></a>
<a id="Call_parameters_items_i2_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i2_offset"></a>
<a id="Call_parameters_items_i2_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i2_limit"></a>
<a id="Call_parameters_items_i2_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i2_force_sql_filters"></a>
<a id="Call_parameters_items_i2_force_sql_filters"></a>
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
###### FilesystemDirEntry

- Schema name: `FilesystemDirEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Entry's base name.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_path"></a>
<a id="Return_value_anyOf_i0_items_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Entry's full path.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_realpath"></a>
<a id="Return_value_anyOf_i0_items_realpath"></a>
###### realpath (required)

- Schema name: `Realpath`
- Type: string

Canonical path of the entry, eliminating any symbolic links.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_type"></a>
<a id="Return_value_anyOf_i0_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of filesystem entry. `DIRECTORY`: Directory/folder `FILE`: Regular file `SYMLINK`: Symbolic link `OTHER`: Other file types (device, pipe, socket, etc.)
###### Must be one of:

- "DIRECTORY"
- "FILE"
- "SYMLINK"
- "OTHER"

<a id="headingReturn_value_anyOf_i0_items_size"></a>
<a id="Return_value_anyOf_i0_items_size"></a>
###### size (required)

- Schema name: `Size`
- Type: integer

Size of the file in bytes. For directories, this may not represent total content size. Corresonds with stx_size.

<a id="headingReturn_value_anyOf_i0_items_allocation_size"></a>
<a id="Return_value_anyOf_i0_items_allocation_size"></a>
###### allocation_size (required)

- Schema name: `Allocation Size`
- Type: integer

Allocated size of file. Calculated by multiplying stx_blocks by 512.

<a id="headingReturn_value_anyOf_i0_items_mode"></a>
<a id="Return_value_anyOf_i0_items_mode"></a>
###### mode (required)

- Schema name: `Mode`
- Type: integer

Entry's mode including file type information and file permission bits. This corresponds with stx_mode.

<a id="headingReturn_value_anyOf_i0_items_mount_id"></a>
<a id="Return_value_anyOf_i0_items_mount_id"></a>
###### mount_id (required)

- Schema name: `Mount Id`
- Type: integer

The mount ID of the mount containing the entry. This corresponds to the number in first field of /proc/self/mountinfo and stx*mnt*id.

<a id="headingReturn_value_anyOf_i0_items_acl"></a>
<a id="Return_value_anyOf_i0_items_acl"></a>
###### acl (required)

- Schema name: `Acl`
- Type: boolean

Specifies whether ACL is present on the entry. If this is the case then file permission bits as reported in `mode` may not be representative of the actual permissions.

<a id="headingReturn_value_anyOf_i0_items_uid"></a>
<a id="Return_value_anyOf_i0_items_uid"></a>
###### uid (required)

- Schema name: `Uid`
- Type: integer

User ID of the entry's owner. This corresponds with stx_uid.

<a id="headingReturn_value_anyOf_i0_items_gid"></a>
<a id="Return_value_anyOf_i0_items_gid"></a>
###### gid (required)

- Schema name: `Gid`
- Type: integer

Group ID of the entry's owner. This corresponds with stx_gid.

<a id="headingReturn_value_anyOf_i0_items_is_mountpoint"></a>
<a id="Return_value_anyOf_i0_items_is_mountpoint"></a>
###### is_mountpoint (required)

- Schema name: `Is Mountpoint`
- Type: boolean

Specifies whether the entry is also the mountpoint of a filesystem.

<a id="headingReturn_value_anyOf_i0_items_is_ctldir"></a>
<a id="Return_value_anyOf_i0_items_is_ctldir"></a>
###### is_ctldir (required)

- Schema name: `Is Ctldir`
- Type: boolean

Specifies whether the entry is located within the ZFS ctldir (for example a snapshot).

<a id="headingReturn_value_anyOf_i0_items_attributes"></a>
<a id="Return_value_anyOf_i0_items_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`
- Type: array of enum (of string)

Extra file attribute indicators for entry as returned by statx. Expanded from stx_attributes.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_attributes_items"></a>
- Type: enum (of string)
###### Must be one of:

- "COMPRESSED"
- "APPEND"
- "NODUMP"
- "ENCRYPTED"
- "IMMUTABLE"
- "AUTOMOUNT"
- "MOUNT_ROOT"
- "VERIFY"
- "DAX"

<a id="headingReturn_value_anyOf_i0_items_xattrs"></a>
<a id="Return_value_anyOf_i0_items_xattrs"></a>
###### xattrs (required)

- Schema name: `Xattrs`
- Type: array of string

List of xattr names of extended attributes on file.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_xattrs_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_zfs_attrs"></a>
<a id="Return_value_anyOf_i0_items_zfs_attrs"></a>
###### zfs_attrs (required)

- Schema name: `Zfs Attrs`

List of extra ZFS-related file attribute indicators on file. Will be None type if filesystem is not ZFS.
<a id="Return_value_anyOf_i0_items_zfs_attrs_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_zfs_attrs_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_zfs_attrs_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_zfs_attrs_anyOf_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "READONLY"
- "HIDDEN"
- "SYSTEM"
- "ARCHIVE"
- "IMMUTABLE"
- "NOUNLINK"
- "APPENDONLY"
- "NODUMP"
- "OPAQUE"
- "AV_QUARANTINED"
- "AV_MODIFIED"
- "REPARSE"
- "OFFLINE"
- "SPARSE"

<a id="tab-pane_Return_value_anyOf_i0_items_zfs_attrs_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_zfs_attrs_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [FilesystemDirEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `FilesystemDirEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Entry's base name.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_path"></a>
<a id="Return_value_anyOf_i1_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Entry's full path.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_realpath"></a>
<a id="Return_value_anyOf_i1_realpath"></a>
###### realpath (required)

- Schema name: `Realpath`
- Type: string

Canonical path of the entry, eliminating any symbolic links.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_type"></a>
<a id="Return_value_anyOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of filesystem entry. `DIRECTORY`: Directory/folder `FILE`: Regular file `SYMLINK`: Symbolic link `OTHER`: Other file types (device, pipe, socket, etc.)
###### Must be one of:

- "DIRECTORY"
- "FILE"
- "SYMLINK"
- "OTHER"

<a id="headingReturn_value_anyOf_i1_size"></a>
<a id="Return_value_anyOf_i1_size"></a>
###### size (required)

- Schema name: `Size`
- Type: integer

Size of the file in bytes. For directories, this may not represent total content size. Corresonds with stx_size.

<a id="headingReturn_value_anyOf_i1_allocation_size"></a>
<a id="Return_value_anyOf_i1_allocation_size"></a>
###### allocation_size (required)

- Schema name: `Allocation Size`
- Type: integer

Allocated size of file. Calculated by multiplying stx_blocks by 512.

<a id="headingReturn_value_anyOf_i1_mode"></a>
<a id="Return_value_anyOf_i1_mode"></a>
###### mode (required)

- Schema name: `Mode`
- Type: integer

Entry's mode including file type information and file permission bits. This corresponds with stx_mode.

<a id="headingReturn_value_anyOf_i1_mount_id"></a>
<a id="Return_value_anyOf_i1_mount_id"></a>
###### mount_id (required)

- Schema name: `Mount Id`
- Type: integer

The mount ID of the mount containing the entry. This corresponds to the number in first field of /proc/self/mountinfo and stx*mnt*id.

<a id="headingReturn_value_anyOf_i1_acl"></a>
<a id="Return_value_anyOf_i1_acl"></a>
###### acl (required)

- Schema name: `Acl`
- Type: boolean

Specifies whether ACL is present on the entry. If this is the case then file permission bits as reported in `mode` may not be representative of the actual permissions.

<a id="headingReturn_value_anyOf_i1_uid"></a>
<a id="Return_value_anyOf_i1_uid"></a>
###### uid (required)

- Schema name: `Uid`
- Type: integer

User ID of the entry's owner. This corresponds with stx_uid.

<a id="headingReturn_value_anyOf_i1_gid"></a>
<a id="Return_value_anyOf_i1_gid"></a>
###### gid (required)

- Schema name: `Gid`
- Type: integer

Group ID of the entry's owner. This corresponds with stx_gid.

<a id="headingReturn_value_anyOf_i1_is_mountpoint"></a>
<a id="Return_value_anyOf_i1_is_mountpoint"></a>
###### is_mountpoint (required)

- Schema name: `Is Mountpoint`
- Type: boolean

Specifies whether the entry is also the mountpoint of a filesystem.

<a id="headingReturn_value_anyOf_i1_is_ctldir"></a>
<a id="Return_value_anyOf_i1_is_ctldir"></a>
###### is_ctldir (required)

- Schema name: `Is Ctldir`
- Type: boolean

Specifies whether the entry is located within the ZFS ctldir (for example a snapshot).

<a id="headingReturn_value_anyOf_i1_attributes"></a>
<a id="Return_value_anyOf_i1_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`
- Type: array of enum (of string)

Extra file attribute indicators for entry as returned by statx. Expanded from stx_attributes.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_attributes_items"></a>
- Type: enum (of string)
###### Must be one of:

- "COMPRESSED"
- "APPEND"
- "NODUMP"
- "ENCRYPTED"
- "IMMUTABLE"
- "AUTOMOUNT"
- "MOUNT_ROOT"
- "VERIFY"
- "DAX"

<a id="headingReturn_value_anyOf_i1_xattrs"></a>
<a id="Return_value_anyOf_i1_xattrs"></a>
###### xattrs (required)

- Schema name: `Xattrs`
- Type: array of string

List of xattr names of extended attributes on file.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_xattrs_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_zfs_attrs"></a>
<a id="Return_value_anyOf_i1_zfs_attrs"></a>
###### zfs_attrs (required)

- Schema name: `Zfs Attrs`

List of extra ZFS-related file attribute indicators on file. Will be None type if filesystem is not ZFS.
<a id="Return_value_anyOf_i1_zfs_attrs_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_zfs_attrs_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_zfs_attrs_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_zfs_attrs_anyOf_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "READONLY"
- "HIDDEN"
- "SYSTEM"
- "ARCHIVE"
- "IMMUTABLE"
- "NOUNLINK"
- "APPENDONLY"
- "NODUMP"
- "OPAQUE"
- "AV_QUARANTINED"
- "AV_MODIFIED"
- "REPARSE"
- "OFFLINE"
- "SPARSE"

<a id="tab-pane_Return_value_anyOf_i1_zfs_attrs_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_zfs_attrs_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### FilesystemDirQueryResultItem

- Schema name: `FilesystemDirQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_name"></a>
<a id="Return_value_anyOf_i2_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Entry's base name.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_path"></a>
<a id="Return_value_anyOf_i2_items_path"></a>
###### path

- Schema name: `Path`
- Type: string

Entry's full path.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_realpath"></a>
<a id="Return_value_anyOf_i2_items_realpath"></a>
###### realpath

- Schema name: `Realpath`
- Type: string

Canonical path of the entry, eliminating any symbolic links.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_type"></a>
<a id="Return_value_anyOf_i2_items_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)

Type of filesystem entry. `DIRECTORY`: Directory/folder `FILE`: Regular file `SYMLINK`: Symbolic link `OTHER`: Other file types (device, pipe, socket, etc.)
###### Must be one of:

- "DIRECTORY"
- "FILE"
- "SYMLINK"
- "OTHER"

<a id="headingReturn_value_anyOf_i2_items_size"></a>
<a id="Return_value_anyOf_i2_items_size"></a>
###### size

- Schema name: `Size`
- Type: integer

Size of the file in bytes. For directories, this may not represent total content size. Corresonds with stx_size.

<a id="headingReturn_value_anyOf_i2_items_allocation_size"></a>
<a id="Return_value_anyOf_i2_items_allocation_size"></a>
###### allocation_size

- Schema name: `Allocation Size`
- Type: integer

Allocated size of file. Calculated by multiplying stx_blocks by 512.

<a id="headingReturn_value_anyOf_i2_items_mode"></a>
<a id="Return_value_anyOf_i2_items_mode"></a>
###### mode

- Schema name: `Mode`
- Type: integer

Entry's mode including file type information and file permission bits. This corresponds with stx_mode.

<a id="headingReturn_value_anyOf_i2_items_mount_id"></a>
<a id="Return_value_anyOf_i2_items_mount_id"></a>
###### mount_id

- Schema name: `Mount Id`
- Type: integer

The mount ID of the mount containing the entry. This corresponds to the number in first field of /proc/self/mountinfo and stx*mnt*id.

<a id="headingReturn_value_anyOf_i2_items_acl"></a>
<a id="Return_value_anyOf_i2_items_acl"></a>
###### acl

- Schema name: `Acl`
- Type: boolean

Specifies whether ACL is present on the entry. If this is the case then file permission bits as reported in `mode` may not be representative of the actual permissions.

<a id="headingReturn_value_anyOf_i2_items_uid"></a>
<a id="Return_value_anyOf_i2_items_uid"></a>
###### uid

- Schema name: `Uid`
- Type: integer

User ID of the entry's owner. This corresponds with stx_uid.

<a id="headingReturn_value_anyOf_i2_items_gid"></a>
<a id="Return_value_anyOf_i2_items_gid"></a>
###### gid

- Schema name: `Gid`
- Type: integer

Group ID of the entry's owner. This corresponds with stx_gid.

<a id="headingReturn_value_anyOf_i2_items_is_mountpoint"></a>
<a id="Return_value_anyOf_i2_items_is_mountpoint"></a>
###### is_mountpoint

- Schema name: `Is Mountpoint`
- Type: boolean

Specifies whether the entry is also the mountpoint of a filesystem.

<a id="headingReturn_value_anyOf_i2_items_is_ctldir"></a>
<a id="Return_value_anyOf_i2_items_is_ctldir"></a>
###### is_ctldir

- Schema name: `Is Ctldir`
- Type: boolean

Specifies whether the entry is located within the ZFS ctldir (for example a snapshot).

<a id="headingReturn_value_anyOf_i2_items_attributes"></a>
<a id="Return_value_anyOf_i2_items_attributes"></a>
###### attributes

- Schema name: `Attributes`
- Type: array of enum (of string)

Extra file attribute indicators for entry as returned by statx. Expanded from stx_attributes.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_attributes_items"></a>
- Type: enum (of string)
###### Must be one of:

- "COMPRESSED"
- "APPEND"
- "NODUMP"
- "ENCRYPTED"
- "IMMUTABLE"
- "AUTOMOUNT"
- "MOUNT_ROOT"
- "VERIFY"
- "DAX"

<a id="headingReturn_value_anyOf_i2_items_xattrs"></a>
<a id="Return_value_anyOf_i2_items_xattrs"></a>
###### xattrs

- Schema name: `Xattrs`
- Type: array of string

List of xattr names of extended attributes on file.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_xattrs_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_zfs_attrs"></a>
<a id="Return_value_anyOf_i2_items_zfs_attrs"></a>
###### zfs_attrs

- Schema name: `Zfs Attrs`

List of extra ZFS-related file attribute indicators on file. Will be None type if filesystem is not ZFS.
<a id="Return_value_anyOf_i2_items_zfs_attrs_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_zfs_attrs_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_zfs_attrs_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_zfs_attrs_anyOf_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "READONLY"
- "HIDDEN"
- "SYSTEM"
- "ARCHIVE"
- "IMMUTABLE"
- "NOUNLINK"
- "APPENDONLY"
- "NODUMP"
- "OPAQUE"
- "AV_QUARANTINED"
- "AV_MODIFIED"
- "REPARSE"
- "OFFLINE"
- "SPARSE"

<a id="tab-pane_Return_value_anyOf_i2_items_zfs_attrs_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_zfs_attrs_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [FilesystemDirQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `FilesystemDirQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_name"></a>
<a id="Return_value_anyOf_i3_name"></a>
###### name

- Schema name: `Name`
- Type: string

Entry's base name.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_path"></a>
<a id="Return_value_anyOf_i3_path"></a>
###### path

- Schema name: `Path`
- Type: string

Entry's full path.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_realpath"></a>
<a id="Return_value_anyOf_i3_realpath"></a>
###### realpath

- Schema name: `Realpath`
- Type: string

Canonical path of the entry, eliminating any symbolic links.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_type"></a>
<a id="Return_value_anyOf_i3_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)

Type of filesystem entry. `DIRECTORY`: Directory/folder `FILE`: Regular file `SYMLINK`: Symbolic link `OTHER`: Other file types (device, pipe, socket, etc.)
###### Must be one of:

- "DIRECTORY"
- "FILE"
- "SYMLINK"
- "OTHER"

<a id="headingReturn_value_anyOf_i3_size"></a>
<a id="Return_value_anyOf_i3_size"></a>
###### size

- Schema name: `Size`
- Type: integer

Size of the file in bytes. For directories, this may not represent total content size. Corresonds with stx_size.

<a id="headingReturn_value_anyOf_i3_allocation_size"></a>
<a id="Return_value_anyOf_i3_allocation_size"></a>
###### allocation_size

- Schema name: `Allocation Size`
- Type: integer

Allocated size of file. Calculated by multiplying stx_blocks by 512.

<a id="headingReturn_value_anyOf_i3_mode"></a>
<a id="Return_value_anyOf_i3_mode"></a>
###### mode

- Schema name: `Mode`
- Type: integer

Entry's mode including file type information and file permission bits. This corresponds with stx_mode.

<a id="headingReturn_value_anyOf_i3_mount_id"></a>
<a id="Return_value_anyOf_i3_mount_id"></a>
###### mount_id

- Schema name: `Mount Id`
- Type: integer

The mount ID of the mount containing the entry. This corresponds to the number in first field of /proc/self/mountinfo and stx*mnt*id.

<a id="headingReturn_value_anyOf_i3_acl"></a>
<a id="Return_value_anyOf_i3_acl"></a>
###### acl

- Schema name: `Acl`
- Type: boolean

Specifies whether ACL is present on the entry. If this is the case then file permission bits as reported in `mode` may not be representative of the actual permissions.

<a id="headingReturn_value_anyOf_i3_uid"></a>
<a id="Return_value_anyOf_i3_uid"></a>
###### uid

- Schema name: `Uid`
- Type: integer

User ID of the entry's owner. This corresponds with stx_uid.

<a id="headingReturn_value_anyOf_i3_gid"></a>
<a id="Return_value_anyOf_i3_gid"></a>
###### gid

- Schema name: `Gid`
- Type: integer

Group ID of the entry's owner. This corresponds with stx_gid.

<a id="headingReturn_value_anyOf_i3_is_mountpoint"></a>
<a id="Return_value_anyOf_i3_is_mountpoint"></a>
###### is_mountpoint

- Schema name: `Is Mountpoint`
- Type: boolean

Specifies whether the entry is also the mountpoint of a filesystem.

<a id="headingReturn_value_anyOf_i3_is_ctldir"></a>
<a id="Return_value_anyOf_i3_is_ctldir"></a>
###### is_ctldir

- Schema name: `Is Ctldir`
- Type: boolean

Specifies whether the entry is located within the ZFS ctldir (for example a snapshot).

<a id="headingReturn_value_anyOf_i3_attributes"></a>
<a id="Return_value_anyOf_i3_attributes"></a>
###### attributes

- Schema name: `Attributes`
- Type: array of enum (of string)

Extra file attribute indicators for entry as returned by statx. Expanded from stx_attributes.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_attributes_items"></a>
- Type: enum (of string)
###### Must be one of:

- "COMPRESSED"
- "APPEND"
- "NODUMP"
- "ENCRYPTED"
- "IMMUTABLE"
- "AUTOMOUNT"
- "MOUNT_ROOT"
- "VERIFY"
- "DAX"

<a id="headingReturn_value_anyOf_i3_xattrs"></a>
<a id="Return_value_anyOf_i3_xattrs"></a>
###### xattrs

- Schema name: `Xattrs`
- Type: array of string

List of xattr names of extended attributes on file.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_xattrs_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_zfs_attrs"></a>
<a id="Return_value_anyOf_i3_zfs_attrs"></a>
###### zfs_attrs

- Schema name: `Zfs Attrs`

List of extra ZFS-related file attribute indicators on file. Will be None type if filesystem is not ZFS.
<a id="Return_value_anyOf_i3_zfs_attrs_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_zfs_attrs_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_zfs_attrs_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_zfs_attrs_anyOf_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "READONLY"
- "HIDDEN"
- "SYSTEM"
- "ARCHIVE"
- "IMMUTABLE"
- "NOUNLINK"
- "APPENDONLY"
- "NODUMP"
- "OPAQUE"
- "AV_QUARANTINED"
- "AV_MODIFIED"
- "REPARSE"
- "OFFLINE"
- "SPARSE"

<a id="tab-pane_Return_value_anyOf_i3_zfs_attrs_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_zfs_attrs_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
