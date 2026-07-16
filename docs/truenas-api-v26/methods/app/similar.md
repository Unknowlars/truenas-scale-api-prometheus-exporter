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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: app_name

#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to find similar apps for.
- Must be at least `1` characters long

#### Parameter 2: train

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

### Return value

- Schema name: `Result`
- Type: array of object

Array of applications similar to the requested one.
- No Additional Items

#### Each item of this array must be:

#### AppAvailableItem

- Schema name: `AppAvailableItem`
- Type: object
##### app_readme (required)

- Schema name: `App Readme`

HTML content of the app README.
###### Any of

####### Option 1

- Type: string
- Must be at most `2147483647` characters long

####### Option 2

- Type: null

##### categories (required)

- Schema name: `Categories`
- Type: array of string

List of categories for the app.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### description (required)

- Schema name: `Description`
- Type: string

Short description of the app.

##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Health status of the app.

##### healthy_error

- Schema name: `Healthy Error`
- Default: null

Error if app is not healthy.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### home (required)

- Schema name: `Home`
- Type: string

Homepage URL of the app.

##### location (required)

- Schema name: `Location`
- Type: string

Local path to the app's location.

##### latest_version (required)

- Schema name: `Latest Version`

Latest available app version.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### latest_app_version (required)

- Schema name: `Latest App Version`

Latest available app version in repository.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### latest_human_version (required)

- Schema name: `Latest Human Version`

Human-readable version of the app.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### last_update (required)

- Schema name: `Last Update`

Timestamp of the last update in ISO format.
###### Any of

####### Option 1

- Type: string
- Type: Format: date-time

####### Option 2

- Type: null

##### name (required)

- Schema name: `Name`
- Type: string

Name of the app.

##### recommended (required)

- Schema name: `Recommended`
- Type: boolean

Indicates if the app is recommended.

##### title (required)

- Schema name: `Title`
- Type: string

Title of the app.

##### maintainers (required)

- Schema name: `Maintainers`
- Type: array of object

List of app maintainers.
- No Additional Items

###### Each item of this array must be:

###### Maintainer

- Schema name: `Maintainer`
- Type: object
- No Additional Properties
####### name (required)

- Schema name: `Name`
- Type: string

Name of the app maintainer.

####### email (required)

- Schema name: `Email`
- Type: string

Email address of the app maintainer.

####### url (required)

- Schema name: `Url`

Website URL of the app maintainer or `null`.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

##### tags (required)

- Schema name: `Tags`
- Type: array of string

Tags associated with the app.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### screenshots (required)

- Schema name: `Screenshots`
- Type: array of string

List of screenshot URLs.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### sources (required)

- Schema name: `Sources`
- Type: array of string

List of source URLs.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### icon_url

- Schema name: `Icon Url`
- Default: null

URL of the app icon.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### catalog (required)

- Schema name: `Catalog`
- Type: string

Name of the catalog this application comes from.
- Must be at least `1` characters long

##### installed (required)

- Schema name: `Installed`
- Type: boolean

Whether this application is currently installed on the system.

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

##### popularity_rank (required)

- Schema name: `Popularity Rank`

Popularity ranking of this application. Lower numbers indicate higher popularity. `null` if not ranked.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
