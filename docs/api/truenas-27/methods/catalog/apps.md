---
title: catalog.apps
kind: method
source_rst: _sources/api_methods_catalog.apps.rst.txt
source_html: api_methods_catalog.apps.html
required_roles:
  - CATALOG_READ
---

# catalog.apps

## Summary

Retrieve apps details for `label` catalog.

`options.cache` is a boolean which when set will try to get apps details for `label` catalog from cache if available.

`options.cache_only` is a boolean which when set will force usage of cache only for retrieving catalog information. If the content for the catalog in question is not cached, no content would be returned. If `options.cache` is unset, this attribute has no effect.

`options.retrieve_all_trains` is a boolean value which when set will retrieve information for all the trains present in the catalog ( it is set by default ).

`options.trains` is a list of train name(s) which will allow selective filtering to retrieve only information of desired trains in a catalog. If `options.retrieve_all_trains` is set, it has precedence over `options.train`.

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

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Catalog apps query parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_cache"></a>
<a id="Call_parameters_items_i0_cache"></a>
##### cache

- Schema name: `Cache`
- Type: boolean
- Default: true

Whether to use cached catalog data if available.

<a id="headingCall_parameters_items_i0_cache_only"></a>
<a id="Call_parameters_items_i0_cache_only"></a>
##### cache_only

- Schema name: `Cache Only`
- Type: boolean
- Default: false

Whether to only return cached data without fetching updates.

<a id="headingCall_parameters_items_i0_retrieve_all_trains"></a>
<a id="Call_parameters_items_i0_retrieve_all_trains"></a>
##### retrieve_all_trains

- Schema name: `Retrieve All Trains`
- Type: boolean
- Default: true

Whether to retrieve apps from all available trains.

<a id="headingCall_parameters_items_i0_trains"></a>
<a id="Call_parameters_items_i0_trains"></a>
##### trains

- Schema name: `Trains`
- Type: array of string

Specific train names to retrieve apps from (empty array means all trains).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_trains_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `CatalogAppsResponse`
- Type: object

Object mapping train names to their app information.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `CatalogTrainInfo`
- Type: object
<a id="headingReturn_value_additionalProperties_additionalProperties"></a>
<a id="Return_value_additionalProperties_additionalProperties"></a>
##### Additional Properties

Each additional property must conform to the following schema
- Schema name: `CatalogAppInfo`
- Type: object
<a id="headingReturn_value_additionalProperties_additionalProperties_app_readme"></a>
<a id="Return_value_additionalProperties_additionalProperties_app_readme"></a>
###### app_readme (required)

- Schema name: `App Readme`

HTML content of the app README.
<a id="Return_value_additionalProperties_additionalProperties_app_readme_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_app_readme_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_additionalProperties_app_readme_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_app_readme_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_additionalProperties_app_readme_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_additionalProperties_categories"></a>
<a id="Return_value_additionalProperties_additionalProperties_categories"></a>
###### categories (required)

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_additionalProperties_additionalProperties_categories_items"></a>
- Type: string

<a id="headingReturn_value_additionalProperties_additionalProperties_description"></a>
<a id="Return_value_additionalProperties_additionalProperties_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Short description of the app.

<a id="headingReturn_value_additionalProperties_additionalProperties_healthy"></a>
<a id="Return_value_additionalProperties_additionalProperties_healthy"></a>
###### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

<a id="headingReturn_value_additionalProperties_additionalProperties_healthy_error"></a>
<a id="Return_value_additionalProperties_additionalProperties_healthy_error"></a>
###### healthy_error

- Schema name: `Healthy Error`
- Default: null

Error if app is not healthy.
<a id="Return_value_additionalProperties_additionalProperties_healthy_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_healthy_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_additionalProperties_healthy_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_healthy_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_additionalProperties_healthy_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_additionalProperties_home"></a>
<a id="Return_value_additionalProperties_additionalProperties_home"></a>
###### home (required)

- Schema name: `Home`
- Type: string

Homepage URL of the app.

<a id="headingReturn_value_additionalProperties_additionalProperties_location"></a>
<a id="Return_value_additionalProperties_additionalProperties_location"></a>
###### location (required)

- Schema name: `Location`
- Type: string

Local path to the app's location.

<a id="headingReturn_value_additionalProperties_additionalProperties_latest_version"></a>
<a id="Return_value_additionalProperties_additionalProperties_latest_version"></a>
###### latest_version (required)

- Schema name: `Latest Version`

