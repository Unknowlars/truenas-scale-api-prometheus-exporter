---
title: sharing.webshare.create
kind: method
source_rst: _sources/api_methods_sharing.webshare.create.rst.txt
source_html: api_methods_sharing.webshare.create.html
required_roles:
  - SHARING_WEBSHARE_WRITE
---

# sharing.webshare.create

## Summary

Create a Webshare share that exposes a local ZFS path over the Webshare protocol.

The shared `path` must reside under `/mnt/` within a ZFS pool. At most one share may set `is_home_base` to `true` to serve as the base path for user home directories.

## Required Roles

- `SHARING_WEBSHARE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Webshare share configuration data for the new share.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Webshare share name.
- Must be at least `1` characters long

##### path (required)

- Schema name: `Path`
- Type: string

Local server path to share by using the Webshare protocol. The path must start with `/mnt/` and must be in a ZFS pool.
- Must be at least `1` characters long

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If unset, the Webshare share is not available.

##### is_home_base

- Schema name: `Is Home Base`
- Type: boolean
- Default: false

If set, this share is used as the base path for user home directories. Only one share can have this enabled.

### Return value

- Schema name: `SharingWebshareEntry`
- Type: object

The created Webshare share configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this Webshare share.

#### name (required)

- Schema name: `Name`
- Type: string

Webshare share name.
- Must be at least `1` characters long

#### path (required)

- Schema name: `Path`
- Type: string

Local server path to share by using the Webshare protocol. The path must start with `/mnt/` and must be in a ZFS pool.
- Must be at least `1` characters long

#### dataset (required)

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/webshare'). Null if path cannot be resolved.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### relative_path (required)

- Schema name: `Relative Path`

Relative path component within the dataset (e.g., 'subdir/data'). Null if path cannot be resolved.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If unset, the Webshare share is not available.

#### is_home_base

- Schema name: `Is Home Base`
- Type: boolean
- Default: false

If set, this share is used as the base path for user home directories. Only one share can have this enabled.

#### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### tier

- Default: null

Storage tier in which the share's underlying dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
##### Any of

###### TierInfo

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
####### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.

####### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
######## Any of

######### ZfsTierRewriteJobEntry

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
########## tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

########## dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

########## job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

########## status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.

######### Option 2

- Type: null

###### Option 2

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

###### ZfsTierRewriteJobEntry

- Type: null

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
