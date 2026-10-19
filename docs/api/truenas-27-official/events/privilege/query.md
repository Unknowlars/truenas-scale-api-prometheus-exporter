---
title: privilege.query
kind: event
source_rst: _sources/api_events_privilege.query.rst.txt
source_html: api_events_privilege.query.html
required_roles:
  - PRIVILEGE_READ
---

# privilege.query

## Summary

Sent on privilege changes.

## Required Roles

- `PRIVILEGE_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `PrivilegeAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `PrivilegeEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the privilege.

<a id="headingADDED_fields_builtin_name"></a>
<a id="ADDED_fields_builtin_name"></a>
##### builtin_name (required)

- Schema name: `Builtin Name`

Name of the built-in privilege if this is a system privilege. `null` for custom privileges.
<a id="ADDED_fields_builtin_name_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_builtin_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_builtin_name_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_builtin_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_builtin_name_anyOf_i1)

- Type: null

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Display name of the privilege. Must be unique.
- Must be at least `1` characters long

<a id="headingADDED_fields_local_groups"></a>
<a id="ADDED_fields_local_groups"></a>
##### local_groups (required)

- Schema name: `Local Groups`
- Type: array

Array of local groups assigned to this privilege.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_local_groups_items"></a>
<a id="ADDED_fields_local_groups_items_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i0"></a>
###### [GroupEntry](#tab-pane_ADDED_fields_local_groups_items_anyOf_i0)

- Schema name: `GroupEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_local_groups_items_anyOf_i0_id"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

<a id="headingADDED_fields_local_groups_items_anyOf_i0_gid"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_gid"></a>
###### gid (required)

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

<a id="headingADDED_fields_local_groups_items_anyOf_i0_name"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

<a id="headingADDED_fields_local_groups_items_anyOf_i0_builtin"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_builtin"></a>
###### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

<a id="headingADDED_fields_local_groups_items_anyOf_i0_sudo_commands"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_sudo_commands"></a>
###### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_local_groups_items_anyOf_i0_sudo_commands_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_local_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
###### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_local_groups_items_anyOf_i0_sudo_commands_nopasswd_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_local_groups_items_anyOf_i0_smb"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_smb"></a>
###### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

<a id="headingADDED_fields_local_groups_items_anyOf_i0_userns_idmap"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_userns_idmap"></a>
###### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
<a id="ADDED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i0)

- Type: const
- Specific value: `"DIRECT"`

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i1)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i2"></a>
###### [Option 3](#tab-pane_ADDED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i2)

- Type: null

<a id="headingADDED_fields_local_groups_items_anyOf_i0_group"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_group"></a>
###### group (required)

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

<a id="headingADDED_fields_local_groups_items_anyOf_i0_local"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_local"></a>
###### local (required)

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

<a id="headingADDED_fields_local_groups_items_anyOf_i0_sid"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_sid"></a>
###### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
<a id="ADDED_fields_local_groups_items_anyOf_i0_sid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i0_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_local_groups_items_anyOf_i0_sid_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i0_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_local_groups_items_anyOf_i0_sid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_local_groups_items_anyOf_i0_roles"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_roles"></a>
###### roles (required)

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_local_groups_items_anyOf_i0_roles_items"></a>
- Type: string

<a id="headingADDED_fields_local_groups_items_anyOf_i0_users"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_users"></a>
###### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_local_groups_items_anyOf_i0_users_items"></a>
- Type: integer

<a id="headingADDED_fields_local_groups_items_anyOf_i0_immutable"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i0_immutable"></a>
###### immutable (required)

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i1"></a>
###### [UnmappedGroupEntry](#tab-pane_ADDED_fields_local_groups_items_anyOf_i1)

- Schema name: `UnmappedGroupEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_local_groups_items_anyOf_i1_gid"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i1_gid"></a>
###### gid (required)

- Schema name: `Gid`

Group ID if this is a local group that couldn't be mapped. `null` for directory service groups.
<a id="ADDED_fields_local_groups_items_anyOf_i1_gid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i1_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_local_groups_items_anyOf_i1_gid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i1_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_local_groups_items_anyOf_i1_gid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_local_groups_items_anyOf_i1_sid"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i1_sid"></a>
###### sid (required)

- Schema name: `Sid`

Security identifier if this is a directory service group that couldn't be mapped. `null` for local groups.
<a id="ADDED_fields_local_groups_items_anyOf_i1_sid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i1_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_local_groups_items_anyOf_i1_sid_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_local_groups_items_anyOf_i1_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_local_groups_items_anyOf_i1_sid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_local_groups_items_anyOf_i1_group"></a>
<a id="ADDED_fields_local_groups_items_anyOf_i1_group"></a>
###### group (required)

- Schema name: `Group`
- Type: null

Always `null` for unmapped groups.

<a id="headingADDED_fields_ds_groups"></a>
<a id="ADDED_fields_ds_groups"></a>
##### ds_groups (required)

- Schema name: `Ds Groups`
- Type: array

Array of directory service groups assigned to this privilege.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_ds_groups_items"></a>
<a id="ADDED_fields_ds_groups_items_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i0"></a>
###### [GroupEntry](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i0)

- Schema name: `GroupEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_ds_groups_items_anyOf_i0_id"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_gid"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_gid"></a>
###### gid (required)

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_name"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_builtin"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_builtin"></a>
###### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_sudo_commands"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_sudo_commands"></a>
###### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_ds_groups_items_anyOf_i0_sudo_commands_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
###### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_ds_groups_items_anyOf_i0_sudo_commands_nopasswd_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_smb"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_smb"></a>
###### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_userns_idmap"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_userns_idmap"></a>
###### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
<a id="ADDED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i0)

