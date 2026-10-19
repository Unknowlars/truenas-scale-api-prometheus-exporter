---
title: user.query
kind: event
source_rst: _sources/api_events_user.query.rst.txt
source_html: api_events_user.query.html
required_roles:
  - ACCOUNT_READ
---

# user.query

## Summary

Sent on user changes.

## Required Roles

- `ACCOUNT_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `UserAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `UserEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the user. Use this ID for `user.update` and `user.delete` API calls. This ID also appears in the `users` array for each group entry in `group.query` results. NOTE: For users from a directory service, the `id` is calculated by adding 100000000 to the `uid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

<a id="headingADDED_fields_uid"></a>
<a id="ADDED_fields_uid"></a>
##### uid (required)

- Schema name: `Uid`
- Type: integer

A non-negative integer used to identify a system user. TrueNAS uses this value for permission checks and many other system purposes.

<a id="headingADDED_fields_username"></a>
<a id="ADDED_fields_username"></a>
##### username (required)

- Schema name: `Username`

A string used to identify a user. Local accounts must use characters from the POSIX portable filename character set.
<a id="ADDED_fields_username_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_username_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_username_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_unixhash"></a>
<a id="ADDED_fields_unixhash"></a>
##### unixhash (required)

- Schema name: `Unixhash`

Hashed password for local accounts. This value is `null` for accounts provided by directory services.
<a id="ADDED_fields_unixhash_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_unixhash_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_unixhash_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_unixhash_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_unixhash_anyOf_i1)

- Type: null

<a id="headingADDED_fields_smbhash"></a>
<a id="ADDED_fields_smbhash"></a>
##### smbhash (required)

- Schema name: `Smbhash`

NT hash of the local account password for `smb` users. This value is `null` for accounts provided by directory services or non-SMB accounts.
<a id="ADDED_fields_smbhash_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_smbhash_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_smbhash_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_smbhash_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_smbhash_anyOf_i1)

- Type: null

<a id="headingADDED_fields_home"></a>
<a id="ADDED_fields_home"></a>
##### home

- Schema name: `Home`
- Type: string
- Default: "/var/empty"

The local file system path for the user account's home directory. Typically, this is required only if the account has shell access (local or SSH) to TrueNAS. This is not required for accounts used only for SMB share access.
- Must be at least `1` characters long

<a id="headingADDED_fields_shell"></a>
<a id="ADDED_fields_shell"></a>
##### shell

- Schema name: `Shell`
- Type: string
- Default: "/usr/bin/zsh"

Available choices can be retrieved with `user.shell_choices`.
- Must be at least `1` characters long

<a id="headingADDED_fields_full_name"></a>
<a id="ADDED_fields_full_name"></a>
##### full_name (required)

- Schema name: `Full Name`
- Type: string

Comment field to provide additional information about the user account. Typically, this is the full name of the user or a short description of a service account. There are no character set restrictions for this field. This field is for information only.

<a id="headingADDED_fields_builtin"></a>
<a id="ADDED_fields_builtin"></a>
##### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `true`, the user account is an internal system account for the TrueNAS server. Typically, one should create dedicated user accounts for access to the TrueNAS server webui and shares.

<a id="headingADDED_fields_smb"></a>
<a id="ADDED_fields_smb"></a>
##### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

The user account may be used to access SMB shares. If set to `true` then TrueNAS stores an NT hash of the user account's password for local accounts. This feature is unavailable for local accounts when General Purpose OS STIG compatibility mode is enabled. If set to `true` the user is automatically added to the `builtin_users` group.

<a id="headingADDED_fields_webshare"></a>
<a id="ADDED_fields_webshare"></a>
##### webshare

- Schema name: `Webshare`
- Type: boolean
- Default: false

The user account may be used to access WebShare shares. If set to `true` the user is automatically added to the `webshare` group.

