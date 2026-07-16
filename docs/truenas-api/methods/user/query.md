---
title: user.query
kind: method
source_rst: _sources/api_methods_user.query.rst.txt
source_html: api_methods_user.query.html
required_roles:
  - ACCOUNT_READ
---

# user.query

## Summary

Query users with `query-filters` and `query-options`.

If users provided by Active Directory or LDAP are not desired, then "local", "=", True should be added to filters.

## Required Roles

- `ACCOUNT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                [
                    "name",
                    "=",
                    "bob"
                ]
            ],
            [
                [
                    "name",
                    "=",
                    "larry"
                ]
            ]
        ]
    ]
]
```

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Query options including pagination, ordering, and additional parameters.
- No Additional Properties
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### UserQueryResultItem

- Schema name: `UserQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: integer

This is the API identifier for the user. Use this ID for `user.update` and `user.delete` API calls. This ID also appears in the `users` array for each group entry in `group.query` results. NOTE: For users from a directory service, the `id` is calculated by adding 100000000 to the `uid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

####### uid

- Schema name: `Uid`
- Type: integer

A non-negative integer used to identify a system user. TrueNAS uses this value for permission checks and many other system purposes.

####### username

- Schema name: `Username`

A string used to identify a user. Local accounts must use characters from the POSIX portable filename character set.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: string
- Must be at least `1` characters long

####### unixhash

- Schema name: `Unixhash`

Hashed password for local accounts. This value is `null` for accounts provided by directory services.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### smbhash

- Schema name: `Smbhash`

NT hash of the local account password for `smb` users. This value is `null` for accounts provided by directory services or non-SMB accounts.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### home

- Schema name: `Home`
- Type: string

The local file system path for the user account's home directory. Typically, this is required only if the account has shell access (local or SSH) to TrueNAS. This is not required for accounts used only for SMB share access.
- Must be at least `1` characters long

####### shell

- Schema name: `Shell`
- Type: string

Available choices can be retrieved with `user.shell_choices`.
- Must be at least `1` characters long

####### full_name

- Schema name: `Full Name`
- Type: string

Comment field to provide additional information about the user account. Typically, this is the full name of the user or a short description of a service account. There are no character set restrictions for this field. This field is for information only.

####### builtin

- Schema name: `Builtin`
- Type: boolean

If `true`, the user account is an internal system account for the TrueNAS server. Typically, one should create dedicated user accounts for access to the TrueNAS server webui and shares.

####### smb

- Schema name: `Smb`
- Type: boolean

The user account may be used to access SMB shares. If set to `true` then TrueNAS stores an NT hash of the user account's password for local accounts. This feature is unavailable for local accounts when General Purpose OS STIG compatibility mode is enabled. If set to `true` the user is automatically added to the `builtin_users` group.

####### userns_idmap

- Schema name: `Userns Idmap`

Specifies the subuid mapping for this user. If DIRECT then the UID will be directly mapped to all containers. Alternatively, the target UID may be explicitly specified. If `null`, then the UID will not be mapped. NOTE: This field will be ignored for users that have been assigned TrueNAS roles.
######## Any of

######### Option 1

- Type: enum (of null or string)

######### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

####### group

- Schema name: `Group`
- Type: object

The primary group of the user account.

####### groups

- Schema name: `Groups`
- Type: array of integer

Array of additional groups to which the user belongs. NOTE: Groups are identified by their group entry `id`, not their Unix group ID (`gid`).
- No Additional Items

######## Each item of this array must be:

- Type: integer

####### password_disabled

- Schema name: `Password Disabled`
- Type: boolean

If set to `true` password authentication for the user account is disabled. NOTE: Users with password authentication disabled may still authenticate to the TrueNAS server by other methods, such as SSH key-based authentication. NOTE: Password authentication is required for `smb` users.

####### ssh_password_enabled

- Schema name: `Ssh Password Enabled`
- Type: boolean

Allow the user to authenticate to the TrueNAS SSH server using a password. WARNING: The established best practice is to use only key-based authentication for SSH servers.

####### sshpubkey

- Schema name: `Sshpubkey`

