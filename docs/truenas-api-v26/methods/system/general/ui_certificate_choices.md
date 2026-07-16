---
title: system.general.ui_certificate_choices
kind: method
source_rst: _sources/api_methods_system.general.ui_certificate_choices.rst.txt
source_html: api_methods_system.general.ui_certificate_choices.html
required_roles:
  - READONLY_ADMIN | SYSTEM_GENERAL_READ
---

# system.general.ui_certificate_choices

## Summary

Return available certificates that may be used to bind the webserver to when connecting via HTTPS protocol.

## Required Roles

- `READONLY_ADMIN | SYSTEM_GENERAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object of available certificate IDs and their names for UI HTTPS.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
