---
title: smb.bindip_choices
kind: method
source_rst: _sources/api_methods_smb.bindip_choices.rst.txt
source_html: api_methods_smb.bindip_choices.html
required_roles:
  - READONLY_ADMIN | SHARING_SMB_READ
---

# smb.bindip_choices

## Summary

List of valid choices for IP addresses to which to bind the SMB service. Addresses assigned by DHCP are excluded from the results.

## Required Roles

- `READONLY_ADMIN | SHARING_SMB_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Available IP addresses that the SMB service can bind to.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
