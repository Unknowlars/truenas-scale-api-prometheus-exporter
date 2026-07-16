---
title: certificate.acme_server_choices
kind: method
source_rst: _sources/api_methods_certificate.acme_server_choices.rst.txt
source_html: api_methods_certificate.acme_server_choices.html
required_roles:
  - CERTIFICATE_READ | READONLY_ADMIN
---

# certificate.acme_server_choices

## Summary

Dictionary of popular ACME Servers with their directory URI endpoints which we display automatically in the UI

## Required Roles

- `CERTIFICATE_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object mapping ACME server identifiers to their directory URLs.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
