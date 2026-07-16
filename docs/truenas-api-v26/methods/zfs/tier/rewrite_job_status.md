---
title: zfs.tier.rewrite_job_status
kind: method
source_rst: _sources/api_methods_zfs.tier.rewrite_job_status.rst.txt
source_html: api_methods_zfs.tier.rewrite_job_status.html
required_roles:
  - DATASET_READ
---

# zfs.tier.rewrite_job_status

## Summary

Get detailed status and statistics for a specific rewrite job.

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: zfs_tier_rewrite_job_status

#### zfs_tier_rewrite_job_status

- Schema name: `zfs_tier_rewrite_job_status`
- Type: object

ZfsTierRewriteJobStatusArgs parameters.
- No Additional Properties
##### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job to query, in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

### Return value

- Schema name: `ZfsTierRewriteJobStatusEntry`
- Type: object

Current status and statistics for the requested rewrite job.
- No Additional Properties
#### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

#### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

#### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

#### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.

#### stats (required)

Progress statistics, or `null` if no statistics have been recorded yet.
##### Any of

###### ZfsTierRewriteJobStats

- Schema name: `ZfsTierRewriteJobStats`
- Type: object
- No Additional Properties
####### start_time (required)

- Schema name: `Start Time`
- Type: integer

Unix timestamp (seconds) when the current run started. Reset each time the job is resumed or recovered.

####### initial_time (required)

- Schema name: `Initial Time`
- Type: integer

Unix timestamp (seconds) when the job was first created. Preserved across resumes.

####### update_time (required)

- Schema name: `Update Time`
- Type: integer

Unix timestamp (seconds) of the most recent statistics update.

####### count_items (required)

- Schema name: `Count Items`
- Type: integer

Number of files processed in the current run. Reset to zero on each resume.

####### count_bytes (required)

- Schema name: `Count Bytes`
- Type: integer

Bytes processed in the current run. Reset to zero on each resume.

####### total_items (required)

- Schema name: `Total Items`
- Type: integer

Total number of files to process across the entire dataset.

####### total_bytes (required)

- Schema name: `Total Bytes`
- Type: integer

Total bytes to process across the entire dataset.

####### failures (required)

- Schema name: `Failures`
- Type: integer

Cumulative count of files that failed rewriting across all runs of this job.

####### success (required)

- Schema name: `Success`
- Type: integer

Cumulative count of files successfully rewritten across all runs of this job.

####### parent (required)

- Schema name: `Parent`
- Type: string

Directory path of the file currently being processed. Also used as the resume checkpoint if the job is interrupted.

####### name (required)

- Schema name: `Name`
- Type: string

Name of the file currently being processed.

###### Option 2

- Type: null

#### error (required)

- Schema name: `Error`

Error message describing why the job entered `ERROR` state, otherwise `null`.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
