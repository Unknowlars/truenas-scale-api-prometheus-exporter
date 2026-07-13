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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

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
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### SharingNFSEntry

- Schema name: `SharingNFSEntry`
- Type: object
- No Additional Properties
####### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NFS share.

####### path (required)

- Schema name: `Path`
- Type: string

Local path to be exported.
- Must be at least `1` characters long

####### dataset (required)

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/share'). Null if path cannot be resolved.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### relative_path (required)

- Schema name: `Relative Path`

Relative path component within the dataset (e.g., 'subdir/data'). Null if path cannot be resolved.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### aliases

- Schema name: `Aliases`
- Type: array of string
- Default: []

IGNORED for now.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### comment

- Schema name: `Comment`
- Type: string
- Default: ""

User comment associated with share.

####### networks

- Schema name: `Networks`
- Type: array of string
- Default: []

List of authorized networks that are allowed to access the share having format "network/mask" CIDR notation. Each entry must be unique. If empty, all networks are allowed. Excessively long lists should be avoided.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### hosts

- Schema name: `Hosts`
- Type: array of string
- Default: []

List of IP's/hostnames which are allowed to access the share. No quotes or spaces are allowed. Each entry must be unique. If empty, all IP's/hostnames are allowed. Excessively long lists should be avoided.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Export the share as read only.

####### maproot_user

- Schema name: `Maproot User`
- Default: null

Map root user client to a specified user.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### maproot_group

- Schema name: `Maproot Group`
- Default: null

Map root group client to a specified group.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### mapall_user

- Schema name: `Mapall User`
- Default: null

Map all client users to a specified user.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### mapall_group

- Schema name: `Mapall Group`
- Default: null

Map all client groups to a specified group.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### security

- Schema name: `Security`
- Type: array of enum (of string)
- Default: []

Specify the security schema.
- No Additional Items

######## Each item of this array must be:

- Type: enum (of string)

####### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Enable or disable the share.

####### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
######## Any of

######### Option 1

- Type: boolean

######### Option 2

- Type: null

####### expose_snapshots

- Schema name: `Expose Snapshots`
- Type: boolean
- Default: false

Enterprise feature to enable access to the ZFS snapshot directory for the export. Export path must be the root directory of a ZFS dataset.

####### tier

- Default: null

Storage tier in which the share's underlying dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
######## Any of

######### TierInfo

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
########## tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.

########## tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
########### Any of

############ ZfsTierRewriteJobEntry

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
############# tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

############# dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

############# job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

############# status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.

############ Option 2

- Type: null

######### Option 2

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

######### ZfsTierRewriteJobEntry

- Type: null

######### Option 2

- Type: null

##### SharingNFSEntry

- Type: string

##### Option 3

- Type: null

##### Option 4

- Type: string

##### Option 5

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: boolean

##### Option 2

- Type: null

##### Option 1

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.

###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
####### Any of

######## ZfsTierRewriteJobEntry

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
######### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

######### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

######### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

######### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.

######## Option 2

- Type: null

##### Option 2

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

###### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.

##### Option 1

- Type: null

##### Option 2

- Type: null

##### TierInfo

- Schema name: `SharingNFSEntry`
- Type: object
- No Additional Properties
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NFS share.

###### path (required)

- Schema name: `Path`
- Type: string

Local path to be exported.
- Must be at least `1` characters long

###### dataset (required)

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/share'). Null if path cannot be resolved.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### relative_path (required)

- Schema name: `Relative Path`

Relative path component within the dataset (e.g., 'subdir/data'). Null if path cannot be resolved.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### aliases

- Schema name: `Aliases`
- Type: array of string
- Default: []

IGNORED for now.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### comment

- Schema name: `Comment`
- Type: string
- Default: ""

User comment associated with share.

###### networks

- Schema name: `Networks`
- Type: array of string
- Default: []

List of authorized networks that are allowed to access the share having format "network/mask" CIDR notation. Each entry must be unique. If empty, all networks are allowed. Excessively long lists should be avoided.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### hosts

- Schema name: `Hosts`
- Type: array of string
- Default: []

List of IP's/hostnames which are allowed to access the share. No quotes or spaces are allowed. Each entry must be unique. If empty, all IP's/hostnames are allowed. Excessively long lists should be avoided.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Export the share as read only.

###### maproot_user

- Schema name: `Maproot User`
- Default: null

Map root user client to a specified user.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### maproot_group

- Schema name: `Maproot Group`
- Default: null

Map root group client to a specified group.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### mapall_user

- Schema name: `Mapall User`
- Default: null

Map all client users to a specified user.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### mapall_group

- Schema name: `Mapall Group`
- Default: null

Map all client groups to a specified group.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### security

- Schema name: `Security`
- Type: array of enum (of string)
- Default: []

Specify the security schema.
- No Additional Items

####### Each item of this array must be:

- Type: enum (of string)

###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Enable or disable the share.

###### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### expose_snapshots

- Schema name: `Expose Snapshots`
- Type: boolean
- Default: false

Enterprise feature to enable access to the ZFS snapshot directory for the export. Export path must be the root directory of a ZFS dataset.

###### tier

- Default: null

Storage tier in which the share's underlying dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

##### Option 2

- Type: string

##### ZfsTierRewriteJobEntry

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: boolean

##### Option 1

- Type: null

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: array of object
- No Additional Items

###### Each item of this array must be:

- Type: object

##### Option 1

- Type: object

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
