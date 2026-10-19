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
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

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
###### AppLatestItem

- Schema name: `AppLatestItem`
- Type: object

Represents the latest version of an available application.
<a id="headingReturn_value_anyOf_i0_items_app_readme"></a>
<a id="Return_value_anyOf_i0_items_app_readme"></a>
###### app_readme (required)

- Schema name: `App Readme`

HTML content of the app README.
<a id="Return_value_anyOf_i0_items_app_readme_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_app_readme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_app_readme_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_app_readme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_app_readme_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_categories"></a>
<a id="Return_value_anyOf_i0_items_categories"></a>
###### categories (required)

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_categories_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_description"></a>
<a id="Return_value_anyOf_i0_items_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Short description of the app.

<a id="headingReturn_value_anyOf_i0_items_healthy"></a>
<a id="Return_value_anyOf_i0_items_healthy"></a>
###### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

<a id="headingReturn_value_anyOf_i0_items_healthy_error"></a>
<a id="Return_value_anyOf_i0_items_healthy_error"></a>
###### healthy_error

- Schema name: `Healthy Error`
- Default: null

Error if app is not healthy.
<a id="Return_value_anyOf_i0_items_healthy_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_healthy_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_healthy_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_healthy_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_healthy_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_home"></a>
<a id="Return_value_anyOf_i0_items_home"></a>
###### home (required)

- Schema name: `Home`
- Type: string

Homepage URL of the app.

<a id="headingReturn_value_anyOf_i0_items_location"></a>
<a id="Return_value_anyOf_i0_items_location"></a>
###### location (required)

- Schema name: `Location`
- Type: string

Local path to the app's location.

<a id="headingReturn_value_anyOf_i0_items_latest_version"></a>
<a id="Return_value_anyOf_i0_items_latest_version"></a>
###### latest_version (required)

- Schema name: `Latest Version`

Latest available app version.
<a id="Return_value_anyOf_i0_items_latest_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_latest_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_latest_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_latest_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_latest_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_latest_app_version"></a>
<a id="Return_value_anyOf_i0_items_latest_app_version"></a>
###### latest_app_version (required)

- Schema name: `Latest App Version`

Latest available app version in repository.
<a id="Return_value_anyOf_i0_items_latest_app_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_latest_app_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_latest_app_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_latest_app_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_latest_app_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_latest_human_version"></a>
<a id="Return_value_anyOf_i0_items_latest_human_version"></a>
###### latest_human_version (required)

- Schema name: `Latest Human Version`

Human-readable version of the app.
<a id="Return_value_anyOf_i0_items_latest_human_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_latest_human_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_latest_human_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_latest_human_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_latest_human_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_last_update"></a>
<a id="Return_value_anyOf_i0_items_last_update"></a>
###### last_update (required)

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
<a id="Return_value_anyOf_i0_items_last_update_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_last_update_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_last_update_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i0_items_last_update_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_last_update_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the app.

<a id="headingReturn_value_anyOf_i0_items_recommended"></a>
<a id="Return_value_anyOf_i0_items_recommended"></a>
###### recommended (required)

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

<a id="headingReturn_value_anyOf_i0_items_title"></a>
<a id="Return_value_anyOf_i0_items_title"></a>
###### title (required)

- Schema name: `Title`
- Type: string

Title of the app.

<a id="headingReturn_value_anyOf_i0_items_maintainers"></a>
<a id="Return_value_anyOf_i0_items_maintainers"></a>
###### maintainers (required)

- Schema name: `Maintainers`
- Type: array of object

List of app maintainers.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_maintainers_items"></a>
###### Maintainer

- Schema name: `Maintainer`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_maintainers_items_name"></a>
<a id="Return_value_anyOf_i0_items_maintainers_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the app maintainer.

<a id="headingReturn_value_anyOf_i0_items_maintainers_items_email"></a>
<a id="Return_value_anyOf_i0_items_maintainers_items_email"></a>
###### email (required)

- Schema name: `Email`
- Type: string

Email address of the app maintainer.

<a id="headingReturn_value_anyOf_i0_items_maintainers_items_url"></a>
<a id="Return_value_anyOf_i0_items_maintainers_items_url"></a>
###### url (required)

- Schema name: `Url`

