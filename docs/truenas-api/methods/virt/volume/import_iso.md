---
title: virt.volume.import_iso
kind: method
source_rst: _sources/api_methods_virt.volume.import_iso.rst.txt
source_html: api_methods_virt.volume.import_iso.html
required_roles:
  - VIRT_IMAGE_WRITE
---

# virt.volume.import_iso

## Summary

This method is a job.

*This job CAN be used with file upload.* See :ref:`uploading-files`.

## Required Roles

- `VIRT_IMAGE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: virt_volume_import_iso

#### virt_volume_import_iso

- Schema name: `virt_volume_import_iso`
- Type: object

VirtVolumeImportIsoArgs parameters.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Specify name of the newly created volume from the ISO specified.
- Must be at least `1` characters long
- Must be at most `63` characters long

##### iso_location

- Schema name: `Iso Location`
- Default: null

Path to the ISO file to import. `null` if uploading via `upload_iso`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### upload_iso

- Schema name: `Upload Iso`
- Type: boolean
- Default: false

Whether to upload an ISO file instead of using a local file path.

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

The newly created volume from the imported ISO file.
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
