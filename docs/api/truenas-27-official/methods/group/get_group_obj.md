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

If `sid_info` is specified, additional SMB / domain information is returned for the group.

## Required Roles

- `ACCOUNT_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: get_group_obj

<a id="Call_parameters_items_i0"></a>
#### get_group_obj

- Schema name: `get_group_obj`
- Type: object

GroupGetGroupObjArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_groupname"></a>
<a id="Call_parameters_items_i0_groupname"></a>
##### groupname

- Schema name: `Groupname`
- Default: null

Name of the group to look up or `null`.
<a id="Call_parameters_items_i0_groupname_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_groupname_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_groupname_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_groupname_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_groupname_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_gid"></a>
<a id="Call_parameters_items_i0_gid"></a>
##### gid

- Schema name: `Gid`
- Default: null

Group ID to look up or `null`.
<a id="Call_parameters_items_i0_gid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_gid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_gid_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_gid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_gid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_sid_info"></a>
<a id="Call_parameters_items_i0_sid_info"></a>
##### sid_info

- Schema name: `Sid Info`
- Type: boolean
- Default: false

Whether to include SID information in the response.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `GroupGetGroupObjResult`
- Type: object

GroupGetGroupObjResult return fields.
- No Additional Properties
<a id="headingReturn_value_gr_name"></a>
<a id="Return_value_gr_name"></a>
#### gr_name (required)

- Schema name: `Gr Name`
- Type: string

Name of the group.

<a id="headingReturn_value_gr_gid"></a>
<a id="Return_value_gr_gid"></a>
#### gr_gid (required)

- Schema name: `Gr Gid`
- Type: integer

Group ID of the group.

<a id="headingReturn_value_gr_mem"></a>
<a id="Return_value_gr_mem"></a>
#### gr_mem (required)

- Schema name: `Gr Mem`
- Type: array of string

List of group names that are members of the group.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_gr_mem_items"></a>
- Type: string

<a id="headingReturn_value_sid"></a>
<a id="Return_value_sid"></a>
#### sid

- Schema name: `Sid`
- Default: null

Optional SID value for the account that is present if `sid_info` is specified in payload.
<a id="Return_value_sid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sid_anyOf_i1)

- Type: null

<a id="headingReturn_value_source"></a>
<a id="Return_value_source"></a>
#### source (required)

- Schema name: `Source`
- Type: enum (of string)

The name server switch module that provided the user. Options are: FILES: Local user in passwd file of server. WINBIND: User provided by winbindd. SSS: User provided by SSSD.
##### Must be one of:

- "LOCAL"
- "ACTIVEDIRECTORY"
- "LDAP"

<a id="headingReturn_value_local"></a>
<a id="Return_value_local"></a>
#### local (required)

- Schema name: `Local`
- Type: boolean

This group is local to the NAS or provided by a directory service.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
