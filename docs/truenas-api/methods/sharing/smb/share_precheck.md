---
title: sharing.smb.share_precheck
kind: method
source_rst: _sources/api_methods_sharing.smb.share_precheck.rst.txt
source_html: api_methods_sharing.smb.share_precheck.html
required_roles:
  - READONLY_ADMIN
---

# sharing.smb.share_precheck

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: smb_share_precheck

#### smb_share_precheck

- Schema name: `smb_share_precheck`
- Type: object

SharingSMBSharePrecheckArgs parameters.
- No Additional Properties
##### name

- Schema name: `Name`
- Default: null

Name of the SMB share to validate (optional).
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the SMB share configuration passes validation checks.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
