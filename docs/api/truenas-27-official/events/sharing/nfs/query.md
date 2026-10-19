---
title: sharing.nfs.query
kind: event
source_rst: _sources/api_events_sharing.nfs.query.rst.txt
source_html: api_events_sharing.nfs.query.html
required_roles:
  - SHARING_NFS_READ
---

# sharing.nfs.query

## Summary

Sent on sharing.nfs changes.

## Required Roles

- `SHARING_NFS_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `SharingNFSAddedEvent`
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

- Schema name: `SharingNFSEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NFS share.

<a id="headingADDED_fields_path"></a>
<a id="ADDED_fields_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Local path to be exported.
- Must be at least `1` characters long

<a id="headingADDED_fields_dataset"></a>
<a id="ADDED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/share'). Null if path cannot be resolved.
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

<a id="headingADDED_fields_aliases"></a>
<a id="ADDED_fields_aliases"></a>
##### aliases

- Schema name: `Aliases`
- Type: array of string
- Default: []

IGNORED for now.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_aliases_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_comment"></a>
<a id="ADDED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

User comment associated with share.

<a id="headingADDED_fields_networks"></a>
<a id="ADDED_fields_networks"></a>
##### networks

- Schema name: `Networks`
- Type: array of string
- Default: []

List of authorized networks that are allowed to access the share having format "network/mask" CIDR notation. Each entry must be unique. If empty, all networks are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_networks_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_hosts"></a>
<a id="ADDED_fields_hosts"></a>
##### hosts

- Schema name: `Hosts`
- Type: array of string
- Default: []

List of IP's/hostnames which are allowed to access the share. No quotes or spaces are allowed. Each entry must be unique. If empty, all IP's/hostnames are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_hosts_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_ro"></a>
<a id="ADDED_fields_ro"></a>
##### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Export the share as read only.

<a id="headingADDED_fields_maproot_user"></a>
<a id="ADDED_fields_maproot_user"></a>
##### maproot_user

- Schema name: `Maproot User`
- Default: null

Map root user client to a specified user.
<a id="ADDED_fields_maproot_user_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_maproot_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_maproot_user_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_maproot_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_maproot_user_anyOf_i1)

- Type: null

<a id="headingADDED_fields_maproot_group"></a>
<a id="ADDED_fields_maproot_group"></a>
##### maproot_group

- Schema name: `Maproot Group`
- Default: null

Map root group client to a specified group.
<a id="ADDED_fields_maproot_group_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_maproot_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_maproot_group_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_maproot_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_maproot_group_anyOf_i1)

- Type: null

<a id="headingADDED_fields_mapall_user"></a>
<a id="ADDED_fields_mapall_user"></a>
##### mapall_user

- Schema name: `Mapall User`
- Default: null

Map all client users to a specified user.
<a id="ADDED_fields_mapall_user_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_mapall_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_mapall_user_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_mapall_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_mapall_user_anyOf_i1)

- Type: null

<a id="headingADDED_fields_mapall_group"></a>
<a id="ADDED_fields_mapall_group"></a>
##### mapall_group

- Schema name: `Mapall Group`
- Default: null

Map all client groups to a specified group.
<a id="ADDED_fields_mapall_group_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_mapall_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_mapall_group_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_mapall_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_mapall_group_anyOf_i1)

- Type: null

<a id="headingADDED_fields_security"></a>
<a id="ADDED_fields_security"></a>
##### security

- Schema name: `Security`
- Type: array of enum (of string)
- Default: []

Specify the security schema.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_security_items"></a>
- Type: enum (of string)
###### Must be one of:

- "SYS"
- "KRB5"
- "KRB5I"
- "KRB5P"

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Enable or disable the share.

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

<a id="headingADDED_fields_expose_snapshots"></a>
<a id="ADDED_fields_expose_snapshots"></a>
##### expose_snapshots

- Schema name: `Expose Snapshots`
- Type: boolean
- Default: false

Enable access to the ZFS snapshot directory for the export. Requires a license carrying the NFS_SNAPSHOT feature, on any hardware. Export path must be the root directory of a ZFS dataset.

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

- Schema name: `SharingNFSChangedEvent`
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

- Schema name: `SharingNFSEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NFS share.

<a id="headingCHANGED_fields_path"></a>
<a id="CHANGED_fields_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Local path to be exported.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_dataset"></a>
<a id="CHANGED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/share'). Null if path cannot be resolved.
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

<a id="headingCHANGED_fields_aliases"></a>
<a id="CHANGED_fields_aliases"></a>
##### aliases

- Schema name: `Aliases`
- Type: array of string
- Default: []

IGNORED for now.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_aliases_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_comment"></a>
<a id="CHANGED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

User comment associated with share.

<a id="headingCHANGED_fields_networks"></a>
<a id="CHANGED_fields_networks"></a>
##### networks

- Schema name: `Networks`
- Type: array of string
- Default: []

List of authorized networks that are allowed to access the share having format "network/mask" CIDR notation. Each entry must be unique. If empty, all networks are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_networks_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_hosts"></a>
<a id="CHANGED_fields_hosts"></a>
##### hosts

- Schema name: `Hosts`
- Type: array of string
- Default: []

List of IP's/hostnames which are allowed to access the share. No quotes or spaces are allowed. Each entry must be unique. If empty, all IP's/hostnames are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_hosts_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_ro"></a>
<a id="CHANGED_fields_ro"></a>
##### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Export the share as read only.

<a id="headingCHANGED_fields_maproot_user"></a>
<a id="CHANGED_fields_maproot_user"></a>
##### maproot_user

- Schema name: `Maproot User`
- Default: null

Map root user client to a specified user.
<a id="CHANGED_fields_maproot_user_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_maproot_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_maproot_user_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_maproot_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_maproot_user_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_maproot_group"></a>
<a id="CHANGED_fields_maproot_group"></a>
##### maproot_group

- Schema name: `Maproot Group`
- Default: null

Map root group client to a specified group.
<a id="CHANGED_fields_maproot_group_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_maproot_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_maproot_group_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_maproot_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_maproot_group_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_mapall_user"></a>
<a id="CHANGED_fields_mapall_user"></a>
##### mapall_user

- Schema name: `Mapall User`
- Default: null

Map all client users to a specified user.
<a id="CHANGED_fields_mapall_user_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_mapall_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_mapall_user_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_mapall_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_mapall_user_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_mapall_group"></a>
<a id="CHANGED_fields_mapall_group"></a>
##### mapall_group

- Schema name: `Mapall Group`
- Default: null

Map all client groups to a specified group.
<a id="CHANGED_fields_mapall_group_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_mapall_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_mapall_group_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_mapall_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_mapall_group_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_security"></a>
<a id="CHANGED_fields_security"></a>
##### security

- Schema name: `Security`
- Type: array of enum (of string)
- Default: []

Specify the security schema.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_security_items"></a>
- Type: enum (of string)
###### Must be one of:

- "SYS"
- "KRB5"
- "KRB5I"
- "KRB5P"

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Enable or disable the share.

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

<a id="headingCHANGED_fields_expose_snapshots"></a>
<a id="CHANGED_fields_expose_snapshots"></a>
##### expose_snapshots

- Schema name: `Expose Snapshots`
- Type: boolean
- Default: false

Enable access to the ZFS snapshot directory for the export. Requires a license carrying the NFS_SNAPSHOT feature, on any hardware. Export path must be the root directory of a ZFS dataset.

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

- Schema name: `SharingNFSRemovedEvent`
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
