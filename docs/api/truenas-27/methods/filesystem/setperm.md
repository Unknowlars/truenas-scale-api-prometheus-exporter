---
title: filesystem.setperm
kind: method
source_rst: _sources/api_methods_filesystem.setperm.rst.txt
source_html: api_methods_filesystem.setperm.html
required_roles:
  - FILESYSTEM_ATTRS_WRITE
---

# filesystem.setperm

## Summary

Set unix permissions on given `path`.

If `mode` is specified then the mode will be applied to the path and files and subdirectories depending on which `options` are selected. Mode should be formatted as string representation of octal permissions bits.

`uid` the desired UID of the file user. If set to None (the default), then user is not changed.

`gid` the desired GID of the file group. If set to None (the default), then group is not changed.

`user` and `group` alternatively allow specifying the owner by name.

WARNING: `uid`, `gid, `user`, and `group` _should_ remain unset _unless_ the administrator wishes to change the owner or group of files.

`stripacl` setperm will fail if an extended ACL is present on `path`, unless `stripacl` is set to True.

`recursive` remove ACLs recursively, but do not traverse dataset boundaries.

`traverse` remove ACLs from child datasets.

If no `mode` is set, and `stripacl` is True, then non-trivial ACLs will be converted to trivial ACLs. An ACL is trivial if it can be expressed as a file mode without losing any access rules.

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

#### Parameter 1: filesystem_setperm

<a id="Call_parameters_items_i0"></a>
#### filesystem_setperm

- Schema name: `filesystem_setperm`
- Type: object

FilesystemSetpermArgs parameters.
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

<a id="headingCall_parameters_items_i0_mode"></a>
<a id="Call_parameters_items_i0_mode"></a>
##### mode

- Schema name: `Mode`
- Default: null

Unix permissions to set (octal format). `null` to leave unchanged.
<a id="Call_parameters_items_i0_mode_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_mode_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_mode_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_mode_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_mode_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_options"></a>
<a id="Call_parameters_items_i0_options"></a>
##### options

- Schema name: `FilesystemSetpermOptions`
- Type: object
- Default:
```json
{
  "recursive": false,
  "traverse": false,
  "stripacl": false
}
```

Additional options for the permission change operation.
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

<a id="headingCall_parameters_items_i0_options_stripacl"></a>
<a id="Call_parameters_items_i0_options_stripacl"></a>
###### stripacl

- Schema name: `Stripacl`
- Type: boolean
- Default: false

Whether to remove existing Access Control Lists when setting permissions.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the permission change is successfully completed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
