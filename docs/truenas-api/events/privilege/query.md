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

### ADDED

- Schema name: `PrivilegeAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `PrivilegeEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the privilege.

##### builtin_name (required)

- Schema name: `Builtin Name`

Name of the built-in privilege if this is a system privilege. `null` for custom privileges.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### name (required)

- Schema name: `Name`
- Type: string

Display name of the privilege.
- Must be at least `1` characters long

##### local_groups (required)

- Schema name: `Local Groups`
- Type: array

Array of local groups assigned to this privilege.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## GroupEntry

- Schema name: `GroupEntry`
- Type: object
- No Additional Properties
######### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

######### gid (required)

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

######### name (required)

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

######### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

######### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

########## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

######### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

########## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

######### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

######### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
########## Any of

########### Option 1

- Type: const

########### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

########### Option 3

- Type: null

######### group (required)

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

######### local (required)

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

######### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### roles (required)

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

########## Each item of this array must be:

- Type: string

######### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

########## Each item of this array must be:

- Type: integer

######### immutable (required)

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

######## UnmappedGroupEntry

- Type: const

######## Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

######## Option 2

- Type: null

######## Option 3

- Type: string

######## Option 1

- Type: null

######## Option 2

- Schema name: `UnmappedGroupEntry`
- Type: object
- No Additional Properties
######### gid (required)

- Schema name: `Gid`

Group ID if this is a local group that couldn't be mapped. `null` for directory service groups.
########## Any of

########### Option 1

- Type: integer

########### Option 2

- Type: null

######### sid (required)

- Schema name: `Sid`

Security identifier if this is a directory service group that couldn't be mapped. `null` for local groups.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### group (required)

- Schema name: `Group`
- Type: null

Always `null` for unmapped groups.

######## Option 1

- Type: integer

######## Option 2

- Type: null

######## Option 1

- Type: string

######## Option 2

- Type: null

##### ds_groups (required)

- Schema name: `Ds Groups`
- Type: array

Array of directory service groups assigned to this privilege.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## GroupEntry

- Schema name: `GroupEntry`
- Type: object
- No Additional Properties
######### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

######### gid (required)

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

######### name (required)

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

######### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

######### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

########## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

######### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

########## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

######### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

######### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
########## Any of

########### Option 1

- Type: const

########### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

########### Option 3

- Type: null

######### group (required)

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

######### local (required)

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

######### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### roles (required)

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

########## Each item of this array must be:

- Type: string

######### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

########## Each item of this array must be:

- Type: integer

######### immutable (required)

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

######## UnmappedGroupEntry

- Type: const

######## Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

######## Option 2

- Type: null

######## Option 3

- Type: string

######## Option 1

- Type: null

######## Option 2

- Schema name: `UnmappedGroupEntry`
- Type: object
- No Additional Properties
######### gid (required)

- Schema name: `Gid`

Group ID if this is a local group that couldn't be mapped. `null` for directory service groups.
########## Any of

########### Option 1

- Type: integer

########### Option 2

- Type: null

######### sid (required)

- Schema name: `Sid`

Security identifier if this is a directory service group that couldn't be mapped. `null` for local groups.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### group (required)

- Schema name: `Group`
- Type: null

Always `null` for unmapped groups.

######## Option 1

- Type: integer

######## Option 2

- Type: null

######## Option 1

- Type: string

######## Option 2

- Type: null

##### roles

- Schema name: `Roles`
- Type: array of string
- Default: []

Array of role names included in this privilege.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### web_shell (required)

- Schema name: `Web Shell`
- Type: boolean

Whether this privilege grants access to the web shell.

### CHANGED

- Schema name: `PrivilegeChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `PrivilegeEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the privilege.

##### builtin_name (required)

- Schema name: `Builtin Name`

Name of the built-in privilege if this is a system privilege. `null` for custom privileges.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### name (required)

- Schema name: `Name`
- Type: string

Display name of the privilege.
- Must be at least `1` characters long

##### local_groups (required)

- Schema name: `Local Groups`
- Type: array

Array of local groups assigned to this privilege.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## GroupEntry

- Schema name: `GroupEntry`
- Type: object
- No Additional Properties
######### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

######### gid (required)

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

######### name (required)

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

######### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

######### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

########## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

######### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

########## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

######### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

######### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
########## Any of

########### Option 1

- Type: const

########### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

########### Option 3

- Type: null

######### group (required)

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

######### local (required)

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

######### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### roles (required)

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

########## Each item of this array must be:

- Type: string

######### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

########## Each item of this array must be:

- Type: integer

######### immutable (required)

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

######## UnmappedGroupEntry

- Type: const

######## Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

######## Option 2

- Type: null

######## Option 3

- Type: string

######## Option 1

- Type: null

######## Option 2

- Schema name: `UnmappedGroupEntry`
- Type: object
- No Additional Properties
######### gid (required)

- Schema name: `Gid`

Group ID if this is a local group that couldn't be mapped. `null` for directory service groups.
########## Any of

########### Option 1

- Type: integer

########### Option 2

- Type: null

######### sid (required)

- Schema name: `Sid`

Security identifier if this is a directory service group that couldn't be mapped. `null` for local groups.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### group (required)

- Schema name: `Group`
- Type: null

Always `null` for unmapped groups.

######## Option 1

- Type: integer

######## Option 2

- Type: null

######## Option 1

- Type: string

######## Option 2

- Type: null

##### ds_groups (required)

- Schema name: `Ds Groups`
- Type: array

Array of directory service groups assigned to this privilege.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## GroupEntry

- Schema name: `GroupEntry`
- Type: object
- No Additional Properties
######### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the group. Use this ID for `group.update` and `group.delete` API calls. This ID also appears in the `groups` array for each user entry in `user.query` results. NOTE: For groups from a directory service, the `id` is calculated by adding 100000000 to the `gid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

######### gid (required)

- Schema name: `Gid`
- Type: integer

A non-negative integer used to identify a group. TrueNAS uses this value for permission checks and many other system purposes.

######### name (required)

- Schema name: `Name`
- Type: string

A string used to identify a group.
- Must be at least `1` characters long

######### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `True`, the group is an internal system account for the TrueNAS server. Typically, one should create dedicated groups for access to the TrueNAS server webui and shares.

######### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

########## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

######### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

########## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

######### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

######### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
########## Any of

########### Option 1

- Type: const

########### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

########### Option 3

- Type: null

######### group (required)

- Schema name: `Group`
- Type: string

A string used to identify a group. Identical to the `name` key.
- Must be at least `1` characters long

######### local (required)

- Schema name: `Local`
- Type: boolean

If `True`, the group is local to the TrueNAS server. If `False`, the group is provided by a directory service.

######### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### roles (required)

- Schema name: `Roles`
- Type: array of string

List of roles assigned to this groups. Roles control administrative access to TrueNAS through the web UI and API. You can change group roles by using `privilege.create`, `privilege.update`, and `privilege.delete`.
- No Additional Items

########## Each item of this array must be:

- Type: string

######### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

########## Each item of this array must be:

- Type: integer

######### immutable (required)

- Schema name: `Immutable`
- Type: boolean

This is a read-only field showing if the group entry can be changed. If `True`, the group is immutable and cannot be changed. If `False`, the group can be changed.

######## UnmappedGroupEntry

- Type: const

######## Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

######## Option 2

- Type: null

######## Option 3

- Type: string

######## Option 1

- Type: null

######## Option 2

- Schema name: `UnmappedGroupEntry`
- Type: object
- No Additional Properties
######### gid (required)

- Schema name: `Gid`

Group ID if this is a local group that couldn't be mapped. `null` for directory service groups.
########## Any of

########### Option 1

- Type: integer

########### Option 2

- Type: null

######### sid (required)

- Schema name: `Sid`

Security identifier if this is a directory service group that couldn't be mapped. `null` for local groups.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### group (required)

- Schema name: `Group`
- Type: null

Always `null` for unmapped groups.

######## Option 1

- Type: integer

######## Option 2

- Type: null

######## Option 1

- Type: string

######## Option 2

- Type: null

##### roles

- Schema name: `Roles`
- Type: array of string
- Default: []

Array of role names included in this privilege.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### web_shell (required)

- Schema name: `Web Shell`
- Type: boolean

Whether this privilege grants access to the web shell.

### REMOVED

- Schema name: `PrivilegeRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
