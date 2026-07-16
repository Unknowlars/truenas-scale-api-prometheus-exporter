---
title: api_key.query
kind: method
source_rst: _sources/api_methods_api_key.query.rst.txt
source_html: api_methods_api_key.query.html
required_roles:
  - API_KEY_READ
---

# api_key.query

## Required Roles

- `API_KEY_READ`

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

###### ApiKeyEntry

- Schema name: `ApiKeyEntry`
- Type: object
- No Additional Properties
####### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

####### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the API key.
- Must be at least `1` characters long
- Must be at most `200` characters long

####### username (required)

- Schema name: `Username`

Username associated with the API key or `null` for system keys.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: string
- Must be at least `1` characters long

######### Option 3

- Type: null

####### user_identifier (required)

- Schema name: `User Identifier`

User ID (numeric) or SID (string) that owns this API key.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: string

####### iterations (required)

- Schema name: `Iterations`
- Type: integer

Number of iterations of PBKDF2-SHA512.

####### salt (required)

- Schema name: `Salt`
- Type: string

Base64 encoded salt for API key.

####### stored_key (required)

- Schema name: `Stored Key`
- Type: string

SCRAM StoredKey for API key.

####### server_key (required)

- Schema name: `Server Key`
- Type: string

SCRAM ServerKey for API key.

####### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the API key was created.

####### expires_at

- Schema name: `Expires At`
- Default: null

Expiration timestamp for the API key or `null` for no expiration.
######## Any of

######### Option 1

- Type: string
- Type: Format: date-time

######### Option 2

- Type: null

####### local (required)

- Schema name: `Local`
- Type: boolean

Whether this API key is for local system use only.

####### revoked (required)

- Schema name: `Revoked`
- Type: boolean

Whether the API key has been revoked and is no longer valid.

####### revoked_reason (required)

- Schema name: `Revoked Reason`

Reason for API key revocation or `null` if not revoked.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

##### ApiKeyEntry

- Type: string

##### Option 3

- Type: string
- Must be at least `1` characters long

##### Option 4

- Type: null

##### Option 5

- Type: integer

##### Option 1

- Type: string

##### Option 2

- Type: string
- Type: Format: date-time

##### Option 3

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Schema name: `ApiKeyEntry`
- Type: object
- No Additional Properties
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

###### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the API key.
- Must be at least `1` characters long
- Must be at most `200` characters long

###### username (required)

- Schema name: `Username`

Username associated with the API key or `null` for system keys.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: string
- Must be at least `1` characters long

######## Option 3

- Type: null

###### user_identifier (required)

- Schema name: `User Identifier`

User ID (numeric) or SID (string) that owns this API key.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: string

###### iterations (required)

- Schema name: `Iterations`
- Type: integer

Number of iterations of PBKDF2-SHA512.

###### salt (required)

- Schema name: `Salt`
- Type: string

Base64 encoded salt for API key.

###### stored_key (required)

- Schema name: `Stored Key`
- Type: string

SCRAM StoredKey for API key.

###### server_key (required)

- Schema name: `Server Key`
- Type: string

SCRAM ServerKey for API key.

###### created_at (required)

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the API key was created.

###### expires_at

- Schema name: `Expires At`
- Default: null

Expiration timestamp for the API key or `null` for no expiration.
####### Any of

######## Option 1

- Type: string
- Type: Format: date-time

######## Option 2

- Type: null

###### local (required)

- Schema name: `Local`
- Type: boolean

Whether this API key is for local system use only.

###### revoked (required)

- Schema name: `Revoked`
- Type: boolean

Whether the API key has been revoked and is no longer valid.

###### revoked_reason (required)

- Schema name: `Revoked Reason`

Reason for API key revocation or `null` if not revoked.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: string

##### Option 3

- Type: string
- Type: Format: date-time

##### Option 1

- Type: null

##### Option 2

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

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
