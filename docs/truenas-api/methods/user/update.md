---
title: user.update
kind: method
source_rst: _sources/api_methods_user.update.rst.txt
source_html: api_methods_user.update.html
required_roles:
  - ACCOUNT_WRITE
---

# user.update

## Summary

Update attributes of an existing user.

## Required Roles

- `ACCOUNT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the user account to update.

#### Parameter 2: user_update

#### user_update

- Schema name: `user_update`
- Type: object

Updated configuration for the user account.
- No Additional Properties
##### username

- Schema name: `Username`
- Type: string

String used to uniquely identify the user on the server. In order to be portable across systems, local user names must be composed of characters from the POSIX portable filename character set (IEEE Std 1003.1-2024 section 3.265). This means alphanumeric characters, hyphens, underscores, and periods. Usernames also may not begin with a hyphen or a period.

##### home

- Schema name: `Home`
- Type: string

The local file system path for the user account's home directory. Typically, this is required only if the account has shell access (local or SSH) to TrueNAS. This is not required for accounts used only for SMB share access.
- Must be at least `1` characters long

##### shell

- Schema name: `Shell`
- Type: string

Available choices can be retrieved with `user.shell_choices`.
- Must be at least `1` characters long

##### full_name

- Schema name: `Full Name`
- Type: string

Comment field to provide additional information about the user account. Typically, this is the full name of the user or a short description of a service account. There are no character set restrictions for this field. This field is for information only.
- Must be at least `1` characters long

##### smb

- Schema name: `Smb`
- Type: boolean

The user account may be used to access SMB shares. If set to `true` then TrueNAS stores an NT hash of the user account's password for local accounts. This feature is unavailable for local accounts when General Purpose OS STIG compatibility mode is enabled. If set to `true` the user is automatically added to the `builtin_users` group.

##### userns_idmap

- Schema name: `Userns Idmap`

Specifies the subuid mapping for this user. If DIRECT then the UID will be directly mapped to all containers. Alternatively, the target UID may be explicitly specified. If `null`, then the UID will not be mapped. NOTE: This field will be ignored for users that have been assigned TrueNAS roles.
###### Any of

####### Option 1

- Type: enum (of null or string)

####### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

##### group

- Schema name: `Group`

The group entry `id` for the user's primary group. This is not the same as the Unix group `gid` value. This is required if `group_create` is `false`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### groups

- Schema name: `Groups`
- Type: array of integer

Array of additional groups to which the user belongs. NOTE: Groups are identified by their group entry `id`, not their Unix group ID (`gid`).
- No Additional Items

###### Each item of this array must be:

- Type: integer

##### password_disabled

- Schema name: `Password Disabled`
- Type: boolean

If set to `true` password authentication for the user account is disabled. NOTE: Users with password authentication disabled may still authenticate to the TrueNAS server by other methods, such as SSH key-based authentication. NOTE: Password authentication is required for `smb` users.

##### ssh_password_enabled

- Schema name: `Ssh Password Enabled`
- Type: boolean

Allow the user to authenticate to the TrueNAS SSH server using a password. WARNING: The established best practice is to use only key-based authentication for SSH servers.

##### sshpubkey

- Schema name: `Sshpubkey`

SSH public keys corresponding to private keys that authenticate this user to the TrueNAS SSH server.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### locked

- Schema name: `Locked`
- Type: boolean

If set to `true` the account is locked. The account cannot be used to authenticate to the TrueNAS server.

##### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is prompted for password when executing any command from the array.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is *not* prompted for password when executing any command from the array.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### email

- Schema name: `Email`

Email address of the user. If the user has the `FULL_ADMIN` role, they will receive email alerts and notifications.
###### Any of

####### Option 1

- Type: string
- Type: Format: email

####### Option 2

- Type: null

##### home_create

- Schema name: `Home Create`
- Type: boolean

Create a new home directory for the user in the specified `home` path.

##### home_mode

- Schema name: `Home Mode`
- Type: string

Filesystem permission to set on the user's home directory.

##### password

- Schema name: `Password`

The password for the user account. This is required if `random_password` is not set.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### random_password

- Schema name: `Random Password`
- Type: boolean

Generate a random 20 character password for the user.

### Return value

- Schema name: `UserCreateUpdateResult`
- Type: object

The updated user account with password information.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the user. Use this ID for `user.update` and `user.delete` API calls. This ID also appears in the `users` array for each group entry in `group.query` results. NOTE: For users from a directory service, the `id` is calculated by adding 100000000 to the `uid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

#### uid (required)

- Schema name: `Uid`
- Type: integer

A non-negative integer used to identify a system user. TrueNAS uses this value for permission checks and many other system purposes.

#### username (required)

- Schema name: `Username`

A string used to identify a user. Local accounts must use characters from the POSIX portable filename character set.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: string
- Must be at least `1` characters long

#### unixhash (required)

- Schema name: `Unixhash`

Hashed password for local accounts. This value is `null` for accounts provided by directory services.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### smbhash (required)

