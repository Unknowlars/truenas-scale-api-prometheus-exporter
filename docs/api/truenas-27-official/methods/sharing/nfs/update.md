---
title: sharing.nfs.update
kind: method
source_rst: _sources/api_methods_sharing.nfs.update.rst.txt
source_html: api_methods_sharing.nfs.update.html
required_roles:
  - SHARING_NFS_WRITE
---

# sharing.nfs.update

## Summary

Update NFS Share of `id`.

## Required Roles

- `SHARING_NFS_WRITE`

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

ID of the NFS share to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Updated NFS share configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_path"></a>
<a id="Call_parameters_items_i1_path"></a>
##### path

- Schema name: `Path`
- Type: string

Local path to be exported.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_aliases"></a>
<a id="Call_parameters_items_i1_aliases"></a>
##### aliases

- Schema name: `Aliases`
- Type: array of string

IGNORED for now.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_aliases_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_comment"></a>
<a id="Call_parameters_items_i1_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string

User comment associated with share.

<a id="headingCall_parameters_items_i1_networks"></a>
<a id="Call_parameters_items_i1_networks"></a>
##### networks

- Schema name: `Networks`
- Type: array of string

List of authorized networks that are allowed to access the share having format "network/mask" CIDR notation. Each entry must be unique. If empty, all networks are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_networks_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_hosts"></a>
<a id="Call_parameters_items_i1_hosts"></a>
##### hosts

- Schema name: `Hosts`
- Type: array of string

List of IP's/hostnames which are allowed to access the share. No quotes or spaces are allowed. Each entry must be unique. If empty, all IP's/hostnames are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_hosts_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_ro"></a>
<a id="Call_parameters_items_i1_ro"></a>
##### ro

- Schema name: `Ro`
- Type: boolean

Export the share as read only.

<a id="headingCall_parameters_items_i1_maproot_user"></a>
<a id="Call_parameters_items_i1_maproot_user"></a>
##### maproot_user

- Schema name: `Maproot User`

Map root user client to a specified user.
<a id="Call_parameters_items_i1_maproot_user_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_maproot_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_maproot_user_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_maproot_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_maproot_user_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_maproot_group"></a>
<a id="Call_parameters_items_i1_maproot_group"></a>
##### maproot_group

- Schema name: `Maproot Group`

Map root group client to a specified group.
<a id="Call_parameters_items_i1_maproot_group_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_maproot_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_maproot_group_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_maproot_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_maproot_group_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_mapall_user"></a>
<a id="Call_parameters_items_i1_mapall_user"></a>
##### mapall_user

- Schema name: `Mapall User`

Map all client users to a specified user.
<a id="Call_parameters_items_i1_mapall_user_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_mapall_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_mapall_user_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_mapall_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_mapall_user_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_mapall_group"></a>
<a id="Call_parameters_items_i1_mapall_group"></a>
##### mapall_group

- Schema name: `Mapall Group`

Map all client groups to a specified group.
<a id="Call_parameters_items_i1_mapall_group_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_mapall_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_mapall_group_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_mapall_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_mapall_group_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_security"></a>
<a id="Call_parameters_items_i1_security"></a>
##### security

- Schema name: `Security`
- Type: array of enum (of string)

Specify the security schema.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_security_items"></a>
- Type: enum (of string)
###### Must be one of:

- "SYS"
- "KRB5"
- "KRB5I"
- "KRB5P"

<a id="headingCall_parameters_items_i1_enabled"></a>
<a id="Call_parameters_items_i1_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean

Enable or disable the share.

<a id="headingCall_parameters_items_i1_expose_snapshots"></a>
<a id="Call_parameters_items_i1_expose_snapshots"></a>
##### expose_snapshots

- Schema name: `Expose Snapshots`
- Type: boolean

