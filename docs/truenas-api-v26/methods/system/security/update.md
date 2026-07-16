---
title: system.security.update
kind: method
source_rst: _sources/api_methods_system.security.update.rst.txt
source_html: api_methods_system.security.update.html
required_roles:
  - SYSTEM_SECURITY_WRITE
---

# system.security.update

## Summary

Update System Security Service Configuration.

This method is used to change the FIPS, STIG, and local account policies for TrueNAS Enterprise. These features are not available in community editions of TrueNAS.

This method is a job.

## Required Roles

- `SYSTEM_SECURITY_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: system_security_update

#### system_security_update

- Schema name: `system_security_update`
- Type: object

SystemSecurityUpdateArgs parameters.
- No Additional Properties
##### enable_fips

- Schema name: `Enable Fips`
- Type: boolean

When set, enables FIPS mode.

##### enable_gpos_stig

- Schema name: `Enable Gpos Stig`
- Type: boolean

When set, enables compatibility with the General Purpose Operating System STIG.

##### min_password_age

- Schema name: `Min Password Age`

The number of days local users will have to wait before they will be allowed to change password again. One reason for setting this parameter is to prevent users from bypassing password history restrictions by rapidly changing their passwords. The value of None means that there is no minimum password age.
###### Any of

####### Option 1

- Type: integer
- Value must be strictly greater than `0`

####### Option 2

- Type: null

##### max_password_age

- Schema name: `Max Password Age`

The number of days after which a password is considered to be expired. After expiration no login will be possible for the user. The user should contact the administrator for a password reset. The value of None means that there is no maximum password age, and password aging is disabled. NOTE: User passwords will never expire if password aging is disabled.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `7` and lesser or equal to `365`

####### Option 2

- Type: null

##### password_complexity_ruleset

- Schema name: `Password Complexity Ruleset`

The password complexity ruleset defines what character types are required for passwords used by local accounts. The value of None means that there are no password complexity requirements. List items indicate a requirement for at least one character in the password to be of the specified character set type.
###### Any of

####### Option 1

- Type: array of enum (of string)
- All items must be unique
- No Additional Items

######## Each item of this array must be:

- Type: enum (of string)

####### Option 2

- Type: null

##### min_password_length

- Schema name: `Min Password Length`

The minimum length of passwords used for local accounts. The value of None means that there is no minimum password length.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `8`

####### Option 2

- Type: null

##### password_history_length

- Schema name: `Password History Length`

The number of password generations to keep in history for checks against password reuse for local user accounts. The value of None means that history checks for password reuse are not performed.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `10`

####### Option 2

- Type: null

### Return value

- Schema name: `SystemSecurityEntry`
- Type: object

The updated system security configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the system security configuration.

#### enable_fips (required)

- Schema name: `Enable Fips`
- Type: boolean

When set, enables FIPS mode.

#### enable_gpos_stig (required)

- Schema name: `Enable Gpos Stig`
- Type: boolean

When set, enables compatibility with the General Purpose Operating System STIG.

#### min_password_age

- Schema name: `Min Password Age`
- Default: null

The number of days local users will have to wait before they will be allowed to change password again. One reason for setting this parameter is to prevent users from bypassing password history restrictions by rapidly changing their passwords. The value of None means that there is no minimum password age.
##### Any of

###### Option 1

- Type: integer
- Value must be strictly greater than `0`

###### Option 2

- Type: null

#### max_password_age

- Schema name: `Max Password Age`
- Default: null

The number of days after which a password is considered to be expired. After expiration no login will be possible for the user. The user should contact the administrator for a password reset. The value of None means that there is no maximum password age, and password aging is disabled. NOTE: User passwords will never expire if password aging is disabled.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `7` and lesser or equal to `365`

###### Option 2

- Type: null

#### password_complexity_ruleset

- Schema name: `Password Complexity Ruleset`
- Default: null

The password complexity ruleset defines what character types are required for passwords used by local accounts. The value of None means that there are no password complexity requirements. List items indicate a requirement for at least one character in the password to be of the specified character set type.
##### Any of

###### Option 1

- Type: array of enum (of string)
- All items must be unique
- No Additional Items

####### Each item of this array must be:

- Type: enum (of string)

###### Option 2

- Type: null

#### min_password_length

- Schema name: `Min Password Length`
- Default: null

The minimum length of passwords used for local accounts. The value of None means that there is no minimum password length.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `8`

###### Option 2

- Type: null

#### password_history_length

- Schema name: `Password History Length`
- Default: null

The number of password generations to keep in history for checks against password reuse for local user accounts. The value of None means that history checks for password reuse are not performed.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `10`

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
