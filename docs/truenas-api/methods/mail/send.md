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

*This job CAN be used with file upload.* See :ref:`uploading-files`.

## Required Roles

- `MAIL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: message

#### message

- Schema name: `message`
- Type: object

Email message content and configuration.
- No Additional Properties
##### subject (required)

- Schema name: `Subject`
- Type: string

Subject line for the email message.

##### text

- Schema name: `Text`
- Type: string

Formatted to HTML using Markdown and rendered using default email template.

##### html

- Schema name: `Html`

Custom HTML (overrides `text`). If null, no HTML MIME part will be added to the email.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### to

- Schema name: `To`
- Type: array of string

Email recipients. Defaults to all local administrators.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### cc

- Schema name: `Cc`
- Type: array of string

Email CC recipients, if any.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### interval

- Schema name: `Interval`

In seconds.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### channel

- Schema name: `Channel`

Defaults to "truenas".
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 300

Time limit for connecting to the SMTP server in seconds.

##### attachments

- Schema name: `Attachments`
- Type: boolean
- Default: false

If set to true, an array compromised of the following object is required via HTTP upload: headers *(array)* name *(string)* value *(string)* params *(object)* content *(string)* Example: [ { "headers": [ { "name": "Content-Transfer-Encoding", "value": "base64" }, { "name": "Content-Type", "value": "application/octet-stream", "params": { "name": "test.txt" } } ], "content": "dGVzdAo=" } ]

##### queue

- Schema name: `Queue`
- Type: boolean
- Default: true

Queue the message to be sent later if it fails to send.

##### extra_headers

- Schema name: `Extra Headers`
- Type: object

Any additional headers to include in the email message.

#### Parameter 2: config

#### config

- Schema name: `config`
- Type: object

Optional mail configuration overrides for this message.
- No Additional Properties
##### fromemail

- Schema name: `Fromemail`
- Type: string

The sending address that the mail server will use for sending emails.

##### fromname

- Schema name: `Fromname`
- Type: string

Display name that will appear as the sender name in outgoing emails.

##### outgoingserver

- Schema name: `Outgoingserver`
- Type: string

Hostname or IP address of the SMTP server used for sending emails.

##### port

- Schema name: `Port`
- Type: integer

TCP port number for the SMTP server connection.

##### security

- Schema name: `Security`
- Type: enum (of string)

Type of encryption.

##### smtp

- Schema name: `Smtp`
- Type: boolean

Whether SMTP authentication is enabled and `user`, `pass` are required.

##### user

- Schema name: `User`

SMTP username.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### pass

- Schema name: `Pass`

SMTP password.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### oauth

- Schema name: `Oauth`

OAuth configuration for email providers that support it or `null` for basic authentication.
###### Any of

####### MailEntryOAuth

- Schema name: `MailEntryOAuth`
- Type: object
- No Additional Properties
######## provider (required)

- Schema name: `Provider`
- Type: string

An email provider, e.g. "gmail", "outlook".

######## client_id (required)

- Schema name: `Client Id`
- Type: string

OAuth client ID provided by the email provider.

######## client_secret (required)

- Schema name: `Client Secret`
- Type: string

OAuth client secret provided by the email provider.

######## refresh_token (required)

- Schema name: `Refresh Token`
- Type: string

OAuth refresh token used to obtain new access tokens for email authentication.

####### EmptyDict

- Schema name: `EmptyDict`
- Type: object

####### Option 3

- Type: null

### Return value

- Schema name: `Result`
- Type: boolean

The message was sent successfully.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
