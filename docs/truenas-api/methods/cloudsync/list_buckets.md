---
title: cloudsync.list_buckets
kind: method
source_rst: _sources/api_methods_cloudsync.list_buckets.rst.txt
source_html: api_methods_cloudsync.list_buckets.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.list_buckets

## Required Roles

- `CLOUD_SYNC_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: credentials_id

#### credentials_id

- Schema name: `credentials_id`
- Type: integer

ID of the cloud credential to use for listing buckets.

### Return value

- Schema name: `Result`
- Type: array of object

Array of bucket information objects.
- No Additional Items

#### Each item of this array must be:

- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