<a id="headingADDED_fields_userns_idmap"></a>
<a id="ADDED_fields_userns_idmap"></a>
##### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subuid mapping for this user. If DIRECT then the UID will be directly mapped to all containers. Alternatively, the target UID may be explicitly specified. If `null`, then the UID will not be mapped. NOTE: This field will be ignored for users that have been assigned TrueNAS roles.
<a id="ADDED_fields_userns_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_userns_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_userns_idmap_anyOf_i0)

- Type: enum (of null or string)
###### Must be one of:

- "DIRECT"
- null

<a id="tab-pane_ADDED_fields_userns_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_userns_idmap_anyOf_i1)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

<a id="headingADDED_fields_group"></a>
<a id="ADDED_fields_group"></a>
##### group (required)

- Schema name: `Group`
- Type: object

The primary group of the user account.

<a id="headingADDED_fields_groups"></a>
<a id="ADDED_fields_groups"></a>
##### groups

- Schema name: `Groups`
- Type: array of integer

Array of additional groups to which the user belongs. NOTE: Groups are identified by their group entry `id`, not their Unix group ID (`gid`).
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_groups_items"></a>
- Type: integer

<a id="headingADDED_fields_password_disabled"></a>
<a id="ADDED_fields_password_disabled"></a>
##### password_disabled

- Schema name: `Password Disabled`
- Type: boolean
- Default: false

If set to `true` password authentication for the user account is disabled. NOTE: Users with password authentication disabled may still authenticate to the TrueNAS server by other methods, such as SSH key-based authentication. NOTE: Password authentication is required for `smb` users.

<a id="headingADDED_fields_ssh_password_enabled"></a>
<a id="ADDED_fields_ssh_password_enabled"></a>
##### ssh_password_enabled

- Schema name: `Ssh Password Enabled`
- Type: boolean
- Default: false

Allow the user to authenticate to the TrueNAS SSH server using a password. WARNING: The established best practice is to use only key-based authentication for SSH servers.

<a id="headingADDED_fields_sshpubkey"></a>
<a id="ADDED_fields_sshpubkey"></a>
##### sshpubkey

- Schema name: `Sshpubkey`
- Default: null

SSH public keys corresponding to private keys that authenticate this user to the TrueNAS SSH server.
<a id="ADDED_fields_sshpubkey_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_sshpubkey_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_sshpubkey_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_sshpubkey_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_sshpubkey_anyOf_i1)

- Type: null

<a id="headingADDED_fields_locked"></a>
<a id="ADDED_fields_locked"></a>
##### locked

- Schema name: `Locked`
- Type: boolean
- Default: false

If set to `true` the account is locked. The account cannot be used to authenticate to the TrueNAS server.

<a id="headingADDED_fields_sudo_commands"></a>
<a id="ADDED_fields_sudo_commands"></a>
##### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is prompted for password when executing any command from the array.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_sudo_commands_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_sudo_commands_nopasswd"></a>
<a id="ADDED_fields_sudo_commands_nopasswd"></a>
##### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is *not* prompted for password when executing any command from the array.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_sudo_commands_nopasswd_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_email"></a>
<a id="ADDED_fields_email"></a>
##### email

- Schema name: `Email`
- Default: null

Email address of the user. If the user has the `FULL_ADMIN` role, they will receive email alerts and notifications.
<a id="ADDED_fields_email_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_email_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_email_anyOf_i1)

- Type: null

<a id="headingADDED_fields_local"></a>
<a id="ADDED_fields_local"></a>
##### local (required)

- Schema name: `Local`
- Type: boolean

If `true`, the account is local to the TrueNAS server. If `false`, the account is provided by a directory service.

<a id="headingADDED_fields_immutable"></a>
<a id="ADDED_fields_immutable"></a>
##### immutable (required)

- Schema name: `Immutable`
- Type: boolean

If `true`, the account is system-provided and most fields related to it may not be changed.

<a id="headingADDED_fields_twofactor_auth_configured"></a>
<a id="ADDED_fields_twofactor_auth_configured"></a>
##### twofactor_auth_configured (required)

- Schema name: `Twofactor Auth Configured`
- Type: boolean

