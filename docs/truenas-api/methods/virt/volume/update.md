---
title: virt.volume.update
kind: method
source_rst: _sources/api_methods_virt.volume.update.rst.txt
source_html: api_methods_virt.volume.update.html
required_roles:
  - VIRT_IMAGE_WRITE
---

# virt.volume.update

## Required Roles

- `VIRT_IMAGE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

Identifier of the virtualization volume to update.
- Must be at least `1` characters long

#### Parameter 2: virt_volume_update

#### virt_volume_update

- Schema name: `virt_volume_update`
- Type: object

Updated configuration for the virtualization volume.
- No Additional Properties
##### size

- Schema name: `Size`
- Type: integer

New size for the volume in MB (minimum 512MB).
- Value must be greater or equal to `512`

### Return value

- Schema name: `VirtVolumeEntry`
- Type: object

The updated virtualization volume configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the virtualization volume.
- Must be at least `1` characters long

#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name of the virtualization volume.
- Must be at least `1` characters long

#### storage_pool (required)

- Schema name: `Storage Pool`
- Type: string

Name of the storage pool containing this volume.
- Must be at least `1` characters long

#### content_type (required)

- Schema name: `Content Type`
- Type: string

Type of content stored in this volume (e.g., 'BLOCK', 'ISO').
- Must be at least `1` characters long

#### created_at (required)

- Schema name: `Created At`
- Type: string

Timestamp when this volume was created.

#### type (required)

- Schema name: `Type`
- Type: string

Volume type indicating its storage backend and characteristics.
- Must be at least `1` characters long

#### config (required)

- Schema name: `Config`
- Type: object

Object containing detailed configuration parameters for this volume.

#### used_by (required)

- Schema name: `Used By`
- Type: array of string

Array of virtual instance names currently using this volume.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
