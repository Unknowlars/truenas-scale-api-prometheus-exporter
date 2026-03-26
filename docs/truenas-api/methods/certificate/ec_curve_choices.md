---
title: certificate.ec_curve_choices
kind: method
source_rst: _sources/api_methods_certificate.ec_curve_choices.rst.txt
source_html: api_methods_certificate.ec_curve_choices.html
required_roles:
  - CERTIFICATE_READ | READONLY_ADMIN
---

# certificate.ec_curve_choices

## Summary

Dictionary of supported EC curves.

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

Object mapping elliptic curve identifiers.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
