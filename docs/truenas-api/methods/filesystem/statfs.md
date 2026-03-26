---
title: filesystem.statfs
kind: method
source_rst: _sources/api_methods_filesystem.statfs.rst.txt
source_html: api_methods_filesystem.statfs.html
required_roles:
  - FILESYSTEM_ATTRS_READ
---

# filesystem.statfs

## Summary

Return stats from the filesystem of a given path.

Raises: CallError(ENOENT) - Path not found

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

Path on the filesystem to get statistics for.
- Must be at least `1` characters long

### Return value

- Schema name: `FilesystemStatfsData`
- Type: object

Filesystem statistics and mount information.
- No Additional Properties
#### flags (required)

- Schema name: `Flags`
- Type: array

Combined per-mount options and per-superblock options for mounted filesystem.
- No Additional Items

##### Each item of this array must be:

###### Any of

####### Option 1

- Type: enum (of string)

####### Option 2

- Type: object

#### fsid (required)

- Schema name: `Fsid`
- Type: string

Unique filesystem ID as returned by statvfs.
- Must be at least `1` characters long

#### fstype (required)

- Schema name: `Fstype`

String representation of filesystem type from mountinfo.
##### Any of

###### Option 1

- Type: enum (of string)

###### Option 2

- Type: object

#### source (required)

- Schema name: `Source`
- Type: string

Source for the mounted filesystem. For ZFS this will be dataset name.
- Must be at least `1` characters long

#### dest (required)

- Schema name: `Dest`
- Type: string

Local path on which filesystem is mounted.
- Must be at least `1` characters long

#### blocksize (required)

- Schema name: `Blocksize`
- Type: integer

Filesystem block size as reported by statvfs.

#### total_blocks (required)

- Schema name: `Total Blocks`
- Type: integer

Filesystem size as reported in blocksize blocks as reported by statvfs.

#### free_blocks (required)

- Schema name: `Free Blocks`
- Type: integer

Number of free blocks as reported by statvfs.

#### avail_blocks (required)

- Schema name: `Avail Blocks`
- Type: integer

Number of available blocks as reported by statvfs.

#### total_blocks_str (required)

- Schema name: `Total Blocks Str`
- Type: string

Total filesystem size in blocks as a human-readable string.
- Must be at least `1` characters long

#### free_blocks_str (required)

- Schema name: `Free Blocks Str`
- Type: string

Free blocks available as a human-readable string.
- Must be at least `1` characters long

#### avail_blocks_str (required)

- Schema name: `Avail Blocks Str`
- Type: string

Available blocks for unprivileged users as a human-readable string.
- Must be at least `1` characters long

#### files (required)

- Schema name: `Files`
- Type: integer

Number of inodes in use as reported by statvfs.

#### free_files (required)

- Schema name: `Free Files`
- Type: integer

Number of free inodes as reported by statvfs.

#### name_max (required)

- Schema name: `Name Max`
- Type: integer

Maximum filename length as reported by statvfs.

#### total_bytes (required)

- Schema name: `Total Bytes`
- Type: integer

Total filesystem size in bytes.

#### free_bytes (required)

- Schema name: `Free Bytes`
- Type: integer

Free space available in bytes.

#### avail_bytes (required)

- Schema name: `Avail Bytes`
- Type: integer

Available space for unprivileged users in bytes.

#### total_bytes_str (required)

- Schema name: `Total Bytes Str`
- Type: string

Total filesystem size in bytes as a human-readable string.
- Must be at least `1` characters long

#### free_bytes_str (required)

- Schema name: `Free Bytes Str`
- Type: string

Free space available in bytes as a human-readable string.
- Must be at least `1` characters long

#### avail_bytes_str (required)

- Schema name: `Avail Bytes Str`
- Type: string

Available space for unprivileged users in bytes as a human-readable string.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
