---
title: group.get_group_obj
kind: method
source_rst: _sources/api_methods_group.get_group_obj.rst.txt
source_html: api_methods_group.get_group_obj.html
required_roles:
  - ACCOUNT_READ
---

# group.get_group_obj

## Summary

Returns dictionary containing information from struct grp for the group specified by either the `groupname` or `gid`.

If `sid_info` is specified then addition SMB / domain information is returned for the group.

## Required Roles

- `ACCOUNT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: get_group_obj

#### get_group_obj

- Schema name: `get_group_obj`
- Type: object

GroupGetGroupObjArgs parameters.
- No Additional Properties
##### groupname

- Schema name: `Groupname`
- Default: null

Name of the group to look up or `null`.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### gid

- Schema name: `Gid`
- Default: null

Group ID to look up or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### sid_info

- Schema name: `Sid Info`
- Type: boolean
- Default: false

Whether to include SID information in the response.

### Return value

- Schema name: `GroupGetGroupObjResult`
- Type: object

GroupGetGroupObjResult return fields.
- No Additional Properties
#### gr_name (required)

- Schema name: `Gr Name`
- Type: string

Name of the group.

#### gr_gid (required)

- Schema name: `Gr Gid`
- Type: integer

Group ID of the group.

#### gr_mem (required)

- Schema name: `Gr Mem`
- Type: array of string

List of group names that are members of the group.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### sid

- Schema name: `Sid`
- Default: null

Optional SID value for the account that is present if `sid_info` is specified in payload.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### source (required)

- Schema name: `Source`
- Type: enum (of string)

The name server switch module that provided the user. Options are: FILES: Local user in passwd file of server. WINBIND: User provided by winbindd. SSS: User provided by SSSD.

#### local (required)

- Schema name: `Local`
- Type: boolean

This group is local to the NAS or provided by a directory service.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
