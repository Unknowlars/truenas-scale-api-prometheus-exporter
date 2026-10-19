---
title: app.similar
kind: method
source_rst: _sources/api_methods_app.similar.rst.txt
source_html: api_methods_app.similar.html
required_roles:
  - CATALOG_READ
---

# app.similar

## Summary

Retrieve applications which are similar to `app_name`.

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

#### Parameter 1: app_name

<a id="Call_parameters_items_i0"></a>
#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to find similar apps for.
- Must be at least `1` characters long

#### Parameter 2: train

<a id="Call_parameters_items_i1"></a>
#### train

- Schema name: `train`
- Type: string

The catalog train to search within.
- Must be at least `1` characters long
Examples:

```json
"stable"
```
Examples:

```json
"enterprise"
```

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of applications similar to the requested one.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### AppAvailableItem

- Schema name: `AppAvailableItem`
- Type: object
<a id="headingReturn_value_items_app_readme"></a>
<a id="Return_value_items_app_readme"></a>
##### app_readme (required)

- Schema name: `App Readme`

HTML content of the app README.
<a id="Return_value_items_app_readme_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_app_readme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_app_readme_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_app_readme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_app_readme_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_categories"></a>
<a id="Return_value_items_categories"></a>
##### categories (required)

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_categories_items"></a>
- Type: string

<a id="headingReturn_value_items_description"></a>
<a id="Return_value_items_description"></a>
##### description (required)

- Schema name: `Description`
- Type: string

Short description of the app.

<a id="headingReturn_value_items_healthy"></a>
<a id="Return_value_items_healthy"></a>
##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

<a id="headingReturn_value_items_healthy_error"></a>
<a id="Return_value_items_healthy_error"></a>
##### healthy_error

- Schema name: `Healthy Error`
- Default: null

Error if app is not healthy.
<a id="Return_value_items_healthy_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_healthy_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_healthy_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_healthy_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_healthy_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_home"></a>
<a id="Return_value_items_home"></a>
##### home (required)

- Schema name: `Home`
- Type: string

Homepage URL of the app.

<a id="headingReturn_value_items_location"></a>
<a id="Return_value_items_location"></a>
##### location (required)

- Schema name: `Location`
- Type: string

Local path to the app's location.

<a id="headingReturn_value_items_latest_version"></a>
<a id="Return_value_items_latest_version"></a>
##### latest_version (required)

- Schema name: `Latest Version`

Latest available app version.
<a id="Return_value_items_latest_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_latest_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_latest_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_latest_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_latest_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_latest_app_version"></a>
<a id="Return_value_items_latest_app_version"></a>
##### latest_app_version (required)

- Schema name: `Latest App Version`

Latest available app version in repository.
<a id="Return_value_items_latest_app_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_latest_app_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_latest_app_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_latest_app_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_latest_app_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_latest_human_version"></a>
<a id="Return_value_items_latest_human_version"></a>
##### latest_human_version (required)

- Schema name: `Latest Human Version`

Human-readable version of the app.
<a id="Return_value_items_latest_human_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_latest_human_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_latest_human_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_latest_human_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_latest_human_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_last_update"></a>
<a id="Return_value_items_last_update"></a>
##### last_update (required)

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
<a id="Return_value_items_last_update_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_last_update_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_last_update_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_items_last_update_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_last_update_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the app.

<a id="headingReturn_value_items_recommended"></a>
<a id="Return_value_items_recommended"></a>
##### recommended (required)

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

<a id="headingReturn_value_items_title"></a>
<a id="Return_value_items_title"></a>
##### title (required)

- Schema name: `Title`
- Type: string

Title of the app.

<a id="headingReturn_value_items_maintainers"></a>
<a id="Return_value_items_maintainers"></a>
##### maintainers (required)

- Schema name: `Maintainers`
- Type: array of object

List of app maintainers.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_maintainers_items"></a>
###### Maintainer

- Schema name: `Maintainer`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_maintainers_items_name"></a>
<a id="Return_value_items_maintainers_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the app maintainer.

<a id="headingReturn_value_items_maintainers_items_email"></a>
<a id="Return_value_items_maintainers_items_email"></a>
###### email (required)

- Schema name: `Email`
- Type: string

Email address of the app maintainer.

<a id="headingReturn_value_items_maintainers_items_url"></a>
<a id="Return_value_items_maintainers_items_url"></a>
###### url (required)

- Schema name: `Url`

Website URL of the app maintainer or `null`.
<a id="Return_value_items_maintainers_items_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_maintainers_items_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_maintainers_items_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_maintainers_items_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_maintainers_items_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_tags"></a>
<a id="Return_value_items_tags"></a>
##### tags (required)

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_tags_items"></a>
- Type: string

<a id="headingReturn_value_items_screenshots"></a>
<a id="Return_value_items_screenshots"></a>
##### screenshots (required)

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_screenshots_items"></a>
- Type: string

<a id="headingReturn_value_items_sources"></a>
<a id="Return_value_items_sources"></a>
##### sources (required)

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_sources_items"></a>
- Type: string

<a id="headingReturn_value_items_icon_url"></a>
<a id="Return_value_items_icon_url"></a>
##### icon_url

- Schema name: `Icon Url`
- Default: null

URL of the app icon.
<a id="Return_value_items_icon_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_icon_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_icon_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_icon_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_icon_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_catalog"></a>
<a id="Return_value_items_catalog"></a>
##### catalog (required)

- Schema name: `Catalog`
- Type: string

Name of the catalog this application comes from.
- Must be at least `1` characters long

<a id="headingReturn_value_items_installed"></a>
<a id="Return_value_items_installed"></a>
##### installed (required)

- Schema name: `Installed`
- Type: boolean

Whether this application is currently installed on the system.

<a id="headingReturn_value_items_train"></a>
<a id="Return_value_items_train"></a>
##### train (required)

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

<a id="headingReturn_value_items_popularity_rank"></a>
<a id="Return_value_items_popularity_rank"></a>
##### popularity_rank (required)

- Schema name: `Popularity Rank`

Popularity ranking of this application. Lower numbers indicate higher popularity. `null` if not ranked.
<a id="Return_value_items_popularity_rank_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_popularity_rank_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_popularity_rank_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_popularity_rank_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_popularity_rank_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_additionalProperties"></a>
<a id="Return_value_items_additionalProperties"></a>
##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
