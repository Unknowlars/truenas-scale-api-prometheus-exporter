---
title: zfs.tier.rewrite_job_failures
kind: method
source_rst: _sources/api_methods_zfs.tier.rewrite_job_failures.rst.txt
source_html: api_methods_zfs.tier.rewrite_job_failures.html
required_roles:
  - DATASET_READ
---

# zfs.tier.rewrite_job_failures

## Summary

List files that failed to be rewritten during a rewrite job.

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: zfs_tier_rewrite_job_failures

#### zfs_tier_rewrite_job_failures

- Schema name: `zfs_tier_rewrite_job_failures`
- Type: object

ZfsTierRewriteJobFailuresArgs parameters.
- No Additional Properties
##### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job to query, in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

##### query-filters

- Schema name: `Query-Filters`
- Type: array
- Default: []

Additional filters to apply to the results.
- No Additional Items

###### Each item of this array must be:

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

##### query-options

- Schema name: `QueryOptions`
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

Options controlling sort order, pagination, and result format.
- No Additional Properties
###### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

###### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

####### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

###### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

####### Each item of this array must be:

######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: array
- No Additional Items

########## Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

###### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

###### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

###### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

###### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

###### force_sql_filters

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

###### ZfsTierRewriteJobFailureEntry

- Schema name: `ZfsTierRewriteJobFailureEntry`
- Type: object
- No Additional Properties
####### filename (required)

- Schema name: `Filename`
- Type: string

Name of the file that failed to migrate storage tier.

####### error (required)

- Schema name: `ZfsTierRewriteJobFailureError`
- Type: object

Error details for the failed storage tier migration.
- No Additional Properties
######## errno (required)

- Schema name: `Errno`
- Type: integer

Error number from the failed storage tier migration.

######## strerror (required)

- Schema name: `Strerror`
- Type: string

Human-readable description of the error.

####### path (required)

- Schema name: `Path`

Absolute path of the file resolved via its file handle, or `null` if the file no longer exists on the filesystem.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

##### ZfsTierRewriteJobFailureEntry

- Type: string

##### Option 3

- Type: null

##### Option 4

- Schema name: `ZfsTierRewriteJobFailureEntry`
- Type: object
- No Additional Properties
###### filename (required)

- Schema name: `Filename`
- Type: string

Name of the file that failed to migrate storage tier.

###### error (required)

- Type: object

Error details for the failed storage tier migration.

###### path (required)

- Schema name: `Path`

Absolute path of the file resolved via its file handle, or `null` if the file no longer exists on the filesystem.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### Option 5

- Type: string

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