If `true`, the account has been configured for two-factor authentication. Users are prompted for a second factor when authenticating to the TrueNAS web UI and API. They may also be prompted when signing in to the TrueNAS SSH server using a password (depending on global two-factor authentication settings).

<a id="headingADDED_fields_sid"></a>
<a id="ADDED_fields_sid"></a>
##### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
<a id="ADDED_fields_sid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_sid_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_sid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_last_password_change"></a>
<a id="ADDED_fields_last_password_change"></a>
##### last_password_change (required)

- Schema name: `Last Password Change`

The date of the last password change for local user accounts.
<a id="ADDED_fields_last_password_change_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_last_password_change_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_last_password_change_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_ADDED_fields_last_password_change_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_last_password_change_anyOf_i1)

- Type: null

<a id="headingADDED_fields_password_age"></a>
<a id="ADDED_fields_password_age"></a>
##### password_age (required)

- Schema name: `Password Age`

The age in days of the password for local user accounts.
<a id="ADDED_fields_password_age_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_password_age_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_password_age_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_password_age_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_password_age_anyOf_i1)

- Type: null

<a id="headingADDED_fields_password_history"></a>
<a id="ADDED_fields_password_history"></a>
##### password_history (required)

- Schema name: `Password History`

This contains hashes of the ten most recent passwords used by local user accounts, and is for enforcing password history requirements as defined in system.security.
<a id="ADDED_fields_password_history_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_password_history_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_password_history_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_password_history_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_ADDED_fields_password_history_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_password_history_anyOf_i1)

- Type: null

<a id="headingADDED_fields_password_change_required"></a>
<a id="ADDED_fields_password_change_required"></a>
##### password_change_required (required)

- Schema name: `Password Change Required`
- Type: boolean

Password change for local user account is required on next login.

<a id="headingADDED_fields_roles"></a>
<a id="ADDED_fields_roles"></a>
##### roles (required)

- Schema name: `Roles`
- Type: array of string

Array of roles assigned to this user's groups. Roles control administrative access to TrueNAS through the web UI and API.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_roles_items"></a>
- Type: string

<a id="headingADDED_fields_api_keys"></a>
<a id="ADDED_fields_api_keys"></a>
##### api_keys (required)

- Schema name: `Api Keys`
- Type: array of integer

