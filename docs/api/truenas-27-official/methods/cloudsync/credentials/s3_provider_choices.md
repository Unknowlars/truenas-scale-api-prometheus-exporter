---
title: cloudsync.credentials.s3_provider_choices
kind: method
source_rst: _sources/api_methods_cloudsync.credentials.s3_provider_choices.rst.txt
source_html: api_methods_cloudsync.credentials.s3_provider_choices.html
required_roles:
  - CLOUD_SYNC_READ
  - READONLY_ADMIN
---

# cloudsync.credentials.s3_provider_choices

## Summary

Provide choices for S3 provider `provider` field.

## Required Roles

- `CLOUD_SYNC_READ`
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
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
