---
title: zfs.tier.rewrite_job_recover
kind: method
source_rst: _sources/api_methods_zfs.tier.rewrite_job_recover.rst.txt
source_html: api_methods_zfs.tier.rewrite_job_recover.html
required_roles:
  - DATASET_WRITE
---

# zfs.tier.rewrite_job_recover

## Summary

Recover a rewrite job in ERROR state by reissuing failed rewrites.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: zfs_tier_rewrite_job_recover

#### zfs_tier_rewrite_job_recover

- Schema name: `zfs_tier_rewrite_job_recover`
- Type: object

ZfsTierRewriteJobRecoverArgs parameters.
- No Additional Properties
##### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job to recover, in `dataset_name@job_uuid` format. The job must be in `ERROR` state.
- Must be at least `1` characters long

### Return value

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object

The job after recovery is initiated. Status will be `RUNNING` if failed files remain to be retried, or `COMPLETE` if all previously failed files were retried successfully.
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

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
