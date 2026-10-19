---
title: user.renew_2fa_secret
kind: method
source_rst: _sources/api_methods_user.renew_2fa_secret.rst.txt
source_html: api_methods_user.renew_2fa_secret.html
required_roles:
  []
---

# user.renew_2fa_secret

## Summary

Renew `username` user's two-factor authentication secret.

.. note::

This username must match the authenticated username unless authenticated credentials have the `FULL_ADMIN` role.

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

#### Parameter 1: username

<a id="Call_parameters_items_i0"></a>
#### username

- Schema name: `username`
- Type: string

Username to renew two-factor authentication secret for.

#### Parameter 2: twofactor_options

<a id="Call_parameters_items_i1"></a>
#### twofactor_options

- Schema name: `twofactor_options`
- Type: object

Configuration options for the new two-factor authentication setup.
- No Additional Properties
<a id="headingCall_parameters_items_i1_otp_digits"></a>
<a id="Call_parameters_items_i1_otp_digits"></a>
##### otp_digits

- Schema name: `Otp Digits`
- Type: integer

Represents number of allowed digits in the OTP.
- Value must be greater or equal to `6` and lesser or equal to `8`

<a id="headingCall_parameters_items_i1_interval"></a>
<a id="Call_parameters_items_i1_interval"></a>
##### interval

- Schema name: `Interval`
- Type: enum (of integer)

Time duration in seconds specifying OTP expiration time from its creation time. Only 30 or 60 are supported.
###### Must be one of:

- 30
- 60

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `UserRenew2faSecretResult`
- Type: object

UserRenew2faSecretResult return fields.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

This is the API identifier for the user. Use this ID for `user.update` and `user.delete` API calls. This ID also appears in the `users` array for each group entry in `group.query` results. NOTE: For users from a directory service, the `id` is calculated by adding 100000000 to the `uid`. This ensures consistent API results. You cannot change directory service accounts through TrueNAS.

<a id="headingReturn_value_uid"></a>
<a id="Return_value_uid"></a>
#### uid (required)

- Schema name: `Uid`
- Type: integer

A non-negative integer used to identify a system user. TrueNAS uses this value for permission checks and many other system purposes.

<a id="headingReturn_value_username"></a>
<a id="Return_value_username"></a>
#### username (required)

- Schema name: `Username`

A string used to identify a user. Local accounts must use characters from the POSIX portable filename character set.
<a id="Return_value_username_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_username_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_username_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_unixhash"></a>
<a id="Return_value_unixhash"></a>
#### unixhash (required)

- Schema name: `Unixhash`

Hashed password for local accounts. This value is `null` for accounts provided by directory services.
<a id="Return_value_unixhash_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_unixhash_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_unixhash_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_unixhash_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_unixhash_anyOf_i1)

- Type: null

<a id="headingReturn_value_smbhash"></a>
<a id="Return_value_smbhash"></a>
#### smbhash (required)

- Schema name: `Smbhash`

NT hash of the local account password for `smb` users. This value is `null` for accounts provided by directory services or non-SMB accounts.
<a id="Return_value_smbhash_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_smbhash_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_smbhash_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_smbhash_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_smbhash_anyOf_i1)

- Type: null

<a id="headingReturn_value_home"></a>
<a id="Return_value_home"></a>
#### home

- Schema name: `Home`
- Type: string
- Default: "/var/empty"

The local file system path for the user account's home directory. Typically, this is required only if the account has shell access (local or SSH) to TrueNAS. This is not required for accounts used only for SMB share access.
- Must be at least `1` characters long

<a id="headingReturn_value_shell"></a>
<a id="Return_value_shell"></a>
#### shell

- Schema name: `Shell`
- Type: string
- Default: "/usr/bin/zsh"

Available choices can be retrieved with `user.shell_choices`.
- Must be at least `1` characters long

<a id="headingReturn_value_full_name"></a>
<a id="Return_value_full_name"></a>
#### full_name (required)

- Schema name: `Full Name`
- Type: string

Comment field to provide additional information about the user account. Typically, this is the full name of the user or a short description of a service account. There are no character set restrictions for this field. This field is for information only.

<a id="headingReturn_value_builtin"></a>
<a id="Return_value_builtin"></a>
#### builtin (required)

- Schema name: `Builtin`
- Type: boolean

If `true`, the user account is an internal system account for the TrueNAS server. Typically, one should create dedicated user accounts for access to the TrueNAS server webui and shares.

<a id="headingReturn_value_smb"></a>
<a id="Return_value_smb"></a>
#### smb

