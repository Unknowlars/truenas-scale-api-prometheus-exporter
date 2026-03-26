---
title: mail.local_administrator_email
kind: method
source_rst: _sources/api_methods_mail.local_administrator_email.rst.txt
source_html: api_methods_mail.local_administrator_email.html
required_roles:
  - ALERT_READ
---

# mail.local_administrator_email

## Required Roles

- `ALERT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`

Email address of the local administrator or `null` if not configured.
#### Any of

##### Option 1

- Type: string

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