Website URL of the app maintainer or `null`.
<a id="Return_value_anyOf_i0_items_maintainers_items_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_maintainers_items_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_maintainers_items_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_maintainers_items_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_maintainers_items_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_tags"></a>
<a id="Return_value_anyOf_i0_items_tags"></a>
###### tags (required)

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_tags_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_screenshots"></a>
<a id="Return_value_anyOf_i0_items_screenshots"></a>
###### screenshots (required)

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_screenshots_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_sources"></a>
<a id="Return_value_anyOf_i0_items_sources"></a>
###### sources (required)

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_sources_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_icon_url"></a>
<a id="Return_value_anyOf_i0_items_icon_url"></a>
###### icon_url

- Schema name: `Icon Url`
- Default: null

URL of the app icon.
<a id="Return_value_anyOf_i0_items_icon_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_icon_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_icon_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_icon_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_icon_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_catalog"></a>
<a id="Return_value_anyOf_i0_items_catalog"></a>
###### catalog (required)

- Schema name: `Catalog`
- Type: string

Name of the catalog this application comes from.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_installed"></a>
<a id="Return_value_anyOf_i0_items_installed"></a>
###### installed (required)

- Schema name: `Installed`
- Type: boolean

Whether this application is currently installed on the system.

<a id="headingReturn_value_anyOf_i0_items_train"></a>
<a id="Return_value_anyOf_i0_items_train"></a>
###### train (required)

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

<a id="headingReturn_value_anyOf_i0_items_popularity_rank"></a>
<a id="Return_value_anyOf_i0_items_popularity_rank"></a>
###### popularity_rank (required)

- Schema name: `Popularity Rank`

Popularity ranking of this application. Lower numbers indicate higher popularity. `null` if not ranked.
<a id="Return_value_anyOf_i0_items_popularity_rank_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_popularity_rank_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_popularity_rank_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_popularity_rank_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_popularity_rank_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_additionalProperties"></a>
<a id="Return_value_anyOf_i0_items_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [AppLatestItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `AppLatestItem`
- Type: object

Represents the latest version of an available application.
<a id="headingReturn_value_anyOf_i1_app_readme"></a>
<a id="Return_value_anyOf_i1_app_readme"></a>
###### app_readme (required)

- Schema name: `App Readme`

HTML content of the app README.
<a id="Return_value_anyOf_i1_app_readme_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_app_readme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_app_readme_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i1_app_readme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_app_readme_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_categories"></a>
<a id="Return_value_anyOf_i1_categories"></a>
###### categories (required)

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_categories_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i1_description"></a>
<a id="Return_value_anyOf_i1_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Short description of the app.

<a id="headingReturn_value_anyOf_i1_healthy"></a>
<a id="Return_value_anyOf_i1_healthy"></a>
###### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

<a id="headingReturn_value_anyOf_i1_healthy_error"></a>
<a id="Return_value_anyOf_i1_healthy_error"></a>
###### healthy_error

- Schema name: `Healthy Error`
- Default: null

Error if app is not healthy.
<a id="Return_value_anyOf_i1_healthy_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_healthy_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_healthy_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_healthy_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_healthy_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_home"></a>
<a id="Return_value_anyOf_i1_home"></a>
###### home (required)

- Schema name: `Home`
- Type: string

Homepage URL of the app.

<a id="headingReturn_value_anyOf_i1_location"></a>
<a id="Return_value_anyOf_i1_location"></a>
###### location (required)

- Schema name: `Location`
- Type: string

Local path to the app's location.

<a id="headingReturn_value_anyOf_i1_latest_version"></a>
<a id="Return_value_anyOf_i1_latest_version"></a>
###### latest_version (required)

- Schema name: `Latest Version`

Latest available app version.
<a id="Return_value_anyOf_i1_latest_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_latest_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_latest_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_latest_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_latest_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_latest_app_version"></a>
<a id="Return_value_anyOf_i1_latest_app_version"></a>
###### latest_app_version (required)

- Schema name: `Latest App Version`

Latest available app version in repository.
<a id="Return_value_anyOf_i1_latest_app_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_latest_app_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_latest_app_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_latest_app_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_latest_app_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_latest_human_version"></a>
<a id="Return_value_anyOf_i1_latest_human_version"></a>
###### latest_human_version (required)

- Schema name: `Latest Human Version`

Human-readable version of the app.
<a id="Return_value_anyOf_i1_latest_human_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_latest_human_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_latest_human_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_latest_human_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_latest_human_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_last_update"></a>
<a id="Return_value_anyOf_i1_last_update"></a>
###### last_update (required)

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
<a id="Return_value_anyOf_i1_last_update_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_last_update_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_last_update_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i1_last_update_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_last_update_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the app.

<a id="headingReturn_value_anyOf_i1_recommended"></a>
<a id="Return_value_anyOf_i1_recommended"></a>
###### recommended (required)

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

