---
title: truenas.set_production
kind: method
source_rst: _sources/api_methods_truenas.set_production.rst.txt
source_html: api_methods_truenas.set_production.html
required_roles:
  - FULL_ADMIN
---

# truenas.set_production

## Summary

Sets system production state and optionally sends initial debug.

This method is a job.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: production

<a id="Call_parameters_items_i0"></a>
#### production

- Schema name: `production`
- Type: boolean

Whether to configure the system for production use.

#### Parameter 2: attach_debug

<a id="Call_parameters_items_i1"></a>
#### attach_debug

- Schema name: `attach_debug`
- Type: boolean
- Default: false

Whether to attach debug information when transitioning to production mode.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

Support ticket details if system was newly marked as production. `null` otherwise.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [SupportNewTicket](#tab-pane_Return_value_anyOf_i0)

- Schema name: `SupportNewTicket`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_ticket"></a>
<a id="Return_value_anyOf_i0_ticket"></a>
###### ticket (required)

- Schema name: `Ticket`

Ticket number if successfully created. `null` if creation failed.
<a id="Return_value_anyOf_i0_ticket_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_ticket_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_ticket_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_ticket_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_ticket_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_url"></a>
<a id="Return_value_anyOf_i0_url"></a>
###### url (required)

- Schema name: `Url`

URL to view the created ticket. `null` if not available.
<a id="Return_value_anyOf_i0_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_has_debug"></a>
<a id="Return_value_anyOf_i0_has_debug"></a>
###### has_debug (required)

- Schema name: `Has Debug`
- Type: boolean

Whether debug information was attached to the ticket.

<a id="headingReturn_value_anyOf_i0_debug_attach_error"></a>
<a id="Return_value_anyOf_i0_debug_attach_error"></a>
###### debug_attach_error (required)

- Schema name: `Debug Attach Error`

If attaching debug information failed, the error message will appear here.
<a id="Return_value_anyOf_i0_debug_attach_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_debug_attach_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_debug_attach_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_debug_attach_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_debug_attach_error_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
