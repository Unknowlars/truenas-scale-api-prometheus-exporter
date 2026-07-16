---
title: virt.volume.query
kind: event
source_rst: _sources/api_events_virt.volume.query.rst.txt
source_html: api_events_virt.volume.query.html
required_roles:
  - VIRT_IMAGE_READ
---

# virt.volume.query

## Summary

Sent on virt.volume changes.

## Required Roles

- `VIRT_IMAGE_READ`

## Schema

- Type: object

### ADDED

- Schema name: `VirtVolumeAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `VirtVolumeEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the virtualization volume.
- Must be at least `1` characters long

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name of the virtualization volume.
- Must be at least `1` characters long

##### storage_pool (required)

- Schema name: `Storage Pool`
- Type: string

Name of the storage pool containing this volume.
- Must be at least `1` characters long

##### content_type (required)

- Schema name: `Content Type`
- Type: string

Type of content stored in this volume (e.g., 'BLOCK', 'ISO').
- Must be at least `1` characters long

##### created_at (required)

- Schema name: `Created At`
- Type: string

Timestamp when this volume was created.

##### type (required)

- Schema name: `Type`
- Type: string

Volume type indicating its storage backend and characteristics.
- Must be at least `1` characters long

##### config (required)

- Schema name: `Config`
- Type: object

Object containing detailed configuration parameters for this volume.

##### used_by (required)

- Schema name: `Used By`
- Type: array of string

Array of virtual instance names currently using this volume.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

### CHANGED

- Schema name: `VirtVolumeChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `VirtVolumeEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the virtualization volume.
- Must be at least `1` characters long

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name of the virtualization volume.
- Must be at least `1` characters long

##### storage_pool (required)

- Schema name: `Storage Pool`
- Type: string

Name of the storage pool containing this volume.
- Must be at least `1` characters long

##### content_type (required)

- Schema name: `Content Type`
- Type: string

Type of content stored in this volume (e.g., 'BLOCK', 'ISO').
- Must be at least `1` characters long

##### created_at (required)

- Schema name: `Created At`
- Type: string

Timestamp when this volume was created.

##### type (required)

- Schema name: `Type`
- Type: string

Volume type indicating its storage backend and characteristics.
- Must be at least `1` characters long

##### config (required)

- Schema name: `Config`
- Type: object

Object containing detailed configuration parameters for this volume.

##### used_by (required)

- Schema name: `Used By`
- Type: array of string

Array of virtual instance names currently using this volume.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

### REMOVED

- Schema name: `VirtVolumeRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
