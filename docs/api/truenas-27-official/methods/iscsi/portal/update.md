---
title: iscsi.portal.update
kind: method
source_rst: _sources/api_methods_iscsi.portal.update.rst.txt
source_html: api_methods_iscsi.portal.update.html
required_roles:
  - SHARING_ISCSI_PORTAL_WRITE
---

# iscsi.portal.update

## Summary

Update iSCSI Portal `id`.

## Required Roles

- `SHARING_ISCSI_PORTAL_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the iSCSI portal to update.

#### Parameter 2: iscsi_portal_update

<a id="Call_parameters_items_i1"></a>
#### iscsi_portal_update

- Schema name: `iscsi_portal_update`
- Type: object

Updated iSCSI portal configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_listen"></a>
<a id="Call_parameters_items_i1_listen"></a>
##### listen

- Schema name: `Listen`
- Type: array of object

Array of IP addresses for the portal to listen on.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_listen_items"></a>
###### IscsiPortalIP

- Schema name: `IscsiPortalIP`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_listen_items_ip"></a>
<a id="Call_parameters_items_i1_listen_items_ip"></a>
###### ip (required)

- Schema name: `Ip`
- Type: string

IP address for the iSCSI portal to listen on.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_comment"></a>
<a id="Call_parameters_items_i1_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string

Optional comment describing the portal.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ISCSIPortalEntry`
- Type: object

The updated iSCSI portal configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI portal.

<a id="headingReturn_value_listen"></a>
<a id="Return_value_listen"></a>
#### listen (required)

- Schema name: `Listen`
- Type: array of object

Array of IP address and port combinations for the portal to listen on.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_listen_items"></a>
##### IscsiPortalIPInfo

- Schema name: `IscsiPortalIPInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_listen_items_ip"></a>
<a id="Return_value_listen_items_ip"></a>
###### ip (required)

- Schema name: `Ip`
- Type: string

IP address for the iSCSI portal to listen on.
- Must be at least `1` characters long

<a id="headingReturn_value_listen_items_port"></a>
<a id="Return_value_listen_items_port"></a>
###### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the iSCSI portal.

<a id="headingReturn_value_tag"></a>
<a id="Return_value_tag"></a>
#### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this portal with iSCSI targets.

<a id="headingReturn_value_comment"></a>
<a id="Return_value_comment"></a>
#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the portal.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
