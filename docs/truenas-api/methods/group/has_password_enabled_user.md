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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: gids

#### gids

- Schema name: `gids`
- Type: array of integer

Array of group IDs to check for password-enabled users.
- No Additional Items

##### Each item of this array must be:

- Type: integer

#### Parameter 2: exclude_user_ids

#### exclude_user_ids

- Schema name: `exclude_user_ids`
- Type: array of integer
- Default: []

Array of user IDs to exclude from the check.
- No Additional Items

##### Each item of this array must be:

- Type: integer

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if any of the groups contain password-enabled users.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