SSH public keys corresponding to private keys that authenticate this user to the TrueNAS SSH server.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### locked

- Schema name: `Locked`
- Type: boolean

If set to `true` the account is locked. The account cannot be used to authenticate to the TrueNAS server.

####### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is prompted for password when executing any command from the array.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is *not* prompted for password when executing any command from the array.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### email

- Schema name: `Email`

Email address of the user. If the user has the `FULL_ADMIN` role, they will receive email alerts and notifications.
######## Any of

######### Option 1

- Type: string
- Must be at least `1` characters long

######### Option 2

- Type: null

####### local

- Schema name: `Local`
- Type: boolean

If `true`, the account is local to the TrueNAS server. If `false`, the account is provided by a directory service.

####### immutable

- Schema name: `Immutable`
- Type: boolean

If `true`, the account is system-provided and most fields related to it may not be changed.

####### twofactor_auth_configured

- Schema name: `Twofactor Auth Configured`
- Type: boolean

If `true`, the account has been configured for two-factor authentication. Users are prompted for a second factor when authenticating to the TrueNAS web UI and API. They may also be prompted when signing in to the TrueNAS SSH server using a password (depending on global two-factor authentication settings).

####### sid

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### last_password_change

- Schema name: `Last Password Change`

The date of the last password change for local user accounts.
######## Any of

######### Option 1

- Type: string
- Type: Format: date-time

######### Option 2

- Type: null

####### password_age

- Schema name: `Password Age`

The age in days of the password for local user accounts.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### password_history

- Schema name: `Password History`

This contains hashes of the ten most recent passwords used by local user accounts, and is for enforcing password history requirements as defined in system.security.
######## Any of

######### Option 1

- Type: array
- No Additional Items

########## Each item of this array must be:

- Type: object

######### Option 2

- Type: null

####### password_change_required

- Schema name: `Password Change Required`
- Type: boolean

Password change for local user account is required on next login.

####### roles

- Schema name: `Roles`
- Type: array of string

Array of roles assigned to this user's groups. Roles control administrative access to TrueNAS through the web UI and API.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### api_keys

- Schema name: `Api Keys`
- Type: array of integer

Array of API key IDs associated with this user account for programmatic access.
- No Additional Items

######## Each item of this array must be:

- Type: integer

##### UserQueryResultItem

- Type: string

##### Option 3

- Type: string
- Must be at least `1` characters long

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: enum (of null or string)

##### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string
- Type: Format: date-time

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: array
- No Additional Items

###### Each item of this array must be:

- Type: object

##### Option 2

- Type: null

##### Option 1

- Schema name: `UserQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: integer

This is the API identifier for the user. Use this ID for `user.update` and `user.delete` API calls. This ID also appears in the `users` array for each group entry in `group.query` results. NOTE: For users from a directory service, the `id` is calculated by adding 100000000 to the `uid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

###### uid

- Schema name: `Uid`
- Type: integer

A non-negative integer used to identify a system user. TrueNAS uses this value for permission checks and many other system purposes.

###### username

- Schema name: `Username`

A string used to identify a user. Local accounts must use characters from the POSIX portable filename character set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: string
- Must be at least `1` characters long

###### unixhash

- Schema name: `Unixhash`

Hashed password for local accounts. This value is `null` for accounts provided by directory services.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### smbhash

- Schema name: `Smbhash`

NT hash of the local account password for `smb` users. This value is `null` for accounts provided by directory services or non-SMB accounts.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### home

- Schema name: `Home`
- Type: string

The local file system path for the user account's home directory. Typically, this is required only if the account has shell access (local or SSH) to TrueNAS. This is not required for accounts used only for SMB share access.
- Must be at least `1` characters long

###### shell

- Schema name: `Shell`
- Type: string

Available choices can be retrieved with `user.shell_choices`.
- Must be at least `1` characters long

###### full_name

- Schema name: `Full Name`
- Type: string

Comment field to provide additional information about the user account. Typically, this is the full name of the user or a short description of a service account. There are no character set restrictions for this field. This field is for information only.

###### builtin

- Schema name: `Builtin`
- Type: boolean

