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

Returns dictionary containing information from struct passwd for the user specified by either the username or uid. Bypasses user cache.

NOTE: results will not include nested groups for Active Directory users.

## Required Roles

- `ACCOUNT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: get_user_obj

#### get_user_obj

- Schema name: `get_user_obj`
- Type: object

UserGetUserObjArgs parameters.
- No Additional Properties
##### username

- Schema name: `Username`
- Default: null

Username to lookup. Either `username` or `uid` must be specified.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### uid

- Schema name: `Uid`
- Default: null

User ID to lookup. Either `username` or `uid` must be specified.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### get_groups

- Schema name: `Get Groups`
- Type: boolean
- Default: false

Retrieve group list for the specified user.

##### sid_info

- Schema name: `Sid Info`
- Type: boolean
- Default: false

Retrieve SID and domain information for the user.

### Return value

- Schema name: `UserGetUserObj`
- Type: object

User account information in Unix passwd format.
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

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
