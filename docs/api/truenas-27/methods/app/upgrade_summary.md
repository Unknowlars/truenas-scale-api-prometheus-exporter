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

Name of the application to get upgrade summary for.
- Must be at least `1` characters long

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {"app_version": "latest"}

Options specifying the target version for the summary.
- No Additional Properties
<a id="headingCall_parameters_items_i1_app_version"></a>
<a id="Call_parameters_items_i1_app_version"></a>
##### app_version

- Schema name: `App Version`
- Type: string
- Default: "latest"

Target version to generate upgrade summary for. Use 'latest' for the newest available version.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `AppUpgradeSummaryResult`
- Type: object

AppUpgradeSummaryResult return fields.
- No Additional Properties
<a id="headingReturn_value_latest_version"></a>
<a id="Return_value_latest_version"></a>
#### latest_version (required)

- Schema name: `Latest Version`
- Type: string

Latest version available for the app.

<a id="headingReturn_value_latest_human_version"></a>
<a id="Return_value_latest_human_version"></a>
#### latest_human_version (required)

- Schema name: `Latest Human Version`
- Type: string

Latest human readable version available for the app.

<a id="headingReturn_value_upgrade_version"></a>
<a id="Return_value_upgrade_version"></a>
#### upgrade_version (required)

- Schema name: `Upgrade Version`
- Type: string

Version user has requested to be upgraded at.

<a id="headingReturn_value_upgrade_human_version"></a>
<a id="Return_value_upgrade_human_version"></a>
#### upgrade_human_version (required)

- Schema name: `Upgrade Human Version`
- Type: string

Human-readable version user has requested to be upgraded at.

<a id="headingReturn_value_available_versions_for_upgrade"></a>
<a id="Return_value_available_versions_for_upgrade"></a>
#### available_versions_for_upgrade (required)

- Schema name: `Available Versions For Upgrade`
- Type: array of object

List of available versions for upgrade.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_available_versions_for_upgrade_items"></a>
##### AppVersionInfo

- Schema name: `AppVersionInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_available_versions_for_upgrade_items_version"></a>
<a id="Return_value_available_versions_for_upgrade_items_version"></a>
###### version (required)

- Schema name: `Version`
- Type: string

Version of the app.

<a id="headingReturn_value_available_versions_for_upgrade_items_human_version"></a>
<a id="Return_value_available_versions_for_upgrade_items_human_version"></a>
###### human_version (required)

- Schema name: `Human Version`
- Type: string

Human-readable version of the app.

<a id="headingReturn_value_changelog"></a>
<a id="Return_value_changelog"></a>
#### changelog (required)

- Schema name: `Changelog`

Changelog or release notes for the upgrade version. `null` if not available.
<a id="Return_value_changelog_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_changelog_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_changelog_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_changelog_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_changelog_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
