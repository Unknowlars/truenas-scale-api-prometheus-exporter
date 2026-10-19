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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the cloud backup task.

#### Parameter 2: snapshot_id

<a id="Call_parameters_items_i1"></a>
#### snapshot_id

- Schema name: `snapshot_id`
- Type: string

ID of the snapshot to restore.
- Must match regular expression: `^[^-]`

#### Parameter 3: subfolder

<a id="Call_parameters_items_i2"></a>
#### subfolder

- Schema name: `subfolder`
- Type: string

Path within the snapshot to restore.

#### Parameter 4: destination_path

<a id="Call_parameters_items_i3"></a>
#### destination_path

- Schema name: `destination_path`
- Type: string

Local path to restore to.

#### Parameter 5: options

<a id="Call_parameters_items_i4"></a>
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
<a id="headingCall_parameters_items_i4_exclude"></a>
<a id="Call_parameters_items_i4_exclude"></a>
##### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Paths to exclude from a restore using `restic restore --exclude`.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i4_exclude_items"></a>
- Type: string

<a id="headingCall_parameters_items_i4_include"></a>
<a id="Call_parameters_items_i4_include"></a>
##### include

- Schema name: `Include`
- Type: array of string
- Default: []

Paths to include in a restore using `restic restore --include`.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i4_include_items"></a>
- Type: string

<a id="headingCall_parameters_items_i4_rate_limit"></a>
<a id="Call_parameters_items_i4_rate_limit"></a>
##### rate_limit

- Schema name: `Rate Limit`
- Default: null

Maximum download rate in KiB/s. Passed to `restic --limit-download`. If provided, overrides the task's rate limit.
<a id="Call_parameters_items_i4_rate_limit_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i4_rate_limit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i4_rate_limit_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0`

<a id="tab-pane_Call_parameters_items_i4_rate_limit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i4_rate_limit_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
