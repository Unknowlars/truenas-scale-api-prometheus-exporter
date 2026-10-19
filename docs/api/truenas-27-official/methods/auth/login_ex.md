---
title: auth.login_ex
kind: method
source_rst: _sources/api_methods_auth.login_ex.rst.txt
source_html: api_methods_auth.login_ex.html
required_roles:
  []
---

# auth.login_ex

## Summary

Authenticate using one of a variety of mechanisms.

The mechanism is selected by the `mechanism` field of the request, and the set of supported mechanisms will be expanded in future releases.

.. warning::

Mechanisms with a `_PLAIN` suffix involve passing plain-text passwords or password-equivalent strings and should not be used over untrusted or insecure transport.

The `response_type` of the result indicates the outcome of the current authentication step and whether further action is required to complete authentication:

- `SUCCESS` -- authentication completed and a session was established. - `OTP_REQUIRED` -- the account requires a one-time password; the client must continue authentication by submitting the token via the `OTP_TOKEN` mechanism. - `AUTH_ERR` -- generic authentication failure corresponding to `PAM_AUTH_ERR` and `PAM_USER_UNKNOWN` from libpam. Returned when the account does not exist or the credential is incorrect. - `EXPIRED` -- the supplied credential is expired and not suitable for authentication. - `REDIRECT` -- authentication must be performed on a different server.

A JSON-RPC `error` response (code `-32001`, *Method call error*) is returned instead of a result in the following cases:

- a multistep challenge-response mechanism is in progress and the supplied `mechanism` does not match the expected next step (errno `EBUSY`) - the `OTP_TOKEN` mechanism is used without a preceding step having requested it (errno `EINVAL`) - the current authenticator assurance level prohibits the supplied mechanism (errno `EOPNOTSUPP`)

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

Authentication data specifying mechanism and credentials.
<a id="Call_parameters_items_i0_oneOf"></a>
##### One of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0"></a>
###### [AuthApiKeyPlain](#tab-pane_Call_parameters_items_i0_oneOf_i0)

- Schema name: `AuthApiKeyPlain`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i0_mechanism"></a>
<a id="Call_parameters_items_i0_oneOf_i0_mechanism"></a>
###### mechanism (required)

- Schema name: `Mechanism`
- Type: const

Authentication mechanism identifier for plain API key authentication.
- Specific value: `"API_KEY_PLAIN"`

<a id="headingCall_parameters_items_i0_oneOf_i0_username"></a>
<a id="Call_parameters_items_i0_oneOf_i0_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username associated with the API key.

<a id="headingCall_parameters_items_i0_oneOf_i0_api_key"></a>
<a id="Call_parameters_items_i0_oneOf_i0_api_key"></a>
###### api_key (required)

- Schema name: `Api Key`
- Type: string

API key for authentication.

<a id="headingCall_parameters_items_i0_oneOf_i0_login_options"></a>
<a id="Call_parameters_items_i0_oneOf_i0_login_options"></a>
###### login_options

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
<a id="headingCall_parameters_items_i0_oneOf_i0_login_options_user_info"></a>
<a id="Call_parameters_items_i0_oneOf_i0_login_options_user_info"></a>
###### user_info

- Schema name: `User Info`
- Type: boolean
- Default: true

Whether to include detailed user information in the authentication response.

<a id="headingCall_parameters_items_i0_oneOf_i0_login_options_reconnect_token"></a>
<a id="Call_parameters_items_i0_oneOf_i0_login_options_reconnect_token"></a>
###### reconnect_token

- Schema name: `Reconnect Token`
- Type: boolean
- Default: false

Whether to include a reauthentication token in the authentication response. The `ttl` for the generated token depends on the TrueNAS webui setting for preferences->lifetime, with a default value of 600 seconds.

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1"></a>
###### [AuthPasswordPlain](#tab-pane_Call_parameters_items_i0_oneOf_i1)

- Schema name: `AuthPasswordPlain`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i1_mechanism"></a>
<a id="Call_parameters_items_i0_oneOf_i1_mechanism"></a>
###### mechanism (required)

- Schema name: `Mechanism`
- Type: const

Authentication mechanism identifier for plain password authentication.
- Specific value: `"PASSWORD_PLAIN"`

<a id="headingCall_parameters_items_i0_oneOf_i1_username"></a>
<a id="Call_parameters_items_i0_oneOf_i1_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username for authentication.

<a id="headingCall_parameters_items_i0_oneOf_i1_password"></a>
<a id="Call_parameters_items_i0_oneOf_i1_password"></a>
###### password (required)

- Schema name: `Password`
- Type: string