- Schema name: `Smb`
- Type: boolean
- Default: true

The user account may be used to access SMB shares. If set to `true` then TrueNAS stores an NT hash of the user account's password for local accounts. This feature is unavailable for local accounts when General Purpose OS STIG compatibility mode is enabled. If set to `true` the user is automatically added to the `builtin_users` group.

<a id="headingReturn_value_webshare"></a>
<a id="Return_value_webshare"></a>
#### webshare

- Schema name: `Webshare`
- Type: boolean
- Default: false

The user account may be used to access WebShare shares. If set to `true` the user is automatically added to the `webshare` group.

<a id="headingReturn_value_userns_idmap"></a>
<a id="Return_value_userns_idmap"></a>
#### userns_idmap

- Schema name: `Userns Idmap`
- Default: null

Specifies the subuid mapping for this user. If DIRECT then the UID will be directly mapped to all containers. Alternatively, the target UID may be explicitly specified. If `null`, then the UID will not be mapped. NOTE: This field will be ignored for users that have been assigned TrueNAS roles.
<a id="Return_value_userns_idmap_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_userns_idmap_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_userns_idmap_anyOf_i0)

- Type: enum (of null or string)
###### Must be one of:

- "DIRECT"
- null

<a id="tab-pane_Return_value_userns_idmap_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_userns_idmap_anyOf_i1)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `4294967294`

<a id="headingReturn_value_group"></a>
<a id="Return_value_group"></a>
#### group (required)

- Schema name: `Group`
- Type: object

The primary group of the user account.

<a id="headingReturn_value_groups"></a>
<a id="Return_value_groups"></a>
#### groups

- Schema name: `Groups`
- Type: array of integer

Array of additional groups to which the user belongs. NOTE: Groups are identified by their group entry `id`, not their Unix group ID (`gid`).
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_groups_items"></a>
- Type: integer

<a id="headingReturn_value_password_disabled"></a>
<a id="Return_value_password_disabled"></a>
#### password_disabled

- Schema name: `Password Disabled`
- Type: boolean
- Default: false

If set to `true` password authentication for the user account is disabled. NOTE: Users with password authentication disabled may still authenticate to the TrueNAS server by other methods, such as SSH key-based authentication. NOTE: Password authentication is required for `smb` users.

<a id="headingReturn_value_ssh_password_enabled"></a>
<a id="Return_value_ssh_password_enabled"></a>
#### ssh_password_enabled

- Schema name: `Ssh Password Enabled`
- Type: boolean
- Default: false

Allow the user to authenticate to the TrueNAS SSH server using a password. WARNING: The established best practice is to use only key-based authentication for SSH servers.

<a id="headingReturn_value_sshpubkey"></a>
<a id="Return_value_sshpubkey"></a>
#### sshpubkey

- Schema name: `Sshpubkey`
- Default: null

SSH public keys corresponding to private keys that authenticate this user to the TrueNAS SSH server.
<a id="Return_value_sshpubkey_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_sshpubkey_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sshpubkey_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_sshpubkey_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sshpubkey_anyOf_i1)

- Type: null

<a id="headingReturn_value_locked"></a>
<a id="Return_value_locked"></a>
#### locked

- Schema name: `Locked`
- Type: boolean
- Default: false

If set to `true` the account is locked. The account cannot be used to authenticate to the TrueNAS server.

<a id="headingReturn_value_sudo_commands"></a>
<a id="Return_value_sudo_commands"></a>
#### sudo_commands

- Schema name: `Sudo Commands`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is prompted for password when executing any command from the array.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_sudo_commands_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_sudo_commands_nopasswd"></a>
<a id="Return_value_sudo_commands_nopasswd"></a>
#### sudo_commands_nopasswd

- Schema name: `Sudo Commands Nopasswd`
- Type: array of string

An array of commands the user may execute with elevated privileges. User is *not* prompted for password when executing any command from the array.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_sudo_commands_nopasswd_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_email"></a>
<a id="Return_value_email"></a>
#### email

- Schema name: `Email`
- Default: null

Email address of the user. If the user has the `FULL_ADMIN` role, they will receive email alerts and notifications.
<a id="Return_value_email_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_email_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_email_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_email_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_email_anyOf_i1)

- Type: null

<a id="headingReturn_value_local"></a>
<a id="Return_value_local"></a>
#### local (required)

- Schema name: `Local`
- Type: boolean

If `true`, the account is local to the TrueNAS server. If `false`, the account is provided by a directory service.

