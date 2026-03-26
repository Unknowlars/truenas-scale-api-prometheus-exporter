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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: onedrive_list_drives

#### onedrive_list_drives

- Schema name: `onedrive_list_drives`
- Type: object

CloudSyncOneDriveListDrivesArgs parameters.
- No Additional Properties
##### client_id

- Schema name: `Client Id`
- Type: string
- Default: ""

OAuth client ID for OneDrive API access.

##### client_secret

- Schema name: `Client Secret`
- Type: string
- Default: ""

OAuth client secret for OneDrive API access.

##### token (required)

- Schema name: `Token`
- Type: string

OAuth access token for OneDrive authentication.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: array of object

Array of available OneDrive drives.
- No Additional Items

#### Each item of this array must be:

#### CloudSyncOneDriveListDrivesDrive

- Schema name: `CloudSyncOneDriveListDrivesDrive`
- Type: object
- No Additional Properties
##### drive_id (required)

- Schema name: `Drive Id`
- Type: string

OneDrive drive identifier.

##### drive_type (required)

- Schema name: `Drive Type`
- Type: enum (of string)

Type of OneDrive.

##### name (required)

- Schema name: `Name`
- Type: string

Display name of the OneDrive.

##### description (required)

- Schema name: `Description`
- Type: string

Description of the OneDrive.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
