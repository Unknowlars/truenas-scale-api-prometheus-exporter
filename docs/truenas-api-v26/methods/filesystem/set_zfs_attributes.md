---
title: filesystem.set_zfs_attributes
kind: method
source_rst: _sources/api_methods_filesystem.set_zfs_attributes.rst.txt
source_html: api_methods_filesystem.set_zfs_attributes.html
required_roles:
  - FILESYSTEM_ATTRS_WRITE
---

# filesystem.set_zfs_attributes

## Summary

Set special ZFS-related file flags (MS-DOS attributes and the BSD-style `immutable`/`nounlink`/`appendonly` flags) on the specified path.

Several of these flags are also surfaced elsewhere. The `immutable` flag appears as `IMMUTABLE` in the `attributes` of :doc:`filesystem.stat <api_methods_filesystem.stat>` output and as `STATX_ATTR_IMMUTABLE` in the `statx()` response; `appendonly` appears as `APPEND` in :doc:`filesystem.stat <api_methods_filesystem.stat>` output and as `STATX_ATTR_APPEND` in `statx()`.

When recursion is requested, the path is treated as the root of a tree walk, and attributes are applied to descendants of the matching type. Recursion stops at dataset boundaries.

This method is a job.

## Required Roles

- `FILESYSTEM_ATTRS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: set_zfs_file_attributes

#### set_zfs_file_attributes

- Schema name: `set_zfs_file_attributes`
- Type: object

FilesystemSetZfsAttributesArgs parameters.
- No Additional Properties
##### path (required)

- Schema name: `Path`
- Type: string

Path to the file or directory to set ZFS attributes on.
- Must be at least `1` characters long

##### zfs_file_attributes (required)

- Schema name: `ZFSFileAttrsData`
- Type: object

ZFS file attributes to set.
- No Additional Properties
###### readonly

- Schema name: `Readonly`
- Default: null

READONLY MS-DOS attribute. When set, file may not be written to (toggling does not impact existing file opens).
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### hidden

- Schema name: `Hidden`
- Default: null

HIDDEN MS-DOS attribute. When set, the SMB HIDDEN flag is set and file is "hidden" from the perspective of SMB clients.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### system

- Schema name: `System`
- Default: null

SYSTEM MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### archive

- Schema name: `Archive`
- Default: null

ARCHIVE MS-DOS attribute. Value is reset to True whenever file is modified.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### immutable

- Schema name: `Immutable`
- Default: null

File may not be altered or deleted. Also appears as IMMUTABLE in attributes in `filesystem.stat` output and as STATX*ATTR*IMMUTABLE in statx() response.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### nounlink

- Schema name: `Nounlink`
- Default: null

File may be altered but not deleted.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### appendonly

- Schema name: `Appendonly`
- Default: null

File may only be opened with O*APPEND flag. Also appears as APPEND in attributes in `filesystem.stat` output and as STATX*ATTR_APPEND in statx() response.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### offline

- Schema name: `Offline`
- Default: null

OFFLINE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### sparse

- Schema name: `Sparse`
- Default: null

SPARSE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

##### options

- Schema name: `FilesystemSetZfsAttributesOptions`
- Type: object
- Default: {"recursive": null}

Additional options including recursion behavior.
- No Additional Properties
###### recursive

- Schema name: `Recursive`
- Default: null

If set, walk the tree under `path` and apply attributes to entries whose type appears in the list (`FILES`, `DIRECTORIES`, or both). The root `path` is included only if its type matches the filter. `null` means no recursion (operate on `path` only). An empty list is rejected.
####### Any of

######## Option 1

- Type: array of enum (of string)
- No Additional Items

######### Each item of this array must be:

- Type: enum (of string)

######## Option 2

- Type: null

### Return value

- Schema name: `ZFSFileAttrsData`
- Type: object

The updated ZFS file attributes for the root `path`.
- No Additional Properties
#### readonly

- Schema name: `Readonly`
- Default: null

READONLY MS-DOS attribute. When set, file may not be written to (toggling does not impact existing file opens).
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### hidden

- Schema name: `Hidden`
- Default: null

HIDDEN MS-DOS attribute. When set, the SMB HIDDEN flag is set and file is "hidden" from the perspective of SMB clients.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### system

- Schema name: `System`
- Default: null

SYSTEM MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### archive

- Schema name: `Archive`
- Default: null

ARCHIVE MS-DOS attribute. Value is reset to True whenever file is modified.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### immutable

- Schema name: `Immutable`
- Default: null

File may not be altered or deleted. Also appears as IMMUTABLE in attributes in `filesystem.stat` output and as STATX*ATTR*IMMUTABLE in statx() response.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### nounlink

- Schema name: `Nounlink`
- Default: null

File may be altered but not deleted.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### appendonly

- Schema name: `Appendonly`
- Default: null

File may only be opened with O*APPEND flag. Also appears as APPEND in attributes in `filesystem.stat` output and as STATX*ATTR_APPEND in statx() response.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### offline

- Schema name: `Offline`
- Default: null

OFFLINE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### sparse

- Schema name: `Sparse`
- Default: null

SPARSE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
