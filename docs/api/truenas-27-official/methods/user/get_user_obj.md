---
title: user.get_user_obj
kind: method
source_rst: _sources/api_methods_user.get_user_obj.rst.txt
source_html: api_methods_user.get_user_obj.html
required_roles:
  - ACCOUNT_READ
---

# user.get_user_obj

## Summary

Returns dictionary containing information from struct passwd for the user specified by either the `username` or `uid`. Bypasses user cache.

.. note::

Results will not include nested groups for Active Directory users.

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

#### Parameter 1: get_user_obj

<a id="Call_parameters_items_i0"></a>
#### get_user_obj

- Schema name: `get_user_obj`
- Type: object

UserGetUserObjArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_username"></a>
<a id="Call_parameters_items_i0_username"></a>
##### username

- Schema name: `Username`
- Default: null

Username to lookup. Either `username` or `uid` must be specified.
<a id="Call_parameters_items_i0_username_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_username_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_username_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_uid"></a>
<a id="Call_parameters_items_i0_uid"></a>
##### uid

- Schema name: `Uid`
- Default: null

User ID to lookup. Either `username` or `uid` must be specified.
<a id="Call_parameters_items_i0_uid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_uid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_uid_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_uid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_uid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_get_groups"></a>
<a id="Call_parameters_items_i0_get_groups"></a>
##### get_groups

- Schema name: `Get Groups`
- Type: boolean
- Default: false

Retrieve group list for the specified user.

<a id="headingCall_parameters_items_i0_sid_info"></a>
<a id="Call_parameters_items_i0_sid_info"></a>
##### sid_info

- Schema name: `Sid Info`
- Type: boolean
- Default: false

Retrieve SID and domain information for the user.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `UserGetUserObj`
- Type: object

User account information in Unix passwd format.
- No Additional Properties
<a id="headingReturn_value_pw_name"></a>
<a id="Return_value_pw_name"></a>
#### pw_name (required)

- Schema name: `Pw Name`
- Type: string

Name of the user.

<a id="headingReturn_value_pw_gecos"></a>
<a id="Return_value_pw_gecos"></a>
#### pw_gecos (required)

- Schema name: `Pw Gecos`
- Type: string

Full username or comment field.

<a id="headingReturn_value_pw_dir"></a>
<a id="Return_value_pw_dir"></a>
#### pw_dir (required)

- Schema name: `Pw Dir`
- Type: string

User home directory.

<a id="headingReturn_value_pw_shell"></a>
<a id="Return_value_pw_shell"></a>
#### pw_shell (required)

- Schema name: `Pw Shell`
- Type: string

User command line interpreter.

<a id="headingReturn_value_pw_uid"></a>
<a id="Return_value_pw_uid"></a>
#### pw_uid (required)

- Schema name: `Pw Uid`
- Type: integer

Numerical user ID of the user.

<a id="headingReturn_value_pw_gid"></a>
<a id="Return_value_pw_gid"></a>
#### pw_gid (required)

- Schema name: `Pw Gid`
- Type: integer

Numerical group id for the user's primary group.

<a id="headingReturn_value_grouplist"></a>
<a id="Return_value_grouplist"></a>
#### grouplist (required)

- Schema name: `Grouplist`

Optional array of group IDs for groups of which this account is a member. If `get_groups` is not specified, this value will be `null`.
<a id="Return_value_grouplist_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_grouplist_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_grouplist_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_grouplist_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_grouplist_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_grouplist_anyOf_i1)

- Type: null

<a id="headingReturn_value_sid"></a>
<a id="Return_value_sid"></a>
#### sid (required)

- Schema name: `Sid`

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

The source for the user account.
##### Must be one of:

- "LOCAL"
- "ACTIVEDIRECTORY"
- "LDAP"

<a id="headingReturn_value_local"></a>
<a id="Return_value_local"></a>
#### local (required)

- Schema name: `Local`
- Type: boolean

The account is local to TrueNAS or provided by a directory service.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
