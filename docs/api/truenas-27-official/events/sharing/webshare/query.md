---
title: sharing.webshare.query
kind: event
source_rst: _sources/api_events_sharing.webshare.query.rst.txt
source_html: api_events_sharing.webshare.query.html
required_roles:
  - SHARING_WEBSHARE_READ
---

# sharing.webshare.query

## Summary

Sent on sharing.webshare changes.

## Required Roles

- `SHARING_WEBSHARE_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `SharingWebshareAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `SharingWebshareEntry`
- Type: object

Webshare share entry on the TrueNAS server.
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this Webshare share.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Webshare share name.
- Must be at least `1` characters long

<a id="headingADDED_fields_path"></a>
<a id="ADDED_fields_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Local server path to share by using the Webshare protocol. The path must start with `/mnt/` and must be in a ZFS pool.
- Must be at least `1` characters long

<a id="headingADDED_fields_dataset"></a>
<a id="ADDED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/webshare'). Null if path cannot be resolved.
<a id="ADDED_fields_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_dataset_anyOf_i1)

- Type: null

<a id="headingADDED_fields_relative_path"></a>
<a id="ADDED_fields_relative_path"></a>
##### relative_path (required)

- Schema name: `Relative Path`

Relative path component within the dataset (e.g., 'subdir/data'). Null if path cannot be resolved.
<a id="ADDED_fields_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_relative_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If unset, the Webshare share is not available.

<a id="headingADDED_fields_is_home_base"></a>
<a id="ADDED_fields_is_home_base"></a>
##### is_home_base

- Schema name: `Is Home Base`
- Type: boolean
- Default: false

If set, this share is used as the base path for user home directories. Only one share can have this enabled.

<a id="headingADDED_fields_locked"></a>
<a id="ADDED_fields_locked"></a>
##### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
<a id="ADDED_fields_locked_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_locked_anyOf_i1)

- Type: null

<a id="headingADDED_fields_tier"></a>
<a id="ADDED_fields_tier"></a>
##### tier

- Default: null

Storage tier in which the share's underlying dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
<a id="ADDED_fields_tier_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_ADDED_fields_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_tier_anyOf_i0_tier_type"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingADDED_fields_tier_anyOf_i0_tier_job"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
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

<a id="tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_tier_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `SharingWebshareChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `SharingWebshareEntry`
- Type: object

Webshare share entry on the TrueNAS server.
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this Webshare share.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Webshare share name.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_path"></a>
<a id="CHANGED_fields_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Local server path to share by using the Webshare protocol. The path must start with `/mnt/` and must be in a ZFS pool.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_dataset"></a>
<a id="CHANGED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/webshare'). Null if path cannot be resolved.
<a id="CHANGED_fields_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_dataset_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_relative_path"></a>
<a id="CHANGED_fields_relative_path"></a>
##### relative_path (required)

- Schema name: `Relative Path`

Relative path component within the dataset (e.g., 'subdir/data'). Null if path cannot be resolved.
<a id="CHANGED_fields_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_relative_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If unset, the Webshare share is not available.

<a id="headingCHANGED_fields_is_home_base"></a>
<a id="CHANGED_fields_is_home_base"></a>
##### is_home_base

- Schema name: `Is Home Base`
- Type: boolean
- Default: false

If set, this share is used as the base path for user home directories. Only one share can have this enabled.

<a id="headingCHANGED_fields_locked"></a>
<a id="CHANGED_fields_locked"></a>
##### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
<a id="CHANGED_fields_locked_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_locked_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_tier"></a>
<a id="CHANGED_fields_tier"></a>
##### tier

- Default: null

Storage tier in which the share's underlying dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
<a id="CHANGED_fields_tier_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_CHANGED_fields_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_tier_anyOf_i0_tier_type"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
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

<a id="tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_tier_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `SharingWebshareRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
