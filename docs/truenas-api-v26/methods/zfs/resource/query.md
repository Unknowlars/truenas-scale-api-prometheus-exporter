---
title: zfs.resource.query
kind: method
source_rst: _sources/api_methods_zfs.resource.query.rst.txt
source_html: api_methods_zfs.resource.query.html
required_roles:
  - ZFS_RESOURCE_READ
---

# zfs.resource.query

## Summary

Query ZFS resources (datasets and volumes) with flexible filtering options.

This method provides a high-performance interface for retrieving information about ZFS resources, including their properties, hierarchical relationships, and metadata. The query can be customized to retrieve specific resources, properties, and control the output format.

To query snapshots, use :doc:`zfs.resource.snapshot.query <api_methods_zfs.resource.snapshot.query>` instead.

Invalid input is returned to the client as a JSON-RPC `error` response (code `-32602`, *Invalid params*); each failing condition appears in the error's `data.extra` array with its own `errno`. A validation error is raised when:

- a snapshot path is supplied (use :doc:`zfs.resource.snapshot.query <api_methods_zfs.resource.snapshot.query>`)

- overlapping paths are supplied with `get_children` enabled

- a requested path does not exist (`ENOENT`)

Examples:

Query all resources with default properties:

.. code:: json

{}

Query specific resources:

.. code:: json

{"paths": ["tank/documents", "tank/media"]}

Query specific properties with children:

.. code:: json

{"paths": ["tank"], "properties": ["mounted", "compression", "used"], "get_children": true}

Get a hierarchical view of resources:

.. code:: json

{"paths": ["tank"], "nest_results": true, "get_children": true}

## Required Roles

- `ZFS_RESOURCE_READ`

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
- Default:
```json
{
  "paths": [],
  "properties": [],
  "get_user_properties": false,
  "get_source": false,
  "nest_results": false,
  "get_children": false,
  "max_depth": 0,
  "exclude_internal_paths": true,
  "get_tier": false
}
```

Query parameters for retrieving ZFS resource information.
- No Additional Properties
##### paths

- Schema name: `Paths`
- Type: array of string
- Default: []

A list of zfs filesystem or volume paths to be queried. In almost all scenarios, you should provide a path of what you want to query. By providing path(s) here, it allows the API to apply optimizations so that the requested information is retrieved as efficiently and quickly as possible. Example 1: {"paths": ["tank/foo"]} will query the relevant information for this resource only. Example 2: {"paths": ["tank/foo", "dozer/test"]} will query the relevant information for these resources only. NOTE: paths must be non-overlapping if `get_children` is True. (i.e. this won't work and will raise a validation error) { "paths": ["tank/foo1", "tank/foo1/foo2"], "get_children": True }
- All items must be unique
- No Additional Items

###### Each item of this array must be:

- Type: string

##### properties

- Schema name: `Properties`
- Default: []

A list of zfs properties to be retrieved. Defaults to an empty list which will return a default set of zfs properties. Setting this to None will retrieve no zfs properties.
###### Any of

####### Option 1

- Type: array of string
- No Additional Items

######## Each item of this array must be:

- Type: string

####### Option 2

- Type: null

##### get_user_properties

- Schema name: `Get User Properties`
- Type: boolean
- Default: false

Retrieve user properties for zfs resource(s).

##### get_source

- Schema name: `Get Source`
- Type: boolean
- Default: false

Retrieve source information for a zfs property.

##### nest_results

- Schema name: `Nest Results`
- Type: boolean
- Default: false

Return a nested object that associates all children to their respective parents in the filesystem. By default, each zfs resource is returned as a separate item in the array and is not associated to its parent.

##### get_children

- Schema name: `Get Children`
- Type: boolean
- Default: false

Retrieve children information for the zfs resource.

##### max_depth

- Schema name: `Max Depth`
- Type: integer
- Default: 0

Maximum depth to recurse when retrieving children. A value of 0 means unlimited recursion (default behavior). A value greater than 0 limits the recursion to that many levels deep. When max*depth > 0, get*children is automatically enabled if not already set. Examples: max*depth=0: Retrieve all descendants (unlimited depth). max*depth=1: Retrieve only immediate children. max*depth=2: Retrieve children and grandchildren. max*depth=3: Retrieve up to great-grandchildren. Note: When max*depth > 0 is specified, it takes priority over get*children. The depth is measured from the specified path(s), not from the pool root.

##### get_tier

- Schema name: `Get Tier`
- Type: boolean
- Default: false

Retrieve tier classification (REGULAR/PERFORMANCE) for FILESYSTEM resources. Requires an active Enterprise license with ZFS tiering enabled.

### Return value

- Schema name: `Result`
- Type: array of object
- No Additional Items

#### Each item of this array must be:

#### ZFSResourceEntry

- Schema name: `ZFSResourceEntry`
- Type: object
- No Additional Properties
##### createtxg (required)

- Schema name: `Createtxg`
- Type: integer

Transaction group when resource was created.

##### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for the resource.

##### name (required)

- Schema name: `Name`
- Type: string

The name of the zfs resource.

##### pool (required)

- Schema name: `Pool`
- Type: string

The name of the zpool that the zfs resouce is associated to.

##### properties (required)

The zfs properties for the resource.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

##### type (required)

- Schema name: `Type`
- Type: enum (of string)

The type of ZFS resource.

##### user_properties (required)

- Schema name: `User Properties`

Custom metadata properties with colon-separated names (max 256 chars).
###### Any of

####### Option 1

- Type: object
######## Additional Properties

Each additional property must conform to the following schema
- Type: string

####### Option 2

- Type: null

##### children (required)

- Schema name: `Children`

The children of this zfs resource.
###### Any of

####### Option 1

- Type: array
- No Additional Items

######## Each item of this array must be:

- Type: object

####### Option 2

- Type: null

##### tier

- Default: null

Tier classification for FILESYSTEM resources. None if not requested or not applicable.
###### Any of

####### TierInfo

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
######## tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.

######## tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
######### Any of

########## ZfsTierRewriteJobEntry

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
########### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

########### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

########### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

########### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.

########## Option 2

- Type: null

####### Option 2

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
######## tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

######## dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

######## job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

######## status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.

####### ZfsTierRewriteJobEntry

- Type: null

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