- Schema name: `Smbhash`

NT hash of the local account password for `smb` users. This value is `null` for accounts provided by directory services or non-SMB accounts.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### home

- Schema name: `Home`
- Type: string
- Default: "/var/empty"

The local file system path for the user account's home directory. Typically, this is required only if the account has shell access (local or SSH) to TrueNAS. This is not required for accounts used only for SMB share access.
- Must be at least `1` characters long

#### shell

- Schema name: `Shell`
- Type: string
- Default: "/usr/bin/zsh"

Available choices can be retrieved with `user.shell_choices`.
- Must be at least `1` characters long

#### full_name (required)

- Schema name: `Full Name`
- Type: string

Comment field to provide additional information about the user account. Typically, this is the full name of the user or a short description of a service account. There are no character set restrictions for this field. This field is for information only.

#### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `true`, the user account is an internal system account for the TrueNAS server. Typically, one should create dedicated user accounts for access to the TrueNAS server webui and shares.

#### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

The user account may be used to access SMB shares. If set to `true` then TrueNAS stores an NT hash of the user account's password for local accounts. This feature is unavailable for local accounts when General Purpose OS STIG compatibility mode is enabled. If set to `true` the user is automatically added to the `builtin_users` group.

#### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subuid mapping for this user. If DIRECT then the UID will be directly mapped to all containers. Alternatively, the target UID may be explicitly specified. If `null`, then the UID will not be mapped. NOTE: This field will be ignored for users that have been assigned TrueNAS roles.
##### Any of

###### Option 1

- Type: enum (of null or string)

###### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

#### group (required)

- Schema name: `Group`
- Type: object

The primary group of the user account.

#### groups

- Schema name: `Groups`
- Type: array of integer

Array of additional groups to which the user belongs. NOTE: Groups are identified by their group entry `id`, not their Unix group ID (`gid`).
- No Additional Items

##### Each item of this array must be:

- Type: integer

#### password_disabled

- Schema name: `Password Disabled`
- Type: boolean
- Default: false

If set to `true` password authentication for the user account is disabled. NOTE: Users with password authentication disabled may still authenticate to the TrueNAS server by other methods, such as SSH key-based authentication. NOTE: Password authentication is required for `smb` users.

#### ssh_password_enabled

- Schema name: `Ssh Password Enabled`
- Type: boolean
- Default: false

Allow the user to authenticate to the TrueNAS SSH server using a password. WARNING: The established best practice is to use only key-based authentication for SSH servers.

#### sshpubkey

- Schema name: `Sshpubkey`
- Default: null

SSH public keys corresponding to private keys that authenticate this user to the TrueNAS SSH server.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### locked

- Schema name: `Locked`
- Type: boolean
- Default: false

If set to `true` the account is locked. The account cannot be used to authenticate to the TrueNAS server.

#### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is prompted for password when executing any command from the array.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is *not* prompted for password when executing any command from the array.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### email

- Schema name: `Email`
- Default: null

Email address of the user. If the user has the `FULL_ADMIN` role, they will receive email alerts and notifications.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### local (required)

- Schema name: `Local`
- Type: boolean

If `true`, the account is local to the TrueNAS server. If `false`, the account is provided by a directory service.

#### immutable (required)

- Schema name: `Immutable`
- Type: boolean

If `true`, the account is system-provided and most fields related to it may not be changed.

#### twofactor_auth_configured (required)

- Schema name: `Twofactor Auth Configured`
- Type: boolean

If `true`, the account has been configured for two-factor authentication. Users are prompted for a second factor when authenticating to the TrueNAS web UI and API. They may also be prompted when signing in to the TrueNAS SSH server using a password (depending on global two-factor authentication settings).

#### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### last_password_change (required)

- Schema name: `Last Password Change`

The date of the last password change for local user accounts.
##### Any of

###### Option 1

- Type: string
- Type: Format: date-time

###### Option 2

- Type: null

#### password_age (required)

- Schema name: `Password Age`

The age in days of the password for local user accounts.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### password_history (required)

- Schema name: `Password History`

This contains hashes of the ten most recent passwords used by local user accounts, and is for enforcing password history requirements as defined in system.security.
##### Any of

###### Option 1

- Type: array
- No Additional Items

####### Each item of this array must be:

- Type: object

###### Option 2

- Type: null

#### password_change_required (required)

- Schema name: `Password Change Required`
- Type: boolean

Password change for local user account is required on next login.

#### roles (required)

- Schema name: `Roles`
- Type: array of string

Array of roles assigned to this user's groups. Roles control administrative access to TrueNAS through the web UI and API.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### api_keys (required)

- Schema name: `Api Keys`
- Type: array of integer

Array of API key IDs associated with this user account for programmatic access.
- No Additional Items

##### Each item of this array must be:

- Type: integer

#### password (required)

- Schema name: `Password`

Password if it was specified in create or update payload. If random_password was specified then this will be a 20 character random string.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
