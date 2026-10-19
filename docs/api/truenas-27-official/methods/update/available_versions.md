---
title: update.available_versions
kind: method
source_rst: _sources/api_methods_update.available_versions.rst.txt
source_html: api_methods_update.available_versions.html
required_roles:
  - SYSTEM_UPDATE_READ
---

# update.available_versions

## Summary

TrueNAS versions available for update.

## Required Roles

- `SYSTEM_UPDATE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of available system update versions across all trains.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### UpdateAvailableVersion

- Schema name: `UpdateAvailableVersion`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_train"></a>
<a id="Return_value_items_train"></a>
##### train (required)

- Schema name: `Train`
- Type: string

Train that provides this version.

<a id="headingReturn_value_items_version"></a>
<a id="Return_value_items_version"></a>
##### version (required)

- Schema name: `UpdateStatusNewVersion`
- Type: object

Detailed information about this available version.
- No Additional Properties
<a id="headingReturn_value_items_version_version"></a>
<a id="Return_value_items_version_version"></a>
###### version (required)

- Schema name: `Version`
- Type: string

Newly available version number.

<a id="headingReturn_value_items_version_manifest"></a>
<a id="Return_value_items_version_manifest"></a>
###### manifest (required)

- Schema name: `Manifest`
- Type: object

Object containing detailed version information and metadata.

<a id="headingReturn_value_items_version_release_notes"></a>
<a id="Return_value_items_version_release_notes"></a>
###### release_notes (required)

- Schema name: `Release Notes`

Release notes.
<a id="Return_value_items_version_release_notes_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_version_release_notes_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_version_release_notes_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_items_version_release_notes_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_version_release_notes_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_version_release_notes_url"></a>
<a id="Return_value_items_version_release_notes_url"></a>
###### release_notes_url (required)

- Schema name: `Release Notes Url`
- Type: string

Release notes URL.
- Must be at most `2147483647` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
