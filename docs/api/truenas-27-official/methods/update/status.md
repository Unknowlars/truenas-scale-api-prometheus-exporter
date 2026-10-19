---
title: update.status
kind: method
source_rst: _sources/api_methods_update.status.rst.txt
source_html: api_methods_update.status.html
required_roles:
  - SYSTEM_UPDATE_READ
---

# update.status

## Summary

Update status.

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

- Schema name: `UpdateStatus`
- Type: object

Current system update status and availability information.
- No Additional Properties
<a id="headingReturn_value_code"></a>
<a id="Return_value_code"></a>
#### code (required)

- Schema name: `Code`
- Type: enum (of string)

Status code: * NORMAL - normal status, see `status` dictionary for details. * ERROR - an error occurred, see `error` for details.
##### Must be one of:

- "NORMAL"
- "ERROR"

<a id="headingReturn_value_status"></a>
<a id="Return_value_status"></a>
#### status (required)

Detailed update status information. `null` if code is ERROR.
<a id="Return_value_status_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_status_anyOf_i0"></a>
###### [UpdateStatusStatus](#tab-pane_Return_value_status_anyOf_i0)

- Schema name: `UpdateStatusStatus`
- Type: object
- No Additional Properties
<a id="headingReturn_value_status_anyOf_i0_current_version"></a>
<a id="Return_value_status_anyOf_i0_current_version"></a>
###### current_version (required)

- Schema name: `UpdateStatusCurrentVersion`
- Type: object

Currently running system version information.
- No Additional Properties
<a id="headingReturn_value_status_anyOf_i0_current_version_train"></a>
<a id="Return_value_status_anyOf_i0_current_version_train"></a>
###### train (required)

- Schema name: `Train`
- Type: string

Train name.

<a id="headingReturn_value_status_anyOf_i0_current_version_profile"></a>
<a id="Return_value_status_anyOf_i0_current_version_profile"></a>
###### profile (required)

- Schema name: `Profile`
- Type: string

Update profile assigned for the version.

<a id="headingReturn_value_status_anyOf_i0_current_version_matches_profile"></a>
<a id="Return_value_status_anyOf_i0_current_version_matches_profile"></a>
###### matches_profile (required)

- Schema name: `Matches Profile`
- Type: boolean

Whether the system version running matches the configured update profile.

<a id="headingReturn_value_status_anyOf_i0_new_version"></a>
<a id="Return_value_status_anyOf_i0_new_version"></a>
###### new_version (required)

New system version information (or `null` if no new system version is available).
<a id="Return_value_status_anyOf_i0_new_version_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_status_anyOf_i0_new_version_anyOf_i0"></a>
###### [UpdateStatusNewVersion](#tab-pane_Return_value_status_anyOf_i0_new_version_anyOf_i0)

- Schema name: `UpdateStatusNewVersion`
- Type: object
- No Additional Properties
<a id="headingReturn_value_status_anyOf_i0_new_version_anyOf_i0_version"></a>
<a id="Return_value_status_anyOf_i0_new_version_anyOf_i0_version"></a>
###### version (required)

- Schema name: `Version`
- Type: string

Newly available version number.

<a id="headingReturn_value_status_anyOf_i0_new_version_anyOf_i0_manifest"></a>
<a id="Return_value_status_anyOf_i0_new_version_anyOf_i0_manifest"></a>
###### manifest (required)

- Schema name: `Manifest`
- Type: object

Object containing detailed version information and metadata.

<a id="headingReturn_value_status_anyOf_i0_new_version_anyOf_i0_release_notes"></a>
<a id="Return_value_status_anyOf_i0_new_version_anyOf_i0_release_notes"></a>
###### release_notes (required)

- Schema name: `Release Notes`

Release notes.
<a id="Return_value_status_anyOf_i0_new_version_anyOf_i0_release_notes_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_status_anyOf_i0_new_version_anyOf_i0_release_notes_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_status_anyOf_i0_new_version_anyOf_i0_release_notes_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_status_anyOf_i0_new_version_anyOf_i0_release_notes_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_status_anyOf_i0_new_version_anyOf_i0_release_notes_anyOf_i1)

- Type: null

<a id="headingReturn_value_status_anyOf_i0_new_version_anyOf_i0_release_notes_url"></a>
<a id="Return_value_status_anyOf_i0_new_version_anyOf_i0_release_notes_url"></a>
###### release_notes_url (required)

- Schema name: `Release Notes Url`
- Type: string

Release notes URL.
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_status_anyOf_i0_new_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_status_anyOf_i0_new_version_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_status_anyOf_i1)

- Type: null

<a id="headingReturn_value_error"></a>
<a id="Return_value_error"></a>
#### error (required)

Error message if code is ERROR. `null` otherwise.
<a id="Return_value_error_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_error_anyOf_i0"></a>
###### [UpdateStatusError](#tab-pane_Return_value_error_anyOf_i0)

- Schema name: `UpdateStatusError`
- Type: object
- No Additional Properties
<a id="headingReturn_value_error_anyOf_i0_errname"></a>
<a id="Return_value_error_anyOf_i0_errname"></a>
###### errname (required)

- Schema name: `Errname`
- Type: string

Error code (i.e. ENONET).

<a id="headingReturn_value_error_anyOf_i0_reason"></a>
<a id="Return_value_error_anyOf_i0_reason"></a>
###### reason (required)

- Schema name: `Reason`
- Type: string

Error text.
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_update_download_progress"></a>
<a id="Return_value_update_download_progress"></a>
#### update_download_progress (required)

Current update download progress.
<a id="Return_value_update_download_progress_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_update_download_progress_anyOf_i0"></a>
###### [UpdateDownloadProgress](#tab-pane_Return_value_update_download_progress_anyOf_i0)

- Schema name: `UpdateDownloadProgress`
- Type: object
- No Additional Properties
<a id="headingReturn_value_update_download_progress_anyOf_i0_percent"></a>
<a id="Return_value_update_download_progress_anyOf_i0_percent"></a>
###### percent (required)

- Schema name: `Percent`
- Type: number

Download completion percentage (0.0 to 100.0).

<a id="headingReturn_value_update_download_progress_anyOf_i0_description"></a>
<a id="Return_value_update_download_progress_anyOf_i0_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the current download activity.
- Must be at most `2147483647` characters long

<a id="headingReturn_value_update_download_progress_anyOf_i0_version"></a>
<a id="Return_value_update_download_progress_anyOf_i0_version"></a>
###### version (required)

- Schema name: `Version`
- Type: string

Version number being downloaded.

<a id="tab-pane_Return_value_update_download_progress_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_update_download_progress_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
