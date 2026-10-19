---
title: iscsi.auth.update
kind: method
source_rst: _sources/api_methods_iscsi.auth.update.rst.txt
source_html: api_methods_iscsi.auth.update.html
required_roles:
  - SHARING_ISCSI_AUTH_WRITE
---

# iscsi.auth.update

## Summary

Update iSCSI Authorized Access of `id`.

## Required Roles

- `SHARING_ISCSI_AUTH_WRITE`

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

ID of the iSCSI authentication credential to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Updated iSCSI authentication credential configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_tag"></a>
<a id="Call_parameters_items_i1_tag"></a>
##### tag

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this credential with iSCSI targets.

<a id="headingCall_parameters_items_i1_user"></a>
<a id="Call_parameters_items_i1_user"></a>
##### user

- Schema name: `User`
- Type: string

Username for iSCSI CHAP authentication.

<a id="headingCall_parameters_items_i1_secret"></a>
<a id="Call_parameters_items_i1_secret"></a>
##### secret

- Schema name: `Secret`
- Type: string

Password/secret for iSCSI CHAP authentication.

<a id="headingCall_parameters_items_i1_peeruser"></a>
<a id="Call_parameters_items_i1_peeruser"></a>
##### peeruser

- Schema name: `Peeruser`
- Type: string

Username for mutual CHAP authentication or empty string if not configured.

<a id="headingCall_parameters_items_i1_peersecret"></a>
<a id="Call_parameters_items_i1_peersecret"></a>
##### peersecret

- Schema name: `Peersecret`
- Type: string

Password/secret for mutual CHAP authentication or empty string if not configured.

<a id="headingCall_parameters_items_i1_discovery_auth"></a>
<a id="Call_parameters_items_i1_discovery_auth"></a>
##### discovery_auth

- Schema name: `Discovery Auth`
- Type: enum (of string)

Authentication method for target discovery. If "CHAP_MUTUAL" is selected for target discovery, it is only permitted for a single entry systemwide.
###### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `iSCSITargetAuthCredentialEntry`
- Type: object

The updated iSCSI authentication credential.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI authentication credential.

<a id="headingReturn_value_tag"></a>
<a id="Return_value_tag"></a>
#### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this credential with iSCSI targets.

<a id="headingReturn_value_user"></a>
<a id="Return_value_user"></a>
#### user (required)

- Schema name: `User`
- Type: string

Username for iSCSI CHAP authentication.

<a id="headingReturn_value_secret"></a>
<a id="Return_value_secret"></a>
#### secret (required)

- Schema name: `Secret`
- Type: string

Password/secret for iSCSI CHAP authentication.

<a id="headingReturn_value_peeruser"></a>
<a id="Return_value_peeruser"></a>
#### peeruser

- Schema name: `Peeruser`
- Type: string
- Default: ""

Username for mutual CHAP authentication or empty string if not configured.

<a id="headingReturn_value_peersecret"></a>
<a id="Return_value_peersecret"></a>
#### peersecret

- Schema name: `Peersecret`
- Type: string
- Default: ""

Password/secret for mutual CHAP authentication or empty string if not configured.

<a id="headingReturn_value_discovery_auth"></a>
<a id="Return_value_discovery_auth"></a>
#### discovery_auth

- Schema name: `Discovery Auth`
- Type: enum (of string)
- Default: "NONE"

Authentication method for target discovery. If "CHAP_MUTUAL" is selected for target discovery, it is only permitted for a single entry systemwide.
##### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
