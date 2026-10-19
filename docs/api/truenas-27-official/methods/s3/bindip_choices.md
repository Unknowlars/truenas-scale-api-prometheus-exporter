---
title: s3.bindip_choices
kind: method
source_rst: _sources/api_methods_s3.bindip_choices.rst.txt
source_html: api_methods_s3.bindip_choices.html
required_roles:
  - READONLY_ADMIN
  - SHARING_S3_READ
---

# s3.bindip_choices

## Summary

Returns the IP addresses a listener may name.

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

IP addresses a listener may name, keyed by address: static ones, loopbacks and the wildcards.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
