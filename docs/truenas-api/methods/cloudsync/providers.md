---
title: cloudsync.providers
kind: method
source_rst: _sources/api_methods_cloudsync.providers.rst.txt
source_html: api_methods_cloudsync.providers.html
required_roles:
  - CLOUD_SYNC_READ
---

# cloudsync.providers

## Summary

Returns a list of dictionaries of supported providers for Cloud Sync Tasks.

## Required Roles

- `CLOUD_SYNC_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of object

Array of available cloud sync providers and their configurations.
- No Additional Items

#### Each item of this array must be:

#### CloudSyncProvider

- Schema name: `CloudSyncProvider`
- Type: object
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Internal name identifier for the cloud provider.

##### title (required)

- Schema name: `Title`
- Type: string

Human-readable title for the cloud provider.

##### credentials_oauth (required)

- Schema name: `Credentials Oauth`

OAuth setup URL for the provider or `null` if not OAuth-based.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### buckets (required)

- Schema name: `Buckets`
- Type: boolean

Set to `true` if provider supports buckets.

##### bucket_title (required)

- Schema name: `Bucket Title`

Title for bucket concept in this provider or `null` if not applicable.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### task_schema (required)

- Schema name: `Task Schema`
- Type: array of object

JSON schema for task attributes.
- No Additional Items

###### Each item of this array must be:

###### CloudSyncProviderTaskSchemaItem

- Schema name: `CloudSyncProviderTaskSchemaItem`
- Type: object
- No Additional Properties
####### property (required)

- Schema name: `Property`
- Type: string

Name of the schema property for task configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
