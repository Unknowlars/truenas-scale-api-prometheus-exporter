---
title: group.create
kind: method
source_rst: _sources/api_methods_group.create.rst.txt
source_html: api_methods_group.create.html
required_roles:
  - ACCOUNT_WRITE
---

# group.create

## Summary

Create a new group.

## Required Roles

- `ACCOUNT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: group_create

#### group_create

- Schema name: `group_create`
- Type: object

Group configuration data for the new group.
- No Additional Properties
##### gid

- Schema name: `Gid`
- Default: null

If `null`, it is automatically filled with the next one available.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `90000000`

####### Option 2

- Type: null

##### name (required)

- Schema name: `Name`
- Type: string

##### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string
- Default: []

A list of commands that group members may execute with elevated privileges. User is not prompted for password when executing any command from the list.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

If set to `True`, the group can be used for SMB share ACL entries. The group is mapped to an NT group account on the TrueNAS SMB server and has a `sid` value.

##### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subgid mapping for this group. If DIRECT then the GID will be directly mapped to all containers. Alternatively, the target GID may be explicitly specified. If null, then the GID will not be mapped. **NOTE: This field will be ignored for groups that have been assigned TrueNAS roles.**
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

####### Option 3

- Type: null

##### users

- Schema name: `Users`
- Type: array of integer
- Default: []

A list a API user identifiers for local users who are members of this group. These IDs match the `id` field from `user.query`. NOTE: This field is empty for groups that come from directory services (`local` is `False`).
- No Additional Items

###### Each item of this array must be:

- Type: integer

### Return value

- Schema name: `Result`
- Type: integer

The API identifier of the newly created group.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
