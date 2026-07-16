---
title: virt.volume.create
kind: method
source_rst: _sources/api_methods_virt.volume.create.rst.txt
source_html: api_methods_virt.volume.create.html
required_roles:
  - VIRT_IMAGE_WRITE
---

# virt.volume.create

## Required Roles

- `VIRT_IMAGE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: virt_volume_create

#### virt_volume_create

- Schema name: `virt_volume_create`
- Type: object

VirtVolumeCreateArgs parameters.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Name for the new virtualization volume (alphanumeric, dashes, dots, underscores).
- Must be at least `1` characters long
- Must be at most `63` characters long

##### content_type

- Schema name: `Content Type`
- Type: const
- Default: "BLOCK"

##### size

- Schema name: `Size`
- Type: integer
- Default: 1024

Size of volume in MB and it should at least be 512 MB.
- Value must be greater or equal to `512`

##### storage_pool

- Schema name: `Storage Pool`
- Default: null

Storage pool in which to create the volume. This must be one of pools listed in virt.global.config output under `storage_pools`. If the value is None, then the pool defined as `pool` in virt.global.config will be used.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

### Return value

- Schema name: `VirtVolumeEntry`
- Type: object

The newly created virtualization volume configuration.
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
