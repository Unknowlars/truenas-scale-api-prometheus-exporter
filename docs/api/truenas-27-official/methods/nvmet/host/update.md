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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the NVMe-oF host to update.

#### Parameter 2: nvmet_host_update

<a id="Call_parameters_items_i1"></a>
#### nvmet_host_update

- Schema name: `nvmet_host_update`
- Type: object

Updated NVMe-oF host configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_hostnqn"></a>
<a id="Call_parameters_items_i1_hostnqn"></a>
##### hostnqn

- Schema name: `Hostnqn`
- Type: string

NQN of the host that will connect to this TrueNAS.
- Must be at least `11` characters long
- Must be at most `223` characters long

<a id="headingCall_parameters_items_i1_description"></a>
<a id="Call_parameters_items_i1_description"></a>
##### description

- Schema name: `Description`
- Type: string

Description of the NVMet host.

<a id="headingCall_parameters_items_i1_dhchap_key"></a>
<a id="Call_parameters_items_i1_dhchap_key"></a>
##### dhchap_key

- Schema name: `Dhchap Key`

If set, the secret that the host must present when connecting. A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="Call_parameters_items_i1_dhchap_key_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_dhchap_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_dhchap_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i1_dhchap_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_dhchap_key_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_dhchap_ctrl_key"></a>
<a id="Call_parameters_items_i1_dhchap_ctrl_key"></a>
##### dhchap_ctrl_key

- Schema name: `Dhchap Ctrl Key`

If set, the secret that this TrueNAS will present to the host when the host is connecting (Bi-Directional Authentication). A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="Call_parameters_items_i1_dhchap_ctrl_key_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_dhchap_ctrl_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_dhchap_ctrl_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i1_dhchap_ctrl_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_dhchap_ctrl_key_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_dhchap_dhgroup"></a>
<a id="Call_parameters_items_i1_dhchap_dhgroup"></a>
##### dhchap_dhgroup

- Schema name: `Dhchap Dhgroup`

If selected, the DH (Diffie-Hellman) key exchange built on top of CHAP to be used for authentication.
<a id="Call_parameters_items_i1_dhchap_dhgroup_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_dhchap_dhgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_dhchap_dhgroup_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "2048-BIT"
- "3072-BIT"
- "4096-BIT"
- "6144-BIT"
- "8192-BIT"

<a id="tab-pane_Call_parameters_items_i1_dhchap_dhgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_dhchap_dhgroup_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_dhchap_hash"></a>
<a id="Call_parameters_items_i1_dhchap_hash"></a>
##### dhchap_hash

- Schema name: `Dhchap Hash`
- Type: enum (of string)

HMAC (Hashed Message Authentication Code) to be used in conjunction if a `dhchap_dhgroup` is selected.
###### Must be one of:

- "SHA-256"
- "SHA-384"
- "SHA-512"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NVMetHostEntry`
- Type: object

The updated NVMe-oF host configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF host.

<a id="headingReturn_value_hostnqn"></a>
<a id="Return_value_hostnqn"></a>
#### hostnqn (required)

- Schema name: `Hostnqn`
- Type: string

NQN of the host that will connect to this TrueNAS.
- Must be at least `1` characters long

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description

- Schema name: `Description`
- Type: string
- Default: ""

Description of the NVMet host.

<a id="headingReturn_value_dhchap_key"></a>
<a id="Return_value_dhchap_key"></a>
#### dhchap_key

- Schema name: `Dhchap Key`
- Default: ""

If set, the secret that the host must present when connecting. A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="Return_value_dhchap_key_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dhchap_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dhchap_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_dhchap_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dhchap_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_dhchap_ctrl_key"></a>
<a id="Return_value_dhchap_ctrl_key"></a>
#### dhchap_ctrl_key

- Schema name: `Dhchap Ctrl Key`
- Default: ""

If set, the secret that this TrueNAS will present to the host when the host is connecting (Bi-Directional Authentication). A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="Return_value_dhchap_ctrl_key_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dhchap_ctrl_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dhchap_ctrl_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_dhchap_ctrl_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dhchap_ctrl_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_dhchap_dhgroup"></a>
<a id="Return_value_dhchap_dhgroup"></a>
#### dhchap_dhgroup

- Schema name: `Dhchap Dhgroup`
- Default: null

If selected, the DH (Diffie-Hellman) key exchange built on top of CHAP to be used for authentication.
<a id="Return_value_dhchap_dhgroup_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dhchap_dhgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dhchap_dhgroup_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "2048-BIT"
- "3072-BIT"
- "4096-BIT"
- "6144-BIT"
- "8192-BIT"

<a id="tab-pane_Return_value_dhchap_dhgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dhchap_dhgroup_anyOf_i1)

- Type: null

<a id="headingReturn_value_dhchap_hash"></a>
<a id="Return_value_dhchap_hash"></a>
#### dhchap_hash

- Schema name: `Dhchap Hash`
- Type: enum (of string)
- Default: "SHA-256"

HMAC (Hashed Message Authentication Code) to be used in conjunction if a `dhchap_dhgroup` is selected.
##### Must be one of:

- "SHA-256"
- "SHA-384"
- "SHA-512"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
