---
title: cloudsync.create_bucket
kind: method
source_rst: _sources/api_methods_cloudsync.create_bucket.rst.txt
source_html: api_methods_cloudsync.create_bucket.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.create_bucket

## Summary

Creates a new bucket `name` using ` credentials_id`.

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

ID of the cloud credential to use for bucket creation.

#### Parameter 2: name

#### name

- Schema name: `name`
- Type: string

Name for the new bucket.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the bucket is successfully created.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
