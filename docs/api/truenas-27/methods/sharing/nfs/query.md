---
title: sharing.nfs.query
kind: method
source_rst: _sources/api_methods_sharing.nfs.query.rst.txt
source_html: api_methods_sharing.nfs.query.html
required_roles:
  - SHARING_NFS_READ
---

# sharing.nfs.query

## Required Roles

- `SHARING_NFS_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Query options including pagination, ordering, and additional parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### SharingNFSQueryResultItem

- Schema name: `SharingNFSQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the NFS share.

<a id="headingReturn_value_anyOf_i0_items_path"></a>
<a id="Return_value_anyOf_i0_items_path"></a>
###### path

- Schema name: `Path`
- Type: string

Local path to be exported.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_dataset"></a>
<a id="Return_value_anyOf_i0_items_dataset"></a>
###### dataset

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/share'). Null if path cannot be resolved.
<a id="Return_value_anyOf_i0_items_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_relative_path"></a>
<a id="Return_value_anyOf_i0_items_relative_path"></a>
###### relative_path

- Schema name: `Relative Path`

Relative path component within the dataset (e.g., 'subdir/data'). Null if path cannot be resolved.
<a id="Return_value_anyOf_i0_items_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_aliases"></a>
<a id="Return_value_anyOf_i0_items_aliases"></a>
###### aliases

- Schema name: `Aliases`
- Type: array of string

IGNORED for now.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_aliases_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_comment"></a>
<a id="Return_value_anyOf_i0_items_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string

User comment associated with share.

<a id="headingReturn_value_anyOf_i0_items_networks"></a>
<a id="Return_value_anyOf_i0_items_networks"></a>
###### networks

- Schema name: `Networks`
- Type: array of string

List of authorized networks that are allowed to access the share having format "network/mask" CIDR notation. Each entry must be unique. If empty, all networks are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_networks_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_hosts"></a>
<a id="Return_value_anyOf_i0_items_hosts"></a>
###### hosts

- Schema name: `Hosts`
- Type: array of string

List of IP's/hostnames which are allowed to access the share. No quotes or spaces are allowed. Each entry must be unique. If empty, all IP's/hostnames are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_hosts_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_ro"></a>
<a id="Return_value_anyOf_i0_items_ro"></a>
###### ro

- Schema name: `Ro`
- Type: boolean

Export the share as read only.

<a id="headingReturn_value_anyOf_i0_items_maproot_user"></a>
<a id="Return_value_anyOf_i0_items_maproot_user"></a>
###### maproot_user

- Schema name: `Maproot User`

Map root user client to a specified user.
<a id="Return_value_anyOf_i0_items_maproot_user_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_maproot_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_maproot_user_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_maproot_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_maproot_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_maproot_group"></a>
<a id="Return_value_anyOf_i0_items_maproot_group"></a>
###### maproot_group

- Schema name: `Maproot Group`

Map root group client to a specified group.
<a id="Return_value_anyOf_i0_items_maproot_group_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_maproot_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_maproot_group_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_maproot_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_maproot_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_mapall_user"></a>
<a id="Return_value_anyOf_i0_items_mapall_user"></a>
###### mapall_user

- Schema name: `Mapall User`

Map all client users to a specified user.
<a id="Return_value_anyOf_i0_items_mapall_user_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_mapall_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_mapall_user_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_mapall_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_mapall_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_mapall_group"></a>
<a id="Return_value_anyOf_i0_items_mapall_group"></a>
###### mapall_group

- Schema name: `Mapall Group`

Map all client groups to a specified group.
<a id="Return_value_anyOf_i0_items_mapall_group_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_mapall_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_mapall_group_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_mapall_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_mapall_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_security"></a>
<a id="Return_value_anyOf_i0_items_security"></a>
###### security

- Schema name: `Security`
- Type: array of enum (of string)

Specify the security schema.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_security_items"></a>
- Type: enum (of string)
###### Must be one of:

- "SYS"
- "KRB5"
- "KRB5I"
- "KRB5P"

<a id="headingReturn_value_anyOf_i0_items_enabled"></a>
<a id="Return_value_anyOf_i0_items_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

Enable or disable the share.

<a id="headingReturn_value_anyOf_i0_items_locked"></a>
<a id="Return_value_anyOf_i0_items_locked"></a>
###### locked

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
<a id="Return_value_anyOf_i0_items_locked_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i0_items_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_locked_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_expose_snapshots"></a>
<a id="Return_value_anyOf_i0_items_expose_snapshots"></a>
###### expose_snapshots

- Schema name: `Expose Snapshots`
- Type: boolean

Enable access to the ZFS snapshot directory for the export. Requires a license carrying the NFS_SNAPSHOT feature, on any hardware. Export path must be the root directory of a ZFS dataset.

<a id="headingReturn_value_anyOf_i0_items_tier"></a>
<a id="Return_value_anyOf_i0_items_tier"></a>
###### tier

