---
title: filesystem.acltemplate.query
kind: method
source_rst: _sources/api_methods_filesystem.acltemplate.query.rst.txt
source_html: api_methods_filesystem.acltemplate.query.html
required_roles:
  - FILESYSTEM_ATTRS_READ
---

# filesystem.acltemplate.query

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

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
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
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
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
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### ACLTemplateQueryResultItem

- Schema name: `ACLTemplateQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the ACL template.

<a id="headingReturn_value_anyOf_i0_items_builtin"></a>
<a id="Return_value_anyOf_i0_items_builtin"></a>
###### builtin

- Schema name: `Builtin`
- Type: boolean

Whether this is a built-in system template or user-created.

<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Human-readable name for the ACL template.

<a id="headingReturn_value_anyOf_i0_items_acltype"></a>
<a id="Return_value_anyOf_i0_items_acltype"></a>
###### acltype

- Schema name: `Acltype`
- Type: enum (of string)

ACL type this template provides.
###### Must be one of:

- "NFS4"
- "POSIX1E"

<a id="headingReturn_value_anyOf_i0_items_acl"></a>
<a id="Return_value_anyOf_i0_items_acl"></a>
###### acl

- Schema name: `Acl`

Array of Access Control Entries defined by this template.
<a id="Return_value_anyOf_i0_items_acl_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items"></a>
###### NFS4ACE

- Schema name: `NFS4ACE`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_tag"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this ACE. `owner@`: File/directory owner `group@`: File/directory primary group `everyone@`: All users `USER`: Specific user account `GROUP`: Specific group
###### Must be one of:

- "owner@"
- "group@"
- "everyone@"
- "USER"
- "GROUP"

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_type"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Access control type. `ALLOW`: Grant the specified permissions `DENY`: Explicitly deny the specified permissions
###### Must be one of:

- "ALLOW"
- "DENY"

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms"></a>
###### perms (required)

- Schema name: `Perms`

Permissions granted or denied by this ACE.
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0"></a>
###### [NFS4ACE_AdvancedPerms](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_READ_DATA"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_READ_DATA"></a>
###### READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_DATA"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_DATA"></a>
###### WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_APPEND_DATA"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_APPEND_DATA"></a>
###### APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
###### READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
###### WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_EXECUTE"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_EXECUTE"></a>
###### EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_DELETE"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_DELETE"></a>
###### DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_DELETE_CHILD"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_DELETE_CHILD"></a>
###### DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
###### READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
###### WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_READ_ACL"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_READ_ACL"></a>
###### READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ACL"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ACL"></a>
###### WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_OWNER"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_OWNER"></a>
###### WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_SYNCHRONIZE"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i0_SYNCHRONIZE"></a>
###### SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i1"></a>
###### [NFS4ACE_BasicPerms](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i1)

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i1_BASIC"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_perms_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only
###### Must be one of:

- "FULL_CONTROL"
- "MODIFY"
- "READ"
- "TRAVERSE"

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_flags"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags"></a>
###### flags (required)

- Schema name: `Flags`

Inheritance and other behavioral flags for this ACE.
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0"></a>
###### [NFS4ACE_AdvancedFlags](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0_FILE_INHERIT"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0_FILE_INHERIT"></a>
###### FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
###### DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
###### NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0_INHERIT_ONLY"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0_INHERIT_ONLY"></a>
###### INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0_INHERITED"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i0_INHERITED"></a>
###### INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i1"></a>
###### [NFS4ACE_BasicFlags](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i1)

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i1_BASIC"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_flags_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects
###### Must be one of:

- "INHERIT"
- "NOINHERIT"

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

UID or GID when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i0_items_who"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="Return_value_anyOf_i0_items_acl_anyOf_i0_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i0_items_who_anyOf_i2)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items"></a>
###### POSIXACE

- Schema name: `POSIXACE`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i1_items_tag"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this POSIX ACE. `USER_OBJ`: File/directory owner `GROUP_OBJ`: File/directory primary group `OTHER`: All other users `MASK`: Maximum permissions for named users and groups `USER`: Specific user account `GROUP`: Specific group
###### Must be one of:

- "USER_OBJ"
- "GROUP_OBJ"
- "OTHER"
- "MASK"
- "USER"
- "GROUP"

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i1_items_perms"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items_perms"></a>
###### perms (required)

- Schema name: `POSIXACE_Perms`
- Type: object

Read, write, and execute permissions for this ACE.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i1_items_perms_READ"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items_perms_READ"></a>
###### READ (required)

- Schema name: `Read`
- Type: boolean

Permission to read file contents or list directory contents.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i1_items_perms_WRITE"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items_perms_WRITE"></a>
###### WRITE (required)

- Schema name: `Write`
- Type: boolean

Permission to write file contents or create/delete files in directory.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i1_items_perms_EXECUTE"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items_perms_EXECUTE"></a>
###### EXECUTE (required)

- Schema name: `Execute`
- Type: boolean

Permission to execute files or traverse directories.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i1_items_default"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items_default"></a>
###### default (required)

- Schema name: `Default`
- Type: boolean

Whether this is a default ACE that applies to newly created child objects.

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i1_items_id"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

Numeric user or group ID when tag is `USER` or `GROUP`. `null` for object entries.
<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1_items_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_acl_anyOf_i1_items_who"></a>
<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when tag is `USER` or `GROUP`. `null` for object entries.
<a id="Return_value_anyOf_i0_items_acl_anyOf_i1_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i0_items_acl_anyOf_i1_items_who_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_comment"></a>
<a id="Return_value_anyOf_i0_items_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string

Optional descriptive comment about the template's purpose.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [ACLTemplateQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `ACLTemplateQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the ACL template.

<a id="headingReturn_value_anyOf_i1_builtin"></a>
<a id="Return_value_anyOf_i1_builtin"></a>
###### builtin

- Schema name: `Builtin`
- Type: boolean

Whether this is a built-in system template or user-created.

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name

- Schema name: `Name`
- Type: string

Human-readable name for the ACL template.

<a id="headingReturn_value_anyOf_i1_acltype"></a>
<a id="Return_value_anyOf_i1_acltype"></a>
###### acltype

- Schema name: `Acltype`
- Type: enum (of string)

ACL type this template provides.
###### Must be one of:

- "NFS4"
- "POSIX1E"

<a id="headingReturn_value_anyOf_i1_acl"></a>
<a id="Return_value_anyOf_i1_acl"></a>
###### acl

- Schema name: `Acl`

Array of Access Control Entries defined by this template.
<a id="Return_value_anyOf_i1_acl_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_acl_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_acl_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_acl_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_Return_value_anyOf_i1_acl_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_acl_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_acl_anyOf_i1_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i1_comment"></a>
<a id="Return_value_anyOf_i1_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string

Optional descriptive comment about the template's purpose.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