<a id="headingReturn_value_anyOf_i1_title"></a>
<a id="Return_value_anyOf_i1_title"></a>
###### title (required)

- Schema name: `Title`
- Type: string

Title of the app.

<a id="headingReturn_value_anyOf_i1_maintainers"></a>
<a id="Return_value_anyOf_i1_maintainers"></a>
###### maintainers (required)

- Schema name: `Maintainers`
- Type: array

List of app maintainers.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_maintainers_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i1_tags"></a>
<a id="Return_value_anyOf_i1_tags"></a>
###### tags (required)

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_tags_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i1_screenshots"></a>
<a id="Return_value_anyOf_i1_screenshots"></a>
###### screenshots (required)

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_screenshots_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i1_sources"></a>
<a id="Return_value_anyOf_i1_sources"></a>
###### sources (required)

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_sources_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i1_icon_url"></a>
<a id="Return_value_anyOf_i1_icon_url"></a>
###### icon_url

- Schema name: `Icon Url`
- Default: null

URL of the app icon.
<a id="Return_value_anyOf_i1_icon_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_icon_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_icon_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_icon_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_icon_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_catalog"></a>
<a id="Return_value_anyOf_i1_catalog"></a>
###### catalog (required)

- Schema name: `Catalog`
- Type: string

Name of the catalog this application comes from.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_installed"></a>
<a id="Return_value_anyOf_i1_installed"></a>
###### installed (required)

- Schema name: `Installed`
- Type: boolean

Whether this application is currently installed on the system.

<a id="headingReturn_value_anyOf_i1_train"></a>
<a id="Return_value_anyOf_i1_train"></a>
###### train (required)

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

<a id="headingReturn_value_anyOf_i1_popularity_rank"></a>
<a id="Return_value_anyOf_i1_popularity_rank"></a>
###### popularity_rank (required)

- Schema name: `Popularity Rank`

Popularity ranking of this application. Lower numbers indicate higher popularity. `null` if not ranked.
<a id="Return_value_anyOf_i1_popularity_rank_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_popularity_rank_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_popularity_rank_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_popularity_rank_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_popularity_rank_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_additionalProperties"></a>
<a id="Return_value_anyOf_i1_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### AppLatestItemQueryResultItem

- Schema name: `AppLatestItemQueryResultItem`
- Type: object
<a id="headingReturn_value_anyOf_i2_items_app_readme"></a>
<a id="Return_value_anyOf_i2_items_app_readme"></a>
###### app_readme

- Schema name: `App Readme`

HTML content of the app README.
<a id="Return_value_anyOf_i2_items_app_readme_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_app_readme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_app_readme_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_app_readme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_app_readme_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_categories"></a>
<a id="Return_value_anyOf_i2_items_categories"></a>
###### categories

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_categories_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i2_items_description"></a>
<a id="Return_value_anyOf_i2_items_description"></a>
###### description

- Schema name: `Description`
- Type: string

Short description of the app.

<a id="headingReturn_value_anyOf_i2_items_healthy"></a>
<a id="Return_value_anyOf_i2_items_healthy"></a>
###### healthy

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

<a id="headingReturn_value_anyOf_i2_items_healthy_error"></a>
<a id="Return_value_anyOf_i2_items_healthy_error"></a>
###### healthy_error

- Schema name: `Healthy Error`

Error if app is not healthy.
<a id="Return_value_anyOf_i2_items_healthy_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_healthy_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_healthy_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_healthy_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_healthy_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_home"></a>
<a id="Return_value_anyOf_i2_items_home"></a>
###### home

- Schema name: `Home`
- Type: string

Homepage URL of the app.

<a id="headingReturn_value_anyOf_i2_items_location"></a>
<a id="Return_value_anyOf_i2_items_location"></a>
###### location

- Schema name: `Location`
- Type: string

Local path to the app's location.

<a id="headingReturn_value_anyOf_i2_items_latest_version"></a>
<a id="Return_value_anyOf_i2_items_latest_version"></a>
###### latest_version

- Schema name: `Latest Version`

Latest available app version.
<a id="Return_value_anyOf_i2_items_latest_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_latest_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_latest_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_latest_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_latest_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_latest_app_version"></a>
<a id="Return_value_anyOf_i2_items_latest_app_version"></a>
###### latest_app_version

- Schema name: `Latest App Version`