Password for authentication.

<a id="headingCall_parameters_items_i0_oneOf_i1_login_options"></a>
<a id="Call_parameters_items_i0_oneOf_i1_login_options"></a>
###### login_options

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
<a id="headingCall_parameters_items_i0_oneOf_i1_login_options_user_info"></a>
<a id="Call_parameters_items_i0_oneOf_i1_login_options_user_info"></a>
###### user_info

- Schema name: `User Info`
- Type: boolean
- Default: true

Whether to include detailed user information in the authentication response.

<a id="headingCall_parameters_items_i0_oneOf_i1_login_options_reconnect_token"></a>
<a id="Call_parameters_items_i0_oneOf_i1_login_options_reconnect_token"></a>
###### reconnect_token

- Schema name: `Reconnect Token`
- Type: boolean
- Default: false

Whether to include a reauthentication token in the authentication response. The `ttl` for the generated token depends on the TrueNAS webui setting for preferences->lifetime, with a default value of 600 seconds.

<a id="tab-pane_Call_parameters_items_i0_oneOf_i2"></a>
###### [AuthTokenPlain](#tab-pane_Call_parameters_items_i0_oneOf_i2)

- Schema name: `AuthTokenPlain`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i2_mechanism"></a>
<a id="Call_parameters_items_i0_oneOf_i2_mechanism"></a>
###### mechanism (required)

- Schema name: `Mechanism`
- Type: const

Authentication mechanism type for plain token login.
- Specific value: `"TOKEN_PLAIN"`

<a id="headingCall_parameters_items_i0_oneOf_i2_token"></a>
<a id="Call_parameters_items_i0_oneOf_i2_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Authentication token (masked for security).

<a id="headingCall_parameters_items_i0_oneOf_i2_login_options"></a>
<a id="Call_parameters_items_i0_oneOf_i2_login_options"></a>
###### login_options

- Schema name: `AuthCommonOptions`
- Type: object
- Default:
```json
{
  "user_info": true,
  "reconnect_token": false
}
```

Common authentication options and settings.
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i2_login_options_user_info"></a>
<a id="Call_parameters_items_i0_oneOf_i2_login_options_user_info"></a>
###### user_info

- Schema name: `User Info`
- Type: boolean
- Default: true

Whether to include detailed user information in the authentication response.

<a id="headingCall_parameters_items_i0_oneOf_i2_login_options_reconnect_token"></a>
<a id="Call_parameters_items_i0_oneOf_i2_login_options_reconnect_token"></a>
###### reconnect_token

- Schema name: `Reconnect Token`
- Type: boolean
- Default: false

Whether to include a reauthentication token in the authentication response. The `ttl` for the generated token depends on the TrueNAS webui setting for preferences->lifetime, with a default value of 600 seconds.

<a id="tab-pane_Call_parameters_items_i0_oneOf_i3"></a>
###### [AuthOTPToken](#tab-pane_Call_parameters_items_i0_oneOf_i3)

- Schema name: `AuthOTPToken`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i3_mechanism"></a>
<a id="Call_parameters_items_i0_oneOf_i3_mechanism"></a>
###### mechanism (required)

- Schema name: `Mechanism`
- Type: const

Authentication mechanism identifier for one-time password tokens.
- Specific value: `"OTP_TOKEN"`

<a id="headingCall_parameters_items_i0_oneOf_i3_otp_token"></a>
<a id="Call_parameters_items_i0_oneOf_i3_otp_token"></a>
###### otp_token (required)

- Schema name: `Otp Token`
- Type: string

One-time password token for authentication.

<a id="headingCall_parameters_items_i0_oneOf_i3_login_options"></a>
<a id="Call_parameters_items_i0_oneOf_i3_login_options"></a>
###### login_options

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
<a id="headingCall_parameters_items_i0_oneOf_i3_login_options_user_info"></a>
<a id="Call_parameters_items_i0_oneOf_i3_login_options_user_info"></a>
###### user_info

- Schema name: `User Info`
- Type: boolean
- Default: true

Whether to include detailed user information in the authentication response.

<a id="headingCall_parameters_items_i0_oneOf_i3_login_options_reconnect_token"></a>
<a id="Call_parameters_items_i0_oneOf_i3_login_options_reconnect_token"></a>
###### reconnect_token

- Schema name: `Reconnect Token`
- Type: boolean
- Default: false

Whether to include a reauthentication token in the authentication response. The `ttl` for the generated token depends on the TrueNAS webui setting for preferences->lifetime, with a default value of 600 seconds.

<a id="tab-pane_Call_parameters_items_i0_oneOf_i4"></a>
###### [AuthSCRAM](#tab-pane_Call_parameters_items_i0_oneOf_i4)

