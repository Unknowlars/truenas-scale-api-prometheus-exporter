---
title: nvmet.host.generate_key
kind: method
source_rst: _sources/api_methods_nvmet.host.generate_key.rst.txt
source_html: api_methods_nvmet.host.generate_key.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.host.generate_key

## Summary

Generate a secret key that may be used when configuring `host` authentication.

## Required Roles

- `SHARING_NVME_TARGET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dhchap_hash

<a id="Call_parameters_items_i0"></a>
#### dhchap_hash

- Schema name: `dhchap_hash`
- Type: enum (of string)
- Default: "SHA-256"

Hash to be used with the generated key.
##### Must be one of:

- "SHA-256"
- "SHA-384"
- "SHA-512"

#### Parameter 2: nqn

<a id="Call_parameters_items_i1"></a>
#### nqn

- Schema name: `nqn`
- Default: null

NQN to be used for the transformation.
<a id="Call_parameters_items_i1_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: string

Generated DH-CHAP key for NVMe-oF authentication.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