- Type: const
- Specific value: `"DIRECT"`

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i1)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i2"></a>
###### [Option 3](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i2)

- Type: null

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_group"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_group"></a>
###### group (required)

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_local"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_local"></a>
###### local (required)

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_sid"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_sid"></a>
###### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
<a id="ADDED_fields_ds_groups_items_anyOf_i0_sid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i0_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i0_sid_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i0_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i0_sid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_roles"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_roles"></a>
###### roles (required)

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_ds_groups_items_anyOf_i0_roles_items"></a>
- Type: string

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_users"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_users"></a>
###### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_ds_groups_items_anyOf_i0_users_items"></a>
- Type: integer

<a id="headingADDED_fields_ds_groups_items_anyOf_i0_immutable"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i0_immutable"></a>
###### immutable (required)

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i1"></a>
###### [UnmappedGroupEntry](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i1)

- Schema name: `UnmappedGroupEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_ds_groups_items_anyOf_i1_gid"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i1_gid"></a>
###### gid (required)

- Schema name: `Gid`

Group ID if this is a local group that couldn't be mapped. `null` for directory service groups.
<a id="ADDED_fields_ds_groups_items_anyOf_i1_gid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i1_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i1_gid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i1_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i1_gid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_ds_groups_items_anyOf_i1_sid"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i1_sid"></a>
###### sid (required)

- Schema name: `Sid`

Security identifier if this is a directory service group that couldn't be mapped. `null` for local groups.
<a id="ADDED_fields_ds_groups_items_anyOf_i1_sid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i1_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i1_sid_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_ds_groups_items_anyOf_i1_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_ds_groups_items_anyOf_i1_sid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_ds_groups_items_anyOf_i1_group"></a>
<a id="ADDED_fields_ds_groups_items_anyOf_i1_group"></a>
###### group (required)

- Schema name: `Group`
- Type: null

Always `null` for unmapped groups.

<a id="headingADDED_fields_roles"></a>
<a id="ADDED_fields_roles"></a>
##### roles

- Schema name: `Roles`
- Type: array of string
- Default: []

Array of role names included in this privilege.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_roles_items"></a>
- Type: string

<a id="headingADDED_fields_web_shell"></a>
<a id="ADDED_fields_web_shell"></a>
##### web_shell (required)

- Schema name: `Web Shell`
- Type: boolean

Whether this privilege grants access to the web shell.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `PrivilegeChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `PrivilegeEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the privilege.

<a id="headingCHANGED_fields_builtin_name"></a>
<a id="CHANGED_fields_builtin_name"></a>
##### builtin_name (required)

- Schema name: `Builtin Name`

Name of the built-in privilege if this is a system privilege. `null` for custom privileges.
<a id="CHANGED_fields_builtin_name_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_builtin_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_builtin_name_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_builtin_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_builtin_name_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Display name of the privilege. Must be unique.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_local_groups"></a>
<a id="CHANGED_fields_local_groups"></a>
##### local_groups (required)

- Schema name: `Local Groups`
- Type: array

Array of local groups assigned to this privilege.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_local_groups_items"></a>
<a id="CHANGED_fields_local_groups_items_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i0"></a>
###### [GroupEntry](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i0)

- Schema name: `GroupEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_id"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_gid"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_gid"></a>
###### gid (required)

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_name"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_builtin"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_builtin"></a>
###### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_sudo_commands"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_sudo_commands"></a>
###### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_local_groups_items_anyOf_i0_sudo_commands_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
###### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_local_groups_items_anyOf_i0_sudo_commands_nopasswd_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_smb"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_smb"></a>
###### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_userns_idmap"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_userns_idmap"></a>
###### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
<a id="CHANGED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i0)

- Type: const
- Specific value: `"DIRECT"`

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i1)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i2"></a>
###### [Option 3](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i0_userns_idmap_anyOf_i2)

