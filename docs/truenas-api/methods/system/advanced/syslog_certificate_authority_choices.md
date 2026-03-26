---
title: system.advanced.syslog_certificate_authority_choices
kind: method
source_rst: _sources/api_methods_system.advanced.syslog_certificate_authority_choices.rst.txt
source_html: api_methods_system.advanced.syslog_certificate_authority_choices.html
required_roles:
  - READONLY_ADMIN | SYSTEM_ADVANCED_READ
---

# system.advanced.syslog_certificate_authority_choices

## Summary

Return choices of certificate authorities which can be used for `syslog_tls_certificate_authority`. ---- NO LONGER USED: TO BE REMOVED AFTER UI UPDATE ----

## Required Roles

- `READONLY_ADMIN | SYSTEM_ADVANCED_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `EmptyDict`
- Type: object

Available certificate authorities for syslog TLS (currently empty).

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
