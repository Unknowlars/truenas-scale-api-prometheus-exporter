---
title: zfs.tier.dataset_set_tier
kind: method
source_rst: _sources/api_methods_zfs.tier.dataset_set_tier.rst.txt
source_html: api_methods_zfs.tier.dataset_set_tier.html
required_roles:
  - DATASET_WRITE
---

# zfs.tier.dataset_set_tier

## Summary

Set the performance tier for a ZFS dataset, optionally migrating existing data.

Datasets with ZFS deduplication enabled cannot be assigned a tier.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: zfs_tier_dataset_set_tier

<a id="Call_parameters_items_i0"></a>
#### zfs_tier_dataset_set_tier

- Schema name: `zfs_tier_dataset_set_tier`
- Type: object

ZfsTierDatasetSetTierArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_dataset_name"></a>
<a id="Call_parameters_items_i0_dataset_name"></a>
##### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset to configure (e.g. `tank/data`).
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_tier_type"></a>
<a id="Call_parameters_items_i0_tier_type"></a>
##### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this dataset.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingCall_parameters_items_i0_move_existing_data"></a>
<a id="Call_parameters_items_i0_move_existing_data"></a>
##### move_existing_data

- Schema name: `Move Existing Data`
- Type: boolean
- Default: false

When `true`, immediately create a rewrite job to physically migrate existing data to match the new tier.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `TierInfo`
- Type: object

Updated tier info for the dataset. If `move_existing_data` was `true`, `tier_job` will contain the newly created rewrite job.
- No Additional Properties
<a id="headingReturn_value_tier_type"></a>
<a id="Return_value_tier_type"></a>
#### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
##### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingReturn_value_tier_job"></a>
<a id="Return_value_tier_job"></a>
#### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="Return_value_tier_job_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_Return_value_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_tier_job_anyOf_i0_tier_job_id"></a>
<a id="Return_value_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_job_anyOf_i0_dataset_name"></a>
<a id="Return_value_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_job_anyOf_i0_job_uuid"></a>
<a id="Return_value_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_job_anyOf_i0_status"></a>
<a id="Return_value_tier_job_anyOf_i0_status"></a>
###### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.
###### Must be one of:

- "COMPLETE"
- "RUNNING"
- "QUEUED"
- "CANCELLED"
- "STOPPED"
- "ERROR"

<a id="tab-pane_Return_value_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_tier_job_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
