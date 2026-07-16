---
title: sharing.smb.share_precheck
kind: method
source_rst: _sources/api_methods_sharing.smb.share_precheck.rst.txt
source_html: api_methods_sharing.smb.share_precheck.html
required_roles:
  - READONLY_ADMIN
---

# sharing.smb.share_precheck

## Summary

Validate prerequisites for creating an SMB share before calling :doc:`sharing.smb.create <api_methods_sharing.smb.create>`.

This is used by the UI to determine whether it should prompt to create SMB users when auto-creating a share. It verifies that the server is joined to a directory service or has at least one local SMB user, and, when `name` is supplied, that the share name is valid and not already in use.

Returns `null` on success. If any check fails, a JSON-RPC `error` response (code `-32602`, *Invalid params*) is returned describing the problem.

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
