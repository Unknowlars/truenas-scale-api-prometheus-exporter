---
title: group.update
kind: method
source_rst: _sources/api_methods_group.update.rst.txt
source_html: api_methods_group.update.html
required_roles:
  - ACCOUNT_WRITE
---

# group.update

## Summary

Update attributes of an existing group.

## Required Roles

- `ACCOUNT_WRITE`

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

The API identifier of the group to update.

#### Parameter 2: group_update

<a id="Call_parameters_items_i1"></a>
#### group_update

- Schema name: `group_update`
- Type: object

Updated group configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_name"></a>
<a id="Call_parameters_items_i1_name"></a>
##### name

- Schema name: `Name`
- Type: string

A string used to identify a group.

<a id="headingCall_parameters_items_i1_sudo_commands"></a>
<a id="Call_parameters_items_i1_sudo_commands"></a>
##### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_sudo_commands_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_sudo_commands_nopasswd"></a>
<a id="Call_parameters_items_i1_sudo_commands_nopasswd"></a>
##### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_sudo_commands_nopasswd_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_smb"></a>
<a id="Call_parameters_items_i1_smb"></a>
##### smb

- Schema name: `Smb`
- Type: boolean

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

<a id="headingCall_parameters_items_i1_userns_idmap"></a>
<a id="Call_parameters_items_i1_userns_idmap"></a>
##### userns_idmap

- Schema name: `Userns Idmap`

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
<a id="Call_parameters_items_i1_userns_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_userns_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_userns_idmap_anyOf_i0)

- Type: const
- Specific value: `"DIRECT"`

<a id="tab-pane_Call_parameters_items_i1_userns_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_userns_idmap_anyOf_i1)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

<a id="tab-pane_Call_parameters_items_i1_userns_idmap_anyOf_i2"></a>
###### [Option 3](#tab-pane_Call_parameters_items_i1_userns_idmap_anyOf_i2)

- Type: null

<a id="headingCall_parameters_items_i1_users"></a>
<a id="Call_parameters_items_i1_users"></a>
##### users

- Schema name: `Users`
- Type: array of integer

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_users_items"></a>
- Type: integer

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: integer

The API identifier of the updated group.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
