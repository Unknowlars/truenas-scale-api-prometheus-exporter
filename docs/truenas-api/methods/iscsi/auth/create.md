---
title: iscsi.auth.create
kind: method
source_rst: _sources/api_methods_iscsi.auth.create.rst.txt
source_html: api_methods_iscsi.auth.create.html
required_roles:
  - SHARING_ISCSI_AUTH_WRITE
---

# iscsi.auth.create

## Summary

Create an iSCSI Authorized Access.

`tag` should be unique among all configured iSCSI Authorized Accesses.

`secret` and `peersecret` should have length between 12-16 letters inclusive.

`peeruser` and `peersecret` are provided only when configuring mutual CHAP. `peersecret` should not be similar to `secret`.

## Required Roles

- `SHARING_ISCSI_AUTH_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

iSCSI authentication credential configuration data for creation.
- No Additional Properties
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

### Return value

- Schema name: `IscsiAuthEntry`
- Type: object

The created iSCSI authentication credential.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI authentication credential.

#### tag (required)

- Schema name: `Tag`
- Type: integer

Numeric tag used to associate this credential with iSCSI targets.

#### user (required)

- Schema name: `User`
- Type: string

Username for iSCSI CHAP authentication.

#### secret (required)

- Schema name: `Secret`
- Type: string

Password/secret for iSCSI CHAP authentication.

#### peeruser

- Schema name: `Peeruser`
- Type: string
- Default: ""

Username for mutual CHAP authentication or empty string if not configured.

#### peersecret

- Schema name: `Peersecret`
- Type: string
- Default: ""

Password/secret for mutual CHAP authentication or empty string if not configured.

#### discovery_auth

- Schema name: `Discovery Auth`
- Type: enum (of string)
- Default: "NONE"

Authentication method for target discovery. If "CHAP_MUTUAL" is selected for target discovery, it is only permitted for a single entry systemwide.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
