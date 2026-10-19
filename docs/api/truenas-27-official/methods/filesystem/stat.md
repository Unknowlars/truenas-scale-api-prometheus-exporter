---
title: filesystem.stat
kind: method
source_rst: _sources/api_methods_filesystem.stat.rst.txt
source_html: api_methods_filesystem.stat.html
required_roles:
  - FILESYSTEM_ATTRS_READ
---

# filesystem.stat

## Summary

Return filesystem information for a given path.

The reported timestamps reflect `statx()` values. The `atime` and `mtime` timestamps are mutable from userspace, and `btime` may also be mutable from userspace depending on the platform.

The returned `attributes` list contains the `statx()` file attributes that apply to the file (see the `statx(2)` manpage for details). ZFS flags set via [filesystem.set_zfs_attributes](set_zfs_attributes.md) are surfaced here: an immutable file reports `IMMUTABLE` and an append-only file reports `APPEND`.

.. note::

`mount_id` uniquely identifies the particular mount underlying the path. Bind mounts share the same `dev` (device id) but have distinct `mount_id` values, so `mount_id` (not `dev`) must be used to identify children of a given mountpoint.

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

Absolute filesystem path to get statistics for.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `FilesystemStatData`
- Type: object

File or directory statistics information.
- No Additional Properties
<a id="headingReturn_value_realpath"></a>
<a id="Return_value_realpath"></a>
#### realpath (required)

- Schema name: `Realpath`
- Type: string

Canonical path of the entry, eliminating any symbolic links.
- Must be at least `1` characters long

<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of filesystem entry.
##### Must be one of:

- "DIRECTORY"
- "FILE"
- "SYMLINK"
- "OTHER"

<a id="headingReturn_value_size"></a>
<a id="Return_value_size"></a>
#### size (required)

- Schema name: `Size`
- Type: integer

Size in bytes of a plain file. This corresonds with stx_size.

<a id="headingReturn_value_allocation_size"></a>
<a id="Return_value_allocation_size"></a>
#### allocation_size (required)

- Schema name: `Allocation Size`
- Type: integer

Allocated size of file. Calculated by multiplying stx_blocks by 512.

<a id="headingReturn_value_mode"></a>
<a id="Return_value_mode"></a>
#### mode (required)

- Schema name: `Mode`
- Type: integer

Entry's mode including file type information and file permission bits. This corresponds with stx_mode.

<a id="headingReturn_value_mount_id"></a>
<a id="Return_value_mount_id"></a>
#### mount_id (required)

- Schema name: `Mount Id`
- Type: integer

The mount ID of the mount containing the entry. This corresponds to the number in first field of /proc/self/mountinfo and stx*mnt*id.

<a id="headingReturn_value_uid"></a>
<a id="Return_value_uid"></a>
#### uid (required)

- Schema name: `Uid`
- Type: integer

User ID of the entry's owner. This corresponds with stx_uid.

<a id="headingReturn_value_gid"></a>
<a id="Return_value_gid"></a>
#### gid (required)

- Schema name: `Gid`
- Type: integer

Group ID of the entry's owner. This corresponds with stx_gid.

<a id="headingReturn_value_atime"></a>
<a id="Return_value_atime"></a>
#### atime (required)

- Schema name: `Atime`
- Type: number

Time of last access. Corresponds with stx_atime. This is mutable from userspace.

<a id="headingReturn_value_mtime"></a>
<a id="Return_value_mtime"></a>
#### mtime (required)

- Schema name: `Mtime`
- Type: number

Time of last modification. Corresponds with stx_mtime. This is mutable from userspace.

<a id="headingReturn_value_ctime"></a>
<a id="Return_value_ctime"></a>
#### ctime (required)

- Schema name: `Ctime`
- Type: number

Time of last status change. Corresponds with stx_ctime.

<a id="headingReturn_value_btime"></a>
<a id="Return_value_btime"></a>
#### btime (required)

- Schema name: `Btime`
- Type: number

Time of creation. Corresponds with stx_btime.

<a id="headingReturn_value_dev"></a>
<a id="Return_value_dev"></a>
#### dev (required)

- Schema name: `Dev`
- Type: integer

The ID of the device containing the filesystem where the file resides. This is not sufficient to uniquely identify a particular filesystem mount. mount*id must be used for that purpose. This corresponds with st*dev.

<a id="headingReturn_value_inode"></a>
<a id="Return_value_inode"></a>
#### inode (required)

- Schema name: `Inode`
- Type: integer

The inode number of the file. This corresponds with stx_ino.

<a id="headingReturn_value_nlink"></a>
<a id="Return_value_nlink"></a>
#### nlink (required)

- Schema name: `Nlink`
- Type: integer

Number of hard links. Corresponds with stx_nlinks.

<a id="headingReturn_value_acl"></a>
<a id="Return_value_acl"></a>
#### acl (required)

- Schema name: `Acl`
- Type: boolean

Specifies whether ACL is present on the entry. If this is the case then file permission bits as reported in `mode` may not be representative of the actual permissions.

<a id="headingReturn_value_is_mountpoint"></a>
<a id="Return_value_is_mountpoint"></a>
#### is_mountpoint (required)

- Schema name: `Is Mountpoint`
- Type: boolean

Specifies whether the entry is also the mountpoint of a filesystem.

<a id="headingReturn_value_is_ctldir"></a>
<a id="Return_value_is_ctldir"></a>
#### is_ctldir (required)

- Schema name: `Is Ctldir`
- Type: boolean

Specifies whether the entry is located within the ZFS ctldir (for example a snapshot).

<a id="headingReturn_value_attributes"></a>
<a id="Return_value_attributes"></a>
#### attributes (required)

- Schema name: `Attributes`
- Type: array of enum (of string)

Extra file attribute indicators for entry as returned by statx. Expanded from stx_attributes.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_attributes_items"></a>
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

<a id="headingReturn_value_user"></a>
<a id="Return_value_user"></a>
#### user (required)

- Schema name: `User`

Username associated with `uid`. Will be None if the User ID does not map to existing user.
<a id="Return_value_user_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_group"></a>
<a id="Return_value_group"></a>
#### group (required)

- Schema name: `Group`

Groupname associated with `gid`. Will be None if the Group ID does not map to existing group.
<a id="Return_value_group_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_group_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_group_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
