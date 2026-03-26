---
title: directoryservices.certificate_choices
kind: method
source_rst: _sources/api_methods_directoryservices.certificate_choices.rst.txt
source_html: api_methods_directoryservices.certificate_choices.html
required_roles:
  - DIRECTORY_SERVICE_READ | READONLY_ADMIN
---

# directoryservices.certificate_choices

## Summary

Available certificate choices for use with the `LDAP_MTLS` `credential_type`. Note that prior configuration of LDAP server is required and uploading a custom certificate to TrueNAS may also be required.

## Required Roles

- `DIRECTORY_SERVICE_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

IDs of certificates mapped to their names.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
