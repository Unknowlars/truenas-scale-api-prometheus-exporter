---
title: user.get_instance
kind: method
source_rst: _sources/api_methods_user.get_instance.rst.txt
source_html: api_methods_user.get_instance.html
required_roles:
  - ACCOUNT_READ
---

# user.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

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

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `UserEntry`
- Type: object
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

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
