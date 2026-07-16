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

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: zfs_tier_dataset_set_tier

#### zfs_tier_dataset_set_tier

- Schema name: `zfs_tier_dataset_set_tier`
- Type: object

ZfsTierDatasetSetTierArgs parameters.
- No Additional Properties
##### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset to configure (e.g. `tank/data`).
- Must be at least `1` characters long

##### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this dataset.

##### move_existing_data

- Schema name: `Move Existing Data`
- Type: boolean
- Default: false

When `true`, immediately create a rewrite job to physically migrate existing data to match the new tier.

### Return value

- Schema name: `TierInfo`
- Type: object

Updated tier info for the dataset. If `move_existing_data` was `true`, `tier_job` will contain the newly created rewrite job.
- No Additional Properties
#### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.

#### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
##### Any of

###### ZfsTierRewriteJobEntry

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
####### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

####### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

####### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

####### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
