---
title: iscsi.portal.create
kind: method
source_rst: _sources/api_methods_iscsi.portal.create.rst.txt
source_html: api_methods_iscsi.portal.create.html
required_roles:
  - SHARING_ISCSI_PORTAL_WRITE
---

# iscsi.portal.create

## Summary

Create a new iSCSI Portal.

## Required Roles

- `SHARING_ISCSI_PORTAL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: iscsi_portal_create

#### iscsi_portal_create

- Schema name: `iscsi_portal_create`
- Type: object

iSCSI portal configuration data for creation.
- No Additional Properties
##### listen (required)

- Schema name: `Listen`
- Type: array of object

Array of IP addresses for the portal to listen on.
- No Additional Items

###### Each item of this array must be:

###### IscsiPortalIP

- Schema name: `IscsiPortalIP`
- Type: object
- No Additional Properties
####### ip (required)

- Schema name: `Ip`
- Type: string

IP address for the iSCSI portal to listen on.
- Must be at least `1` characters long

##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the portal.

### Return value

- Schema name: `IscsiPortalEntry`
- Type: object

The created iSCSI portal configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI portal.

#### listen (required)

- Schema name: `Listen`
- Type: array of object

Array of IP address and port combinations for the portal to listen on.
- No Additional Items

##### Each item of this array must be:

##### IscsiPortalIPInfo

- Schema name: `IscsiPortalIPInfo`
- Type: object
- No Additional Properties
###### ip (required)

- Schema name: `Ip`
- Type: string

IP address for the iSCSI portal to listen on.
- Must be at least `1` characters long

###### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the iSCSI portal.

#### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this portal with iSCSI targets.

#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the portal.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
