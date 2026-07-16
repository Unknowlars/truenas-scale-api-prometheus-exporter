---
title: filesystem.listdir
kind: method
source_rst: _sources/api_methods_filesystem.listdir.rst.txt
source_html: api_methods_filesystem.listdir.html
required_roles:
  - FILESYSTEM_ATTRS_READ
---

# filesystem.listdir

## Summary

Get the contents of a directory.

The select option may be used to optimize listdir performance. Metadata-related fields that are not selected will not be retrieved from the filesystem.

For example {"select": ["path", "type"]} will avoid querying an xattr list and ZFS attributes for files in a directory.

NOTE: an empty list for select (default) is treated as requesting all information.

Each entry of the list consists of: name(str): name of the file path(str): absolute path of the entry realpath(str): absolute real path of the entry (if SYMLINK) type(str): DIRECTORY | FILE | SYMLINK | OTHER size(int): size of the entry allocation_size(int): on-disk size of entry mode(int): file mode/permission uid(int): user id of entry owner gid(int): group id of entry owner acl(bool): extended ACL is present on file is_mountpoint(bool): path is a mountpoint is_ctldir(bool): path is within special .zfs directory attributes(list): list of statx file attributes that apply to the file. See statx(2) manpage for more details. xattrs(list): list of extended attribute names. zfs_attrs(list): list of ZFS file attributes on file

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

Directory path to list contents of.
- Must be at least `1` characters long

#### Parameter 2: query_filters

#### query_filters

- Schema name: `query_filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                [
                    "name",
                    "=",
                    "bob"
                ]
            ],
            [
                [
                    "name",
                    "=",
                    "larry"
                ]
            ]
        ]
    ]
]
```

#### Parameter 3: query_options

#### query_options

- Schema name: `query_options`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Query options for sorting and pagination.
- No Additional Properties
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### FilesystemDirQueryResultItem

- Schema name: `FilesystemDirQueryResultItem`
- Type: object
- No Additional Properties
####### name

- Schema name: `Name`
- Type: string

Entry's base name.
- Must be at least `1` characters long

####### path

- Schema name: `Path`
- Type: string

Entry's full path.
- Must be at least `1` characters long

####### realpath

- Schema name: `Realpath`
- Type: string

Canonical path of the entry, eliminating any symbolic links.
- Must be at least `1` characters long

####### type

- Schema name: `Type`
- Type: enum (of string)

Type of filesystem entry. `DIRECTORY`: Directory/folder `FILE`: Regular file `SYMLINK`: Symbolic link `OTHER`: Other file types (device, pipe, socket, etc.)

####### size

- Schema name: `Size`
- Type: integer

Size of the file in bytes. For directories, this may not represent total content size. Corresonds with stx_size.

####### allocation_size

- Schema name: `Allocation Size`
- Type: integer

Allocated size of file. Calculated by multiplying stx_blocks by 512.

####### mode

- Schema name: `Mode`
- Type: integer

Entry's mode including file type information and file permission bits. This corresponds with stx_mode.

####### mount_id

- Schema name: `Mount Id`
- Type: integer

The mount ID of the mount containing the entry. This corresponds to the number in first field of /proc/self/mountinfo and stx*mnt*id.

####### acl

- Schema name: `Acl`
- Type: boolean

Specifies whether ACL is present on the entry. If this is the case then file permission bits as reported in `mode` may not be representative of the actual permissions.

####### uid

- Schema name: `Uid`
- Type: integer

User ID of the entry's owner. This corresponds with stx_uid.

####### gid

- Schema name: `Gid`
- Type: integer

Group ID of the entry's owner. This corresponds with stx_gid.

####### is_mountpoint

- Schema name: `Is Mountpoint`
- Type: boolean

Specifies whether the entry is also the mountpoint of a filesystem.

####### is_ctldir

- Schema name: `Is Ctldir`
- Type: boolean

Specifies whether the entry is located within the ZFS ctldir (for example a snapshot).

####### attributes

- Schema name: `Attributes`
- Type: array of enum (of string)

Extra file attribute indicators for entry as returned by statx. Expanded from stx_attributes.
- No Additional Items

######## Each item of this array must be:

- Type: enum (of string)

####### xattrs

- Schema name: `Xattrs`
- Type: array of string

List of xattr names of extended attributes on file.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### zfs_attrs

- Schema name: `Zfs Attrs`

List of extra ZFS-related file attribute indicators on file. Will be None type if filesystem is not ZFS.
######## Any of

######### Option 1

- Type: array of enum (of string)
- No Additional Items

########## Each item of this array must be:

- Type: enum (of string)

######### Option 2

- Type: null

##### FilesystemDirQueryResultItem

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

- Type: enum (of string)

##### Option 3

- Type: null

##### Option 1

- Schema name: `FilesystemDirQueryResultItem`
- Type: object
- No Additional Properties
###### name

- Schema name: `Name`
- Type: string

Entry's base name.
- Must be at least `1` characters long

###### path

- Schema name: `Path`
- Type: string

Entry's full path.
- Must be at least `1` characters long

###### realpath

- Schema name: `Realpath`
- Type: string

Canonical path of the entry, eliminating any symbolic links.
- Must be at least `1` characters long

###### type

- Schema name: `Type`
- Type: enum (of string)

Type of filesystem entry. `DIRECTORY`: Directory/folder `FILE`: Regular file `SYMLINK`: Symbolic link `OTHER`: Other file types (device, pipe, socket, etc.)

###### size

- Schema name: `Size`
- Type: integer

Size of the file in bytes. For directories, this may not represent total content size. Corresonds with stx_size.

###### allocation_size

- Schema name: `Allocation Size`
- Type: integer

Allocated size of file. Calculated by multiplying stx_blocks by 512.

###### mode

- Schema name: `Mode`
- Type: integer

Entry's mode including file type information and file permission bits. This corresponds with stx_mode.

###### mount_id

- Schema name: `Mount Id`
- Type: integer

The mount ID of the mount containing the entry. This corresponds to the number in first field of /proc/self/mountinfo and stx*mnt*id.

###### acl

- Schema name: `Acl`
- Type: boolean

Specifies whether ACL is present on the entry. If this is the case then file permission bits as reported in `mode` may not be representative of the actual permissions.

###### uid

- Schema name: `Uid`
- Type: integer

User ID of the entry's owner. This corresponds with stx_uid.

###### gid

- Schema name: `Gid`
- Type: integer

Group ID of the entry's owner. This corresponds with stx_gid.

###### is_mountpoint

- Schema name: `Is Mountpoint`
- Type: boolean

Specifies whether the entry is also the mountpoint of a filesystem.

###### is_ctldir

- Schema name: `Is Ctldir`
- Type: boolean

Specifies whether the entry is located within the ZFS ctldir (for example a snapshot).

###### attributes

- Schema name: `Attributes`
- Type: array of enum (of string)

Extra file attribute indicators for entry as returned by statx. Expanded from stx_attributes.
- No Additional Items

####### Each item of this array must be:

- Type: enum (of string)

###### xattrs

- Schema name: `Xattrs`
- Type: array of string

List of xattr names of extended attributes on file.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### zfs_attrs

- Schema name: `Zfs Attrs`

List of extra ZFS-related file attribute indicators on file. Will be None type if filesystem is not ZFS.
####### Any of

######## Option 1

- Type: array of enum (of string)
- No Additional Items

######### Each item of this array must be:

- Type: enum (of string)

######## Option 2

- Type: null

##### Option 2

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

- Type: enum (of string)

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
