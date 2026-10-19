---
title: support.attach_ticket
kind: method
source_rst: _sources/api_methods_support.attach_ticket.rst.txt
source_html: api_methods_support.attach_ticket.html
required_roles:
  - READONLY_ADMIN
  - SUPPORT_WRITE
---

# support.attach_ticket

## Summary

Method to attach a file to an existing ticket.

This method is a job.

*This job MUST be used with file upload.* See [uploading-files](../../shared/jobs.md#uploading-files).

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
- Type: object

SupportAttachTicketArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_ticket"></a>
<a id="Call_parameters_items_i0_ticket"></a>
##### ticket (required)

- Schema name: `Ticket`
- Type: integer

Ticket number to attach the file to.

<a id="headingCall_parameters_items_i0_filename"></a>
<a id="Call_parameters_items_i0_filename"></a>
##### filename (required)

- Schema name: `Filename`
- Type: string

Path to the file to attach to the ticket.
- Must be at most `2147483647` characters long

<a id="headingCall_parameters_items_i0_token"></a>
<a id="Call_parameters_items_i0_token"></a>
##### token

- Schema name: `Token`
- Type: string

Authentication token for attaching files.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful file attachment.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
