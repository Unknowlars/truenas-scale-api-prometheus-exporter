---
title: user.set_password
kind: method
source_rst: _sources/api_methods_user.set_password.rst.txt
source_html: api_methods_user.set_password.html
required_roles:
  []
---

# user.set_password

## Summary

Set the password of the specified `username` to the `new_password` specified in payload.

ValidationErrors will be raised in the following situations: * username does not exist * account is not local to the NAS (Active Directory, LDAP, etc) * account has password authentication disabled * account is locked

NOTE: when authenticated session has less than FULL_ADMIN role, password changes will be rejected if the payload does not match the currently-authenticated user.

NOTE: users authenticated with a one-time password will be able to change the password without submitting a second time.

## Required Roles

- None documented.

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: set_password_data

<a id="Call_parameters_items_i0"></a>
#### set_password_data

- Schema name: `set_password_data`
- Type: object

UserSetPasswordArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_username"></a>
<a id="Call_parameters_items_i0_username"></a>
##### username (required)

- Schema name: `Username`
- Type: string

Username of the account to change password for.

<a id="headingCall_parameters_items_i0_old_password"></a>
<a id="Call_parameters_items_i0_old_password"></a>
##### old_password

- Schema name: `Old Password`
- Default: null

Current password for verification. `null` if changing password as administrator.
<a id="Call_parameters_items_i0_old_password_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_old_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_old_password_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_old_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_old_password_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_new_password"></a>
<a id="Call_parameters_items_i0_new_password"></a>
##### new_password (required)

- Schema name: `New Password`
- Type: string

New password to set for the user account.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful password change.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
