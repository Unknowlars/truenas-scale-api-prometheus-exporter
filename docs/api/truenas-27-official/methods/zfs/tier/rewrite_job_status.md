---
title: zfs.tier.rewrite_job_status
kind: method
source_rst: _sources/api_methods_zfs.tier.rewrite_job_status.rst.txt
source_html: api_methods_zfs.tier.rewrite_job_status.html
required_roles:
  - ZFS_RESOURCE_READ
---

# zfs.tier.rewrite_job_status

## Summary

Get detailed status and statistics for a specific rewrite job.

## Required Roles

- `ZFS_RESOURCE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: zfs_tier_rewrite_job_status

<a id="Call_parameters_items_i0"></a>
#### zfs_tier_rewrite_job_status

- Schema name: `zfs_tier_rewrite_job_status`
- Type: object

ZfsTierRewriteJobStatusArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_tier_job_id"></a>
<a id="Call_parameters_items_i0_tier_job_id"></a>
##### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job to query, in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ZfsTierRewriteJobStatusEntry`
- Type: object

Current status and statistics for the requested rewrite job.
- No Additional Properties
<a id="headingReturn_value_tier_job_id"></a>
<a id="Return_value_tier_job_id"></a>
#### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value_dataset_name"></a>
<a id="Return_value_dataset_name"></a>
#### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingReturn_value_job_uuid"></a>
<a id="Return_value_job_uuid"></a>
#### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingReturn_value_status"></a>
<a id="Return_value_status"></a>
#### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.
##### Must be one of:

- "COMPLETE"
- "RUNNING"
- "QUEUED"
- "CANCELLED"
- "STOPPED"
- "ERROR"

<a id="headingReturn_value_stats"></a>
<a id="Return_value_stats"></a>
#### stats (required)

Progress statistics, or `null` if no statistics have been recorded yet.
<a id="Return_value_stats_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_stats_anyOf_i0"></a>
###### [ZfsTierRewriteJobStats](#tab-pane_Return_value_stats_anyOf_i0)

- Schema name: `ZfsTierRewriteJobStats`
- Type: object
- No Additional Properties
<a id="headingReturn_value_stats_anyOf_i0_start_time"></a>
<a id="Return_value_stats_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: integer

Unix timestamp (seconds) when the current run started. Reset each time the job is resumed or recovered.

<a id="headingReturn_value_stats_anyOf_i0_initial_time"></a>
<a id="Return_value_stats_anyOf_i0_initial_time"></a>
###### initial_time (required)

- Schema name: `Initial Time`
- Type: integer

Unix timestamp (seconds) when the job was first created. Preserved across resumes.

<a id="headingReturn_value_stats_anyOf_i0_update_time"></a>
<a id="Return_value_stats_anyOf_i0_update_time"></a>
###### update_time (required)

- Schema name: `Update Time`
- Type: integer

Unix timestamp (seconds) of the most recent statistics update.

<a id="headingReturn_value_stats_anyOf_i0_count_items"></a>
<a id="Return_value_stats_anyOf_i0_count_items"></a>
###### count_items (required)

- Schema name: `Count Items`
- Type: integer

Number of files processed in the current run. Reset to zero on each resume.

<a id="headingReturn_value_stats_anyOf_i0_count_bytes"></a>
<a id="Return_value_stats_anyOf_i0_count_bytes"></a>
###### count_bytes (required)

- Schema name: `Count Bytes`
- Type: integer

Bytes processed in the current run. Reset to zero on each resume.

<a id="headingReturn_value_stats_anyOf_i0_total_items"></a>
<a id="Return_value_stats_anyOf_i0_total_items"></a>
###### total_items (required)

- Schema name: `Total Items`
- Type: integer

Total number of files to process across the entire dataset.

<a id="headingReturn_value_stats_anyOf_i0_total_bytes"></a>
<a id="Return_value_stats_anyOf_i0_total_bytes"></a>
###### total_bytes (required)

- Schema name: `Total Bytes`
- Type: integer

Total bytes to process across the entire dataset.

<a id="headingReturn_value_stats_anyOf_i0_failures"></a>
<a id="Return_value_stats_anyOf_i0_failures"></a>
###### failures (required)

- Schema name: `Failures`
- Type: integer

Cumulative count of files that failed rewriting across all runs of this job.

<a id="headingReturn_value_stats_anyOf_i0_success"></a>
<a id="Return_value_stats_anyOf_i0_success"></a>
###### success (required)

- Schema name: `Success`
- Type: integer

Cumulative count of files successfully rewritten across all runs of this job.

<a id="headingReturn_value_stats_anyOf_i0_parent"></a>
<a id="Return_value_stats_anyOf_i0_parent"></a>
###### parent (required)

- Schema name: `Parent`
- Type: string

Directory path of the file currently being processed. Also used as the resume checkpoint if the job is interrupted.

<a id="headingReturn_value_stats_anyOf_i0_name"></a>
<a id="Return_value_stats_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the file currently being processed.

<a id="tab-pane_Return_value_stats_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_stats_anyOf_i1)

- Type: null

<a id="headingReturn_value_error"></a>
<a id="Return_value_error"></a>
#### error (required)

- Schema name: `Error`

Error message describing why the job entered `ERROR` state, otherwise `null`.
<a id="Return_value_error_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_error_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
