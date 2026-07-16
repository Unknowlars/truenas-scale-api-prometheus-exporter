---
title: cloudsync.credentials.update
kind: method
source_rst: _sources/api_methods_cloudsync.credentials.update.rst.txt
source_html: api_methods_cloudsync.credentials.update.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.credentials.update

## Summary

Update Cloud Sync Credentials of `id`.

## Required Roles

- `CLOUD_SYNC_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the cloud credential to update.

#### Parameter 2: cloud_sync_credentials_update

#### cloud_sync_credentials_update

- Schema name: `cloud_sync_credentials_update`
- Type: object

Updated cloud credential configuration data.
- No Additional Properties
##### name

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

##### provider

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.

### Return value

- Schema name: `CloudCredentialEntry`
- Type: object

The updated cloud credential configuration.
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
