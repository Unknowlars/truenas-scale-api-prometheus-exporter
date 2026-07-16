---
title: cloudsync.credentials.create
kind: method
source_rst: _sources/api_methods_cloudsync.credentials.create.rst.txt
source_html: api_methods_cloudsync.credentials.create.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.credentials.create

## Summary

Create Cloud Sync Credentials.

`attributes` is a dictionary of valid values which will be used to authorize with the `provider`.

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
- Type: object

Cloud credential configuration data for the new credential.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

##### provider (required)

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.

### Return value

- Schema name: `CloudCredentialEntry`
- Type: object

The created cloud credential configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

#### provider (required)

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
