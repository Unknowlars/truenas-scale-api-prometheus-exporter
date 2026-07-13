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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dhchap_hash

#### dhchap_hash

- Schema name: `dhchap_hash`
- Type: enum (of string)
- Default: "SHA-256"

Hash to be used with the generated key.

#### Parameter 2: nqn

#### nqn

- Schema name: `nqn`
- Default: null

NQN to be used for the transformation.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: string

Generated DH-CHAP key for NVMe-oF authentication.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
