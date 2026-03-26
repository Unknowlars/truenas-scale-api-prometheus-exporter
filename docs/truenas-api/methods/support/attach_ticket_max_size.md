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

Returns maximum uploaded file size for `support.attach_ticket`

## Required Roles

- `SUPPORT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: integer

Maximum file size in bytes allowed for ticket attachments.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