Latest available app version in repository.
<a id="Return_value_anyOf_i2_items_latest_app_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_latest_app_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_latest_app_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_latest_app_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_latest_app_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_latest_human_version"></a>
<a id="Return_value_anyOf_i2_items_latest_human_version"></a>
###### latest_human_version

- Schema name: `Latest Human Version`

Human-readable version of the app.
<a id="Return_value_anyOf_i2_items_latest_human_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_latest_human_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_latest_human_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_latest_human_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_latest_human_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_last_update"></a>
<a id="Return_value_anyOf_i2_items_last_update"></a>
###### last_update

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
<a id="Return_value_anyOf_i2_items_last_update_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_last_update_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_last_update_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i2_items_last_update_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_last_update_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_name"></a>
<a id="Return_value_anyOf_i2_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Name of the app.

<a id="headingReturn_value_anyOf_i2_items_recommended"></a>
<a id="Return_value_anyOf_i2_items_recommended"></a>
###### recommended

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

<a id="headingReturn_value_anyOf_i2_items_title"></a>
<a id="Return_value_anyOf_i2_items_title"></a>
###### title

- Schema name: `Title`
- Type: string

Title of the app.

<a id="headingReturn_value_anyOf_i2_items_maintainers"></a>
<a id="Return_value_anyOf_i2_items_maintainers"></a>
###### maintainers

- Schema name: `Maintainers`
- Type: array of object

List of app maintainers.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_maintainers_items"></a>
###### Maintainer

- Schema name: `Maintainer`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_maintainers_items_name"></a>
<a id="Return_value_anyOf_i2_items_maintainers_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the app maintainer.

<a id="headingReturn_value_anyOf_i2_items_maintainers_items_email"></a>
<a id="Return_value_anyOf_i2_items_maintainers_items_email"></a>
###### email (required)

- Schema name: `Email`
- Type: string

Email address of the app maintainer.

<a id="headingReturn_value_anyOf_i2_items_maintainers_items_url"></a>
<a id="Return_value_anyOf_i2_items_maintainers_items_url"></a>
###### url (required)

- Schema name: `Url`

Website URL of the app maintainer or `null`.
<a id="Return_value_anyOf_i2_items_maintainers_items_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_maintainers_items_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_maintainers_items_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_maintainers_items_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_maintainers_items_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_tags"></a>
<a id="Return_value_anyOf_i2_items_tags"></a>
###### tags

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_tags_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i2_items_screenshots"></a>
<a id="Return_value_anyOf_i2_items_screenshots"></a>
###### screenshots

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_screenshots_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i2_items_sources"></a>
<a id="Return_value_anyOf_i2_items_sources"></a>
###### sources

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_sources_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i2_items_icon_url"></a>
<a id="Return_value_anyOf_i2_items_icon_url"></a>
###### icon_url

- Schema name: `Icon Url`

URL of the app icon.
<a id="Return_value_anyOf_i2_items_icon_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_icon_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_icon_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_icon_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_icon_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_catalog"></a>
<a id="Return_value_anyOf_i2_items_catalog"></a>
###### catalog

- Schema name: `Catalog`
- Type: string

Name of the catalog this application comes from.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_installed"></a>
<a id="Return_value_anyOf_i2_items_installed"></a>
###### installed

- Schema name: `Installed`
- Type: boolean

Whether this application is currently installed on the system.

<a id="headingReturn_value_anyOf_i2_items_train"></a>
<a id="Return_value_anyOf_i2_items_train"></a>
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

<a id="headingReturn_value_anyOf_i2_items_popularity_rank"></a>
<a id="Return_value_anyOf_i2_items_popularity_rank"></a>
###### popularity_rank

- Schema name: `Popularity Rank`

Popularity ranking of this application. Lower numbers indicate higher popularity. `null` if not ranked.
<a id="Return_value_anyOf_i2_items_popularity_rank_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_popularity_rank_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_popularity_rank_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_popularity_rank_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_popularity_rank_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_additionalProperties"></a>
<a id="Return_value_anyOf_i2_items_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [AppLatestItemQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `AppLatestItemQueryResultItem`
- Type: object
<a id="headingReturn_value_anyOf_i3_app_readme"></a>
<a id="Return_value_anyOf_i3_app_readme"></a>
###### app_readme

- Schema name: `App Readme`

HTML content of the app README.
<a id="Return_value_anyOf_i3_app_readme_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_app_readme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_app_readme_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_anyOf_i3_app_readme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_app_readme_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_categories"></a>
<a id="Return_value_anyOf_i3_categories"></a>
###### categories

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_categories_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i3_description"></a>
<a id="Return_value_anyOf_i3_description"></a>
###### description

