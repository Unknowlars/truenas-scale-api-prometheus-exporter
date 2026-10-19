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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of available cloud sync providers and their configurations.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### CloudSyncProvider

- Schema name: `CloudSyncProvider`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Internal name identifier for the cloud provider.

<a id="headingReturn_value_items_title"></a>
<a id="Return_value_items_title"></a>
##### title (required)

- Schema name: `Title`
- Type: string

Human-readable title for the cloud provider.

<a id="headingReturn_value_items_credentials_oauth"></a>
<a id="Return_value_items_credentials_oauth"></a>
##### credentials_oauth (required)

- Schema name: `Credentials Oauth`

OAuth setup URL for the provider or `null` if not OAuth-based.
<a id="Return_value_items_credentials_oauth_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_credentials_oauth_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_credentials_oauth_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_credentials_oauth_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_credentials_oauth_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_buckets"></a>
<a id="Return_value_items_buckets"></a>
##### buckets (required)

- Schema name: `Buckets`
- Type: boolean

Set to `true` if provider supports buckets.

<a id="headingReturn_value_items_bucket_title"></a>
<a id="Return_value_items_bucket_title"></a>
##### bucket_title (required)

- Schema name: `Bucket Title`

Title for bucket concept in this provider or `null` if not applicable.
<a id="Return_value_items_bucket_title_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_bucket_title_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_bucket_title_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_bucket_title_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_bucket_title_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_task_schema"></a>
<a id="Return_value_items_task_schema"></a>
##### task_schema (required)

- Schema name: `Task Schema`
- Type: array of object

JSON schema for task attributes.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_task_schema_items"></a>
###### CloudSyncProviderTaskSchemaItem

- Schema name: `CloudSyncProviderTaskSchemaItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_task_schema_items_property"></a>
<a id="Return_value_items_task_schema_items_property"></a>
###### property (required)

- Schema name: `Property`
- Type: string

Name of the schema property for task configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
