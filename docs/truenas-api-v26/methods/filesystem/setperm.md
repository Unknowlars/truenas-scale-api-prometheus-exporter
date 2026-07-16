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

Set Unix permissions on the given `path`.

If `mode` is specified then the mode is applied to the path, and to files and subdirectories depending on which `options` are selected.

This method will fail if an extended ACL is present on `path` unless `stripacl` is set. If no `mode` is set and `stripacl` is `true`, then non-trivial ACLs are converted to trivial ACLs. An ACL is trivial if it can be expressed as a file mode without losing any access rules.

.. important::

`uid`, `gid`, `user`, and `group` *should* remain unset *unless* the administrator wishes to change the owner or group of files.

This method is a job.

## Required Roles

- `FILESYSTEM_ATTRS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filesystem_setperm

#### filesystem_setperm

- Schema name: `filesystem_setperm`
- Type: object

FilesystemSetpermArgs parameters.
- No Additional Properties
##### path (required)

- Schema name: `Path`
- Type: string

Filesystem path to modify.
- Must be at least `1` characters long

##### uid

- Schema name: `Uid`
- Default: null

Numeric user ID to set as owner. `null` to leave unchanged.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

####### Option 2

- Type: null

##### user

- Schema name: `User`
- Default: null

Username to set as owner. `null` to leave unchanged.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### gid

- Schema name: `Gid`
- Default: null

Numeric group ID to set as group owner. `null` to leave unchanged.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

####### Option 2

- Type: null

##### group

- Schema name: `Group`
- Default: null

Group name to set as group owner. `null` to leave unchanged.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### mode

- Schema name: `Mode`
- Default: null

Unix permissions to set (octal format). `null` to leave unchanged.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

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
###### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to apply the operation recursively to subdirectories.

###### traverse

- Schema name: `Traverse`
- Type: boolean
- Default: false

If set do not limit to single dataset / filesystem.

###### stripacl

- Schema name: `Stripacl`
- Type: boolean
- Default: false

Whether to remove existing Access Control Lists when setting permissions.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the permission change is successfully completed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
