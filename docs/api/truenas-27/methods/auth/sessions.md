---
title: auth.sessions
kind: method
source_rst: _sources/api_methods_auth.sessions.rst.txt
source_html: api_methods_auth.sessions.html
required_roles:
  - AUTH_SESSIONS_READ
---

# auth.sessions

## Summary

Returns list of active auth sessions.

Example of return value:

[ { "id": "NyhB1J5vjPjIV82yZ6caU12HLA1boDJcZNWuVQM4hQWuiyUWMGZTz2ElDp7Yk87d", "origin": "192.168.0.3:40392", "credentials": "LOGIN_PASSWORD", "credentials_data": {"username": "root"}, "current": True, "internal": False, "created_at": {"$date": 1545842426070} } ]

`credentials` can be `UNIX_SOCKET`, `ROOT_TCP_SOCKET`, `LOGIN_PASSWORD`, `API_KEY` or `TOKEN`, depending on what authentication method was used. For `UNIX_SOCKET` and `LOGIN_PASSWORD` logged-in `username` field will be provided in `credentials_data`. For `API_KEY` corresponding `api_key` will be provided in `credentials_data`. For `TOKEN` its `parent` credential will be provided in `credentials_data`.

If you want to exclude all internal connections from the list, call this method with following arguments:

[ [ ["internal", "=", True] ] ]

## Required Roles

- `AUTH_SESSIONS_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
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

<a id="Call_parameters_items_i1"></a>
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
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### AuthSessionsQueryResultItem

- Schema name: `AuthSessionsQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: string

Unique identifier for the authentication session.

<a id="headingReturn_value_anyOf_i0_items_current"></a>
<a id="Return_value_anyOf_i0_items_current"></a>
###### current

- Schema name: `Current`
- Type: boolean

Whether this is the current active session.

<a id="headingReturn_value_anyOf_i0_items_internal"></a>
<a id="Return_value_anyOf_i0_items_internal"></a>
###### internal

- Schema name: `Internal`
- Type: boolean

Whether this is an internal system session.

<a id="headingReturn_value_anyOf_i0_items_origin"></a>
<a id="Return_value_anyOf_i0_items_origin"></a>
###### origin

- Schema name: `Origin`
- Type: string

Origin information for the session (IP address, hostname, etc.).

<a id="headingReturn_value_anyOf_i0_items_credentials"></a>
<a id="Return_value_anyOf_i0_items_credentials"></a>
###### credentials

- Schema name: `Credentials`
- Type: enum (of string)

Authentication method used for this session. `UNIX_SOCKET`: Local Unix domain socket authentication `LOGIN_PASSWORD`: Username and password authentication `LOGIN_TWOFACTOR`: Two-factor authentication login `LOGIN_ONETIME_PASSWORD`: One-time password authentication `API_KEY`: API key authentication `TOKEN`: Token-based authentication `TRUENAS_NODE`: TrueNAS cluster node authentication
###### Must be one of:

- "UNIX_SOCKET"
- "LOGIN_PASSWORD"
- "LOGIN_TWOFACTOR"
- "LOGIN_ONETIME_PASSWORD"
- "API_KEY"
- "TOKEN"
- "TRUENAS_NODE"

<a id="headingReturn_value_anyOf_i0_items_credentials_data"></a>
<a id="Return_value_anyOf_i0_items_credentials_data"></a>
###### credentials_data

- Schema name: `Credentials Data`

Detailed credential information specific to the authentication method.
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i0"></a>
###### [BaseCredentialData](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i0)

- Schema name: `BaseCredentialData`
- Type: object

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i1"></a>
###### [UserCredentialData](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i1)

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i1_username"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i1_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i1_login_id"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i1_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i1_login_at"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i1_login_at"></a>
###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i2"></a>
###### [APIKeyCredentialData](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i2)

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i2_username"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i2_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i2_login_id"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i2_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i2_login_at"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i2_login_at"></a>
###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i2_api_key"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i2_api_key"></a>
###### api_key (required)

- Schema name: `APIKeySessionData`
- Type: object

API key information used for authentication.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i2_api_key_id"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i2_api_key_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i2_api_key_name"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i2_api_key_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human-readable name of the API key.

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3"></a>
###### [TokenCredentialData](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3)

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent"></a>
###### parent (required)

- Schema name: `TokenParentCredentialsData`
- Type: object

Parent credential information that generated this token.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials"></a>
###### credentials (required)

- Schema name: `Credentials`
- Type: enum (of string)

Type of credentials used to generate this token.
###### Must be one of:

- "UNIX_SOCKET"
- "LOGIN_PASSWORD"
- "LOGIN_TWOFACTOR"
- "API_KEY"
- "TOKEN"
- "TRUENAS_NODE"

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data"></a>
###### credentials_data (required)

- Schema name: `Credentials Data`

Credential data used to authenticate the token request.
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i0"></a>
###### [BaseCredentialData](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i0)

- Schema name: `BaseCredentialData`
- Type: object

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1"></a>
###### [UserCredentialData](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1)

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_username"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_login_id"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_login_at"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i1_login_at"></a>
###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2"></a>
###### [APIKeyCredentialData](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2)

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_username"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_login_id"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_login_at"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_login_at"></a>
###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_api_key"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i2_api_key"></a>
###### api_key (required)

- Type: object

API key information used for authentication.

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3"></a>
###### [TokenCredentialData](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3)

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_parent"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_parent"></a>
###### parent (required)

- Type: object

Parent credential information that generated this token.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_login_id"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username"></a>
###### username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_parent_credentials_data_anyOf_i3_username_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_login_id"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_login_id"></a>
###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

<a id="headingReturn_value_anyOf_i0_items_credentials_data_anyOf_i3_username"></a>
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_username"></a>
###### username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
<a id="Return_value_anyOf_i0_items_credentials_data_anyOf_i3_username_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_username_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_username_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_username_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_credentials_data_anyOf_i3_username_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_created_at"></a>
<a id="Return_value_anyOf_i0_items_created_at"></a>
###### created_at

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the session was created.

<a id="headingReturn_value_anyOf_i0_items_secure_transport"></a>
<a id="Return_value_anyOf_i0_items_secure_transport"></a>
###### secure_transport

- Schema name: `Secure Transport`
- Type: boolean

Whether the session was established over a secure transport (HTTPS/WSS).

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [AuthSessionsQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `AuthSessionsQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: string

Unique identifier for the authentication session.

<a id="headingReturn_value_anyOf_i1_current"></a>
<a id="Return_value_anyOf_i1_current"></a>
###### current

- Schema name: `Current`
- Type: boolean

Whether this is the current active session.

<a id="headingReturn_value_anyOf_i1_internal"></a>
<a id="Return_value_anyOf_i1_internal"></a>
###### internal

- Schema name: `Internal`
- Type: boolean

Whether this is an internal system session.

<a id="headingReturn_value_anyOf_i1_origin"></a>
<a id="Return_value_anyOf_i1_origin"></a>
###### origin

- Schema name: `Origin`
- Type: string

Origin information for the session (IP address, hostname, etc.).

<a id="headingReturn_value_anyOf_i1_credentials"></a>
<a id="Return_value_anyOf_i1_credentials"></a>
###### credentials

- Schema name: `Credentials`
- Type: enum (of string)

Authentication method used for this session. `UNIX_SOCKET`: Local Unix domain socket authentication `LOGIN_PASSWORD`: Username and password authentication `LOGIN_TWOFACTOR`: Two-factor authentication login `LOGIN_ONETIME_PASSWORD`: One-time password authentication `API_KEY`: API key authentication `TOKEN`: Token-based authentication `TRUENAS_NODE`: TrueNAS cluster node authentication
###### Must be one of:

- "UNIX_SOCKET"
- "LOGIN_PASSWORD"
- "LOGIN_TWOFACTOR"
- "LOGIN_ONETIME_PASSWORD"
- "API_KEY"
- "TOKEN"
- "TRUENAS_NODE"

<a id="headingReturn_value_anyOf_i1_credentials_data"></a>
<a id="Return_value_anyOf_i1_credentials_data"></a>
###### credentials_data

- Schema name: `Credentials Data`

Detailed credential information specific to the authentication method.
<a id="Return_value_anyOf_i1_credentials_data_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_credentials_data_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_credentials_data_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_credentials_data_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_credentials_data_anyOf_i1)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_credentials_data_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i1_credentials_data_anyOf_i2)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_credentials_data_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_anyOf_i1_credentials_data_anyOf_i3)

- Type: object

<a id="headingReturn_value_anyOf_i1_created_at"></a>
<a id="Return_value_anyOf_i1_created_at"></a>
###### created_at

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the session was created.

<a id="headingReturn_value_anyOf_i1_secure_transport"></a>
<a id="Return_value_anyOf_i1_secure_transport"></a>
###### secure_transport

- Schema name: `Secure Transport`
- Type: boolean

Whether the session was established over a secure transport (HTTPS/WSS).

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
