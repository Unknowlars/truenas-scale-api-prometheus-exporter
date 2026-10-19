---
title: nvmet.host.query
kind: event
source_rst: _sources/api_events_nvmet.host.query.rst.txt
source_html: api_events_nvmet.host.query.html
required_roles:
  - SHARING_NVME_TARGET_READ
---

# nvmet.host.query

## Summary

Sent on nvmet.host changes.

## Required Roles

- `SHARING_NVME_TARGET_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `NVMetHostAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `NVMetHostEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF host.

<a id="headingADDED_fields_hostnqn"></a>
<a id="ADDED_fields_hostnqn"></a>
##### hostnqn (required)

- Schema name: `Hostnqn`
- Type: string

NQN of the host that will connect to this TrueNAS.
- Must be at least `1` characters long

<a id="headingADDED_fields_description"></a>
<a id="ADDED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Description of the NVMet host.

<a id="headingADDED_fields_dhchap_key"></a>
<a id="ADDED_fields_dhchap_key"></a>
##### dhchap_key

- Schema name: `Dhchap Key`
- Default: ""

If set, the secret that the host must present when connecting. A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="ADDED_fields_dhchap_key_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_dhchap_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_dhchap_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_dhchap_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_dhchap_key_anyOf_i1)

- Type: null

<a id="headingADDED_fields_dhchap_ctrl_key"></a>
<a id="ADDED_fields_dhchap_ctrl_key"></a>
##### dhchap_ctrl_key

- Schema name: `Dhchap Ctrl Key`
- Default: ""

If set, the secret that this TrueNAS will present to the host when the host is connecting (Bi-Directional Authentication). A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="ADDED_fields_dhchap_ctrl_key_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_dhchap_ctrl_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_dhchap_ctrl_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_dhchap_ctrl_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_dhchap_ctrl_key_anyOf_i1)

- Type: null

<a id="headingADDED_fields_dhchap_dhgroup"></a>
<a id="ADDED_fields_dhchap_dhgroup"></a>
##### dhchap_dhgroup

- Schema name: `Dhchap Dhgroup`
- Default: null

If selected, the DH (Diffie-Hellman) key exchange built on top of CHAP to be used for authentication.
<a id="ADDED_fields_dhchap_dhgroup_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_dhchap_dhgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_dhchap_dhgroup_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "2048-BIT"
- "3072-BIT"
- "4096-BIT"
- "6144-BIT"
- "8192-BIT"

<a id="tab-pane_ADDED_fields_dhchap_dhgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_dhchap_dhgroup_anyOf_i1)

- Type: null

<a id="headingADDED_fields_dhchap_hash"></a>
<a id="ADDED_fields_dhchap_hash"></a>
##### dhchap_hash

- Schema name: `Dhchap Hash`
- Type: enum (of string)
- Default: "SHA-256"

HMAC (Hashed Message Authentication Code) to be used in conjunction if a `dhchap_dhgroup` is selected.
###### Must be one of:

- "SHA-256"
- "SHA-384"
- "SHA-512"

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `NVMetHostChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `NVMetHostEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF host.

<a id="headingCHANGED_fields_hostnqn"></a>
<a id="CHANGED_fields_hostnqn"></a>
##### hostnqn (required)

- Schema name: `Hostnqn`
- Type: string

NQN of the host that will connect to this TrueNAS.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Description of the NVMet host.

<a id="headingCHANGED_fields_dhchap_key"></a>
<a id="CHANGED_fields_dhchap_key"></a>
##### dhchap_key

- Schema name: `Dhchap Key`
- Default: ""

If set, the secret that the host must present when connecting. A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="CHANGED_fields_dhchap_key_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_dhchap_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_dhchap_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_dhchap_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_dhchap_key_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_dhchap_ctrl_key"></a>
<a id="CHANGED_fields_dhchap_ctrl_key"></a>
##### dhchap_ctrl_key

- Schema name: `Dhchap Ctrl Key`
- Default: ""

If set, the secret that this TrueNAS will present to the host when the host is connecting (Bi-Directional Authentication). A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="CHANGED_fields_dhchap_ctrl_key_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_dhchap_ctrl_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_dhchap_ctrl_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_dhchap_ctrl_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_dhchap_ctrl_key_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_dhchap_dhgroup"></a>
<a id="CHANGED_fields_dhchap_dhgroup"></a>
##### dhchap_dhgroup

- Schema name: `Dhchap Dhgroup`
- Default: null

If selected, the DH (Diffie-Hellman) key exchange built on top of CHAP to be used for authentication.
<a id="CHANGED_fields_dhchap_dhgroup_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_dhchap_dhgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_dhchap_dhgroup_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "2048-BIT"
- "3072-BIT"
- "4096-BIT"
- "6144-BIT"
- "8192-BIT"

<a id="tab-pane_CHANGED_fields_dhchap_dhgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_dhchap_dhgroup_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_dhchap_hash"></a>
<a id="CHANGED_fields_dhchap_hash"></a>
##### dhchap_hash

- Schema name: `Dhchap Hash`
- Type: enum (of string)
- Default: "SHA-256"

HMAC (Hashed Message Authentication Code) to be used in conjunction if a `dhchap_dhgroup` is selected.
###### Must be one of:

- "SHA-256"
- "SHA-384"
- "SHA-512"

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `NVMetHostRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
