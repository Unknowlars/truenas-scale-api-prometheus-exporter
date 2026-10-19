---
title: group.has_password_enabled_user
kind: method
source_rst: _sources/api_methods_group.has_password_enabled_user.rst.txt
source_html: api_methods_group.has_password_enabled_user.html
required_roles:
  - ACCOUNT_READ
---

# group.has_password_enabled_user

## Summary

Checks whether at least one local user with a password is a member of any of the `group_ids`.

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

#### Parameter 1: gids

<a id="Call_parameters_items_i0"></a>
#### gids

- Schema name: `gids`
- Type: array of integer

Array of group IDs to check for password-enabled users.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
- Type: integer

#### Parameter 2: exclude_user_ids

<a id="Call_parameters_items_i1"></a>
#### exclude_user_ids

- Schema name: `exclude_user_ids`
- Type: array of integer
- Default: []

Array of user IDs to exclude from the check.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i1_items"></a>
- Type: integer

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if any of the groups contain password-enabled users.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
