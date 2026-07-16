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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `AuthMeResult`
- Type: object

AuthMeResult return fields.
- No Additional Properties
#### pw_name (required)

- Schema name: `Pw Name`
- Type: string

Name of the user.

#### pw_gecos (required)

- Schema name: `Pw Gecos`
- Type: string

Full username or comment field.

#### pw_dir (required)

- Schema name: `Pw Dir`
- Type: string

User home directory.

#### pw_shell (required)

- Schema name: `Pw Shell`
- Type: string

User command line interpreter.

#### pw_uid (required)

- Schema name: `Pw Uid`
- Type: integer

Numerical user ID of the user.

#### pw_gid (required)

- Schema name: `Pw Gid`
- Type: integer

Numerical group id for the user's primary group.

#### grouplist (required)

- Schema name: `Grouplist`

Optional array of group IDs for groups of which this account is a member. If `get_groups` is not specified, this value will be `null`.
##### Any of

###### Option 1

- Type: array of integer
- No Additional Items

####### Each item of this array must be:

- Type: integer

###### Option 2

- Type: null

#### sid (required)

- Schema name: `Sid`

Optional SID value for the account that is present if `sid_info` is specified in payload.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### source (required)

- Schema name: `Source`
- Type: enum (of string)

The source for the user account.

#### local (required)

- Schema name: `Local`
- Type: boolean

The account is local to TrueNAS or provided by a directory service.

#### attributes (required)

- Schema name: `Attributes`
- Type: object

Custom user attributes and metadata.

#### two_factor_config (required)

- Schema name: `Two Factor Config`
- Type: object

Two-factor authentication configuration for the user.

#### privilege (required)

- Schema name: `Privilege`
- Type: object

User privilege and role information.

#### account_attributes (required)

- Schema name: `Account Attributes`
- Type: array of string

Array of account attribute names available for this user.
- No Additional Items

##### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
