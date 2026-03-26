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

`realpath(str)`: absolute real path of the entry (if SYMLINK)

`type(str)`: DIRECTORY | FILE | SYMLINK | OTHER

`size(int)`: size of the entry

`allocation_size(int)`: on-disk size of entry

`mode(int)`: file mode/permission

`uid(int)`: user id of file owner

`gid(int)`: group id of file owner

`atime(float)`: timestamp for when file was last accessed. NOTE: this timestamp may be changed from userspace.

`mtime(float)`: timestamp for when file data was last modified NOTE: this timestamp may be changed from userspace.

`ctime(float)`: timestamp for when file was last changed.

`btime(float)`: timestamp for when file was initially created. NOTE: depending on platform this may be changed from userspace.

`dev(int)`: device id of the device containing the file. In the context of the TrueNAS API, this is sufficient to uniquely identify a given dataset.

`mount_id(int)`: the mount id for the filesystem underlying the given path. Bind mounts will have same device id, but different mount IDs. This value is sufficient to uniquely identify the particular mount which can be used to identify children of the given mountpoint.

`inode(int)`: inode number of the file. This number uniquely identifies the file on the given device, but once a file is deleted its inode number may be reused.

`nlink(int)`: number of hard lnks to the file.

`acl(bool)`: extended ACL is present on file

`is_mountpoint(bool)`: path is a mountpoint

`is_ctldir(bool)`: path is within special .zfs directory

`attributes(list)`: list of statx file attributes that apply to the file. See statx(2) manpage for more details.

## Required Roles

- `FILESYSTEM_ATTRS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: path

#### path

- Schema name: `path`
- Type: string

Absolute filesystem path to get statistics for.
- Must be at least `1` characters long

### Return value

- Schema name: `FilesystemStatData`
- Type: object

File or directory statistics information.
- No Additional Properties
#### realpath (required)

- Schema name: `Realpath`
- Type: string

Canonical path of the entry, eliminating any symbolic links.
- Must be at least `1` characters long

#### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of filesystem entry.

#### size (required)

- Schema name: `Size`
- Type: integer

Size in bytes of a plain file. This corresonds with stx_size.

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

#### uid (required)

- Schema name: `Uid`
- Type: integer

User ID of the entry's owner. This corresponds with stx_uid.

#### gid (required)

- Schema name: `Gid`
- Type: integer

Group ID of the entry's owner. This corresponds with stx_gid.

#### atime (required)

- Schema name: `Atime`
- Type: number

Time of last access. Corresponds with stx_atime. This is mutable from userspace.

#### mtime (required)

- Schema name: `Mtime`
- Type: number

Time of last modification. Corresponds with stx_mtime. This is mutable from userspace.

#### ctime (required)

- Schema name: `Ctime`
- Type: number

Time of last status change. Corresponds with stx_ctime.

#### btime (required)

- Schema name: `Btime`
- Type: number

Time of creation. Corresponds with stx_btime.

#### dev (required)

- Schema name: `Dev`
- Type: integer

The ID of the device containing the filesystem where the file resides. This is not sufficient to uniquely identify a particular filesystem mount. mount*id must be used for that purpose. This corresponds with st*dev.

#### inode (required)

- Schema name: `Inode`
- Type: integer

The inode number of the file. This corresponds with stx_ino.

#### nlink (required)

- Schema name: `Nlink`
- Type: integer

Number of hard links. Corresponds with stx_nlinks.

#### acl (required)

- Schema name: `Acl`
- Type: boolean

Specifies whether ACL is present on the entry. If this is the case then file permission bits as reported in `mode` may not be representative of the actual permissions.

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

#### user (required)

- Schema name: `User`

Username associated with `uid`. Will be None if the User ID does not map to existing user.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### group (required)

- Schema name: `Group`

Groupname associated with `gid`. Will be None if the Group ID does not map to existing group.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