If `true`, the user account is an internal system account for the TrueNAS server. Typically, one should create dedicated user accounts for access to the TrueNAS server webui and shares.

###### smb

- Schema name: `Smb`
- Type: boolean

The user account may be used to access SMB shares. If set to `true` then TrueNAS stores an NT hash of the user account's password for local accounts. This feature is unavailable for local accounts when General Purpose OS STIG compatibility mode is enabled. If set to `true` the user is automatically added to the `builtin_users` group.

###### userns_idmap

- Schema name: `Userns Idmap`

Specifies the subuid mapping for this user. If DIRECT then the UID will be directly mapped to all containers. Alternatively, the target UID may be explicitly specified. If `null`, then the UID will not be mapped. NOTE: This field will be ignored for users that have been assigned TrueNAS roles.
####### Any of

######## Option 1

- Type: enum (of null or string)

######## Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

###### group

- Schema name: `Group`
- Type: object

The primary group of the user account.

###### groups

- Schema name: `Groups`
- Type: array of integer

Array of additional groups to which the user belongs. NOTE: Groups are identified by their group entry `id`, not their Unix group ID (`gid`).
- No Additional Items

####### Each item of this array must be:

- Type: integer

###### password_disabled

- Schema name: `Password Disabled`
- Type: boolean

If set to `true` password authentication for the user account is disabled. NOTE: Users with password authentication disabled may still authenticate to the TrueNAS server by other methods, such as SSH key-based authentication. NOTE: Password authentication is required for `smb` users.

###### ssh_password_enabled

- Schema name: `Ssh Password Enabled`
- Type: boolean

Allow the user to authenticate to the TrueNAS SSH server using a password. WARNING: The established best practice is to use only key-based authentication for SSH servers.

###### sshpubkey

- Schema name: `Sshpubkey`

SSH public keys corresponding to private keys that authenticate this user to the TrueNAS SSH server.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### locked

- Schema name: `Locked`
- Type: boolean

If set to `true` the account is locked. The account cannot be used to authenticate to the TrueNAS server.

###### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is prompted for password when executing any command from the array.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is *not* prompted for password when executing any command from the array.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### email

- Schema name: `Email`

Email address of the user. If the user has the `FULL_ADMIN` role, they will receive email alerts and notifications.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### local

- Schema name: `Local`
- Type: boolean

If `true`, the account is local to the TrueNAS server. If `false`, the account is provided by a directory service.

###### immutable

- Schema name: `Immutable`
- Type: boolean

If `true`, the account is system-provided and most fields related to it may not be changed.

###### twofactor_auth_configured

- Schema name: `Twofactor Auth Configured`
- Type: boolean

If `true`, the account has been configured for two-factor authentication. Users are prompted for a second factor when authenticating to the TrueNAS web UI and API. They may also be prompted when signing in to the TrueNAS SSH server using a password (depending on global two-factor authentication settings).

###### sid

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### last_password_change

- Schema name: `Last Password Change`

The date of the last password change for local user accounts.
####### Any of

######## Option 1

- Type: string
- Type: Format: date-time

######## Option 2

- Type: null

###### password_age

- Schema name: `Password Age`

The age in days of the password for local user accounts.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### password_history

- Schema name: `Password History`

This contains hashes of the ten most recent passwords used by local user accounts, and is for enforcing password history requirements as defined in system.security.
####### Any of

######## Option 1

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

######## Option 2

- Type: null

###### password_change_required

- Schema name: `Password Change Required`
- Type: boolean

Password change for local user account is required on next login.

###### roles

- Schema name: `Roles`
- Type: array of string

Array of roles assigned to this user's groups. Roles control administrative access to TrueNAS through the web UI and API.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### api_keys

- Schema name: `Api Keys`
- Type: array of integer

Array of API key IDs associated with this user account for programmatic access.
- No Additional Items

####### Each item of this array must be:

- Type: integer

##### Option 2

- Type: string

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: enum (of null or string)

##### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string
- Must be at least `1` characters long

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string
- Type: Format: date-time

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: array
- No Additional Items

###### Each item of this array must be:

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
