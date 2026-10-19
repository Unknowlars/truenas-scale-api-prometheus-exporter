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

Set special ZFS-related file flags on the specified path.

`readonly` - READONLY MS-DOS attribute. When set, file may not be written to (toggling does not impact existing file opens).

`hidden` - HIDDEN MS-DOS attribute. When set, the SMB HIDDEN flag is set and file is "hidden" from the perspective of SMB clients.

`system` - SYSTEM MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.

`archive` - ARCHIVE MS-DOS attribute. Value is reset to True whenever file is modified.

`immutable` - file may not be altered or deleted. Also appears as IMMUTABLE in attributes in `filesystem.stat` output and as STATX_ATTR_IMMUTABLE in statx().

`nounlink` - file may be altered but not deleted.

`appendonly` - file may only be opened with O_APPEND flag. Also appears as APPEND in attributes in `filesystem.stat` output and as STATX_ATTR_APPEND in statx() response.

`offline` - OFFLINE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.

`sparse` - SPARSE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.

`options.recursive` - if set to a non-empty list of `FILES`/`DIRECTORIES`, the path is treated as the root of a tree walk and attributes are applied to descendants of the matching type. The root `path` itself is included only if its type matches the filter. `null` (the default) preserves the legacy single-path behavior. Recursion stops at dataset boundaries.

This method is a job.

## Required Roles

- `FILESYSTEM_ATTRS_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: set_zfs_file_attributes

<a id="Call_parameters_items_i0"></a>
#### set_zfs_file_attributes

- Schema name: `set_zfs_file_attributes`
- Type: object

FilesystemSetZfsAttributesArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Path to the file or directory to set ZFS attributes on.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_zfs_file_attributes"></a>
<a id="Call_parameters_items_i0_zfs_file_attributes"></a>
##### zfs_file_attributes (required)

- Schema name: `ZFSFileAttrsData`
- Type: object

ZFS file attributes to set.
- No Additional Properties
<a id="headingCall_parameters_items_i0_zfs_file_attributes_readonly"></a>
<a id="Call_parameters_items_i0_zfs_file_attributes_readonly"></a>
###### readonly

- Schema name: `Readonly`
- Default: null

READONLY MS-DOS attribute. When set, file may not be written to (toggling does not impact existing file opens).
<a id="Call_parameters_items_i0_zfs_file_attributes_readonly_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_readonly_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_readonly_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_readonly_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_readonly_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_zfs_file_attributes_hidden"></a>
<a id="Call_parameters_items_i0_zfs_file_attributes_hidden"></a>
###### hidden

- Schema name: `Hidden`
- Default: null

HIDDEN MS-DOS attribute. When set, the SMB HIDDEN flag is set and file is "hidden" from the perspective of SMB clients.
<a id="Call_parameters_items_i0_zfs_file_attributes_hidden_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_hidden_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_hidden_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_hidden_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_hidden_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_zfs_file_attributes_system"></a>
<a id="Call_parameters_items_i0_zfs_file_attributes_system"></a>
###### system

- Schema name: `System`
- Default: null

SYSTEM MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
<a id="Call_parameters_items_i0_zfs_file_attributes_system_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_system_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_system_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_system_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_system_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_zfs_file_attributes_archive"></a>
<a id="Call_parameters_items_i0_zfs_file_attributes_archive"></a>
###### archive

- Schema name: `Archive`
- Default: null

ARCHIVE MS-DOS attribute. Value is reset to True whenever file is modified.
<a id="Call_parameters_items_i0_zfs_file_attributes_archive_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_archive_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_archive_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_archive_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_archive_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_zfs_file_attributes_immutable"></a>
<a id="Call_parameters_items_i0_zfs_file_attributes_immutable"></a>
###### immutable

- Schema name: `Immutable`
- Default: null

File may not be altered or deleted. Also appears as IMMUTABLE in attributes in `filesystem.stat` output and as STATX*ATTR*IMMUTABLE in statx() response.
<a id="Call_parameters_items_i0_zfs_file_attributes_immutable_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_immutable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_immutable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_immutable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_immutable_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_zfs_file_attributes_nounlink"></a>
<a id="Call_parameters_items_i0_zfs_file_attributes_nounlink"></a>
###### nounlink

- Schema name: `Nounlink`
- Default: null

File may be altered but not deleted.
<a id="Call_parameters_items_i0_zfs_file_attributes_nounlink_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_nounlink_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_nounlink_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_nounlink_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_nounlink_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_zfs_file_attributes_appendonly"></a>
<a id="Call_parameters_items_i0_zfs_file_attributes_appendonly"></a>
###### appendonly

- Schema name: `Appendonly`
- Default: null

File may only be opened with O*APPEND flag. Also appears as APPEND in attributes in `filesystem.stat` output and as STATX*ATTR_APPEND in statx() response.
<a id="Call_parameters_items_i0_zfs_file_attributes_appendonly_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_appendonly_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_appendonly_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_appendonly_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_appendonly_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_zfs_file_attributes_offline"></a>
<a id="Call_parameters_items_i0_zfs_file_attributes_offline"></a>
###### offline

- Schema name: `Offline`
- Default: null

OFFLINE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
<a id="Call_parameters_items_i0_zfs_file_attributes_offline_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_offline_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_offline_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_offline_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_offline_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_zfs_file_attributes_sparse"></a>
<a id="Call_parameters_items_i0_zfs_file_attributes_sparse"></a>
###### sparse

- Schema name: `Sparse`
- Default: null

SPARSE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
<a id="Call_parameters_items_i0_zfs_file_attributes_sparse_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_sparse_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_sparse_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_zfs_file_attributes_sparse_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_zfs_file_attributes_sparse_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_options"></a>
<a id="Call_parameters_items_i0_options"></a>
##### options

- Schema name: `FilesystemSetZfsAttributesOptions`
- Type: object
- Default: {"recursive": null}

Additional options including recursion behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_recursive"></a>
<a id="Call_parameters_items_i0_options_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Default: null

If set, walk the tree under `path` and apply attributes to entries whose type appears in the list (`FILES`, `DIRECTORIES`, or both). The root `path` is included only if its type matches the filter. `null` means no recursion (operate on `path` only). An empty list is rejected.
<a id="Call_parameters_items_i0_options_recursive_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_options_recursive_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_options_recursive_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_recursive_anyOf_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "FILES"
- "DIRECTORIES"

<a id="tab-pane_Call_parameters_items_i0_options_recursive_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_options_recursive_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ZFSFileAttrsData`
- Type: object