- Schema name: `AuthSCRAM`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i4_mechanism"></a>
<a id="Call_parameters_items_i0_oneOf_i4_mechanism"></a>
###### mechanism (required)

- Schema name: `Mechanism`
- Type: const

Authentication mechanism that implements SHA512-based RFC5802 authentication. The authentication mechanism provides replay resistence and capability for mutual validation of server and client sessions. The authentication mechanism is currently limited to API key credentials, but at a future point will be expanded to cover local user authentication. Channel binding (RFC 5929 tls-server-end-point) is supported and negotiated per exchange. A client that requires it sends a `p=tls-server-end-point` gs2 header over a TLS connection (see `rfc_str`) and the server verifies it against the certificate it serves; binding is only honored over TLS and remains optional, so clients that do not request it still authenticate. C and python libraries to for managing the client-side portion of the authentication exchanges are provided at https://github.com/truenas/truenas_scram.
- Specific value: `"SCRAM"`

<a id="headingCall_parameters_items_i0_oneOf_i4_scram_type"></a>
<a id="Call_parameters_items_i0_oneOf_i4_scram_type"></a>
###### scram_type (required)

- Schema name: `Scram Type`
- Type: enum (of string)

Scram message type from client. The scram types indicate the message type that is represented by the `rfc_str` field. CLIENT*FIRST*MESSAGE - this corresponds with the client-first-message as defined in RFC5802. CLIENT*FINAL*MESSAGE - this corresponds with the client-final-message as defined in RFC5802.
###### Must be one of:

- "CLIENT_FIRST_MESSAGE"
- "CLIENT_FINAL_MESSAGE"

<a id="headingCall_parameters_items_i0_oneOf_i4_rfc_str"></a>
<a id="Call_parameters_items_i0_oneOf_i4_rfc_str"></a>
###### rfc_str (required)

- Schema name: `Rfc Str`
- Type: string

This field contains the SCRAM authentication exchange message as defined in RFC5802. The expected format and contents depends on the `scram_type`. CLIENT*FIRST*MESSAGE: `n,,n=user:10,r=fyko+d2lbbFgONRv9qkxdawL` The `n,,` component indicates that client does not support channel bindings. `n=user:10` specifies the username and API key id (separated by `:` character). `r=fyko+d2lbbFgONRv9qkxdawL` specifies a base64-encoded nonce generated client-side. CLIENT*FINAL*MESSAGE: c=biws,r=fyko+d2lbbFgONRv9qkxdawL3rfcNHYJY1ZVvWVs7j, p=v0X8v3Bz2T0CJGbJQyF0X+HI4Ts= `c=biws` contains channel binding information. In this example it's the base64-encoded string `n,,` (no channel binding support). `r=fyko+d2lbbFgONRv9qkxdawL3rfcNHYJY1ZVvWVs7j` contains the combined client and server nonce as returned by the response to the CLIENT*FIRST*MESSAGE. `p=v0X8v3Bz2T0CJGbJQyF0X+HI4Ts=` contains the base64-encoded client proof generated based on client-side key material and client + server nonce.
Examples:

```json
"n,,n=user,r=fyko+d2lbbFgONRv9qkxdawL"
```
Examples:

```json
"c=biws,r=fyko+d2lbbFgONRv9qkxdawL3rfcNHYJY1ZVvWVs7j,p=v0X8v3Bz2T0CJGbJQyF0X+HI4Ts="
```

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

Authentication response indicating success, failure, or additional steps required.
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
##### [AuthRespScram](#tab-pane_Return_value_oneOf_i5)

- Schema name: `AuthRespScram`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oneOf_i5_response_type"></a>
<a id="Return_value_oneOf_i5_response_type"></a>
###### response_type (required)

- Schema name: `Response Type`
- Type: const

Authentication response type indicating a SCRAM server response.
- Specific value: `"SCRAM_RESPONSE"`

<a id="headingReturn_value_oneOf_i5_scram_type"></a>
<a id="Return_value_oneOf_i5_scram_type"></a>
###### scram_type (required)

- Schema name: `Scram Type`
- Type: enum (of string)

The type of server response. The SERVER*FIRST*RESPONSE will contain nonce, salt, and iterations. The SERVER*FINAL*RESPONSE will contain the server verification proof for client mutual validation.
###### Must be one of:

- "SERVER_FIRST_RESPONSE"
- "SERVER_FINAL_RESPONSE"

<a id="headingReturn_value_oneOf_i5_rfc_str"></a>
<a id="Return_value_oneOf_i5_rfc_str"></a>
###### rfc_str (required)

