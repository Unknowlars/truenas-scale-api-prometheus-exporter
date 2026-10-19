---
title: mail.config
kind: method
source_rst: _sources/api_methods_mail.config.rst.txt
source_html: api_methods_mail.config.html
required_roles:
  - ALERT_READ
---

# mail.config

## Required Roles

- `ALERT_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `MailEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_fromemail"></a>
<a id="Return_value_fromemail"></a>
#### fromemail (required)

- Schema name: `Fromemail`
- Type: string

The sending address that the mail server will use for sending emails.

<a id="headingReturn_value_fromname"></a>
<a id="Return_value_fromname"></a>
#### fromname (required)

- Schema name: `Fromname`
- Type: string

Display name that will appear as the sender name in outgoing emails.

<a id="headingReturn_value_outgoingserver"></a>
<a id="Return_value_outgoingserver"></a>
#### outgoingserver (required)

- Schema name: `Outgoingserver`
- Type: string

Hostname or IP address of the SMTP server used for sending emails.

<a id="headingReturn_value_port"></a>
<a id="Return_value_port"></a>
#### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the SMTP server connection.

<a id="headingReturn_value_security"></a>
<a id="Return_value_security"></a>
#### security (required)

- Schema name: `Security`
- Type: enum (of string)

Type of encryption.
##### Must be one of:

- "PLAIN"
- "SSL"
- "TLS"

<a id="headingReturn_value_smtp"></a>
<a id="Return_value_smtp"></a>
#### smtp (required)

- Schema name: `Smtp`
- Type: boolean

Whether SMTP authentication is enabled and `user`, `pass` are required.

<a id="headingReturn_value_user"></a>
<a id="Return_value_user"></a>
#### user (required)

- Schema name: `User`

SMTP username.
<a id="Return_value_user_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_user_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_pass"></a>
<a id="Return_value_pass"></a>
#### pass (required)

- Schema name: `Pass`

SMTP password.
<a id="Return_value_pass_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_pass_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pass_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_pass_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pass_anyOf_i1)

- Type: null

<a id="headingReturn_value_oauth"></a>
<a id="Return_value_oauth"></a>
#### oauth (required)

- Schema name: `Oauth`

OAuth configuration for email providers that support it or `null` for basic authentication.
<a id="Return_value_oauth_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_oauth_anyOf_i0"></a>
###### [MailEntryOAuth](#tab-pane_Return_value_oauth_anyOf_i0)

- Schema name: `MailEntryOAuth`
- Type: object
- No Additional Properties
<a id="headingReturn_value_oauth_anyOf_i0_provider"></a>
<a id="Return_value_oauth_anyOf_i0_provider"></a>
###### provider (required)

- Schema name: `Provider`
- Type: string

An email provider, e.g. "gmail", "outlook".

<a id="headingReturn_value_oauth_anyOf_i0_client_id"></a>
<a id="Return_value_oauth_anyOf_i0_client_id"></a>
###### client_id (required)

- Schema name: `Client Id`
- Type: string

OAuth client ID provided by the email provider.

<a id="headingReturn_value_oauth_anyOf_i0_client_secret"></a>
<a id="Return_value_oauth_anyOf_i0_client_secret"></a>
###### client_secret (required)

- Schema name: `Client Secret`
- Type: string

OAuth client secret provided by the email provider.

<a id="headingReturn_value_oauth_anyOf_i0_refresh_token"></a>
<a id="Return_value_oauth_anyOf_i0_refresh_token"></a>
###### refresh_token (required)

- Schema name: `Refresh Token`
- Type: string

OAuth refresh token used to obtain new access tokens for email authentication.
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_oauth_anyOf_i1"></a>
###### [EmptyDict](#tab-pane_Return_value_oauth_anyOf_i1)

- Schema name: `EmptyDict`
- Type: object

<a id="tab-pane_Return_value_oauth_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_oauth_anyOf_i2)

- Type: null

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this mail configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
