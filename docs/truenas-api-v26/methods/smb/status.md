---
title: smb.status
kind: method
source_rst: _sources/api_methods_smb.status.rst.txt
source_html: api_methods_smb.status.html
required_roles:
  - SHARING_SMB_READ
---

# smb.status

## Summary

Returns SMB server status (sessions, open files, locks, notifications).

## Required Roles

- `SHARING_SMB_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: info_level

#### info_level

- Schema name: `info_level`
- Type: enum (of string)
- Default: "ALL"

Type of information requests. Defaults to "ALL".

#### Parameter 2: filters

#### filters

- Schema name: `filters`
- Type: array
- Default: []

Query filters to apply to the status results.
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

#### Parameter 3: options

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

Query options for controlling result pagination and ordering.
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

#### Parameter 4: status_options

#### status_options

- Schema name: `status_options`
- Type: object
- Default:
```json
{
  "verbose": true,
  "fast": false,
  "restrict_user": "",
  "restrict_session": "",
  "resolve_uids": true
}
```

Additional options for retrieving and formatting SMB status information.
- No Additional Properties
##### verbose

- Schema name: `Verbose`
- Type: boolean
- Default: true

Return verbose status output.

##### fast

- Schema name: `Fast`
- Type: boolean
- Default: false

Do not check if the status data is valid by checking if the processes that the status data refer to all still exist. This option decreases execution time on busy systems and clusters but may display stale data of processes that died without cleaning up properly.

##### restrict_user

- Schema name: `Restrict User`
- Type: string
- Default: ""

Limit results to the specified user.

##### restrict_session

- Schema name: `Restrict Session`
- Type: string
- Default: ""

Limit results to the specified SMB session ID.

##### resolve_uids

- Schema name: `Resolve Uids`
- Type: boolean
- Default: true

Resolve Unix user IDs and group IDs to usernames and group names in the status output.

### Return value

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

- Type: object

##### Option 2

- Type: object

##### Option 3

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