Array of API key IDs associated with this user account for programmatic access.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_api_keys_items"></a>
- Type: integer

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `UserChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `UserEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the user. Use this ID for `user.update` and `user.delete` API calls. This ID also appears in the `users` array for each group entry in `group.query` results. NOTE: For users from a directory service, the `id` is calculated by adding 100000000 to the `uid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

<a id="headingCHANGED_fields_uid"></a>
<a id="CHANGED_fields_uid"></a>
##### uid (required)

- Schema name: `Uid`
- Type: integer

A non-negative integer used to identify a system user. TrueNAS uses this value for permission checks and many other system purposes.

<a id="headingCHANGED_fields_username"></a>
<a id="CHANGED_fields_username"></a>
##### username (required)

- Schema name: `Username`

A string used to identify a user. Local accounts must use characters from the POSIX portable filename character set.
<a id="CHANGED_fields_username_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_username_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_username_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_unixhash"></a>
<a id="CHANGED_fields_unixhash"></a>
##### unixhash (required)

- Schema name: `Unixhash`

Hashed password for local accounts. This value is `null` for accounts provided by directory services.
<a id="CHANGED_fields_unixhash_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_unixhash_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_unixhash_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_unixhash_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_unixhash_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_smbhash"></a>
<a id="CHANGED_fields_smbhash"></a>
##### smbhash (required)

- Schema name: `Smbhash`

NT hash of the local account password for `smb` users. This value is `null` for accounts provided by directory services or non-SMB accounts.
<a id="CHANGED_fields_smbhash_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_smbhash_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_smbhash_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_smbhash_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_smbhash_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_home"></a>
<a id="CHANGED_fields_home"></a>
##### home

- Schema name: `Home`
- Type: string
- Default: "/var/empty"

The local file system path for the user account's home directory. Typically, this is required only if the account has shell access (local or SSH) to TrueNAS. This is not required for accounts used only for SMB share access.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_shell"></a>
<a id="CHANGED_fields_shell"></a>
##### shell

- Schema name: `Shell`
- Type: string
- Default: "/usr/bin/zsh"

Available choices can be retrieved with `user.shell_choices`.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_full_name"></a>
<a id="CHANGED_fields_full_name"></a>
##### full_name (required)

- Schema name: `Full Name`
- Type: string

Comment field to provide additional information about the user account. Typically, this is the full name of the user or a short description of a service account. There are no character set restrictions for this field. This field is for information only.

<a id="headingCHANGED_fields_builtin"></a>
<a id="CHANGED_fields_builtin"></a>
##### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `true`, the user account is an internal system account for the TrueNAS server. Typically, one should create dedicated user accounts for access to the TrueNAS server webui and shares.

<a id="headingCHANGED_fields_smb"></a>
<a id="CHANGED_fields_smb"></a>
##### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

The user account may be used to access SMB shares. If set to `true` then TrueNAS stores an NT hash of the user account's password for local accounts. This feature is unavailable for local accounts when General Purpose OS STIG compatibility mode is enabled. If set to `true` the user is automatically added to the `builtin_users` group.

<a id="headingCHANGED_fields_webshare"></a>
<a id="CHANGED_fields_webshare"></a>
##### webshare

- Schema name: `Webshare`
- Type: boolean
- Default: false

The user account may be used to access WebShare shares. If set to `true` the user is automatically added to the `webshare` group.

<a id="headingCHANGED_fields_userns_idmap"></a>
<a id="CHANGED_fields_userns_idmap"></a>
##### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subuid mapping for this user. If DIRECT then the UID will be directly mapped to all containers. Alternatively, the target UID may be explicitly specified. If `null`, then the UID will not be mapped. NOTE: This field will be ignored for users that have been assigned TrueNAS roles.
<a id="CHANGED_fields_userns_idmap_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_userns_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_userns_idmap_anyOf_i0)

- Type: enum (of null or string)
###### Must be one of:

- "DIRECT"
- null

<a id="tab-pane_CHANGED_fields_userns_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_userns_idmap_anyOf_i1)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

<a id="headingCHANGED_fields_group"></a>
<a id="CHANGED_fields_group"></a>
##### group (required)

- Schema name: `Group`
- Type: object

The primary group of the user account.

<a id="headingCHANGED_fields_groups"></a>
<a id="CHANGED_fields_groups"></a>
##### groups

- Schema name: `Groups`
- Type: array of integer

Array of additional groups to which the user belongs. NOTE: Groups are identified by their group entry `id`, not their Unix group ID (`gid`).
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_groups_items"></a>
- Type: integer

<a id="headingCHANGED_fields_password_disabled"></a>
<a id="CHANGED_fields_password_disabled"></a>
##### password_disabled

- Schema name: `Password Disabled`
- Type: boolean
- Default: false

If set to `true` password authentication for the user account is disabled. NOTE: Users with password authentication disabled may still authenticate to the TrueNAS server by other methods, such as SSH key-based authentication. NOTE: Password authentication is required for `smb` users.

<a id="headingCHANGED_fields_ssh_password_enabled"></a>
<a id="CHANGED_fields_ssh_password_enabled"></a>
##### ssh_password_enabled

- Schema name: `Ssh Password Enabled`
- Type: boolean
- Default: false

Allow the user to authenticate to the TrueNAS SSH server using a password. WARNING: The established best practice is to use only key-based authentication for SSH servers.

<a id="headingCHANGED_fields_sshpubkey"></a>
<a id="CHANGED_fields_sshpubkey"></a>
##### sshpubkey

- Schema name: `Sshpubkey`
- Default: null

SSH public keys corresponding to private keys that authenticate this user to the TrueNAS SSH server.
<a id="CHANGED_fields_sshpubkey_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_sshpubkey_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_sshpubkey_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_sshpubkey_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_sshpubkey_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_locked"></a>
<a id="CHANGED_fields_locked"></a>
##### locked

- Schema name: `Locked`
- Type: boolean
- Default: false

If set to `true` the account is locked. The account cannot be used to authenticate to the TrueNAS server.

<a id="headingCHANGED_fields_sudo_commands"></a>
<a id="CHANGED_fields_sudo_commands"></a>
##### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is prompted for password when executing any command from the array.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_sudo_commands_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_sudo_commands_nopasswd"></a>
<a id="CHANGED_fields_sudo_commands_nopasswd"></a>
##### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is *not* prompted for password when executing any command from the array.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_sudo_commands_nopasswd_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_email"></a>
<a id="CHANGED_fields_email"></a>
##### email

- Schema name: `Email`
- Default: null

Email address of the user. If the user has the `FULL_ADMIN` role, they will receive email alerts and notifications.
<a id="CHANGED_fields_email_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_email_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_email_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_local"></a>
<a id="CHANGED_fields_local"></a>
##### local (required)

- Schema name: `Local`
- Type: boolean

If `true`, the account is local to the TrueNAS server. If `false`, the account is provided by a directory service.

<a id="headingCHANGED_fields_immutable"></a>
<a id="CHANGED_fields_immutable"></a>
##### immutable (required)

- Schema name: `Immutable`
- Type: boolean

If `true`, the account is system-provided and most fields related to it may not be changed.

<a id="headingCHANGED_fields_twofactor_auth_configured"></a>
<a id="CHANGED_fields_twofactor_auth_configured"></a>
##### twofactor_auth_configured (required)

- Schema name: `Twofactor Auth Configured`
- Type: boolean

If `true`, the account has been configured for two-factor authentication. Users are prompted for a second factor when authenticating to the TrueNAS web UI and API. They may also be prompted when signing in to the TrueNAS SSH server using a password (depending on global two-factor authentication settings).

<a id="headingCHANGED_fields_sid"></a>
<a id="CHANGED_fields_sid"></a>
##### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
<a id="CHANGED_fields_sid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_sid_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_sid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_last_password_change"></a>
<a id="CHANGED_fields_last_password_change"></a>
##### last_password_change (required)

- Schema name: `Last Password Change`

The date of the last password change for local user accounts.
<a id="CHANGED_fields_last_password_change_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_last_password_change_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_last_password_change_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_fields_last_password_change_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_last_password_change_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_password_age"></a>
<a id="CHANGED_fields_password_age"></a>
##### password_age (required)

- Schema name: `Password Age`

The age in days of the password for local user accounts.
<a id="CHANGED_fields_password_age_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_password_age_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_password_age_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_password_age_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_password_age_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_password_history"></a>
<a id="CHANGED_fields_password_history"></a>
##### password_history (required)

- Schema name: `Password History`

This contains hashes of the ten most recent passwords used by local user accounts, and is for enforcing password history requirements as defined in system.security.
<a id="CHANGED_fields_password_history_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_password_history_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_password_history_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_password_history_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_CHANGED_fields_password_history_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_password_history_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_password_change_required"></a>
<a id="CHANGED_fields_password_change_required"></a>
##### password_change_required (required)

- Schema name: `Password Change Required`
- Type: boolean

Password change for local user account is required on next login.

<a id="headingCHANGED_fields_roles"></a>
<a id="CHANGED_fields_roles"></a>
##### roles (required)

- Schema name: `Roles`
- Type: array of string

Array of roles assigned to this user's groups. Roles control administrative access to TrueNAS through the web UI and API.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_roles_items"></a>
- Type: string

<a id="headingCHANGED_fields_api_keys"></a>
<a id="CHANGED_fields_api_keys"></a>
##### api_keys (required)

- Schema name: `Api Keys`
- Type: array of integer

Array of API key IDs associated with this user account for programmatic access.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_api_keys_items"></a>
- Type: integer

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `UserRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
