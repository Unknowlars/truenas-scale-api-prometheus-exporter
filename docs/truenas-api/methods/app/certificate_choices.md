---
title: app.certificate_choices
kind: method
source_rst: _sources/api_methods_app.certificate_choices.rst.txt
source_html: api_methods_app.certificate_choices.html
required_roles:
  - APPS_READ | READONLY_ADMIN
---

# app.certificate_choices

## Summary

Returns certificates which can be used by applications.

## Required Roles

- `APPS_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of object

Array of available certificates that can be used by applications.
- No Additional Items

#### Each item of this array must be:

#### AppCertificate

- Schema name: `AppCertificate`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the certificate.

##### name (required)

- Schema name: `Name`
- Type: string

Display name of the certificate.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
