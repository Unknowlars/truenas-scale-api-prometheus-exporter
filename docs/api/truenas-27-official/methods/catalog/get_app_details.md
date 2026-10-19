---
title: catalog.get_app_details
kind: method
source_rst: _sources/api_methods_catalog.get_app_details.rst.txt
source_html: api_methods_catalog.get_app_details.html
required_roles:
  - CATALOG_READ
---

# catalog.get_app_details

## Summary

Retrieve information of `app_name` `app_version_details.catalog` catalog app.

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

Name of the app to get details for.
- Must be at least `1` characters long

#### Parameter 2: app_version_details

<a id="Call_parameters_items_i1"></a>
#### app_version_details

- Schema name: `app_version_details`
- Type: object

Version and train information for the specific app.
- No Additional Properties
<a id="headingCall_parameters_items_i1_train"></a>
<a id="Call_parameters_items_i1_train"></a>
##### train (required)

- Schema name: `Train`
- Type: string

Train name where the app version is located.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `CatalogAppDetails`
- Type: object

Detailed information about the requested app, including all available versions.
<a id="headingReturn_value_app_readme"></a>
<a id="Return_value_app_readme"></a>
#### app_readme (required)

- Schema name: `App Readme`

HTML content of the app README.
<a id="Return_value_app_readme_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_app_readme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_app_readme_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_app_readme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_app_readme_anyOf_i1)

- Type: null

<a id="headingReturn_value_categories"></a>
<a id="Return_value_categories"></a>
#### categories (required)

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_categories_items"></a>
- Type: string

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description (required)

- Schema name: `Description`
- Type: string

Short description of the app.

<a id="headingReturn_value_healthy"></a>
<a id="Return_value_healthy"></a>
#### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

<a id="headingReturn_value_healthy_error"></a>
<a id="Return_value_healthy_error"></a>
#### healthy_error

- Schema name: `Healthy Error`
- Default: null

Error if app is not healthy.
<a id="Return_value_healthy_error_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_healthy_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_healthy_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_healthy_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_healthy_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_home"></a>
<a id="Return_value_home"></a>
#### home (required)

- Schema name: `Home`
- Type: string

Homepage URL of the app.

<a id="headingReturn_value_location"></a>
<a id="Return_value_location"></a>
#### location (required)

- Schema name: `Location`
- Type: string

Local path to the app's location.

<a id="headingReturn_value_latest_version"></a>
<a id="Return_value_latest_version"></a>
#### latest_version (required)

- Schema name: `Latest Version`

Latest available app version.
<a id="Return_value_latest_version_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_latest_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_latest_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_latest_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_latest_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_latest_app_version"></a>
<a id="Return_value_latest_app_version"></a>
#### latest_app_version (required)

- Schema name: `Latest App Version`

Latest available app version in repository.
<a id="Return_value_latest_app_version_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_latest_app_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_latest_app_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_latest_app_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_latest_app_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_latest_human_version"></a>
<a id="Return_value_latest_human_version"></a>
#### latest_human_version (required)

- Schema name: `Latest Human Version`

Human-readable version of the app.
<a id="Return_value_latest_human_version_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_latest_human_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_latest_human_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_latest_human_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_latest_human_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_last_update"></a>
<a id="Return_value_last_update"></a>
#### last_update (required)

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
<a id="Return_value_last_update_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_last_update_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_last_update_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_last_update_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_last_update_anyOf_i1)

- Type: null

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Name of the app.

<a id="headingReturn_value_recommended"></a>
<a id="Return_value_recommended"></a>
#### recommended (required)

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

<a id="headingReturn_value_title"></a>
<a id="Return_value_title"></a>
#### title (required)

- Schema name: `Title`
- Type: string

Title of the app.

<a id="headingReturn_value_maintainers"></a>
<a id="Return_value_maintainers"></a>
#### maintainers (required)

- Schema name: `Maintainers`
- Type: array of object

List of app maintainers.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_maintainers_items"></a>
##### Maintainer

- Schema name: `Maintainer`
- Type: object
- No Additional Properties
<a id="headingReturn_value_maintainers_items_name"></a>
<a id="Return_value_maintainers_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the app maintainer.

<a id="headingReturn_value_maintainers_items_email"></a>
<a id="Return_value_maintainers_items_email"></a>
###### email (required)

- Schema name: `Email`
- Type: string

Email address of the app maintainer.

<a id="headingReturn_value_maintainers_items_url"></a>
<a id="Return_value_maintainers_items_url"></a>
###### url (required)

- Schema name: `Url`

Website URL of the app maintainer or `null`.
<a id="Return_value_maintainers_items_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_maintainers_items_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_maintainers_items_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_maintainers_items_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_maintainers_items_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_tags"></a>
<a id="Return_value_tags"></a>
#### tags (required)

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_tags_items"></a>
- Type: string

<a id="headingReturn_value_screenshots"></a>
<a id="Return_value_screenshots"></a>
#### screenshots (required)

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_screenshots_items"></a>
- Type: string

<a id="headingReturn_value_sources"></a>
<a id="Return_value_sources"></a>
#### sources (required)

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_sources_items"></a>
- Type: string

<a id="headingReturn_value_icon_url"></a>
<a id="Return_value_icon_url"></a>
#### icon_url

- Schema name: `Icon Url`
- Default: null

URL of the app icon.
<a id="Return_value_icon_url_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_icon_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_icon_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_icon_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_icon_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_versions"></a>
<a id="Return_value_versions"></a>
#### versions (required)

- Schema name: `Versions`
- Type: object

Mapping of version strings.

<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
