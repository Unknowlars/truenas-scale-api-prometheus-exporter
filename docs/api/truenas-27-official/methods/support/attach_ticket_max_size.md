---
title: support.attach_ticket_max_size
kind: method
source_rst: _sources/api_methods_support.attach_ticket_max_size.rst.txt
source_html: api_methods_support.attach_ticket_max_size.html
required_roles:
  - SUPPORT_READ
---

# support.attach_ticket_max_size

## Summary

Returns maximum uploaded file size for [support.attach_ticket](attach_ticket.md).

## Required Roles

- `SUPPORT_READ`

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

- Schema name: `Result`
- Type: integer

Maximum file size in bytes allowed for ticket attachments.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
