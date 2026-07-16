---
title: pool.scrub.get_instance
kind: method
source_rst: _sources/api_methods_pool.scrub.get_instance.rst.txt
source_html: api_methods_pool.scrub.get_instance.html
required_roles:
  - POOL_SCRUB_READ
---

# pool.scrub.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `POOL_SCRUB_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
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

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `PoolScrubEntry`
- Type: object
- No Additional Properties
#### pool (required)

- Schema name: `Pool`
- Type: integer

ID of the pool to scrub.
- Value must be strictly greater than `0`

#### threshold

- Schema name: `Threshold`
- Type: integer
- Default: 35

Days before a scrub is due when a scrub should automatically start.
- Value must be greater or equal to `0`

#### description

- Schema name: `Description`
- Type: string
- Default: ""

Description or notes for this scrub schedule.

#### schedule

- Schema name: `PoolScrubCron`
- Type: object

Cron schedule for when scrubs should run.
- No Additional Properties
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the scrub should run (cron format).

##### hour

- Schema name: `Hour`
- Type: string
- Default: "00"

Hour when the scrub should run (cron format).

##### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

##### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

##### dow

- Schema name: `Dow`
- Type: string
- Default: "7"

Day of week when the scrub should run (cron format, 7=Sunday).

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this scrub schedule is enabled.

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the scrub schedule.

#### pool_name (required)

- Schema name: `Pool Name`
- Type: string

Name of the pool being scrubbed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
