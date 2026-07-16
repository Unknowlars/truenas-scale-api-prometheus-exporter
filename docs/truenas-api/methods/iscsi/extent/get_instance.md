---
title: iscsi.extent.get_instance
kind: method
source_rst: _sources/api_methods_iscsi.extent.get_instance.rst.txt
source_html: api_methods_iscsi.extent.get_instance.html
required_roles:
  - SHARING_ISCSI_EXTENT_READ
---

# iscsi.extent.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `SHARING_ISCSI_EXTENT_READ`

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

- Schema name: `IscsiExtentEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI extent.

#### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI extent.
- Must be at least `1` characters long
- Must be at most `64` characters long

#### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "DISK"

Type of the extent storage backend.

#### disk

- Schema name: `Disk`
- Default: null

Disk device to use for the extent or `null` if using a file.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### serial

- Schema name: `Serial`
- Default: null

Serial number for the extent or `null` to auto-generate.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### path

- Schema name: `Path`
- Default: null

File path for file-based extents or `null` if using a disk.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### filesize

- Schema name: `Filesize`
- Default: "0"

Size of the file-based extent in bytes.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: integer

#### blocksize

- Schema name: `Blocksize`
- Type: enum (of integer)
- Default: 512

Block size for the extent in bytes.

#### pblocksize

- Schema name: `Pblocksize`
- Type: boolean
- Default: false

Whether to use physical block size reporting.

#### avail_threshold

- Schema name: `Avail Threshold`
- Default: null

Available space threshold percentage or `null` to disable.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `99`

###### Option 2

- Type: null

#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the extent.

#### naa (required)

- Schema name: `Naa`
- Type: string

Network Address Authority (NAA) identifier for the extent.
- Must be at most `34` characters long

#### insecure_tpc

- Schema name: `Insecure Tpc`
- Type: boolean
- Default: true

Whether to enable insecure Third Party Copy (TPC) operations.

#### xen

- Schema name: `Xen`
- Type: boolean
- Default: false

Whether to enable Xen compatibility mode.

#### rpm

- Schema name: `Rpm`
- Type: enum (of string)
- Default: "SSD"

Reported RPM type for the extent.

#### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Whether the extent is read-only.

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the extent is enabled and available for use.

#### vendor (required)

- Schema name: `Vendor`
- Type: string

Vendor string reported by the extent.

#### product_id

- Schema name: `Product Id`
- Default: null

Product ID string for the extent or `null` for default.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long
- Must be at most `16` characters long

###### Option 2

- Type: null

#### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the iscsi extent is located on a locked dataset. `true`: The extent is in a locked dataset. `false`: The extent is not in a locked dataset. `null`: Lock status is not available because path locking information was not requested.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
