---
title: filesystem.get_zfs_attributes
kind: method
source_rst: _sources/api_methods_filesystem.get_zfs_attributes.rst.txt
source_html: api_methods_filesystem.get_zfs_attributes.html
required_roles:
  - FILESYSTEM_ATTRS_READ
---

# filesystem.get_zfs_attributes

## Summary

Get the current ZFS attributes for the file at the given path

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

Path to the file to get ZFS attributes for.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ZFSFileAttrsData`
- Type: object

The current ZFS file attributes.
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
