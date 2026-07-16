---
title: virt.volume.get_instance
kind: method
source_rst: _sources/api_methods_virt.volume.get_instance.rst.txt
source_html: api_methods_virt.volume.get_instance.html
required_roles:
  - VIRT_IMAGE_READ
---

# virt.volume.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `VIRT_IMAGE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

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

- Schema name: `VirtVolumeEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the virtualization volume.
- Must be at least `1` characters long

#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name of the virtualization volume.
- Must be at least `1` characters long

#### storage_pool (required)

- Schema name: `Storage Pool`
- Type: string

Name of the storage pool containing this volume.
- Must be at least `1` characters long

#### content_type (required)

- Schema name: `Content Type`
- Type: string

Type of content stored in this volume (e.g., 'BLOCK', 'ISO').
- Must be at least `1` characters long

#### created_at (required)

- Schema name: `Created At`
- Type: string

Timestamp when this volume was created.

#### type (required)

- Schema name: `Type`
- Type: string

Volume type indicating its storage backend and characteristics.
- Must be at least `1` characters long

#### config (required)

- Schema name: `Config`
- Type: object

Object containing detailed configuration parameters for this volume.

#### used_by (required)

- Schema name: `Used By`
- Type: array of string

Array of virtual instance names currently using this volume.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