- Schema name: `Description`
- Type: string

Short description of the app.

<a id="headingReturn_value_anyOf_i3_healthy"></a>
<a id="Return_value_anyOf_i3_healthy"></a>
###### healthy

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

<a id="headingReturn_value_anyOf_i3_healthy_error"></a>
<a id="Return_value_anyOf_i3_healthy_error"></a>
###### healthy_error

- Schema name: `Healthy Error`

Error if app is not healthy.
<a id="Return_value_anyOf_i3_healthy_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_healthy_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_healthy_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_healthy_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_healthy_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_home"></a>
<a id="Return_value_anyOf_i3_home"></a>
###### home

- Schema name: `Home`
- Type: string

Homepage URL of the app.

<a id="headingReturn_value_anyOf_i3_location"></a>
<a id="Return_value_anyOf_i3_location"></a>
###### location

- Schema name: `Location`
- Type: string

Local path to the app's location.

<a id="headingReturn_value_anyOf_i3_latest_version"></a>
<a id="Return_value_anyOf_i3_latest_version"></a>
###### latest_version

- Schema name: `Latest Version`

Latest available app version.
<a id="Return_value_anyOf_i3_latest_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_latest_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_latest_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_latest_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_latest_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_latest_app_version"></a>
<a id="Return_value_anyOf_i3_latest_app_version"></a>
###### latest_app_version

- Schema name: `Latest App Version`

Latest available app version in repository.
<a id="Return_value_anyOf_i3_latest_app_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_latest_app_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_latest_app_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_latest_app_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_latest_app_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_latest_human_version"></a>
<a id="Return_value_anyOf_i3_latest_human_version"></a>
###### latest_human_version

- Schema name: `Latest Human Version`

Human-readable version of the app.
<a id="Return_value_anyOf_i3_latest_human_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_latest_human_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_latest_human_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_latest_human_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_latest_human_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_last_update"></a>
<a id="Return_value_anyOf_i3_last_update"></a>
###### last_update

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
<a id="Return_value_anyOf_i3_last_update_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_last_update_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_last_update_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i3_last_update_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_last_update_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_name"></a>
<a id="Return_value_anyOf_i3_name"></a>
###### name

- Schema name: `Name`
- Type: string

Name of the app.

<a id="headingReturn_value_anyOf_i3_recommended"></a>
<a id="Return_value_anyOf_i3_recommended"></a>
###### recommended

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

<a id="headingReturn_value_anyOf_i3_title"></a>
<a id="Return_value_anyOf_i3_title"></a>
###### title

- Schema name: `Title`
- Type: string

Title of the app.

<a id="headingReturn_value_anyOf_i3_maintainers"></a>
<a id="Return_value_anyOf_i3_maintainers"></a>
###### maintainers

- Schema name: `Maintainers`
- Type: array

List of app maintainers.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_maintainers_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i3_tags"></a>
<a id="Return_value_anyOf_i3_tags"></a>
###### tags

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_tags_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i3_screenshots"></a>
<a id="Return_value_anyOf_i3_screenshots"></a>
###### screenshots

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_screenshots_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i3_sources"></a>
<a id="Return_value_anyOf_i3_sources"></a>
###### sources

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_sources_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i3_icon_url"></a>
<a id="Return_value_anyOf_i3_icon_url"></a>
###### icon_url

- Schema name: `Icon Url`

URL of the app icon.
<a id="Return_value_anyOf_i3_icon_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_icon_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_icon_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_icon_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_icon_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_catalog"></a>
<a id="Return_value_anyOf_i3_catalog"></a>
###### catalog

- Schema name: `Catalog`
- Type: string

Name of the catalog this application comes from.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_installed"></a>
<a id="Return_value_anyOf_i3_installed"></a>
###### installed

- Schema name: `Installed`
- Type: boolean

Whether this application is currently installed on the system.

<a id="headingReturn_value_anyOf_i3_train"></a>
<a id="Return_value_anyOf_i3_train"></a>
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

<a id="headingReturn_value_anyOf_i3_popularity_rank"></a>
<a id="Return_value_anyOf_i3_popularity_rank"></a>
###### popularity_rank

- Schema name: `Popularity Rank`

Popularity ranking of this application. Lower numbers indicate higher popularity. `null` if not ranked.
<a id="Return_value_anyOf_i3_popularity_rank_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_popularity_rank_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_popularity_rank_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_popularity_rank_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_popularity_rank_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_additionalProperties"></a>
<a id="Return_value_anyOf_i3_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
