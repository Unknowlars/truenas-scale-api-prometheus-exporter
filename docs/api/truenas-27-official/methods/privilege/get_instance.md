---
title: privilege.get_instance
kind: method
source_rst: _sources/api_methods_privilege.get_instance.rst.txt
source_html: api_methods_privilege.get_instance.html
required_roles:
  - PRIVILEGE_READ
---

# privilege.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `PRIVILEGE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
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
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

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

- Schema name: `PrivilegeEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the privilege.

<a id="headingReturn_value_builtin_name"></a>
<a id="Return_value_builtin_name"></a>
#### builtin_name (required)

- Schema name: `Builtin Name`

Name of the built-in privilege if this is a system privilege. `null` for custom privileges.
<a id="Return_value_builtin_name_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_builtin_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_builtin_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_builtin_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_builtin_name_anyOf_i1)

- Type: null

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Display name of the privilege.
- Must be at least `1` characters long

<a id="headingReturn_value_local_groups"></a>
<a id="Return_value_local_groups"></a>
#### local_groups (required)

- Schema name: `Local Groups`
- Type: array

Array of local groups assigned to this privilege.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_local_groups_items"></a>
<a id="Return_value_local_groups_items_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_local_groups_items_anyOf_i0"></a>
###### [GroupEntry](#tab-pane_Return_value_local_groups_items_anyOf_i0)

- Schema name: `GroupEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_local_groups_items_anyOf_i0_id"></a>
<a id="Return_value_local_groups_items_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

<a id="headingReturn_value_local_groups_items_anyOf_i0_gid"></a>
<a id="Return_value_local_groups_items_anyOf_i0_gid"></a>
###### gid (required)

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

<a id="headingReturn_value_local_groups_items_anyOf_i0_name"></a>
<a id="Return_value_local_groups_items_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

<a id="headingReturn_value_local_groups_items_anyOf_i0_builtin"></a>
<a id="Return_value_local_groups_items_anyOf_i0_builtin"></a>
###### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

<a id="headingReturn_value_local_groups_items_anyOf_i0_sudo_commands"></a>
<a id="Return_value_local_groups_items_anyOf_i0_sudo_commands"></a>
###### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_local_groups_items_anyOf_i0_sudo_commands_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_local_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
<a id="Return_value_local_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
###### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_local_groups_items_anyOf_i0_sudo_commands_nopasswd_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_local_groups_items_anyOf_i0_smb"></a>
<a id="Return_value_local_groups_items_anyOf_i0_smb"></a>
###### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

<a id="headingReturn_value_local_groups_items_anyOf_i0_userns_idmap"></a>
<a id="Return_value_local_groups_items_anyOf_i0_userns_idmap"></a>
###### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
<a id="Return_value_local_groups_items_anyOf_i0_userns_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_local_groups_items_anyOf_i0_userns_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_local_groups_items_anyOf_i0_userns_idmap_anyOf_i0)

- Type: const
- Specific value: `"DIRECT"`

<a id="tab-pane_Return_value_local_groups_items_anyOf_i0_userns_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_local_groups_items_anyOf_i0_userns_idmap_anyOf_i1)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

<a id="tab-pane_Return_value_local_groups_items_anyOf_i0_userns_idmap_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_local_groups_items_anyOf_i0_userns_idmap_anyOf_i2)

- Type: null

<a id="headingReturn_value_local_groups_items_anyOf_i0_group"></a>
<a id="Return_value_local_groups_items_anyOf_i0_group"></a>
###### group (required)

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

<a id="headingReturn_value_local_groups_items_anyOf_i0_local"></a>
<a id="Return_value_local_groups_items_anyOf_i0_local"></a>
###### local (required)

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

<a id="headingReturn_value_local_groups_items_anyOf_i0_sid"></a>
<a id="Return_value_local_groups_items_anyOf_i0_sid"></a>
###### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
<a id="Return_value_local_groups_items_anyOf_i0_sid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_local_groups_items_anyOf_i0_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_local_groups_items_anyOf_i0_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_local_groups_items_anyOf_i0_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_local_groups_items_anyOf_i0_sid_anyOf_i1)

- Type: null

<a id="headingReturn_value_local_groups_items_anyOf_i0_roles"></a>
<a id="Return_value_local_groups_items_anyOf_i0_roles"></a>
###### roles (required)

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_local_groups_items_anyOf_i0_roles_items"></a>
- Type: string

<a id="headingReturn_value_local_groups_items_anyOf_i0_users"></a>
<a id="Return_value_local_groups_items_anyOf_i0_users"></a>
###### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_local_groups_items_anyOf_i0_users_items"></a>
- Type: integer

<a id="headingReturn_value_local_groups_items_anyOf_i0_immutable"></a>
<a id="Return_value_local_groups_items_anyOf_i0_immutable"></a>
###### immutable (required)

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

<a id="tab-pane_Return_value_local_groups_items_anyOf_i1"></a>
###### [UnmappedGroupEntry](#tab-pane_Return_value_local_groups_items_anyOf_i1)

