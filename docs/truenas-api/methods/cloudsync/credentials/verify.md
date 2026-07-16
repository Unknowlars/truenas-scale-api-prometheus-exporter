---
title: cloudsync.credentials.verify
kind: method
source_rst: _sources/api_methods_cloudsync.credentials.verify.rst.txt
source_html: api_methods_cloudsync.credentials.verify.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.credentials.verify

## Summary

Verify if `attributes` provided for `provider` are authorized by the `provider`.

## Required Roles

- `CLOUD_SYNC_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: cloud_sync_credentials_create

#### cloud_sync_credentials_create

- Schema name: `cloud_sync_credentials_create`

Cloud provider configuration to verify connectivity and authentication.

### Return value

- Schema name: `CredentialsVerifyResult`
- Type: object

CredentialsVerifyResult return fields.
- No Additional Properties
#### valid (required)

- Schema name: `Valid`
- Type: boolean

Whether the cloud credentials are valid and functional.

#### error

- Schema name: `Error`
- Default: null

Error message if credential verification failed or `null` on success.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### excerpt

- Schema name: `Excerpt`
- Default: null

Logs excerpt (or `null` if no error occurred).
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