<a id="headingReturn_value_immutable"></a>
<a id="Return_value_immutable"></a>
#### immutable (required)

- Schema name: `Immutable`
- Type: boolean

If `true`, the account is system-provided and most fields related to it may not be changed.

<a id="headingReturn_value_twofactor_auth_configured"></a>
<a id="Return_value_twofactor_auth_configured"></a>
#### twofactor_auth_configured (required)

- Schema name: `Twofactor Auth Configured`
- Type: boolean

If `true`, the account has been configured for two-factor authentication. Users are prompted for a second factor when authenticating to the TrueNAS web UI and API. They may also be prompted when signing in to the TrueNAS SSH server using a password (depending on global two-factor authentication settings).

<a id="headingReturn_value_sid"></a>
<a id="Return_value_sid"></a>
#### sid (required)

- Schema name: `Sid`

The Security Identifier (SID) of the user if the account an `smb` account. The SMB server uses this value to check share access and for other purposes.
<a id="Return_value_sid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sid_anyOf_i1)

- Type: null

<a id="headingReturn_value_last_password_change"></a>
<a id="Return_value_last_password_change"></a>
#### last_password_change (required)

- Schema name: `Last Password Change`

The date of the last password change for local user accounts.
<a id="Return_value_last_password_change_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_last_password_change_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_last_password_change_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_last_password_change_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_last_password_change_anyOf_i1)

- Type: null

<a id="headingReturn_value_password_age"></a>
<a id="Return_value_password_age"></a>
#### password_age (required)

- Schema name: `Password Age`

The age in days of the password for local user accounts.
<a id="Return_value_password_age_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_password_age_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_password_age_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_password_age_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_password_age_anyOf_i1)

- Type: null

<a id="headingReturn_value_password_history"></a>
<a id="Return_value_password_history"></a>
#### password_history (required)

- Schema name: `Password History`

This contains hashes of the ten most recent passwords used by local user accounts, and is for enforcing password history requirements as defined in system.security.
<a id="Return_value_password_history_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_password_history_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_password_history_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_password_history_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_Return_value_password_history_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_password_history_anyOf_i1)

- Type: null

<a id="headingReturn_value_password_change_required"></a>
<a id="Return_value_password_change_required"></a>
#### password_change_required (required)

- Schema name: `Password Change Required`
- Type: boolean

Password change for local user account is required on next login.

<a id="headingReturn_value_roles"></a>
<a id="Return_value_roles"></a>
#### roles (required)

- Schema name: `Roles`
- Type: array of string

Array of roles assigned to this user's groups. Roles control administrative access to TrueNAS through the web UI and API.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_roles_items"></a>
- Type: string

<a id="headingReturn_value_api_keys"></a>
<a id="Return_value_api_keys"></a>
#### api_keys (required)

- Schema name: `Api Keys`
- Type: array of integer

Array of API key IDs associated with this user account for programmatic access.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_api_keys_items"></a>
- Type: integer

<a id="headingReturn_value_twofactor_config"></a>
<a id="Return_value_twofactor_config"></a>
#### twofactor_config (required)

- Schema name: `UserTwofactorConfigEntry`
- Type: object

New two-factor authentication configuration with provisioning details.
- No Additional Properties
<a id="headingReturn_value_twofactor_config_provisioning_uri"></a>
<a id="Return_value_twofactor_config_provisioning_uri"></a>
##### provisioning_uri (required)

- Schema name: `Provisioning Uri`

QR code URI for setting up two-factor authentication in authenticator apps. `null` if not available.
<a id="Return_value_twofactor_config_provisioning_uri_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_twofactor_config_provisioning_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_twofactor_config_provisioning_uri_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_twofactor_config_provisioning_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_twofactor_config_provisioning_uri_anyOf_i1)

- Type: null

<a id="headingReturn_value_twofactor_config_secret_configured"></a>
<a id="Return_value_twofactor_config_secret_configured"></a>
##### secret_configured (required)

- Schema name: `Secret Configured`
- Type: boolean

Whether a two-factor authentication secret has been configured for this user.

<a id="headingReturn_value_twofactor_config_interval"></a>
<a id="Return_value_twofactor_config_interval"></a>
##### interval (required)

- Schema name: `Interval`
- Type: integer

Time interval in seconds for OTP validity period.

<a id="headingReturn_value_twofactor_config_otp_digits"></a>
<a id="Return_value_twofactor_config_otp_digits"></a>
##### otp_digits (required)

- Schema name: `Otp Digits`
- Type: integer

Number of digits in the generated one-time password codes.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
