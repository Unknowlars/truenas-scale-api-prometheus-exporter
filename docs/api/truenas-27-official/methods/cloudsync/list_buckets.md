---
title: cloudsync.list_buckets
kind: method
source_rst: _sources/api_methods_cloudsync.list_buckets.rst.txt
source_html: api_methods_cloudsync.list_buckets.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.list_buckets

## Summary

List the buckets available to the cloud sync credential identified by `credentials_id`.

Use this when configuring a cloud sync task to discover which buckets a set of credentials can access. Each returned entry describes a bucket as a directory-like listing.

Only providers that organize storage into buckets (such as Amazon S3 or Storj) are supported. A JSON-RPC `error` response (code `-32001`, *Method call error*) is returned when the credential does not exist or its provider does not use buckets.

## Required Roles

- `CLOUD_SYNC_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: credentials_id

<a id="Call_parameters_items_i0"></a>
#### credentials_id

- Schema name: `credentials_id`
- Type: integer

ID of the cloud credential to use for listing buckets.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of bucket information objects.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
