---
title: auth.login_ex_continue
kind: method
source_rst: _sources/api_methods_auth.login_ex_continue.rst.txt
source_html: api_methods_auth.login_ex_continue.html
required_roles:
  []
---

# auth.login_ex_continue

## Summary

Continue in-progress authentication attempt. This endpoint should be called to continue an auth.login_ex attempt that returned OTP_REQUIRED.

This is a convenience wrapper around auth.login_ex for API consumers.

params: mechanism: the mechanism by which to continue authentication. Currently the only supported mechanism here is OTP_TOKEN.

OTP_TOKEN otp_token: one-time password token. This is only permitted if a previous auth.login_ex call responded with "OTP_REQUIRED".

returns: JSON object containing the following keys:

`response_type` - will be one of the following: SUCCESS - continued auth was required

OTP_REQUIRED - otp token was rejected. API consumer may call this endpoint again with correct OTP token.

AUTH_ERR - invalid OTP token submitted too many times.

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

#### Parameter 1: login_data

<a id="Call_parameters_items_i0"></a>
#### login_data

- Schema name: `login_data`
- Type: object

OTP token data to continue two-factor authentication flow.
- No Additional Properties
<a id="headingCall_parameters_items_i0_mechanism"></a>
<a id="Call_parameters_items_i0_mechanism"></a>
##### mechanism (required)

- Schema name: `Mechanism`
- Type: const

Authentication mechanism identifier for one-time password tokens.
- Specific value: `"OTP_TOKEN"`

<a id="headingCall_parameters_items_i0_otp_token"></a>
<a id="Call_parameters_items_i0_otp_token"></a>
##### otp_token (required)

- Schema name: `Otp Token`
- Type: string

One-time password token for authentication.

<a id="headingCall_parameters_items_i0_login_options"></a>
<a id="Call_parameters_items_i0_login_options"></a>
##### login_options

- Schema name: `AuthCommonOptions`
- Type: object
- Default:
```json
{
  "user_info": true,
  "reconnect_token": false
}
```

Additional options for the authentication process.
- No Additional Properties
<a id="headingCall_parameters_items_i0_login_options_user_info"></a>
<a id="Call_parameters_items_i0_login_options_user_info"></a>
###### user_info

- Schema name: `User Info`
- Type: boolean
- Default: true

Whether to include detailed user information in the authentication response.

<a id="headingCall_parameters_items_i0_login_options_reconnect_token"></a>
<a id="Call_parameters_items_i0_login_options_reconnect_token"></a>
###### reconnect_token

- Schema name: `Reconnect Token`
- Type: boolean
- Default: false

Whether to include a reauthentication token in the authentication response. The `ttl` for the generated token depends on the TrueNAS webui setting for preferences->lifetime, with a default value of 600 seconds.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

Authentication response after continuing with OTP token.
<a id="Return_value_oneOf"></a>
#### One of

<a id="tab-pane_Return_value_oneOf_i0"></a>
##### [AuthRespSuccess](#tab-pane_Return_value_oneOf_i0)

- Schema name: `AuthRespSuccess`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oneOf_i0_response_type"></a>
<a id="Return_value_oneOf_i0_response_type"></a>
###### response_type (required)

- Schema name: `Response Type`
- Type: const

Authentication response type indicating successful login.
- Specific value: `"SUCCESS"`

<a id="headingReturn_value_oneOf_i0_user_info"></a>
<a id="Return_value_oneOf_i0_user_info"></a>
###### user_info (required)

Authenticated user information or `null` if not available.
<a id="Return_value_oneOf_i0_user_info_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_oneOf_i0_user_info_anyOf_i0"></a>
###### [AuthUserInfo](#tab-pane_Return_value_oneOf_i0_user_info_anyOf_i0)

- Schema name: `AuthUserInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_pw_name"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_pw_name"></a>
###### pw_name (required)

- Schema name: `Pw Name`
- Type: string

Name of the user.

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_pw_gecos"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_pw_gecos"></a>
###### pw_gecos (required)

- Schema name: `Pw Gecos`
- Type: string

Full username or comment field.

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_pw_dir"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_pw_dir"></a>
###### pw_dir (required)

- Schema name: `Pw Dir`
- Type: string

User home directory.

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_pw_shell"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_pw_shell"></a>
###### pw_shell (required)

- Schema name: `Pw Shell`
- Type: string

User command line interpreter.

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_pw_uid"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_pw_uid"></a>
###### pw_uid (required)

- Schema name: `Pw Uid`
- Type: integer

Numerical user ID of the user.

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_pw_gid"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_pw_gid"></a>
###### pw_gid (required)

- Schema name: `Pw Gid`
- Type: integer

Numerical group id for the user's primary group.

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_grouplist"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_grouplist"></a>
###### grouplist (required)

- Schema name: `Grouplist`

Optional array of group IDs for groups of which this account is a member. If `get_groups` is not specified, this value will be `null`.
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_grouplist_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_oneOf_i0_user_info_anyOf_i0_grouplist_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_oneOf_i0_user_info_anyOf_i0_grouplist_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_oneOf_i0_user_info_anyOf_i0_grouplist_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_oneOf_i0_user_info_anyOf_i0_grouplist_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_oneOf_i0_user_info_anyOf_i0_grouplist_anyOf_i1)

- Type: null

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_sid"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_sid"></a>
###### sid (required)

- Schema name: `Sid`

Optional SID value for the account that is present if `sid_info` is specified in payload.
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_sid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_oneOf_i0_user_info_anyOf_i0_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_oneOf_i0_user_info_anyOf_i0_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_oneOf_i0_user_info_anyOf_i0_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_oneOf_i0_user_info_anyOf_i0_sid_anyOf_i1)

- Type: null

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_source"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: enum (of string)

The source for the user account.
###### Must be one of:

- "LOCAL"
- "ACTIVEDIRECTORY"
- "LDAP"

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_local"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_local"></a>
###### local (required)

- Schema name: `Local`
- Type: boolean

The account is local to TrueNAS or provided by a directory service.

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_attributes"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`
- Type: object

