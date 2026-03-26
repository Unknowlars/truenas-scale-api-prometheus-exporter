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

Set special ZFS-related file flags on the specified path

`readonly` - this maps to READONLY MS-DOS attribute. When set, file may not be written to (toggling does not impact existing file opens).

`hidden` - this maps to HIDDEN MS-DOS attribute. When set, the SMB HIDDEN flag is set and file is "hidden" from the perspective of SMB clients.

`system` - this maps to SYSTEM MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.

`archive` - this maps to ARCHIVE MS-DOS attribute. Value is reset to True whenever file is modified.

`immutable` - file may not be altered or deleted. Also appears as IMMUTABLE in attributes in `filesystem.stat` output and as STATX_ATTR_IMMUTABLE in statx() response.

`nounlink` - file may be altered but not deleted.

`appendonly` - file may only be opened with O_APPEND flag. Also appears as APPEND in attributes in `filesystem.stat` output and as STATX_ATTR_APPEND in statx() response.

`offline` - this maps to OFFLINE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.

`sparse` - maps to SPARSE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.

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

Path to the file to set ZFS attributes on.
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

### Return value

- Schema name: `ZFSFileAttrsData`
- Type: object

The updated ZFS file attributes.
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
