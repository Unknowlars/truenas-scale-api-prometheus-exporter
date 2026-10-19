---
title: iscsi.auth.query
kind: event
source_rst: _sources/api_events_iscsi.auth.query.rst.txt
source_html: api_events_iscsi.auth.query.html
required_roles:
  - SHARING_ISCSI_AUTH_READ
---

# iscsi.auth.query

## Summary

Sent on iscsi.auth changes.

## Required Roles

- `SHARING_ISCSI_AUTH_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `iSCSITargetAuthCredentialAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `iSCSITargetAuthCredentialEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI authentication credential.

<a id="headingADDED_fields_tag"></a>
<a id="ADDED_fields_tag"></a>
##### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this credential with iSCSI targets. Must be unique among iSCSI Authorized Accesses.

<a id="headingADDED_fields_user"></a>
<a id="ADDED_fields_user"></a>
##### user (required)

- Schema name: `User`
- Type: string

Username for iSCSI CHAP authentication.

<a id="headingADDED_fields_secret"></a>
<a id="ADDED_fields_secret"></a>
##### secret (required)

- Schema name: `Secret`
- Type: string

Password/secret for iSCSI CHAP authentication. Must be 12-16 characters.

<a id="headingADDED_fields_peeruser"></a>
<a id="ADDED_fields_peeruser"></a>
##### peeruser

- Schema name: `Peeruser`
- Type: string
- Default: ""

Username for mutual CHAP authentication or empty string if not configured.

<a id="headingADDED_fields_peersecret"></a>
<a id="ADDED_fields_peersecret"></a>
##### peersecret

- Schema name: `Peersecret`
- Type: string
- Default: ""

Password/secret for mutual CHAP authentication, or empty string if not configured. Must be 12-16 characters when set and must differ from `secret`.

<a id="headingADDED_fields_discovery_auth"></a>
<a id="ADDED_fields_discovery_auth"></a>
##### discovery_auth

- Schema name: `Discovery Auth`
- Type: enum (of string)
- Default: "NONE"

Authentication method for target discovery. If "CHAP_MUTUAL" is selected for target discovery, it is only permitted for a single entry systemwide.
###### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `iSCSITargetAuthCredentialChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `iSCSITargetAuthCredentialEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI authentication credential.

<a id="headingCHANGED_fields_tag"></a>
<a id="CHANGED_fields_tag"></a>
##### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this credential with iSCSI targets. Must be unique among iSCSI Authorized Accesses.

<a id="headingCHANGED_fields_user"></a>
<a id="CHANGED_fields_user"></a>
##### user (required)

- Schema name: `User`
- Type: string

Username for iSCSI CHAP authentication.

<a id="headingCHANGED_fields_secret"></a>
<a id="CHANGED_fields_secret"></a>
##### secret (required)

- Schema name: `Secret`
- Type: string

Password/secret for iSCSI CHAP authentication. Must be 12-16 characters.

<a id="headingCHANGED_fields_peeruser"></a>
<a id="CHANGED_fields_peeruser"></a>
##### peeruser

- Schema name: `Peeruser`
- Type: string
- Default: ""

Username for mutual CHAP authentication or empty string if not configured.

<a id="headingCHANGED_fields_peersecret"></a>
<a id="CHANGED_fields_peersecret"></a>
##### peersecret

- Schema name: `Peersecret`
- Type: string
- Default: ""

Password/secret for mutual CHAP authentication, or empty string if not configured. Must be 12-16 characters when set and must differ from `secret`.

<a id="headingCHANGED_fields_discovery_auth"></a>
<a id="CHANGED_fields_discovery_auth"></a>
##### discovery_auth

- Schema name: `Discovery Auth`
- Type: enum (of string)
- Default: "NONE"

Authentication method for target discovery. If "CHAP_MUTUAL" is selected for target discovery, it is only permitted for a single entry systemwide.
###### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `iSCSITargetAuthCredentialRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
