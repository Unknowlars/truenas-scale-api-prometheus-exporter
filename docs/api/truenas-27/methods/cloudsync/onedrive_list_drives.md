---
title: cloudsync.onedrive_list_drives
kind: method
source_rst: _sources/api_methods_cloudsync.onedrive_list_drives.rst.txt
source_html: api_methods_cloudsync.onedrive_list_drives.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.onedrive_list_drives

## Summary

Lists all available drives and their types for given Microsoft OneDrive credentials.

## Required Roles

- `CLOUD_SYNC_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: onedrive_list_drives

<a id="Call_parameters_items_i0"></a>
#### onedrive_list_drives

- Schema name: `onedrive_list_drives`
- Type: object

CloudSyncOneDriveListDrivesArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_client_id"></a>
<a id="Call_parameters_items_i0_client_id"></a>
##### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for OneDrive API access.

<a id="headingCall_parameters_items_i0_client_secret"></a>
<a id="Call_parameters_items_i0_client_secret"></a>
##### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for OneDrive API access.

<a id="headingCall_parameters_items_i0_token"></a>
<a id="Call_parameters_items_i0_token"></a>
##### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for OneDrive authentication.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of available OneDrive drives.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### CloudSyncOneDriveListDrivesDrive

- Schema name: `CloudSyncOneDriveListDrivesDrive`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_drive_id"></a>
<a id="Return_value_items_drive_id"></a>
##### drive_id (required)

- Schema name: `Drive Id`
- Type: string

OneDrive drive identifier.

<a id="headingReturn_value_items_drive_type"></a>
<a id="Return_value_items_drive_type"></a>
##### drive_type (required)

- Schema name: `Drive Type`
- Type: enum (of string)

Type of OneDrive.
###### Must be one of:

- "PERSONAL"
- "BUSINESS"
- "DOCUMENT_LIBRARY"

<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Display name of the OneDrive.

<a id="headingReturn_value_items_description"></a>
<a id="Return_value_items_description"></a>
##### description (required)

- Schema name: `Description`
- Type: string

Description of the OneDrive.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
