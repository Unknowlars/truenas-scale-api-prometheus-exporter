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

This method is a job.

## Required Roles

- `FILESYSTEM_ATTRS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filesystem_chown

#### filesystem_chown

- Schema name: `filesystem_chown`
- Type: object

FilesystemChownArgs parameters.
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

##### options

- Schema name: `FilesystemChownOptions`
- Type: object
- Default: {"recursive": false, "traverse": false}

Additional options for the ownership change operation.
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

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the ownership change is successfully completed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
