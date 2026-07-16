---
title: iscsi.targetextent.create
kind: method
source_rst: _sources/api_methods_iscsi.targetextent.create.rst.txt
source_html: api_methods_iscsi.targetextent.create.html
required_roles:
  - SHARING_ISCSI_TARGETEXTENT_WRITE
---

# iscsi.targetextent.create

## Summary

Create an Associated Target.

`lunid` will be automatically assigned if it is not provided based on the `target`.

## Required Roles

- `SHARING_ISCSI_TARGETEXTENT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: iscsi_target_to_extent_create

#### iscsi_target_to_extent_create

- Schema name: `iscsi_target_to_extent_create`
- Type: object

Target-to-extent association configuration data for creation.
- No Additional Properties
##### target (required)

- Schema name: `Target`
- Type: integer

ID of the iSCSI target to associate with the extent.

##### lunid

- Schema name: `Lunid`
- Default: null

LUN ID to assign or `null` to auto-assign the next available LUN.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### extent (required)

- Schema name: `Extent`
- Type: integer

ID of the iSCSI extent to associate with the target.

### Return value

- Schema name: `IscsiTargetToExtentEntry`
- Type: object

The created target-to-extent association.
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