Latest available app version.
<a id="Return_value_additionalProperties_additionalProperties_latest_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_latest_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_additionalProperties_latest_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_latest_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_additionalProperties_latest_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_additionalProperties_latest_app_version"></a>
<a id="Return_value_additionalProperties_additionalProperties_latest_app_version"></a>
###### latest_app_version (required)

- Schema name: `Latest App Version`

Latest available app version in repository.
<a id="Return_value_additionalProperties_additionalProperties_latest_app_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_latest_app_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_additionalProperties_latest_app_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_latest_app_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_additionalProperties_latest_app_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_additionalProperties_latest_human_version"></a>
<a id="Return_value_additionalProperties_additionalProperties_latest_human_version"></a>
###### latest_human_version (required)

- Schema name: `Latest Human Version`

Human-readable version of the app.
<a id="Return_value_additionalProperties_additionalProperties_latest_human_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_latest_human_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_additionalProperties_latest_human_version_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_latest_human_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_additionalProperties_latest_human_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_additionalProperties_last_update"></a>
<a id="Return_value_additionalProperties_additionalProperties_last_update"></a>
###### last_update (required)

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
<a id="Return_value_additionalProperties_additionalProperties_last_update_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_last_update_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_additionalProperties_last_update_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_last_update_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_additionalProperties_last_update_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_additionalProperties_name"></a>
<a id="Return_value_additionalProperties_additionalProperties_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the app.

<a id="headingReturn_value_additionalProperties_additionalProperties_recommended"></a>
<a id="Return_value_additionalProperties_additionalProperties_recommended"></a>
###### recommended (required)

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

<a id="headingReturn_value_additionalProperties_additionalProperties_title"></a>
<a id="Return_value_additionalProperties_additionalProperties_title"></a>
###### title (required)

- Schema name: `Title`
- Type: string

Title of the app.

<a id="headingReturn_value_additionalProperties_additionalProperties_maintainers"></a>
<a id="Return_value_additionalProperties_additionalProperties_maintainers"></a>
###### maintainers (required)

- Schema name: `Maintainers`
- Type: array of object

List of app maintainers.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_additionalProperties_additionalProperties_maintainers_items"></a>
###### Maintainer

- Schema name: `Maintainer`
- Type: object
- No Additional Properties
<a id="headingReturn_value_additionalProperties_additionalProperties_maintainers_items_name"></a>
<a id="Return_value_additionalProperties_additionalProperties_maintainers_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the app maintainer.

<a id="headingReturn_value_additionalProperties_additionalProperties_maintainers_items_email"></a>
<a id="Return_value_additionalProperties_additionalProperties_maintainers_items_email"></a>
###### email (required)

- Schema name: `Email`
- Type: string

Email address of the app maintainer.

<a id="headingReturn_value_additionalProperties_additionalProperties_maintainers_items_url"></a>
<a id="Return_value_additionalProperties_additionalProperties_maintainers_items_url"></a>
###### url (required)

- Schema name: `Url`

Website URL of the app maintainer or `null`.
<a id="Return_value_additionalProperties_additionalProperties_maintainers_items_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_maintainers_items_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_additionalProperties_maintainers_items_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_maintainers_items_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_additionalProperties_maintainers_items_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_additionalProperties_tags"></a>
<a id="Return_value_additionalProperties_additionalProperties_tags"></a>
###### tags (required)

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_additionalProperties_additionalProperties_tags_items"></a>
- Type: string

<a id="headingReturn_value_additionalProperties_additionalProperties_screenshots"></a>
<a id="Return_value_additionalProperties_additionalProperties_screenshots"></a>
###### screenshots (required)

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_additionalProperties_additionalProperties_screenshots_items"></a>
- Type: string

<a id="headingReturn_value_additionalProperties_additionalProperties_sources"></a>
<a id="Return_value_additionalProperties_additionalProperties_sources"></a>
###### sources (required)

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_additionalProperties_additionalProperties_sources_items"></a>
- Type: string

<a id="headingReturn_value_additionalProperties_additionalProperties_icon_url"></a>
<a id="Return_value_additionalProperties_additionalProperties_icon_url"></a>
###### icon_url

- Schema name: `Icon Url`
- Default: null

URL of the app icon.
<a id="Return_value_additionalProperties_additionalProperties_icon_url_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_icon_url_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_additionalProperties_additionalProperties_icon_url_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_additionalProperties_additionalProperties_icon_url_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_additionalProperties_additionalProperties_icon_url_anyOf_i1)

- Type: null

<a id="headingReturn_value_additionalProperties_additionalProperties_additionalProperties"></a>
<a id="Return_value_additionalProperties_additionalProperties_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
