---
title: auth.me
kind: method
source_rst: _sources/api_methods_auth.me.rst.txt
source_html: api_methods_auth.me.html
required_roles:
  []
---

# auth.me

## Summary

Returns currently logged-in user.

## Required Roles

- None documented.

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `AuthMeResult`
- Type: object

AuthMeResult return fields.
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

<a id="headingReturn_value_attributes"></a>
<a id="Return_value_attributes"></a>
#### attributes (required)

- Schema name: `Attributes`
- Type: object

Custom user attributes and metadata.

<a id="headingReturn_value_two_factor_config"></a>
<a id="Return_value_two_factor_config"></a>
#### two_factor_config (required)

- Schema name: `Two Factor Config`
- Type: object

Two-factor authentication configuration for the user.

<a id="headingReturn_value_privilege"></a>
<a id="Return_value_privilege"></a>
#### privilege (required)

- Schema name: `Privilege`
- Type: object

User privilege and role information.

<a id="headingReturn_value_account_attributes"></a>
<a id="Return_value_account_attributes"></a>
#### account_attributes (required)

- Schema name: `Account Attributes`
- Type: array of string

Array of account attribute names available for this user.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_account_attributes_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
