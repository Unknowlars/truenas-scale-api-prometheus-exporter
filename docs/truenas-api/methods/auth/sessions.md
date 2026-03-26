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

###### AuthSessionsQueryResultItem

- Schema name: `AuthSessionsQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: string

Unique identifier for the authentication session.

####### current

- Schema name: `Current`
- Type: boolean

Whether this is the current active session.

####### internal

- Schema name: `Internal`
- Type: boolean

Whether this is an internal system session.

####### origin

- Schema name: `Origin`
- Type: string

Origin information for the session (IP address, hostname, etc.).

####### credentials

- Schema name: `Credentials`
- Type: enum (of string)

Authentication method used for this session. `UNIX_SOCKET`: Local Unix domain socket authentication `LOGIN_PASSWORD`: Username and password authentication `LOGIN_TWOFACTOR`: Two-factor authentication login `LOGIN_ONETIME_PASSWORD`: One-time password authentication `API_KEY`: API key authentication `TOKEN`: Token-based authentication `TRUENAS_NODE`: TrueNAS cluster node authentication

####### credentials_data

- Schema name: `Credentials Data`

Detailed credential information specific to the authentication method.
######## Any of

######### BaseCredentialData

- Schema name: `BaseCredentialData`
- Type: object

######### UserCredentialData

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
########## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

########## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

########## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

######### APIKeyCredentialData

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
########## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

########## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

########## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

########## api_key (required)

- Schema name: `APIKeySessionData`
- Type: object

API key information used for authentication.
- No Additional Properties
########### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

########### name (required)

- Schema name: `Name`
- Type: string

Human-readable name of the API key.

######### TokenCredentialData

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
########## parent (required)

- Schema name: `TokenParentCredentialsData`
- Type: object

Parent credential information that generated this token.
- No Additional Properties
########### credentials (required)

- Schema name: `Credentials`
- Type: enum (of string)

Type of credentials used to generate this token.

########### credentials_data (required)

- Schema name: `Credentials Data`

Credential data used to authenticate the token request.
############ Any of

############# BaseCredentialData

- Schema name: `BaseCredentialData`
- Type: object

############# UserCredentialData

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
############## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

############## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

############## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

############# APIKeyCredentialData

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
############## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

############## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

############## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

############## api_key (required)

- Type: object

API key information used for authentication.

############# TokenCredentialData

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
############## parent (required)

- Type: object

Parent credential information that generated this token.

############## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

############## username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
############### Any of

################ Option 1

- Type: string

################ Option 2

- Type: null

############# Option 1

- Type: string

############# Option 2

- Type: null

########## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

########## username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
########### Any of

############ Option 1

- Type: string

############ Option 2

- Type: null

######### BaseCredentialData

- Schema name: `BaseCredentialData`
- Type: object

######### UserCredentialData

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
########## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

########## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

########## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

######### APIKeyCredentialData

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
########## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

########## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

########## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

########## api_key (required)

- Type: object

API key information used for authentication.

######### TokenCredentialData

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
########## parent (required)

- Type: object

Parent credential information that generated this token.

########## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

########## username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
########### Any of

############ Option 1

- Type: string

############ Option 2

- Type: null

######### Option 1

- Type: string

######### Option 2

- Type: null

######### Option 1

- Type: string

######### Option 2

- Type: null

####### created_at

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the session was created.

####### secure_transport

- Schema name: `Secure Transport`
- Type: boolean

Whether the session was established over a secure transport (HTTPS/WSS).

##### AuthSessionsQueryResultItem

- Schema name: `BaseCredentialData`
- Type: object

##### Option 3

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

##### BaseCredentialData

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

###### api_key (required)

- Schema name: `APIKeySessionData`
- Type: object

API key information used for authentication.
- No Additional Properties
####### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the API key.

####### name (required)

- Schema name: `Name`
- Type: string

Human-readable name of the API key.

##### UserCredentialData

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
###### parent (required)

- Schema name: `TokenParentCredentialsData`
- Type: object

Parent credential information that generated this token.
- No Additional Properties
####### credentials (required)

- Schema name: `Credentials`
- Type: enum (of string)

Type of credentials used to generate this token.

####### credentials_data (required)

- Schema name: `Credentials Data`

Credential data used to authenticate the token request.
######## Any of

######### BaseCredentialData

- Schema name: `BaseCredentialData`
- Type: object

######### UserCredentialData

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
########## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

########## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

########## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

######### APIKeyCredentialData

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
########## username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

########## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

########## login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

########## api_key (required)

- Type: object

API key information used for authentication.

######### TokenCredentialData

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
########## parent (required)

- Type: object

Parent credential information that generated this token.

########## login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

########## username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
########### Any of

############ Option 1

- Type: string

############ Option 2

- Type: null

######### Option 1

- Type: string

######### Option 2

- Type: null

###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

###### username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### APIKeyCredentialData

- Schema name: `BaseCredentialData`
- Type: object

##### TokenCredentialData

- Schema name: `UserCredentialData`
- Type: object
- No Additional Properties
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

##### BaseCredentialData

- Schema name: `APIKeyCredentialData`
- Type: object
- No Additional Properties
###### username (required)

- Schema name: `Username`
- Type: string

Username of the authenticated user.

###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

###### login_at (required)

- Schema name: `Login At`
- Type: string
- Type: Format: date-time

Timestamp of when the user logged in.

###### api_key (required)

- Type: object

API key information used for authentication.

##### UserCredentialData

- Schema name: `TokenCredentialData`
- Type: object
- No Additional Properties
###### parent (required)

- Type: object

Parent credential information that generated this token.

###### login_id (required)

- Schema name: `Login Id`
- Type: string

Unique identifier for the login.

###### username (required)

- Schema name: `Username`

Username associated with the token. `null` if not user-specific.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### APIKeyCredentialData

- Type: string

##### TokenCredentialData

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Schema name: `AuthSessionsQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: string

Unique identifier for the authentication session.

###### current

- Schema name: `Current`
- Type: boolean

Whether this is the current active session.

###### internal

- Schema name: `Internal`
- Type: boolean

Whether this is an internal system session.

###### origin

- Schema name: `Origin`
- Type: string

Origin information for the session (IP address, hostname, etc.).

###### credentials

- Schema name: `Credentials`
- Type: enum (of string)

Authentication method used for this session. `UNIX_SOCKET`: Local Unix domain socket authentication `LOGIN_PASSWORD`: Username and password authentication `LOGIN_TWOFACTOR`: Two-factor authentication login `LOGIN_ONETIME_PASSWORD`: One-time password authentication `API_KEY`: API key authentication `TOKEN`: Token-based authentication `TRUENAS_NODE`: TrueNAS cluster node authentication

###### credentials_data

- Schema name: `Credentials Data`

Detailed credential information specific to the authentication method.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: object

######## Option 3

- Type: object

######## Option 4

- Type: object

###### created_at

- Schema name: `Created At`
- Type: string
- Type: Format: date-time

Timestamp when the session was created.

###### secure_transport

- Schema name: `Secure Transport`
- Type: boolean

Whether the session was established over a secure transport (HTTPS/WSS).

##### Option 2

- Type: object

##### Option 1

- Type: object

##### Option 2

- Type: object

##### Option 3

- Type: object

##### Option 4

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
