---
title: iscsi.auth.query
kind: method
source_rst: _sources/api_methods_iscsi.auth.query.rst.txt
source_html: api_methods_iscsi.auth.query.html
required_roles:
  - SHARING_ISCSI_AUTH_READ
---

# iscsi.auth.query

## Required Roles

- `SHARING_ISCSI_AUTH_READ`

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
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### IscsiAuthQueryResultItem

- Schema name: `IscsiAuthQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI authentication credential.

####### tag

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this credential with iSCSI targets.

####### user

- Schema name: `User`
- Type: string

Username for iSCSI CHAP authentication.

####### secret

- Schema name: `Secret`
- Type: string

Password/secret for iSCSI CHAP authentication.

####### peeruser

- Schema name: `Peeruser`
- Type: string

Username for mutual CHAP authentication or empty string if not configured.

####### peersecret

- Schema name: `Peersecret`
- Type: string

Password/secret for mutual CHAP authentication or empty string if not configured.

####### discovery_auth

- Schema name: `Discovery Auth`
- Type: enum (of string)

Authentication method for target discovery. If "CHAP_MUTUAL" is selected for target discovery, it is only permitted for a single entry systemwide.

##### IscsiAuthQueryResultItem

- Schema name: `IscsiAuthQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI authentication credential.

###### tag

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this credential with iSCSI targets.

###### user

- Schema name: `User`
- Type: string

Username for iSCSI CHAP authentication.

###### secret

- Schema name: `Secret`
- Type: string

Password/secret for iSCSI CHAP authentication.

###### peeruser

- Schema name: `Peeruser`
- Type: string

Username for mutual CHAP authentication or empty string if not configured.

###### peersecret

- Schema name: `Peersecret`
- Type: string

Password/secret for mutual CHAP authentication or empty string if not configured.

###### discovery_auth

- Schema name: `Discovery Auth`
- Type: enum (of string)

Authentication method for target discovery. If "CHAP_MUTUAL" is selected for target discovery, it is only permitted for a single entry systemwide.

##### Option 3

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
