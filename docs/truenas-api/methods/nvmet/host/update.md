---
title: nvmet.host.update
kind: method
source_rst: _sources/api_methods_nvmet.host.update.rst.txt
source_html: api_methods_nvmet.host.update.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.host.update

## Summary

Update NVMe target `host` of `id`.

## Required Roles

- `SHARING_NVME_TARGET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the NVMe-oF host to update.

#### Parameter 2: nvmet_host_update

#### nvmet_host_update

- Schema name: `nvmet_host_update`
- Type: object

Updated NVMe-oF host configuration data.
- No Additional Properties
##### hostnqn

- Schema name: `Hostnqn`
- Type: string

NQN of the host that will connect to this TrueNAS.
- Must be at least `11` characters long
- Must be at most `223` characters long

##### dhchap_key

- Schema name: `Dhchap Key`

If set, the secret that the host must present when connecting. A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### dhchap_ctrl_key

- Schema name: `Dhchap Ctrl Key`

If set, the secret that this TrueNAS will present to the host when the host is connecting (Bi-Directional Authentication). A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### dhchap_dhgroup

- Schema name: `Dhchap Dhgroup`

If selected, the DH (Diffie-Hellman) key exchange built on top of CHAP to be used for authentication.
###### Any of

####### Option 1

- Type: enum (of string)

####### Option 2

- Type: null

##### dhchap_hash

- Schema name: `Dhchap Hash`
- Type: enum (of string)

HMAC (Hashed Message Authentication Code) to be used in conjunction if a `dhchap_dhgroup` is selected.

### Return value

- Schema name: `NVMetHostEntry`
- Type: object

The updated NVMe-oF host configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF host.

#### hostnqn (required)

- Schema name: `Hostnqn`
- Type: string

NQN of the host that will connect to this TrueNAS.
- Must be at least `1` characters long

#### dhchap_key

- Schema name: `Dhchap Key`
- Default: null

If set, the secret that the host must present when connecting. A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### dhchap_ctrl_key

- Schema name: `Dhchap Ctrl Key`
- Default: null

If set, the secret that this TrueNAS will present to the host when the host is connecting (Bi-Directional Authentication). A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### dhchap_dhgroup

- Schema name: `Dhchap Dhgroup`
- Default: null

If selected, the DH (Diffie-Hellman) key exchange built on top of CHAP to be used for authentication.
##### Any of

###### Option 1

- Type: enum (of string)

###### Option 2

- Type: null

#### dhchap_hash

- Schema name: `Dhchap Hash`
- Type: enum (of string)
- Default: "SHA-256"

HMAC (Hashed Message Authentication Code) to be used in conjunction if a `dhchap_dhgroup` is selected.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
