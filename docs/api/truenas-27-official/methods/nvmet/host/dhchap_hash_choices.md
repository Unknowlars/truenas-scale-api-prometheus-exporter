---
title: nvmet.host.dhchap_hash_choices
kind: method
source_rst: _sources/api_methods_nvmet.host.dhchap_hash_choices.rst.txt
source_html: api_methods_nvmet.host.dhchap_hash_choices.html
required_roles:
  - READONLY_ADMIN
  - SHARING_NVME_TARGET_READ
---

# nvmet.host.dhchap_hash_choices

## Summary

Returns possible choices for `dhchap_hash` attribute of `host` create and update.

## Required Roles

- `READONLY_ADMIN`
- `SHARING_NVME_TARGET_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of enum (of string)

Array of available DH-CHAP hash algorithm options.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: enum (of string)
##### Must be one of:

- "SHA-256"
- "SHA-384"
- "SHA-512"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
