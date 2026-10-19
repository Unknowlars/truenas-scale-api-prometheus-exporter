---
title: support.new_ticket
kind: method
source_rst: _sources/api_methods_support.new_ticket.rst.txt
source_html: api_methods_support.new_ticket.html
required_roles:
  - READONLY_ADMIN
  - SUPPORT_WRITE
---

# support.new_ticket

## Summary

Creates a new ticket for support. This is done using the support proxy API. For TrueNAS Community Edition it will be created on JIRA and for TrueNAS Enterprise on Salesforce.

This method is a job.

## Required Roles

- `READONLY_ADMIN`
- `SUPPORT_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`

Support ticket data for either enterprise or community support.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [SupportNewTicketEnterprise](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Schema name: `SupportNewTicketEnterprise`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_anyOf_i0_title"></a>
<a id="Call_parameters_items_i0_anyOf_i0_title"></a>
###### title (required)

- Schema name: `Title`
- Type: string

Title of the support ticket.
- Must be at most `200` characters long

<a id="headingCall_parameters_items_i0_anyOf_i0_body"></a>
<a id="Call_parameters_items_i0_anyOf_i0_body"></a>
###### body (required)

- Schema name: `Body`
- Type: string

Detailed description of the issue or request.
- Must be at most `20000` characters long

<a id="headingCall_parameters_items_i0_anyOf_i0_category"></a>
<a id="Call_parameters_items_i0_anyOf_i0_category"></a>
###### category (required)

- Schema name: `Category`
- Type: string

Category or classification of the support issue.

<a id="headingCall_parameters_items_i0_anyOf_i0_attach_debug"></a>
<a id="Call_parameters_items_i0_anyOf_i0_attach_debug"></a>
###### attach_debug

- Schema name: `Attach Debug`
- Type: boolean
- Default: false

Whether to attach debug information to the ticket.

<a id="headingCall_parameters_items_i0_anyOf_i0_criticality"></a>
<a id="Call_parameters_items_i0_anyOf_i0_criticality"></a>
###### criticality (required)

- Schema name: `Criticality`
- Type: string

Priority or criticality level of the issue.

<a id="headingCall_parameters_items_i0_anyOf_i0_environment"></a>
<a id="Call_parameters_items_i0_anyOf_i0_environment"></a>
###### environment (required)

- Schema name: `Environment`
- Type: string

Description of the environment where the issue occurs.
- Must be at most `2147483647` characters long

<a id="headingCall_parameters_items_i0_anyOf_i0_phone"></a>
<a id="Call_parameters_items_i0_anyOf_i0_phone"></a>
###### phone (required)

- Schema name: `Phone`
- Type: string

Contact phone number for this ticket.

<a id="headingCall_parameters_items_i0_anyOf_i0_name"></a>
<a id="Call_parameters_items_i0_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Contact name for this ticket.

<a id="headingCall_parameters_items_i0_anyOf_i0_email"></a>
<a id="Call_parameters_items_i0_anyOf_i0_email"></a>
###### email (required)

- Schema name: `Email`
- Type: string

Contact email address for this ticket.

<a id="headingCall_parameters_items_i0_anyOf_i0_cc"></a>
<a id="Call_parameters_items_i0_anyOf_i0_cc"></a>
###### cc

- Schema name: `Cc`
- Type: array of string
- Default: []

Array of email addresses to copy on the ticket.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_anyOf_i0_cc_items"></a>
- Type: string

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [SupportNewTicketCommunity](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Schema name: `SupportNewTicketCommunity`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_anyOf_i1_title"></a>
<a id="Call_parameters_items_i0_anyOf_i1_title"></a>
###### title (required)

- Schema name: `Title`
- Type: string

Title of the support ticket.
- Must be at most `200` characters long

<a id="headingCall_parameters_items_i0_anyOf_i1_body"></a>
<a id="Call_parameters_items_i0_anyOf_i1_body"></a>
###### body (required)

- Schema name: `Body`
- Type: string

Detailed description of the issue or request.
- Must be at most `20000` characters long

<a id="headingCall_parameters_items_i0_anyOf_i1_attach_debug"></a>
<a id="Call_parameters_items_i0_anyOf_i1_attach_debug"></a>
###### attach_debug

- Schema name: `Attach Debug`
- Type: boolean
- Default: false

Whether to attach debug information to the ticket.

<a id="headingCall_parameters_items_i0_anyOf_i1_token"></a>
<a id="Call_parameters_items_i0_anyOf_i1_token"></a>
###### token (required)

- Schema name: `Token`
- Type: string

Authentication token for creating community tickets.

<a id="headingCall_parameters_items_i0_anyOf_i1_type"></a>
<a id="Call_parameters_items_i0_anyOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of ticket being created.
###### Must be one of:

- "BUG"
- "FEATURE"

<a id="headingCall_parameters_items_i0_anyOf_i1_cc"></a>
<a id="Call_parameters_items_i0_anyOf_i1_cc"></a>
###### cc

- Schema name: `Cc`
- Type: array of string
- Default: []

Array of email addresses to copy on the ticket.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_anyOf_i1_cc_items"></a>
- Type: string

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SupportNewTicket`
- Type: object

Created support ticket details.
- No Additional Properties
<a id="headingReturn_value_ticket"></a>
<a id="Return_value_ticket"></a>
#### ticket (required)

- Schema name: `Ticket`

Ticket number if successfully created. `null` if creation failed.
<a id="Return_value_ticket_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_ticket_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ticket_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_ticket_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ticket_anyOf_i1)

- Type: null

<a id="headingReturn_value_url"></a>
<a id="Return_value_url"></a>
#### url (required)

- Schema name: `Url`

URL to view the created ticket. `null` if not available.
<a id="Return_value_url_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_has_debug"></a>
<a id="Return_value_has_debug"></a>
#### has_debug (required)

- Schema name: `Has Debug`
- Type: boolean

Whether debug information was attached to the ticket.

<a id="headingReturn_value_debug_attach_error"></a>
<a id="Return_value_debug_attach_error"></a>
#### debug_attach_error (required)

- Schema name: `Debug Attach Error`

If attaching debug information failed, the error message will appear here.
<a id="Return_value_debug_attach_error_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_debug_attach_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_debug_attach_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_debug_attach_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_debug_attach_error_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
