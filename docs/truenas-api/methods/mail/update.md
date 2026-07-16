---
title: mail.update
kind: method
source_rst: _sources/api_methods_mail.update.rst.txt
source_html: api_methods_mail.update.html
required_roles:
  - ALERT_WRITE
---

# mail.update

## Summary

Update Mail Service Configuration.

## Required Roles

- `ALERT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Mail configuration fields to update.
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

- Schema name: `MailEntry`
- Type: object

The resulting mail configuration.
- No Additional Properties
#### fromemail (required)

- Schema name: `Fromemail`
- Type: string

The sending address that the mail server will use for sending emails.

#### fromname (required)

- Schema name: `Fromname`
- Type: string

Display name that will appear as the sender name in outgoing emails.

#### outgoingserver (required)

- Schema name: `Outgoingserver`
- Type: string

Hostname or IP address of the SMTP server used for sending emails.

#### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the SMTP server connection.

#### security (required)

- Schema name: `Security`
- Type: enum (of string)

Type of encryption.

#### smtp (required)

- Schema name: `Smtp`
- Type: boolean

Whether SMTP authentication is enabled and `user`, `pass` are required.

#### user (required)

- Schema name: `User`

SMTP username.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### pass (required)

- Schema name: `Pass`

SMTP password.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### oauth (required)

- Schema name: `Oauth`

OAuth configuration for email providers that support it or `null` for basic authentication.
##### Any of

###### MailEntryOAuth

- Schema name: `MailEntryOAuth`
- Type: object
- No Additional Properties
####### provider (required)

- Schema name: `Provider`
- Type: string

An email provider, e.g. "gmail", "outlook".

####### client_id (required)

- Schema name: `Client Id`
- Type: string

OAuth client ID provided by the email provider.

####### client_secret (required)

- Schema name: `Client Secret`
- Type: string

OAuth client secret provided by the email provider.

####### refresh_token (required)

- Schema name: `Refresh Token`
- Type: string

OAuth refresh token used to obtain new access tokens for email authentication.

###### EmptyDict

- Schema name: `EmptyDict`
- Type: object

###### Option 3

- Type: null

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this mail configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
