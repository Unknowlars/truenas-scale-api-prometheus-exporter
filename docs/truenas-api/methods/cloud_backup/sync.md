---
title: cloud_backup.sync
kind: method
source_rst: _sources/api_methods_cloud_backup.sync.rst.txt
source_html: api_methods_cloud_backup.sync.html
required_roles:
  - CLOUD_BACKUP_WRITE
---

# cloud_backup.sync

## Summary

Run the cloud backup job `id`.

This method is a job.

## Required Roles

- `CLOUD_BACKUP_WRITE`

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

The cloud backup task ID.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Sync options.
- No Additional Properties
##### dry_run

- Schema name: `Dry Run`
- Type: boolean
- Default: false

Simulate the backup without actually writing to the remote repository.

##### rate_limit

- Schema name: `Rate Limit`
- Default: null

Maximum upload rate in KiB/s. Passed to `restic --limit-upload`. If provided, overrides the task's rate limit.
###### Any of

####### Option 1

- Type: integer
- Value must be strictly greater than `0`

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