Storage tier in which the share's underlying dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
<a id="Return_value_anyOf_i0_items_tier_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_Return_value_anyOf_i0_items_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_tier_anyOf_i0_tier_type"></a>
<a id="Return_value_anyOf_i0_items_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingReturn_value_anyOf_i0_items_tier_anyOf_i0_tier_job"></a>
<a id="Return_value_anyOf_i0_items_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="Return_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_Return_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="Return_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="Return_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="Return_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="Return_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
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

<a id="tab-pane_Return_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_tier_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [SharingNFSQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `SharingNFSQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the NFS share.

<a id="headingReturn_value_anyOf_i1_path"></a>
<a id="Return_value_anyOf_i1_path"></a>
###### path

- Schema name: `Path`
- Type: string

Local path to be exported.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_dataset"></a>
<a id="Return_value_anyOf_i1_dataset"></a>
###### dataset

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/share'). Null if path cannot be resolved.
<a id="Return_value_anyOf_i1_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_relative_path"></a>
<a id="Return_value_anyOf_i1_relative_path"></a>
###### relative_path

- Schema name: `Relative Path`

Relative path component within the dataset (e.g., 'subdir/data'). Null if path cannot be resolved.
<a id="Return_value_anyOf_i1_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_aliases"></a>
<a id="Return_value_anyOf_i1_aliases"></a>
###### aliases

- Schema name: `Aliases`
- Type: array of string

IGNORED for now.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_aliases_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_comment"></a>
<a id="Return_value_anyOf_i1_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string

User comment associated with share.

<a id="headingReturn_value_anyOf_i1_networks"></a>
<a id="Return_value_anyOf_i1_networks"></a>
###### networks

- Schema name: `Networks`
- Type: array of string

List of authorized networks that are allowed to access the share having format "network/mask" CIDR notation. Each entry must be unique. If empty, all networks are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_networks_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_hosts"></a>
<a id="Return_value_anyOf_i1_hosts"></a>
###### hosts

- Schema name: `Hosts`
- Type: array of string

List of IP's/hostnames which are allowed to access the share. No quotes or spaces are allowed. Each entry must be unique. If empty, all IP's/hostnames are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_hosts_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_ro"></a>
<a id="Return_value_anyOf_i1_ro"></a>
###### ro

- Schema name: `Ro`
- Type: boolean

Export the share as read only.

<a id="headingReturn_value_anyOf_i1_maproot_user"></a>
<a id="Return_value_anyOf_i1_maproot_user"></a>
###### maproot_user

- Schema name: `Maproot User`

Map root user client to a specified user.
<a id="Return_value_anyOf_i1_maproot_user_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_maproot_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_maproot_user_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_maproot_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_maproot_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_maproot_group"></a>
<a id="Return_value_anyOf_i1_maproot_group"></a>
###### maproot_group

- Schema name: `Maproot Group`

Map root group client to a specified group.
<a id="Return_value_anyOf_i1_maproot_group_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_maproot_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_maproot_group_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_maproot_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_maproot_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_mapall_user"></a>
<a id="Return_value_anyOf_i1_mapall_user"></a>
###### mapall_user

- Schema name: `Mapall User`

Map all client users to a specified user.
<a id="Return_value_anyOf_i1_mapall_user_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_mapall_user_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_mapall_user_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_mapall_user_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_mapall_user_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_mapall_group"></a>
<a id="Return_value_anyOf_i1_mapall_group"></a>
###### mapall_group

- Schema name: `Mapall Group`

Map all client groups to a specified group.
<a id="Return_value_anyOf_i1_mapall_group_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_mapall_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_mapall_group_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_mapall_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_mapall_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_security"></a>
<a id="Return_value_anyOf_i1_security"></a>
###### security

- Schema name: `Security`
- Type: array of enum (of string)

Specify the security schema.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_security_items"></a>
- Type: enum (of string)
###### Must be one of:

- "SYS"
- "KRB5"
- "KRB5I"
- "KRB5P"

<a id="headingReturn_value_anyOf_i1_enabled"></a>
<a id="Return_value_anyOf_i1_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

Enable or disable the share.

<a id="headingReturn_value_anyOf_i1_locked"></a>
<a id="Return_value_anyOf_i1_locked"></a>
###### locked

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
<a id="Return_value_anyOf_i1_locked_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i1_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_locked_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_expose_snapshots"></a>
<a id="Return_value_anyOf_i1_expose_snapshots"></a>
###### expose_snapshots

- Schema name: `Expose Snapshots`
- Type: boolean

Enable access to the ZFS snapshot directory for the export. Requires a license carrying the NFS_SNAPSHOT feature, on any hardware. Export path must be the root directory of a ZFS dataset.

<a id="headingReturn_value_anyOf_i1_tier"></a>
<a id="Return_value_anyOf_i1_tier"></a>
###### tier

Storage tier in which the share's underlying dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
<a id="Return_value_anyOf_i1_tier_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_tier_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_tier_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_tier_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
