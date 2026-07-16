---
title: app.upgrade_summary
kind: method
source_rst: _sources/api_methods_app.upgrade_summary.rst.txt
source_html: api_methods_app.upgrade_summary.html
required_roles:
  - APPS_READ
---

# app.upgrade_summary

## Summary

Retrieve upgrade summary for `app_name`.

## Required Roles

- `APPS_READ`

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

Name of the application to get upgrade summary for.
- Must be at least `1` characters long

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {"app_version": "latest"}

Options specifying the target version for the summary.
- No Additional Properties
##### app_version

- Schema name: `App Version`
- Type: string
- Default: "latest"

Target version to generate upgrade summary for. Use 'latest' for the newest available version.
- Must be at least `1` characters long

### Return value

- Schema name: `AppUpgradeSummaryResult`
- Type: object

AppUpgradeSummaryResult return fields.
- No Additional Properties
#### latest_version (required)

- Schema name: `Latest Version`
- Type: string

Latest version available for the app.

#### latest_human_version (required)

- Schema name: `Latest Human Version`
- Type: string

Latest human readable version available for the app.

#### upgrade_version (required)

- Schema name: `Upgrade Version`
- Type: string

Version user has requested to be upgraded at.

#### upgrade_human_version (required)

- Schema name: `Upgrade Human Version`
- Type: string

Human-readable version user has requested to be upgraded at.

#### available_versions_for_upgrade (required)

- Schema name: `Available Versions For Upgrade`
- Type: array of object

List of available versions for upgrade.
- No Additional Items

##### Each item of this array must be:

##### AppVersionInfo

- Schema name: `AppVersionInfo`
- Type: object
- No Additional Properties
###### version (required)

- Schema name: `Version`
- Type: string

Version of the app.

###### human_version (required)

- Schema name: `Human Version`
- Type: string

Human-readable version of the app.

#### changelog (required)

- Schema name: `Changelog`

Changelog or release notes for the upgrade version. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
