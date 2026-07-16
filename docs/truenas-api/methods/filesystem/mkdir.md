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

The following options are supported:

`mode` - specify the permissions to set on the new directory (0o755 is default). `raise_chmod_error` - choose whether to raise an exception if the attempt to set mode fails. In this case, the newly created directory will be removed to prevent use with unintended permissions.

NOTE: if chmod error is skipped, the resulting `mode` key in mkdir response will indicate the current permissions on the directory and not the permissions specified in the mkdir payload

## Required Roles

- `FILESYSTEM_DATA_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filesystem_mkdir

#### filesystem_mkdir

- Schema name: `filesystem_mkdir`
- Type: object

FilesystemMkdirArgs parameters.
- No Additional Properties
##### path (required)

- Schema name: `Path`
- Type: string

Path where the new directory should be created.
- Must be at least `1` characters long

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
###### mode

- Schema name: `Mode`
- Type: string
- Default: "755"

Unix permissions for the new directory.

###### raise_chmod_error

- Schema name: `Raise Chmod Error`
- Type: boolean
- Default: true

Whether to raise an error if chmod fails.

### Return value

- Schema name: `FilesystemDirEntry`
- Type: object

Information about the created directory.
- No Additional Properties
#### name (required)

- Schema name: `Name`
- Type: string

Entry's base name.
- Must be at least `1` characters long

#### path (required)

- Schema name: `Path`
- Type: string

Entry's full path.
- Must be at least `1` characters long

#### realpath (required)

- Schema name: `Realpath`
- Type: string

Canonical path of the entry, eliminating any symbolic links.
- Must be at least `1` characters long

#### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of filesystem entry. `DIRECTORY`: Directory/folder `FILE`: Regular file `SYMLINK`: Symbolic link `OTHER`: Other file types (device, pipe, socket, etc.)

#### size (required)

- Schema name: `Size`
- Type: integer

Size of the file in bytes. For directories, this may not represent total content size. Corresonds with stx_size.

#### allocation_size (required)

- Schema name: `Allocation Size`
- Type: integer

Allocated size of file. Calculated by multiplying stx_blocks by 512.

#### mode (required)

- Schema name: `Mode`
- Type: integer

Entry's mode including file type information and file permission bits. This corresponds with stx_mode.

#### mount_id (required)

- Schema name: `Mount Id`
- Type: integer

The mount ID of the mount containing the entry. This corresponds to the number in first field of /proc/self/mountinfo and stx*mnt*id.

#### acl (required)

- Schema name: `Acl`
- Type: boolean

Specifies whether ACL is present on the entry. If this is the case then file permission bits as reported in `mode` may not be representative of the actual permissions.

#### uid (required)

- Schema name: `Uid`
- Type: integer

User ID of the entry's owner. This corresponds with stx_uid.

#### gid (required)

- Schema name: `Gid`
- Type: integer

Group ID of the entry's owner. This corresponds with stx_gid.

#### is_mountpoint (required)

- Schema name: `Is Mountpoint`
- Type: boolean

Specifies whether the entry is also the mountpoint of a filesystem.

#### is_ctldir (required)

- Schema name: `Is Ctldir`
- Type: boolean

Specifies whether the entry is located within the ZFS ctldir (for example a snapshot).

#### attributes (required)

- Schema name: `Attributes`
- Type: array of enum (of string)

Extra file attribute indicators for entry as returned by statx. Expanded from stx_attributes.
- No Additional Items

##### Each item of this array must be:

- Type: enum (of string)

#### xattrs (required)

- Schema name: `Xattrs`
- Type: array of string

List of xattr names of extended attributes on file.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### zfs_attrs (required)

- Schema name: `Zfs Attrs`

List of extra ZFS-related file attribute indicators on file. Will be None type if filesystem is not ZFS.
##### Any of

###### Option 1

- Type: array of enum (of string)
- No Additional Items

####### Each item of this array must be:

- Type: enum (of string)

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
