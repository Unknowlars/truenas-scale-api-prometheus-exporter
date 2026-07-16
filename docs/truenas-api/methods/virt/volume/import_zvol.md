---
title: virt.volume.import_zvol
kind: method
source_rst: _sources/api_methods_virt.volume.import_zvol.rst.txt
source_html: api_methods_virt.volume.import_zvol.html
required_roles:
  - VIRT_IMAGE_WRITE
---

# virt.volume.import_zvol

## Summary

This method is a job.

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

VirtVolumeImportZvolArgs parameters.
- No Additional Properties
##### to_import (required)

- Schema name: `To Import`
- Type: array of object

Array of ZFS volumes to import as virtualization volumes.
- No Additional Items

###### Each item of this array must be:

###### ZvolImportEntry

- Schema name: `ZvolImportEntry`
- Type: object
- No Additional Properties
####### virt_volume_name (required)

- Schema name: `Virt Volume Name`
- Type: string

Name for the new virtualization volume created from the imported ZFS volume.
- Must be at least `1` characters long
- Must be at most `63` characters long

####### zvol_path (required)

- Schema name: `Zvol Path`
- Type: string

Full path to the ZFS volume device in /dev/zvol/.
- Must be at least `1` characters long

##### clone

- Schema name: `Clone`
- Type: boolean
- Default: false

Whether to clone and promote the ZFS volume instead of importing directly.

### Return value

- Schema name: `VirtVolumeEntry`
- Type: object

The newly created volume from the imported ZFS volume.
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