- Type: null

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_group"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_group"></a>
###### group (required)

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_local"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_local"></a>
###### local (required)

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_sid"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_sid"></a>
###### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
<a id="CHANGED_fields_local_groups_items_anyOf_i0_sid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i0_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i0_sid_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i0_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i0_sid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_roles"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_roles"></a>
###### roles (required)

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_local_groups_items_anyOf_i0_roles_items"></a>
- Type: string

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_users"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_users"></a>
###### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_local_groups_items_anyOf_i0_users_items"></a>
- Type: integer

<a id="headingCHANGED_fields_local_groups_items_anyOf_i0_immutable"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i0_immutable"></a>
###### immutable (required)

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i1"></a>
###### [UnmappedGroupEntry](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i1)

- Schema name: `UnmappedGroupEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_local_groups_items_anyOf_i1_gid"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i1_gid"></a>
###### gid (required)

- Schema name: `Gid`

Group ID if this is a local group that couldn't be mapped. `null` for directory service groups.
<a id="CHANGED_fields_local_groups_items_anyOf_i1_gid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i1_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i1_gid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i1_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i1_gid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_local_groups_items_anyOf_i1_sid"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i1_sid"></a>
###### sid (required)

- Schema name: `Sid`

Security identifier if this is a directory service group that couldn't be mapped. `null` for local groups.
<a id="CHANGED_fields_local_groups_items_anyOf_i1_sid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i1_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i1_sid_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_local_groups_items_anyOf_i1_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_local_groups_items_anyOf_i1_sid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_local_groups_items_anyOf_i1_group"></a>
<a id="CHANGED_fields_local_groups_items_anyOf_i1_group"></a>
###### group (required)

- Schema name: `Group`
- Type: null

Always `null` for unmapped groups.

<a id="headingCHANGED_fields_ds_groups"></a>
<a id="CHANGED_fields_ds_groups"></a>
##### ds_groups (required)

- Schema name: `Ds Groups`
- Type: array

Array of directory service groups assigned to this privilege.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_ds_groups_items"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0"></a>
###### [GroupEntry](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0)

- Schema name: `GroupEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_id"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_gid"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_gid"></a>
###### gid (required)

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_name"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_builtin"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_builtin"></a>
###### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_sudo_commands"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_sudo_commands"></a>
###### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_ds_groups_items_anyOf_i0_sudo_commands_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_sudo_commands_nopasswd"></a>
###### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_ds_groups_items_anyOf_i0_sudo_commands_nopasswd_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_smb"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_smb"></a>
###### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_userns_idmap"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_userns_idmap"></a>
###### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i0)

- Type: const
- Specific value: `"DIRECT"`

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i1)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i2"></a>
###### [Option 3](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0_userns_idmap_anyOf_i2)

- Type: null

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_group"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_group"></a>
###### group (required)

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_local"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_local"></a>
###### local (required)

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_sid"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_sid"></a>
###### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_sid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0_sid_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i0_sid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_roles"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_roles"></a>
###### roles (required)

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_ds_groups_items_anyOf_i0_roles_items"></a>
- Type: string

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_users"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_users"></a>
###### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_ds_groups_items_anyOf_i0_users_items"></a>
- Type: integer

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i0_immutable"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i0_immutable"></a>
###### immutable (required)

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i1"></a>
###### [UnmappedGroupEntry](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i1)

- Schema name: `UnmappedGroupEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_ds_groups_items_anyOf_i1_gid"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i1_gid"></a>
###### gid (required)

- Schema name: `Gid`

Group ID if this is a local group that couldn't be mapped. `null` for directory service groups.
<a id="CHANGED_fields_ds_groups_items_anyOf_i1_gid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i1_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i1_gid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i1_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i1_gid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i1_sid"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i1_sid"></a>
###### sid (required)

- Schema name: `Sid`

Security identifier if this is a directory service group that couldn't be mapped. `null` for local groups.
<a id="CHANGED_fields_ds_groups_items_anyOf_i1_sid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i1_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i1_sid_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_ds_groups_items_anyOf_i1_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_ds_groups_items_anyOf_i1_sid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_ds_groups_items_anyOf_i1_group"></a>
<a id="CHANGED_fields_ds_groups_items_anyOf_i1_group"></a>
###### group (required)

- Schema name: `Group`
- Type: null

Always `null` for unmapped groups.

<a id="headingCHANGED_fields_roles"></a>
<a id="CHANGED_fields_roles"></a>
##### roles

- Schema name: `Roles`
- Type: array of string
- Default: []

Array of role names included in this privilege.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_roles_items"></a>
- Type: string

<a id="headingCHANGED_fields_web_shell"></a>
<a id="CHANGED_fields_web_shell"></a>
##### web_shell (required)

- Schema name: `Web Shell`
- Type: boolean

Whether this privilege grants access to the web shell.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `PrivilegeRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