Enable access to the ZFS snapshot directory for the export. Requires a license carrying the NFS_SNAPSHOT feature, on any hardware. Export path must be the root directory of a ZFS dataset.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SharingNFSEntry`
- Type: object

The updated NFS share configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NFS share.

<a id="headingReturn_value_path"></a>
<a id="Return_value_path"></a>
#### path (required)

- Schema name: `Path`
- Type: string

Local path to be exported.
- Must be at least `1` characters long

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/share'). Null if path cannot be resolved.
<a id="Return_value_dataset_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_relative_path"></a>
<a id="Return_value_relative_path"></a>
#### relative_path (required)

- Schema name: `Relative Path`

Relative path component within the dataset (e.g., 'subdir/data'). Null if path cannot be resolved.
<a id="Return_value_relative_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_aliases"></a>
<a id="Return_value_aliases"></a>
#### aliases

- Schema name: `Aliases`
- Type: array of string
- Default: []

IGNORED for now.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_aliases_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_comment"></a>
<a id="Return_value_comment"></a>
#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

User comment associated with share.

<a id="headingReturn_value_networks"></a>
<a id="Return_value_networks"></a>
#### networks

- Schema name: `Networks`
- Type: array of string
- Default: []

List of authorized networks that are allowed to access the share having format "network/mask" CIDR notation. Each entry must be unique. If empty, all networks are allowed. Excessively long lists should be avoided.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_networks_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_hosts"></a>
<a id="Return_value_hosts"></a>
#### hosts

- Schema name: `Hosts`
- Type: array of string
- Default: []

List of IP's/hostnames which are allowed to access the share. No quotes or spaces are allowed. Each entry must be unique. If empty, all IP's/hostnames are allowed. Excessively long lists should be avoided.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_hosts_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_ro"></a>
<a id="Return_value_ro"></a>
#### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Export the share as read only.

<a id="headingReturn_value_maproot_user"></a>
<a id="Return_value_maproot_user"></a>
#### maproot_user

- Schema name: `Maproot User`
- Default: null

Map root user client to a specified user.
<a id="Return_value_maproot_user_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_maproot_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_maproot_user_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_maproot_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_maproot_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_maproot_group"></a>
<a id="Return_value_maproot_group"></a>
#### maproot_group

- Schema name: `Maproot Group`
- Default: null

Map root group client to a specified group.
<a id="Return_value_maproot_group_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_maproot_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_maproot_group_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_maproot_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_maproot_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_mapall_user"></a>
<a id="Return_value_mapall_user"></a>
#### mapall_user

- Schema name: `Mapall User`
- Default: null

Map all client users to a specified user.
<a id="Return_value_mapall_user_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_mapall_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_mapall_user_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_mapall_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_mapall_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_mapall_group"></a>
<a id="Return_value_mapall_group"></a>
#### mapall_group

- Schema name: `Mapall Group`
- Default: null

Map all client groups to a specified group.
<a id="Return_value_mapall_group_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_mapall_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_mapall_group_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_mapall_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_mapall_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_security"></a>
<a id="Return_value_security"></a>
#### security

- Schema name: `Security`
- Type: array of enum (of string)
- Default: []

Specify the security schema.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_security_items"></a>
- Type: enum (of string)
###### Must be one of:

- "SYS"
- "KRB5"
- "KRB5I"
- "KRB5P"

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Enable or disable the share.

<a id="headingReturn_value_locked"></a>
<a id="Return_value_locked"></a>
#### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
<a id="Return_value_locked_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_locked_anyOf_i1)

- Type: null

<a id="headingReturn_value_expose_snapshots"></a>
<a id="Return_value_expose_snapshots"></a>
#### expose_snapshots

- Schema name: `Expose Snapshots`
- Type: boolean
- Default: false

Enable access to the ZFS snapshot directory for the export. Requires a license carrying the NFS_SNAPSHOT feature, on any hardware. Export path must be the root directory of a ZFS dataset.

<a id="headingReturn_value_tier"></a>
<a id="Return_value_tier"></a>
#### tier

- Default: null

Storage tier in which the share's underlying dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
<a id="Return_value_tier_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_Return_value_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_tier_anyOf_i0_tier_type"></a>
<a id="Return_value_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingReturn_value_tier_anyOf_i0_tier_job"></a>
<a id="Return_value_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
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

<a id="tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_tier_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
