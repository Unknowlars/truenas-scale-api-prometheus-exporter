---
title: app.latest
kind: method
source_rst: _sources/api_methods_app.latest.rst.txt
source_html: api_methods_app.latest.html
required_roles:
  - CATALOG_READ
---

# app.latest

## Summary

Retrieve latest updated apps.

## Required Roles

- `CATALOG_READ`

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

###### AppLatestItemQueryResultItem

- Schema name: `AppLatestItemQueryResultItem`
- Type: object
####### app_readme

- Schema name: `App Readme`

HTML content of the app README.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### categories

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### description

- Schema name: `Description`
- Type: string

Short description of the app.

####### healthy

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

####### healthy_error

- Schema name: `Healthy Error`

Error if app is not healthy.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### home

- Schema name: `Home`
- Type: string

Homepage URL of the app.

####### location

- Schema name: `Location`
- Type: string

Local path to the app's location.

####### latest_version

- Schema name: `Latest Version`

Latest available app version.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### latest_app_version

- Schema name: `Latest App Version`

Latest available app version in repository.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### latest_human_version

- Schema name: `Latest Human Version`

Human-readable version of the app.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### last_update

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
######## Any of

######### Option 1

- Type: string
- Type: Format: date-time

######### Option 2

- Type: null

####### name

- Schema name: `Name`
- Type: string

Name of the app.

####### recommended

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

####### title

- Schema name: `Title`
- Type: string

Title of the app.

####### maintainers

- Schema name: `Maintainers`
- Type: array of object

List of app maintainers.
- No Additional Items

######## Each item of this array must be:

######## Maintainer

- Schema name: `Maintainer`
- Type: object
- No Additional Properties
######### name (required)

- Schema name: `Name`
- Type: string

Name of the app maintainer.

######### email (required)

- Schema name: `Email`
- Type: string

Email address of the app maintainer.

######### url (required)

- Schema name: `Url`

Website URL of the app maintainer or `null`.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

####### tags

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### screenshots

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### sources

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### icon_url

- Schema name: `Icon Url`

URL of the app icon.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### catalog

- Schema name: `Catalog`
- Type: string

Name of the catalog this application comes from.
- Must be at least `1` characters long

####### installed

- Schema name: `Installed`
- Type: boolean

Whether this application is currently installed on the system.

####### train

- Schema name: `Train`
- Type: string

The catalog train this application version belongs to.
- Must be at least `1` characters long
Examples:

```json
"stable"
```
Examples:

```json
"enterprise"
```

####### popularity_rank

- Schema name: `Popularity Rank`

Popularity ranking of this application. Lower numbers indicate higher popularity. `null` if not ranked.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### Additional Properties

Additional Properties of any type are allowed.
- Type: object

##### AppLatestItemQueryResultItem

- Type: string

##### Option 3

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string
- Type: Format: date-time

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Schema name: `AppLatestItemQueryResultItem`
- Type: object
###### app_readme

- Schema name: `App Readme`

HTML content of the app README.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### categories

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### description

- Schema name: `Description`
- Type: string

Short description of the app.

###### healthy

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

###### healthy_error

- Schema name: `Healthy Error`

Error if app is not healthy.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### home

- Schema name: `Home`
- Type: string

Homepage URL of the app.

###### location

- Schema name: `Location`
- Type: string

Local path to the app's location.

###### latest_version

- Schema name: `Latest Version`

Latest available app version.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### latest_app_version

- Schema name: `Latest App Version`

Latest available app version in repository.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### latest_human_version

- Schema name: `Latest Human Version`

Human-readable version of the app.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### last_update

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
####### Any of

######## Option 1

- Type: string
- Type: Format: date-time

######## Option 2

- Type: null

###### name

- Schema name: `Name`
- Type: string

Name of the app.

###### recommended

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

###### title

- Schema name: `Title`
- Type: string

Title of the app.

###### maintainers

- Schema name: `Maintainers`
- Type: array

List of app maintainers.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### tags

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### screenshots

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### sources

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### icon_url

- Schema name: `Icon Url`

URL of the app icon.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### catalog

- Schema name: `Catalog`
- Type: string

Name of the catalog this application comes from.
- Must be at least `1` characters long

###### installed

- Schema name: `Installed`
- Type: boolean

Whether this application is currently installed on the system.

###### train

- Schema name: `Train`
- Type: string

The catalog train this application version belongs to.
- Must be at least `1` characters long
Examples:

```json
"stable"
```
Examples:

```json
"enterprise"
```

###### popularity_rank

- Schema name: `Popularity Rank`

Popularity ranking of this application. Lower numbers indicate higher popularity. `null` if not ranked.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string
- Type: Format: date-time

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
