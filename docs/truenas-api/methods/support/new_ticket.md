---
title: support.new_ticket
kind: method
source_rst: _sources/api_methods_support.new_ticket.rst.txt
source_html: api_methods_support.new_ticket.html
required_roles:
  - READONLY_ADMIN | SUPPORT_WRITE
---

# support.new_ticket

## Summary

Creates a new ticket for support. This is done using the support proxy API. For TrueNAS Community Edition it will be created on JIRA and for TrueNAS Enterprise on Salesforce.

For Community Edition, `criticality`, `environment`, `phone`, `name`, and `email` attributes are not required. For Enterprise, `token` and `type` attributes are not required.

This method is a job.

## Required Roles

- `READONLY_ADMIN | SUPPORT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`

Support ticket data for either enterprise or community support.
##### Any of

###### SupportNewTicketEnterprise

- Schema name: `SupportNewTicketEnterprise`
- Type: object
- No Additional Properties
####### title (required)

- Schema name: `Title`
- Type: string

Title of the support ticket.
- Must be at most `200` characters long

####### body (required)

- Schema name: `Body`
- Type: string

Detailed description of the issue or request.
- Must be at most `20000` characters long

####### category (required)

- Schema name: `Category`
- Type: string

Category or classification of the support issue.

####### attach_debug

- Schema name: `Attach Debug`
- Type: boolean
- Default: false

Whether to attach debug information to the ticket.

####### criticality (required)

- Schema name: `Criticality`
- Type: string

Priority or criticality level of the issue.

####### environment (required)

- Schema name: `Environment`
- Type: string

Description of the environment where the issue occurs.

####### phone (required)

- Schema name: `Phone`
- Type: string

Contact phone number for this ticket.

####### name (required)

- Schema name: `Name`
- Type: string

Contact name for this ticket.

####### email (required)

- Schema name: `Email`
- Type: string

Contact email address for this ticket.

####### cc

- Schema name: `Cc`
- Type: array of string
- Default: []

Array of email addresses to copy on the ticket.
- No Additional Items

######## Each item of this array must be:

- Type: string

###### SupportNewTicketCommunity

- Schema name: `SupportNewTicketCommunity`
- Type: object
- No Additional Properties
####### title (required)

- Schema name: `Title`
- Type: string

Title of the support ticket.
- Must be at most `200` characters long

####### body (required)

- Schema name: `Body`
- Type: string

Detailed description of the issue or request.
- Must be at most `20000` characters long

####### attach_debug

- Schema name: `Attach Debug`
- Type: boolean
- Default: false

Whether to attach debug information to the ticket.

####### token (required)

- Schema name: `Token`
- Type: string

Authentication token for creating community tickets.

####### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of ticket being created.

####### cc

- Schema name: `Cc`
- Type: array of string
- Default: []

Array of email addresses to copy on the ticket.
- No Additional Items

######## Each item of this array must be:

- Type: string

### Return value

- Schema name: `SupportNewTicketResult`
- Type: object

SupportNewTicketResult return fields.
- No Additional Properties
#### ticket (required)

- Schema name: `Ticket`

Ticket number if successfully created. `null` if creation failed.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### url (required)

- Schema name: `Url`

URL to view the created ticket. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### has_debug (required)

- Schema name: `Has Debug`
- Type: boolean

Whether debug information was attached to the ticket.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