Custom user attributes and metadata.

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_two_factor_config"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_two_factor_config"></a>
###### two_factor_config (required)

- Schema name: `Two Factor Config`
- Type: object

Two-factor authentication configuration for the user.

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_privilege"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_privilege"></a>
###### privilege (required)

- Schema name: `Privilege`
- Type: object

User privilege and role information.

<a id="headingReturn_value_oneOf_i0_user_info_anyOf_i0_account_attributes"></a>
<a id="Return_value_oneOf_i0_user_info_anyOf_i0_account_attributes"></a>
###### account_attributes (required)

- Schema name: `Account Attributes`
- Type: array of string

Array of account attribute names available for this user.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_oneOf_i0_user_info_anyOf_i0_account_attributes_items"></a>
- Type: string

<a id="tab-pane_Return_value_oneOf_i0_user_info_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_oneOf_i0_user_info_anyOf_i1)

- Type: null

<a id="headingReturn_value_oneOf_i0_authenticator"></a>
<a id="Return_value_oneOf_i0_authenticator"></a>
###### authenticator (required)

- Schema name: `Authenticator`
- Type: enum (of string)

Authentication level achieved (LEVEL*1 for password, LEVEL*2 for two-factor).
###### Must be one of:

- "LEVEL_1"
- "LEVEL_2"

<a id="headingReturn_value_oneOf_i0_reconnect_token"></a>
<a id="Return_value_oneOf_i0_reconnect_token"></a>
###### reconnect_token (required)

- Schema name: `Reconnect Token`

Single-use token that can be used to reauthenticate to the truenas server in case websocket session is interrupted. This will be `null` in the following situations: 1) The initiating authentication request set `reconnect_token` to `false` (default). 2) The user authenticated via a one-time password, which does not support reconnect token creation.
<a id="Return_value_oneOf_i0_reconnect_token_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_oneOf_i0_reconnect_token_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_oneOf_i0_reconnect_token_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_oneOf_i0_reconnect_token_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_oneOf_i0_reconnect_token_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_oneOf_i1"></a>
##### [AuthRespAuthErr](#tab-pane_Return_value_oneOf_i1)

- Schema name: `AuthRespAuthErr`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oneOf_i1_response_type"></a>
<a id="Return_value_oneOf_i1_response_type"></a>
###### response_type (required)

- Schema name: `Response Type`
- Type: const

Authentication response type indicating authentication failure.
- Specific value: `"AUTH_ERR"`

<a id="tab-pane_Return_value_oneOf_i2"></a>
##### [AuthRespExpired](#tab-pane_Return_value_oneOf_i2)

- Schema name: `AuthRespExpired`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oneOf_i2_response_type"></a>
<a id="Return_value_oneOf_i2_response_type"></a>
###### response_type (required)

- Schema name: `Response Type`
- Type: const

Authentication response type indicating the session or token has expired.
- Specific value: `"EXPIRED"`

<a id="tab-pane_Return_value_oneOf_i3"></a>
##### [AuthRespOTPRequired](#tab-pane_Return_value_oneOf_i3)

- Schema name: `AuthRespOTPRequired`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oneOf_i3_response_type"></a>
<a id="Return_value_oneOf_i3_response_type"></a>
###### response_type (required)

- Schema name: `Response Type`
- Type: const

Authentication response type indicating one-time password is required.
- Specific value: `"OTP_REQUIRED"`

<a id="headingReturn_value_oneOf_i3_username"></a>
<a id="Return_value_oneOf_i3_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username for which OTP is required.

<a id="tab-pane_Return_value_oneOf_i4"></a>
##### [AuthRespAuthRedirect](#tab-pane_Return_value_oneOf_i4)

- Schema name: `AuthRespAuthRedirect`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oneOf_i4_response_type"></a>
<a id="Return_value_oneOf_i4_response_type"></a>
###### response_type (required)

- Schema name: `Response Type`
- Type: const

Authentication response type indicating redirect is required.
- Specific value: `"REDIRECT"`

<a id="headingReturn_value_oneOf_i4_urls"></a>
<a id="Return_value_oneOf_i4_urls"></a>
###### urls (required)

- Schema name: `Urls`
- Type: array of string

Array of URLs to redirect to for authentication completion.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_oneOf_i4_urls_items"></a>
- Type: string

<a id="tab-pane_Return_value_oneOf_i5"></a>
##### [AuthRespDenied](#tab-pane_Return_value_oneOf_i5)

- Schema name: `AuthRespDenied`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oneOf_i5_response_type"></a>
<a id="Return_value_oneOf_i5_response_type"></a>
###### response_type (required)

- Schema name: `Response Type`
- Type: const

Authentication response type indicating that the credential lacks API access.
- Specific value: `"DENIED"`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
