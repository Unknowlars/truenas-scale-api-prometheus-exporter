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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: catalog_apps_options

#### catalog_apps_options

- Schema name: `catalog_apps_options`
- Type: object

CatalogAppsArgs parameters.
- No Additional Properties
##### cache

- Schema name: `Cache`
- Type: boolean
- Default: true

Whether to use cached catalog data if available.

##### cache_only

- Schema name: `Cache Only`
- Type: boolean
- Default: false

Whether to only return cached data without fetching updates.

##### retrieve_all_trains

- Schema name: `Retrieve All Trains`
- Type: boolean
- Default: true

Whether to retrieve apps from all available trains.

##### trains

- Schema name: `Trains`
- Type: array of string

Specific train names to retrieve apps from (empty array means all trains).
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: object

Object mapping train names to their app information.
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `CatalogTrainInfo`
- Type: object
##### Additional Properties

Each additional property must conform to the following schema
- Schema name: `CatalogAppInfo`
- Type: object
###### app_readme (required)

- Schema name: `App Readme`

HTML content of the app README.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### categories (required)

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### description (required)

- Schema name: `Description`
- Type: string

Short description of the app.

###### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

###### healthy_error

- Schema name: `Healthy Error`
- Default: null

Error if app is not healthy.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### home (required)

- Schema name: `Home`
- Type: string

Homepage URL of the app.

###### location (required)

- Schema name: `Location`
- Type: string

Local path to the app's location.

###### latest_version (required)

- Schema name: `Latest Version`

Latest available app version.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### latest_app_version (required)

- Schema name: `Latest App Version`

Latest available app version in repository.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### latest_human_version (required)

- Schema name: `Latest Human Version`

Human-readable version of the app.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### last_update (required)

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
####### Any of

######## Option 1

- Type: string
- Type: Format: date-time

######## Option 2

- Type: null

###### name (required)

- Schema name: `Name`
- Type: string

Name of the app.

###### recommended (required)

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

###### title (required)

- Schema name: `Title`
- Type: string

Title of the app.

###### maintainers (required)

- Schema name: `Maintainers`
- Type: array of object

List of app maintainers.
- No Additional Items

####### Each item of this array must be:

####### Maintainer

- Schema name: `Maintainer`
- Type: object
- No Additional Properties
######## name (required)

- Schema name: `Name`
- Type: string

Name of the app maintainer.

######## email (required)

- Schema name: `Email`
- Type: string

Email address of the app maintainer.

######## url (required)

- Schema name: `Url`

Website URL of the app maintainer or `null`.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

###### tags (required)

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### screenshots (required)

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### sources (required)

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### icon_url

- Schema name: `Icon Url`
- Default: null

URL of the app icon.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
