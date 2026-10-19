---
title: filesystem.mkdir
kind: method
source_rst: _sources/api_methods_filesystem.mkdir.rst.txt
source_html: api_methods_filesystem.mkdir.html
required_roles:
  - FILESYSTEM_DATA_WRITE
---

# filesystem.mkdir

## Summary

Create a directory at the specified path.

If the requested `mode` cannot be applied and `raise_chmod_error` is set, the newly created directory is removed to prevent its use with unintended permissions.

.. note::

If the chmod error is skipped, the `mode` key in the response will indicate the current permissions on the directory and not the permissions specified in the request payload.

## Required Roles

- `FILESYSTEM_DATA_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filesystem_mkdir

<a id="Call_parameters_items_i0"></a>
#### filesystem_mkdir

- Schema name: `filesystem_mkdir`
- Type: object

FilesystemMkdirArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Path where the new directory should be created.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_options"></a>
<a id="Call_parameters_items_i0_options"></a>
##### options

- Schema name: `FilesystemMkdirOptions`
- Type: object
- Default:
```json
{
  "mode": "755",
  "raise_chmod_error": true
}
```

Options controlling directory creation behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_mode"></a>
<a id="Call_parameters_items_i0_options_mode"></a>
###### mode

- Schema name: `Mode`
- Type: string
- Default: "755"

Unix permissions for the new directory.

<a id="headingCall_parameters_items_i0_options_raise_chmod_error"></a>
<a id="Call_parameters_items_i0_options_raise_chmod_error"></a>
###### raise_chmod_error

- Schema name: `Raise Chmod Error`
- Type: boolean
- Default: true

Whether to raise an error if chmod fails.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `FilesystemDirEntry`
- Type: object

Information about the created directory.
- No Additional Properties
<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Entry's base name.
- Must be at least `1` characters long

<a id="headingReturn_value_path"></a>
<a id="Return_value_path"></a>
#### path (required)

- Schema name: `Path`
- Type: string

Entry's full path.
- Must be at least `1` characters long

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

Type of filesystem entry. `DIRECTORY`: Directory/folder `FILE`: Regular file `SYMLINK`: Symbolic link `OTHER`: Other file types (device, pipe, socket, etc.)
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

Size of the file in bytes. For directories, this may not represent total content size. Corresonds with stx_size.

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

<a id="headingReturn_value_acl"></a>
<a id="Return_value_acl"></a>
#### acl (required)

- Schema name: `Acl`
- Type: boolean

Specifies whether ACL is present on the entry. If this is the case then file permission bits as reported in `mode` may not be representative of the actual permissions.

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

<a id="headingReturn_value_xattrs"></a>
<a id="Return_value_xattrs"></a>
#### xattrs (required)

- Schema name: `Xattrs`
- Type: array of string

List of xattr names of extended attributes on file.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_xattrs_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_zfs_attrs"></a>
<a id="Return_value_zfs_attrs"></a>
#### zfs_attrs (required)

- Schema name: `Zfs Attrs`

List of extra ZFS-related file attribute indicators on file. Will be None type if filesystem is not ZFS.
<a id="Return_value_zfs_attrs_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_zfs_attrs_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_zfs_attrs_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_zfs_attrs_anyOf_i0_items"></a>
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

<a id="tab-pane_Return_value_zfs_attrs_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_zfs_attrs_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
