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

The cloud backup task ID.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Sync options.
- No Additional Properties
<a id="headingCall_parameters_items_i1_dry_run"></a>
<a id="Call_parameters_items_i1_dry_run"></a>
##### dry_run

- Schema name: `Dry Run`
- Type: boolean
- Default: false

Simulate the backup without actually writing to the remote repository.

<a id="headingCall_parameters_items_i1_rate_limit"></a>
<a id="Call_parameters_items_i1_rate_limit"></a>
##### rate_limit

- Schema name: `Rate Limit`
- Default: null

Maximum upload rate in KiB/s. Passed to `restic --limit-upload`. If provided, overrides the task's rate limit.
<a id="Call_parameters_items_i1_rate_limit_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_rate_limit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_rate_limit_anyOf_i0)

- Type: integer
- Value must be strictly greater than `0`

<a id="tab-pane_Call_parameters_items_i1_rate_limit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_rate_limit_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
