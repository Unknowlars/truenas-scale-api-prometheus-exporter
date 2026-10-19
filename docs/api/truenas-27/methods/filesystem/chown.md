---
title: filesystem.chown
kind: method
source_rst: _sources/api_methods_filesystem.chown.rst.txt
source_html: api_methods_filesystem.chown.html
required_roles:
  - FILESYSTEM_ATTRS_WRITE
---

# filesystem.chown

## Summary

Change owner or group of file at `path`.

`uid` and `gid` specify new owner of the file. If either key is absent or None, then existing value on the file is not changed.

`user` and `group` alternatively allow specifying a uid gid by user name or group name.

`recursive` performs action recursively, but does not traverse filesystem mount points.

If `traverse` and `recursive` are specified, then the chown operation will traverse filesystem mount points.

A recursive change may not target the mountpoint of a dataset consumed by an S3 bucket, nor traverse into one; apply it to the bucket's `s3data` directory instead.

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

#### Parameter 1: filesystem_chown

<a id="Call_parameters_items_i0"></a>
#### filesystem_chown

- Schema name: `filesystem_chown`
- Type: object

FilesystemChownArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Filesystem path to modify.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_uid"></a>
<a id="Call_parameters_items_i0_uid"></a>
##### uid

- Schema name: `Uid`
- Default: null

Numeric user ID to set as owner. `null` to leave unchanged.
<a id="Call_parameters_items_i0_uid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_uid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_uid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Call_parameters_items_i0_uid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_uid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_user"></a>
<a id="Call_parameters_items_i0_user"></a>
##### user

- Schema name: `User`
- Default: null

Username to set as owner. `null` to leave unchanged.
<a id="Call_parameters_items_i0_user_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_user_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_user_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_gid"></a>
<a id="Call_parameters_items_i0_gid"></a>
##### gid

- Schema name: `Gid`
- Default: null

Numeric group ID to set as group owner. `null` to leave unchanged.
<a id="Call_parameters_items_i0_gid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_gid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Call_parameters_items_i0_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_gid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_group"></a>
<a id="Call_parameters_items_i0_group"></a>
##### group

- Schema name: `Group`
- Default: null

Group name to set as group owner. `null` to leave unchanged.
<a id="Call_parameters_items_i0_group_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_group_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_group_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_options"></a>
<a id="Call_parameters_items_i0_options"></a>
##### options

- Schema name: `FilesystemChownOptions`
- Type: object
- Default: {"recursive": false, "traverse": false}

Additional options for the ownership change operation.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_recursive"></a>
<a id="Call_parameters_items_i0_options_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to apply the operation recursively to subdirectories.

<a id="headingCall_parameters_items_i0_options_traverse"></a>
<a id="Call_parameters_items_i0_options_traverse"></a>
###### traverse

- Schema name: `Traverse`
- Type: boolean
- Default: false

If set do not limit to single dataset / filesystem.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the ownership change is successfully completed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
