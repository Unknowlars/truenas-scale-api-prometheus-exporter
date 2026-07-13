---
title: cloud_backup.restore
kind: method
source_rst: _sources/api_methods_cloud_backup.restore.rst.txt
source_html: api_methods_cloud_backup.restore.html
required_roles:
  - FILESYSTEM_DATA_WRITE
---

# cloud_backup.restore

## Summary

Restore files to the directory `destination_path` from the `snapshot_id` subfolder `subfolder` created by the cloud backup job `id`.

This method is a job.

## Required Roles

- `FILESYSTEM_DATA_WRITE`

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

ID of the cloud backup task.

#### Parameter 2: snapshot_id

#### snapshot_id

- Schema name: `snapshot_id`
- Type: string

ID of the snapshot to restore.

#### Parameter 3: subfolder

#### subfolder

- Schema name: `subfolder`
- Type: string

Path within the snapshot to restore.

#### Parameter 4: destination_path

#### destination_path

- Schema name: `destination_path`
- Type: string

Local path to restore to.

#### Parameter 5: options

#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "exclude": [],
  "include": [],
  "rate_limit": null
}
```

Additional restore options.
- No Additional Properties
##### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Paths to exclude from a restore using `restic restore --exclude`.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### include

- Schema name: `Include`
- Type: array of string
- Default: []

Paths to include in a restore using `restic restore --include`.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### rate_limit

- Schema name: `Rate Limit`
- Default: null

Maximum download rate in KiB/s. Passed to `restic --limit-download`. If provided, overrides the task's rate limit.
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
