---
title: nvmet.host.dhchap_dhgroup_choices
kind: method
source_rst: _sources/api_methods_nvmet.host.dhchap_dhgroup_choices.rst.txt
source_html: api_methods_nvmet.host.dhchap_dhgroup_choices.html
required_roles:
  - READONLY_ADMIN
  - SHARING_NVME_TARGET_READ
---

# nvmet.host.dhchap_dhgroup_choices

## Summary

Returns possible choices for `dhchap_dhgroup` attribute of `host` create and update. None is an additional choice.

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

Array of available DH-CHAP Diffie-Hellman group options.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: enum (of string)
##### Must be one of:

- "2048-BIT"
- "3072-BIT"
- "4096-BIT"
- "6144-BIT"
- "8192-BIT"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
