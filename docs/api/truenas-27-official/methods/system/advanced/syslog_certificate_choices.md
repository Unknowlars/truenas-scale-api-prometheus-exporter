---
title: system.advanced.syslog_certificate_choices
kind: method
source_rst: _sources/api_methods_system.advanced.syslog_certificate_choices.rst.txt
source_html: api_methods_system.advanced.syslog_certificate_choices.html
required_roles:
  - READONLY_ADMIN
  - SYSTEM_ADVANCED_READ
---

# system.advanced.syslog_certificate_choices

## Summary

Return choices of certificates which can be used for `syslogservers.N.tls_certificate`.

## Required Roles

- `READONLY_ADMIN`
- `SYSTEM_ADVANCED_READ`

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
- Type: object

IDs of certificates mapped to their names.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
