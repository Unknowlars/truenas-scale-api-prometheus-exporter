---
title: mail.send
kind: method
source_rst: _sources/api_methods_mail.send.rst.txt
source_html: api_methods_mail.send.html
required_roles:
  - MAIL_WRITE
---

# mail.send

## Summary

Sends mail using configured mail settings.

This method is a job.

*This job CAN be used with file upload.* See [uploading-files](../../shared/jobs.md#uploading-files).

## Required Roles

- `MAIL_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: message

<a id="Call_parameters_items_i0"></a>
#### message

- Schema name: `message`
- Type: object

Email message content and configuration.
- No Additional Properties
<a id="headingCall_parameters_items_i0_subject"></a>
<a id="Call_parameters_items_i0_subject"></a>
##### subject (required)

- Schema name: `Subject`
- Type: string

Subject line for the email message.

<a id="headingCall_parameters_items_i0_text"></a>
<a id="Call_parameters_items_i0_text"></a>
##### text

- Schema name: `Text`
- Type: string

Formatted to HTML using Markdown and rendered using default email template.

<a id="headingCall_parameters_items_i0_html"></a>
<a id="Call_parameters_items_i0_html"></a>
##### html

- Schema name: `Html`

Custom HTML (overrides `text`). If null, no HTML MIME part will be added to the email.
<a id="Call_parameters_items_i0_html_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_html_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_html_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_html_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_html_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_to"></a>
<a id="Call_parameters_items_i0_to"></a>
##### to

- Schema name: `To`
- Type: array of string

Email recipients. Defaults to all local administrators.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_to_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_cc"></a>
<a id="Call_parameters_items_i0_cc"></a>
##### cc

- Schema name: `Cc`
- Type: array of string

Email CC recipients, if any.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_cc_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_interval"></a>
<a id="Call_parameters_items_i0_interval"></a>
##### interval

- Schema name: `Interval`

In seconds.
<a id="Call_parameters_items_i0_interval_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_interval_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_interval_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_interval_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_interval_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_channel"></a>
<a id="Call_parameters_items_i0_channel"></a>
##### channel

- Schema name: `Channel`

Defaults to "truenas".
<a id="Call_parameters_items_i0_channel_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_channel_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_channel_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_channel_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_channel_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_timeout"></a>
<a id="Call_parameters_items_i0_timeout"></a>
##### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 300

Time limit for connecting to the SMTP server in seconds.

<a id="headingCall_parameters_items_i0_attachments"></a>
<a id="Call_parameters_items_i0_attachments"></a>
##### attachments

- Schema name: `Attachments`
- Type: boolean
- Default: false

If set to true, an array compromised of the following object is required via HTTP upload: headers *(array)* name *(string)* value *(string)* params *(object)* content *(string)* Example: [ { "headers": [ { "name": "Content-Transfer-Encoding", "value": "base64" }, { "name": "Content-Type", "value": "application/octet-stream", "params": { "name": "test.txt" } } ], "content": "dGVzdAo=" } ]

<a id="headingCall_parameters_items_i0_queue"></a>
<a id="Call_parameters_items_i0_queue"></a>
##### queue

- Schema name: `Queue`
- Type: boolean
- Default: true

Queue the message to be sent later if it fails to send.

<a id="headingCall_parameters_items_i0_extra_headers"></a>
<a id="Call_parameters_items_i0_extra_headers"></a>
##### extra_headers

- Schema name: `Extra Headers`
- Type: object

Any additional headers to include in the email message.

#### Parameter 2: config

<a id="Call_parameters_items_i1"></a>
#### config

- Schema name: `config`
- Type: object

Optional mail configuration overrides for this message.
- No Additional Properties
<a id="headingCall_parameters_items_i1_fromemail"></a>
<a id="Call_parameters_items_i1_fromemail"></a>
##### fromemail

- Schema name: `Fromemail`
- Type: string

The sending address that the mail server will use for sending emails.

<a id="headingCall_parameters_items_i1_fromname"></a>
<a id="Call_parameters_items_i1_fromname"></a>
##### fromname

- Schema name: `Fromname`
- Type: string

Display name that will appear as the sender name in outgoing emails.

<a id="headingCall_parameters_items_i1_outgoingserver"></a>
<a id="Call_parameters_items_i1_outgoingserver"></a>
##### outgoingserver

- Schema name: `Outgoingserver`
- Type: string

Hostname or IP address of the SMTP server used for sending emails.

<a id="headingCall_parameters_items_i1_port"></a>
<a id="Call_parameters_items_i1_port"></a>
##### port

- Schema name: `Port`
- Type: integer

TCP port number for the SMTP server connection.

<a id="headingCall_parameters_items_i1_security"></a>
<a id="Call_parameters_items_i1_security"></a>
##### security

- Schema name: `Security`
- Type: enum (of string)

Type of encryption.
###### Must be one of:

- "PLAIN"
- "SSL"
- "TLS"

<a id="headingCall_parameters_items_i1_smtp"></a>
<a id="Call_parameters_items_i1_smtp"></a>
##### smtp

- Schema name: `Smtp`
- Type: boolean

Whether SMTP authentication is enabled and `user`, `pass` are required.

<a id="headingCall_parameters_items_i1_user"></a>
<a id="Call_parameters_items_i1_user"></a>
##### user

- Schema name: `User`

SMTP username.
<a id="Call_parameters_items_i1_user_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_user_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_user_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_pass"></a>
<a id="Call_parameters_items_i1_pass"></a>
##### pass

- Schema name: `Pass`

SMTP password.
<a id="Call_parameters_items_i1_pass_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_pass_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_pass_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_pass_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_pass_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_oauth"></a>
<a id="Call_parameters_items_i1_oauth"></a>
##### oauth

- Schema name: `Oauth`

OAuth configuration for email providers that support it or `null` for basic authentication.
<a id="Call_parameters_items_i1_oauth_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_oauth_anyOf_i0"></a>
###### [MailEntryOAuth](#tab-pane_Call_parameters_items_i1_oauth_anyOf_i0)

- Schema name: `MailEntryOAuth`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_oauth_anyOf_i0_provider"></a>
<a id="Call_parameters_items_i1_oauth_anyOf_i0_provider"></a>
###### provider (required)

- Schema name: `Provider`
- Type: string

An email provider, e.g. "gmail", "outlook".

<a id="headingCall_parameters_items_i1_oauth_anyOf_i0_client_id"></a>
<a id="Call_parameters_items_i1_oauth_anyOf_i0_client_id"></a>
###### client_id (required)

- Schema name: `Client Id`
- Type: string

OAuth client ID provided by the email provider.

<a id="headingCall_parameters_items_i1_oauth_anyOf_i0_client_secret"></a>
<a id="Call_parameters_items_i1_oauth_anyOf_i0_client_secret"></a>
###### client_secret (required)

- Schema name: `Client Secret`
- Type: string

OAuth client secret provided by the email provider.

<a id="headingCall_parameters_items_i1_oauth_anyOf_i0_refresh_token"></a>
<a id="Call_parameters_items_i1_oauth_anyOf_i0_refresh_token"></a>
###### refresh_token (required)

- Schema name: `Refresh Token`
- Type: string

OAuth refresh token used to obtain new access tokens for email authentication.

<a id="tab-pane_Call_parameters_items_i1_oauth_anyOf_i1"></a>
###### [EmptyDict](#tab-pane_Call_parameters_items_i1_oauth_anyOf_i1)

- Schema name: `EmptyDict`
- Type: object

<a id="tab-pane_Call_parameters_items_i1_oauth_anyOf_i2"></a>
###### [Option 3](#tab-pane_Call_parameters_items_i1_oauth_anyOf_i2)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

The message was sent successfully.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