- Schema name: `Rfc Str`
- Type: string

Server authentication response containing string per RFC5802.
Examples:

```json
"r=fyko+d2lbbFgONRv9qkxdawL3rfcNHYJY1ZVvWVs7j,s=QSXCR+Q6sek8bf92,i=500000"
```
Examples:

```json
"v=rmF9pqV8S7suAoZWja4dJRkFsKQ="
```

<a id="headingReturn_value_oneOf_i5_user_info"></a>
<a id="Return_value_oneOf_i5_user_info"></a>
###### user_info (required)

Authenticated user information on SERVER*FINAL*RESPONSE or null on SERVER*FIRST*RESPONSE.
<a id="Return_value_oneOf_i5_user_info_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_oneOf_i5_user_info_anyOf_i0"></a>
###### [AuthUserInfo](#tab-pane_Return_value_oneOf_i5_user_info_anyOf_i0)

- Schema name: `AuthUserInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_pw_name"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_pw_name"></a>
###### pw_name (required)

- Schema name: `Pw Name`
- Type: string

Name of the user.

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_pw_gecos"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_pw_gecos"></a>
###### pw_gecos (required)

- Schema name: `Pw Gecos`
- Type: string

Full username or comment field.

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_pw_dir"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_pw_dir"></a>
###### pw_dir (required)

- Schema name: `Pw Dir`
- Type: string

User home directory.

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_pw_shell"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_pw_shell"></a>
###### pw_shell (required)

- Schema name: `Pw Shell`
- Type: string

User command line interpreter.

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_pw_uid"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_pw_uid"></a>
###### pw_uid (required)

- Schema name: `Pw Uid`
- Type: integer

Numerical user ID of the user.

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_pw_gid"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_pw_gid"></a>
###### pw_gid (required)

- Schema name: `Pw Gid`
- Type: integer

Numerical group id for the user's primary group.

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_grouplist"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_grouplist"></a>
###### grouplist (required)

- Schema name: `Grouplist`

Optional array of group IDs for groups of which this account is a member. If `get_groups` is not specified, this value will be `null`.
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_grouplist_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_oneOf_i5_user_info_anyOf_i0_grouplist_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_oneOf_i5_user_info_anyOf_i0_grouplist_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_oneOf_i5_user_info_anyOf_i0_grouplist_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_oneOf_i5_user_info_anyOf_i0_grouplist_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_oneOf_i5_user_info_anyOf_i0_grouplist_anyOf_i1)

- Type: null

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_sid"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_sid"></a>
###### sid (required)

- Schema name: `Sid`

Optional SID value for the account that is present if `sid_info` is specified in payload.
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_sid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_oneOf_i5_user_info_anyOf_i0_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_oneOf_i5_user_info_anyOf_i0_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_oneOf_i5_user_info_anyOf_i0_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_oneOf_i5_user_info_anyOf_i0_sid_anyOf_i1)

- Type: null

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_source"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: enum (of string)

The source for the user account.
###### Must be one of:

- "LOCAL"
- "ACTIVEDIRECTORY"
- "LDAP"

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_local"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_local"></a>
###### local (required)

- Schema name: `Local`
- Type: boolean

The account is local to TrueNAS or provided by a directory service.

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_attributes"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`
- Type: object

Custom user attributes and metadata.

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_two_factor_config"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_two_factor_config"></a>
###### two_factor_config (required)

- Schema name: `Two Factor Config`
- Type: object

Two-factor authentication configuration for the user.

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_privilege"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_privilege"></a>
###### privilege (required)

- Schema name: `Privilege`
- Type: object

User privilege and role information.

<a id="headingReturn_value_oneOf_i5_user_info_anyOf_i0_account_attributes"></a>
<a id="Return_value_oneOf_i5_user_info_anyOf_i0_account_attributes"></a>
###### account_attributes (required)

- Schema name: `Account Attributes`
- Type: array of string

Array of account attribute names available for this user.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_oneOf_i5_user_info_anyOf_i0_account_attributes_items"></a>
- Type: string

<a id="tab-pane_Return_value_oneOf_i5_user_info_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_oneOf_i5_user_info_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_oneOf_i6"></a>
##### [AuthRespDenied](#tab-pane_Return_value_oneOf_i6)

- Schema name: `AuthRespDenied`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oneOf_i6_response_type"></a>
<a id="Return_value_oneOf_i6_response_type"></a>
###### response_type (required)

- Schema name: `Response Type`
- Type: const

Authentication response type indicating that the credential lacks API access.
- Specific value: `"DENIED"`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
