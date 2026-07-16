---
title: iscsi.targetextent.update
kind: method
source_rst: _sources/api_methods_iscsi.targetextent.update.rst.txt
source_html: api_methods_iscsi.targetextent.update.html
required_roles:
  - SHARING_ISCSI_TARGETEXTENT_WRITE
---

# iscsi.targetextent.update

## Summary

Update Associated Target of `id`.

## Required Roles

- `SHARING_ISCSI_TARGETEXTENT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the target-to-extent association to update.

#### Parameter 2: iscsi_target_to_extent_update

#### iscsi_target_to_extent_update

- Schema name: `iscsi_target_to_extent_update`
- Type: object

Updated target-to-extent association configuration data.
- No Additional Properties
##### id

- Schema name: `Id`
- Type: integer

Unique identifier for the target-to-extent association.

##### target

- Schema name: `Target`
- Type: integer

ID of the iSCSI target to associate with the extent.

##### lunid

- Schema name: `Lunid`
- Type: integer

Logical Unit Number (LUN) ID for presenting the extent to the target.

##### extent

- Schema name: `Extent`
- Type: integer

ID of the iSCSI extent to associate with the target.

### Return value

- Schema name: `IscsiTargetToExtentEntry`
- Type: object

The updated target-to-extent association.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the target-to-extent association.

#### target (required)

- Schema name: `Target`
- Type: integer

ID of the iSCSI target to associate with the extent.

#### lunid (required)

- Schema name: `Lunid`
- Type: integer

Logical Unit Number (LUN) ID for presenting the extent to the target.

#### extent (required)

- Schema name: `Extent`
- Type: integer

ID of the iSCSI extent to associate with the target.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
