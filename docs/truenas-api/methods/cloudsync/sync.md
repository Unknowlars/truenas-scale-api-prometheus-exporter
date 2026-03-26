---
title: cloudsync.sync
kind: method
source_rst: _sources/api_methods_cloudsync.sync.rst.txt
source_html: api_methods_cloudsync.sync.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.sync

## Summary

Run the cloud_sync job `id`, syncing the local data to remote.

This method is a job.

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

ID of the cloud sync task to run.

#### Parameter 2: cloud_sync_sync_options

#### cloud_sync_sync_options

- Schema name: `cloud_sync_sync_options`
- Type: object

Options for the sync operation.
- No Additional Properties
##### dry_run

- Schema name: `Dry Run`
- Type: boolean
- Default: false

Whether to perform a dry run without making actual changes.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the sync operation is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