The updated ZFS file attributes for the root `path`.
- No Additional Properties
<a id="headingReturn_value_readonly"></a>
<a id="Return_value_readonly"></a>
#### readonly

- Schema name: `Readonly`
- Default: null

READONLY MS-DOS attribute. When set, file may not be written to (toggling does not impact existing file opens).
<a id="Return_value_readonly_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_readonly_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_readonly_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_readonly_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_readonly_anyOf_i1)

- Type: null

<a id="headingReturn_value_hidden"></a>
<a id="Return_value_hidden"></a>
#### hidden

- Schema name: `Hidden`
- Default: null

HIDDEN MS-DOS attribute. When set, the SMB HIDDEN flag is set and file is "hidden" from the perspective of SMB clients.
<a id="Return_value_hidden_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_hidden_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_hidden_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_hidden_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_hidden_anyOf_i1)

- Type: null

<a id="headingReturn_value_system"></a>
<a id="Return_value_system"></a>
#### system

- Schema name: `System`
- Default: null

SYSTEM MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
<a id="Return_value_system_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_system_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_system_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_system_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_system_anyOf_i1)

- Type: null

<a id="headingReturn_value_archive"></a>
<a id="Return_value_archive"></a>
#### archive

- Schema name: `Archive`
- Default: null

ARCHIVE MS-DOS attribute. Value is reset to True whenever file is modified.
<a id="Return_value_archive_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_archive_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_archive_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_archive_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_archive_anyOf_i1)

- Type: null

<a id="headingReturn_value_immutable"></a>
<a id="Return_value_immutable"></a>
#### immutable

- Schema name: `Immutable`
- Default: null

File may not be altered or deleted. Also appears as IMMUTABLE in attributes in `filesystem.stat` output and as STATX*ATTR*IMMUTABLE in statx() response.
<a id="Return_value_immutable_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_immutable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_immutable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_immutable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_immutable_anyOf_i1)

- Type: null

<a id="headingReturn_value_nounlink"></a>
<a id="Return_value_nounlink"></a>
#### nounlink

- Schema name: `Nounlink`
- Default: null

File may be altered but not deleted.
<a id="Return_value_nounlink_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_nounlink_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_nounlink_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_nounlink_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_nounlink_anyOf_i1)

- Type: null

<a id="headingReturn_value_appendonly"></a>
<a id="Return_value_appendonly"></a>
#### appendonly

- Schema name: `Appendonly`
- Default: null

File may only be opened with O*APPEND flag. Also appears as APPEND in attributes in `filesystem.stat` output and as STATX*ATTR_APPEND in statx() response.
<a id="Return_value_appendonly_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_appendonly_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_appendonly_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_appendonly_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_appendonly_anyOf_i1)

- Type: null

<a id="headingReturn_value_offline"></a>
<a id="Return_value_offline"></a>
#### offline

- Schema name: `Offline`
- Default: null

OFFLINE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
<a id="Return_value_offline_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_offline_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_offline_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_offline_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_offline_anyOf_i1)

- Type: null

<a id="headingReturn_value_sparse"></a>
<a id="Return_value_sparse"></a>
#### sparse

- Schema name: `Sparse`
- Default: null

SPARSE MS-DOS attribute. Is presented to SMB clients, but has no impact on local filesystem.
<a id="Return_value_sparse_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_sparse_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sparse_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_sparse_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sparse_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
