---
title: cloudsync.credentials.s3_provider_choices
kind: method
source_rst: _sources/api_methods_cloudsync.credentials.s3_provider_choices.rst.txt
source_html: api_methods_cloudsync.credentials.s3_provider_choices.html
required_roles:
  - CLOUD_SYNC_READ | READONLY_ADMIN
---

# cloudsync.credentials.s3_provider_choices

## Summary

Provide choices for S3 provider `provider` field.

## Required Roles

- `CLOUD_SYNC_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
