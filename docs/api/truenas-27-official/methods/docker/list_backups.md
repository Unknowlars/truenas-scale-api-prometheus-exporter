---
title: docker.list_backups
kind: method
source_rst: _sources/api_methods_docker.list_backups.rst.txt
source_html: api_methods_docker.list_backups.html
required_roles:
  - DOCKER_READ
---

# docker.list_backups

## Summary

List existing app backups.

## Required Roles

- `DOCKER_READ`

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

- Schema name: `DockerBackupInfo`
- Type: object

Object mapping backup names to their detailed information.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `BackupInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_additionalProperties_name"></a>
<a id="Return_value_additionalProperties_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the backup.
- Must be at least `1` characters long

<a id="headingReturn_value_additionalProperties_apps"></a>
<a id="Return_value_additionalProperties_apps"></a>
##### apps (required)

- Schema name: `Apps`
- Type: array of object

Array of applications included in this backup.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_additionalProperties_apps_items"></a>
###### AppInfo

- Schema name: `AppInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_additionalProperties_apps_items_id"></a>
<a id="Return_value_additionalProperties_apps_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: string

Unique identifier of the application.
- Must be at least `1` characters long

<a id="headingReturn_value_additionalProperties_apps_items_name"></a>
<a id="Return_value_additionalProperties_apps_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human-readable name of the application.
- Must be at least `1` characters long

<a id="headingReturn_value_additionalProperties_apps_items_state"></a>
<a id="Return_value_additionalProperties_apps_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

Current running state of the application.
- Must be at least `1` characters long

<a id="headingReturn_value_additionalProperties_snapshot_name"></a>
<a id="Return_value_additionalProperties_snapshot_name"></a>
##### snapshot_name (required)

- Schema name: `Snapshot Name`
- Type: string

ZFS snapshot name associated with this backup.
- Must be at least `1` characters long

<a id="headingReturn_value_additionalProperties_created_on"></a>
<a id="Return_value_additionalProperties_created_on"></a>
##### created_on (required)

- Schema name: `Created On`
- Type: string

Timestamp when the backup was created.
- Must be at least `1` characters long

<a id="headingReturn_value_additionalProperties_backup_path"></a>
<a id="Return_value_additionalProperties_backup_path"></a>
##### backup_path (required)

- Schema name: `Backup Path`
- Type: string

Filesystem path where the backup is stored.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
