---
title: sharing.s3.audit_choices
kind: method
source_rst: _sources/api_methods_sharing.s3.audit_choices.rst.txt
source_html: api_methods_sharing.s3.audit_choices.html
required_roles:
  - READONLY_ADMIN
  - SHARING_S3_READ
---

# sharing.s3.audit_choices

## Summary

Returns the actions an audit mask may name.

## Required Roles

- `READONLY_ADMIN`
- `SHARING_S3_READ`

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

Actions an audit mask may name, keyed by name.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
