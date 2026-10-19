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

If `path` does not exist, the method raises a `CallError` (code `-32001`, *Method call error*).

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

Path on the filesystem to get statistics for.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `FilesystemStatfsData`
- Type: object

Filesystem statistics and mount information.
- No Additional Properties
<a id="headingReturn_value_flags"></a>
<a id="Return_value_flags"></a>
#### flags (required)

- Schema name: `Flags`
- Type: array

Combined per-mount options and per-superblock options for mounted filesystem.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_flags_items"></a>
<a id="Return_value_flags_items_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_flags_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_flags_items_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "RW"
- "RO"
- "XATTR"
- "NOACL"
- "NFS4ACL"
- "POSIXACL"
- "CASESENSITIVE"
- "CASEINSENSITIVE"
- "NOATIME"
- "RELATIME"
- "NOSUID"
- "NODEV"
- "NOEXEC"

<a id="tab-pane_Return_value_flags_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_flags_items_anyOf_i1)

- Type: object

<a id="headingReturn_value_fsid"></a>
<a id="Return_value_fsid"></a>
#### fsid (required)

- Schema name: `Fsid`
- Type: string

Unique filesystem ID as returned by statvfs.
- Must be at least `1` characters long

<a id="headingReturn_value_fstype"></a>
<a id="Return_value_fstype"></a>
#### fstype (required)

- Schema name: `Fstype`

String representation of filesystem type from mountinfo.
<a id="Return_value_fstype_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_fstype_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_fstype_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "RW"
- "RO"
- "XATTR"
- "NOACL"
- "NFS4ACL"
- "POSIXACL"
- "CASESENSITIVE"
- "CASEINSENSITIVE"
- "NOATIME"
- "RELATIME"
- "NOSUID"
- "NODEV"
- "NOEXEC"

<a id="tab-pane_Return_value_fstype_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_fstype_anyOf_i1)

- Type: object

<a id="headingReturn_value_source"></a>
<a id="Return_value_source"></a>
#### source (required)

- Schema name: `Source`
- Type: string

Source for the mounted filesystem. For ZFS this will be dataset name.
- Must be at least `1` characters long

<a id="headingReturn_value_dest"></a>
<a id="Return_value_dest"></a>
#### dest (required)

- Schema name: `Dest`
- Type: string

Local path on which filesystem is mounted.
- Must be at least `1` characters long

<a id="headingReturn_value_blocksize"></a>
<a id="Return_value_blocksize"></a>
#### blocksize (required)

- Schema name: `Blocksize`
- Type: integer

Filesystem block size as reported by statvfs.

<a id="headingReturn_value_total_blocks"></a>
<a id="Return_value_total_blocks"></a>
#### total_blocks (required)

- Schema name: `Total Blocks`
- Type: integer

Filesystem size as reported in blocksize blocks as reported by statvfs.

<a id="headingReturn_value_free_blocks"></a>
<a id="Return_value_free_blocks"></a>
#### free_blocks (required)

- Schema name: `Free Blocks`
- Type: integer

Number of free blocks as reported by statvfs.

<a id="headingReturn_value_avail_blocks"></a>
<a id="Return_value_avail_blocks"></a>
#### avail_blocks (required)

- Schema name: `Avail Blocks`
- Type: integer

Number of available blocks as reported by statvfs.

<a id="headingReturn_value_total_blocks_str"></a>
<a id="Return_value_total_blocks_str"></a>
#### total_blocks_str (required)

- Schema name: `Total Blocks Str`
- Type: string

Total filesystem size in blocks as a human-readable string.
- Must be at least `1` characters long

<a id="headingReturn_value_free_blocks_str"></a>
<a id="Return_value_free_blocks_str"></a>
#### free_blocks_str (required)

- Schema name: `Free Blocks Str`
- Type: string

Free blocks available as a human-readable string.
- Must be at least `1` characters long

<a id="headingReturn_value_avail_blocks_str"></a>
<a id="Return_value_avail_blocks_str"></a>
#### avail_blocks_str (required)

- Schema name: `Avail Blocks Str`
- Type: string

Available blocks for unprivileged users as a human-readable string.
- Must be at least `1` characters long

<a id="headingReturn_value_files"></a>
<a id="Return_value_files"></a>
#### files (required)

- Schema name: `Files`
- Type: integer

Number of inodes in use as reported by statvfs.

<a id="headingReturn_value_free_files"></a>
<a id="Return_value_free_files"></a>
#### free_files (required)

- Schema name: `Free Files`
- Type: integer

Number of free inodes as reported by statvfs.

<a id="headingReturn_value_name_max"></a>
<a id="Return_value_name_max"></a>
#### name_max (required)

- Schema name: `Name Max`
- Type: integer

Maximum filename length as reported by statvfs.

<a id="headingReturn_value_total_bytes"></a>
<a id="Return_value_total_bytes"></a>
#### total_bytes (required)

- Schema name: `Total Bytes`
- Type: integer

Total filesystem size in bytes.

<a id="headingReturn_value_free_bytes"></a>
<a id="Return_value_free_bytes"></a>
#### free_bytes (required)

- Schema name: `Free Bytes`
- Type: integer

Free space available in bytes.

<a id="headingReturn_value_avail_bytes"></a>
<a id="Return_value_avail_bytes"></a>
#### avail_bytes (required)

- Schema name: `Avail Bytes`
- Type: integer

Available space for unprivileged users in bytes.

<a id="headingReturn_value_total_bytes_str"></a>
<a id="Return_value_total_bytes_str"></a>
#### total_bytes_str (required)

- Schema name: `Total Bytes Str`
- Type: string

Total filesystem size in bytes as a human-readable string.
- Must be at least `1` characters long

<a id="headingReturn_value_free_bytes_str"></a>
<a id="Return_value_free_bytes_str"></a>
#### free_bytes_str (required)

- Schema name: `Free Bytes Str`
- Type: string

Free space available in bytes as a human-readable string.
- Must be at least `1` characters long

<a id="headingReturn_value_avail_bytes_str"></a>
<a id="Return_value_avail_bytes_str"></a>
#### avail_bytes_str (required)

- Schema name: `Avail Bytes Str`
- Type: string

Available space for unprivileged users in bytes as a human-readable string.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
