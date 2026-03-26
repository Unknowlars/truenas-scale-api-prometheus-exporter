---
title: cloudsync.credentials.query
kind: event
source_rst: _sources/api_events_cloudsync.credentials.query.rst.txt
source_html: api_events_cloudsync.credentials.query.html
required_roles:
  - CLOUD_SYNC_READ
---

# cloudsync.credentials.query

## Summary

Sent on cloudsync.credentials changes.

## Required Roles

- `CLOUD_SYNC_READ`

## Schema

- Type: object

### ADDED

- Schema name: `CloudCredentialAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `CloudCredentialEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

##### provider (required)

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.

### CHANGED

- Schema name: `CloudCredentialChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `CloudCredentialEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cloud credential.

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the cloud credential.
- Must be at least `1` characters long

##### provider (required)

- Schema name: `Provider`

Cloud provider configuration including type and authentication details.

### REMOVED

- Schema name: `CloudCredentialRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
