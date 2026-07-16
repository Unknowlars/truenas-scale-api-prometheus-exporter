---
title: group.query
kind: method
source_rst: _sources/api_methods_group.query.rst.txt
source_html: api_methods_group.query.html
required_roles:
  - ACCOUNT_READ
---

# group.query

## Summary

Query groups with `query-filters` and `query-options`.

## Required Roles

- `ACCOUNT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

#### filters

- Schema name: `filters`
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

#### Parameter 2: options

#### options

- Schema name: `options`
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

Query options including pagination, ordering, and additional parameters.
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

###### GroupQueryResultItem

- Schema name: `GroupQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

####### gid

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

####### name

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

####### builtin

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

####### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### smb

- Schema name: `Smb`
- Type: boolean

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

####### userns_idmap

- Schema name: `Userns Idmap`

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
######## Any of

######### Option 1

- Type: const

######### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

######### Option 3

- Type: null

####### group

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

####### local

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

####### sid

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### roles

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### users

- Schema name: `Users`
- Type: array of integer

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

######## Each item of this array must be:

- Type: integer

####### immutable

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

##### GroupQueryResultItem

- Type: const

##### Option 3

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 3

- Type: null

##### Option 1

- Schema name: `GroupQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

###### gid

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

###### name

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

###### builtin

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

###### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### smb

- Schema name: `Smb`
- Type: boolean

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

###### userns_idmap

- Schema name: `Userns Idmap`

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
####### Any of

######## Option 1

- Type: const

######## Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

######## Option 3

- Type: null

###### group

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

###### local

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

###### sid

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### roles

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### users

- Schema name: `Users`
- Type: array of integer

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

####### Each item of this array must be:

- Type: integer

###### immutable

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

##### Option 2

- Type: const

##### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

##### Option 2

- Type: null

##### Option 3

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
