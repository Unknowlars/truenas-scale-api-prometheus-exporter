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

### ADDED

- Schema name: `IscsiAuthAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `IscsiAuthEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI authentication credential.

##### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this credential with iSCSI targets.

##### user (required)

- Schema name: `User`
- Type: string

Username for iSCSI CHAP authentication.

##### secret (required)

- Schema name: `Secret`
- Type: string

Password/secret for iSCSI CHAP authentication.

##### peeruser

- Schema name: `Peeruser`
- Type: string
- Default: ""

Username for mutual CHAP authentication or empty string if not configured.

##### peersecret

- Schema name: `Peersecret`
- Type: string
- Default: ""

Password/secret for mutual CHAP authentication or empty string if not configured.

##### discovery_auth

- Schema name: `Discovery Auth`
- Type: enum (of string)
- Default: "NONE"

Authentication method for target discovery. If "CHAP_MUTUAL" is selected for target discovery, it is only permitted for a single entry systemwide.

### CHANGED

- Schema name: `IscsiAuthChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `IscsiAuthEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI authentication credential.

##### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this credential with iSCSI targets.

##### user (required)

- Schema name: `User`
- Type: string

Username for iSCSI CHAP authentication.

##### secret (required)

- Schema name: `Secret`
- Type: string

Password/secret for iSCSI CHAP authentication.

##### peeruser

- Schema name: `Peeruser`
- Type: string
- Default: ""

Username for mutual CHAP authentication or empty string if not configured.

##### peersecret

- Schema name: `Peersecret`
- Type: string
- Default: ""

Password/secret for mutual CHAP authentication or empty string if not configured.

##### discovery_auth

- Schema name: `Discovery Auth`
- Type: enum (of string)
- Default: "NONE"

Authentication method for target discovery. If "CHAP_MUTUAL" is selected for target discovery, it is only permitted for a single entry systemwide.

### REMOVED

- Schema name: `IscsiAuthRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
