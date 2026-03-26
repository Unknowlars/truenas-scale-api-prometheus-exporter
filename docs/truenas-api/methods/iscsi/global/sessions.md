---
title: iscsi.global.sessions
kind: method
source_rst: _sources/api_methods_iscsi.global.sessions.rst.txt
source_html: api_methods_iscsi.global.sessions.html
required_roles:
  - SHARING_ISCSI_GLOBAL_READ
---

# iscsi.global.sessions

## Summary

Get a list of currently running iSCSI sessions. This includes initiator and target names and the unique connection IDs.

## Required Roles

- `SHARING_ISCSI_GLOBAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: query_filters

#### query_filters

- Schema name: `query_filters`
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
                [
                    "name",
                    "=",
                    "bob"
                ]
            ],
            [
                [
                    "name",
                    "=",
                    "larry"
                ]
            ]
        ]
    ]
]
```

#### Parameter 2: query_options

#### query_options

- Schema name: `query_options`
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

Query options for sorting and pagination.
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

- Schema name: `Result`
- Type: array of object

Array of active iSCSI sessions.
- No Additional Items

#### Each item of this array must be:

#### IscsiSession

- Schema name: `IscsiSession`
- Type: object
- No Additional Properties
##### initiator (required)

- Schema name: `Initiator`
- Type: string

iSCSI Qualified Name (IQN) of the initiator.

##### initiator_addr (required)

- Schema name: `Initiator Addr`
- Type: string

IP address of the initiator.

##### initiator_alias (required)

- Schema name: `Initiator Alias`

Alias name of the initiator or `null` if not set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### target (required)

- Schema name: `Target`
- Type: string

iSCSI Qualified Name (IQN) of the target.

##### target_alias (required)

- Schema name: `Target Alias`
- Type: string

Alias name of the target.

##### header_digest (required)

- Schema name: `Header Digest`

Header digest algorithm used for the session or `null`.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### data_digest (required)

- Schema name: `Data Digest`

Data digest algorithm used for the session or `null`.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### max_data_segment_length (required)

- Schema name: `Max Data Segment Length`

Maximum data segment length for the session or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### max_receive_data_segment_length (required)

- Schema name: `Max Receive Data Segment Length`

Maximum receive data segment length or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### max_xmit_data_segment_length (required)

- Schema name: `Max Xmit Data Segment Length`

Maximum transmit data segment length or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### max_burst_length (required)

- Schema name: `Max Burst Length`

Maximum burst length for the session or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### first_burst_length (required)

- Schema name: `First Burst Length`

First burst length for the session or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### immediate_data (required)

- Schema name: `Immediate Data`
- Type: boolean

Whether immediate data transfer is enabled.

##### iser (required)

- Schema name: `Iser`
- Type: boolean

Whether this session is using iSER (iSCSI Extensions for RDMA).

##### offload (required)

- Schema name: `Offload`
- Type: boolean

Whether hardware offload is enabled for this session.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
