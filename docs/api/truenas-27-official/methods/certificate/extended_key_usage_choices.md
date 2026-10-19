---
title: certificate.extended_key_usage_choices
kind: method
source_rst: _sources/api_methods_certificate.extended_key_usage_choices.rst.txt
source_html: api_methods_certificate.extended_key_usage_choices.html
required_roles:
  - CERTIFICATE_READ
  - READONLY_ADMIN
---

# certificate.extended_key_usage_choices

## Summary

Dictionary of names that can be used in the ExtendedKeyUsage attribute of a certificate request.

## Required Roles

- `CERTIFICATE_READ`
- `READONLY_ADMIN`

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

Object mapping extended key usage OIDs.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