- Schema name: `UnmappedGroupEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_local_groups_items_anyOf_i1_gid"></a>
<a id="Return_value_local_groups_items_anyOf_i1_gid"></a>
###### gid (required)

- Schema name: `Gid`

Group ID if this is a local group that couldn't be mapped. `null` for directory service groups.
<a id="Return_value_local_groups_items_anyOf_i1_gid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_local_groups_items_anyOf_i1_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_local_groups_items_anyOf_i1_gid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_local_groups_items_anyOf_i1_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_local_groups_items_anyOf_i1_gid_anyOf_i1)

- Type: null

<a id="headingReturn_value_local_groups_items_anyOf_i1_sid"></a>
<a id="Return_value_local_groups_items_anyOf_i1_sid"></a>
###### sid (required)

- Schema name: `Sid`

Security identifier if this is a directory service group that couldn't be mapped. `null` for local groups.
<a id="Return_value_local_groups_items_anyOf_i1_sid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_local_groups_items_anyOf_i1_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_local_groups_items_anyOf_i1_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_local_groups_items_anyOf_i1_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_local_groups_items_anyOf_i1_sid_anyOf_i1)

- Type: null

<a id="headingReturn_value_local_groups_items_anyOf_i1_group"></a>
<a id="Return_value_local_groups_items_anyOf_i1_group"></a>
###### group (required)

- Schema name: `Group`
- Type: null

Always `null` for unmapped groups.

<a id="headingReturn_value_ds_groups"></a>
<a id="Return_value_ds_groups"></a>
#### ds_groups (required)

- Schema name: `Ds Groups`
- Type: array

Array of directory service groups assigned to this privilege.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_ds_groups_items"></a>
<a id="Return_value_ds_groups_items_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i0"></a>
###### [GroupEntry](#tab-pane_Return_value_ds_groups_items_anyOf_i0)

- Schema name: `GroupEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_ds_groups_items_anyOf_i0_id"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

<a id="headingReturn_value_ds_groups_items_anyOf_i0_gid"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_gid"></a>
###### gid (required)

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

<a id="headingReturn_value_ds_groups_items_anyOf_i0_name"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

<a id="headingReturn_value_ds_groups_items_anyOf_i0_builtin"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_builtin"></a>
###### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

<a id="headingReturn_value_ds_groups_items_anyOf_i0_sudo_commands"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_sudo_commands"></a>
###### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_ds_groups_items_anyOf_i0_sudo_commands_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_ds_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
###### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_ds_groups_items_anyOf_i0_sudo_commands_nopasswd_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_ds_groups_items_anyOf_i0_smb"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_smb"></a>
###### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

<a id="headingReturn_value_ds_groups_items_anyOf_i0_userns_idmap"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_userns_idmap"></a>
###### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
<a id="Return_value_ds_groups_items_anyOf_i0_userns_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i0)

- Type: const
- Specific value: `"DIRECT"`

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i1)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i2)

- Type: null

<a id="headingReturn_value_ds_groups_items_anyOf_i0_group"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_group"></a>
###### group (required)

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

<a id="headingReturn_value_ds_groups_items_anyOf_i0_local"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_local"></a>
###### local (required)

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

<a id="headingReturn_value_ds_groups_items_anyOf_i0_sid"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_sid"></a>
###### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
<a id="Return_value_ds_groups_items_anyOf_i0_sid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i0_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ds_groups_items_anyOf_i0_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i0_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ds_groups_items_anyOf_i0_sid_anyOf_i1)

- Type: null

<a id="headingReturn_value_ds_groups_items_anyOf_i0_roles"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_roles"></a>
###### roles (required)

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_ds_groups_items_anyOf_i0_roles_items"></a>
- Type: string

<a id="headingReturn_value_ds_groups_items_anyOf_i0_users"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_users"></a>
###### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_ds_groups_items_anyOf_i0_users_items"></a>
- Type: integer

<a id="headingReturn_value_ds_groups_items_anyOf_i0_immutable"></a>
<a id="Return_value_ds_groups_items_anyOf_i0_immutable"></a>
###### immutable (required)

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i1"></a>
###### [UnmappedGroupEntry](#tab-pane_Return_value_ds_groups_items_anyOf_i1)

- Schema name: `UnmappedGroupEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_ds_groups_items_anyOf_i1_gid"></a>
<a id="Return_value_ds_groups_items_anyOf_i1_gid"></a>
###### gid (required)

- Schema name: `Gid`

Group ID if this is a local group that couldn't be mapped. `null` for directory service groups.
<a id="Return_value_ds_groups_items_anyOf_i1_gid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i1_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ds_groups_items_anyOf_i1_gid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i1_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ds_groups_items_anyOf_i1_gid_anyOf_i1)

- Type: null

<a id="headingReturn_value_ds_groups_items_anyOf_i1_sid"></a>
<a id="Return_value_ds_groups_items_anyOf_i1_sid"></a>
###### sid (required)

- Schema name: `Sid`

Security identifier if this is a directory service group that couldn't be mapped. `null` for local groups.
<a id="Return_value_ds_groups_items_anyOf_i1_sid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i1_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ds_groups_items_anyOf_i1_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_ds_groups_items_anyOf_i1_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ds_groups_items_anyOf_i1_sid_anyOf_i1)

- Type: null

<a id="headingReturn_value_ds_groups_items_anyOf_i1_group"></a>
<a id="Return_value_ds_groups_items_anyOf_i1_group"></a>
###### group (required)

- Schema name: `Group`
- Type: null

Always `null` for unmapped groups.

<a id="headingReturn_value_roles"></a>
<a id="Return_value_roles"></a>
#### roles

- Schema name: `Roles`
- Type: array of string
- Default: []

Array of role names included in this privilege.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_roles_items"></a>
- Type: string

<a id="headingReturn_value_web_shell"></a>
<a id="Return_value_web_shell"></a>
#### web_shell (required)

- Schema name: `Web Shell`
- Type: boolean

Whether this privilege grants access to the web shell.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
