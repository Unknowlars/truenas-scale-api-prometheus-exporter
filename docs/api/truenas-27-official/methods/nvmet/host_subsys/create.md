---
title: nvmet.host_subsys.create
kind: method
source_rst: _sources/api_methods_nvmet.host_subsys.create.rst.txt
source_html: api_methods_nvmet.host_subsys.create.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.host_subsys.create

## Summary

Create an association between a `host` and a subsystem (`subsys`).

This will enable the `host` to access the subsystem, even if the subsystem does not have the `allow_any_host` attribute set.

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

#### Parameter 1: nvmet_host_subsys_create

<a id="Call_parameters_items_i0"></a>
#### nvmet_host_subsys_create

- Schema name: `nvmet_host_subsys_create`
- Type: object

Host-subsystem association configuration data for creation.
- No Additional Properties
<a id="headingCall_parameters_items_i0_host_id"></a>
<a id="Call_parameters_items_i0_host_id"></a>
##### host_id (required)

- Schema name: `Host Id`
- Type: integer

ID of the NVMe-oF host to authorize.

<a id="headingCall_parameters_items_i0_subsys_id"></a>
<a id="Call_parameters_items_i0_subsys_id"></a>
##### subsys_id (required)

- Schema name: `Subsys Id`
- Type: integer

ID of the NVMe-oF subsystem to grant access to.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NVMetHostSubsysEntry`
- Type: object

The created host-subsystem association.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the host-subsystem association.

<a id="headingReturn_value_host"></a>
<a id="Return_value_host"></a>
#### host (required)

- Schema name: `NVMetHostEntry`
- Type: object

NVMe-oF host that is authorized to access the subsystem.
- No Additional Properties
<a id="headingReturn_value_host_id"></a>
<a id="Return_value_host_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF host.

<a id="headingReturn_value_host_hostnqn"></a>
<a id="Return_value_host_hostnqn"></a>
##### hostnqn (required)

- Schema name: `Hostnqn`
- Type: string

NQN of the host that will connect to this TrueNAS.
- Must be at least `1` characters long

<a id="headingReturn_value_host_description"></a>
<a id="Return_value_host_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Description of the NVMet host.

<a id="headingReturn_value_host_dhchap_key"></a>
<a id="Return_value_host_dhchap_key"></a>
##### dhchap_key

- Schema name: `Dhchap Key`
- Default: ""

If set, the secret that the host must present when connecting. A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="Return_value_host_dhchap_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_host_dhchap_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_dhchap_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_host_dhchap_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_dhchap_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_dhchap_ctrl_key"></a>
<a id="Return_value_host_dhchap_ctrl_key"></a>
##### dhchap_ctrl_key

- Schema name: `Dhchap Ctrl Key`
- Default: ""

If set, the secret that this TrueNAS will present to the host when the host is connecting (Bi-Directional Authentication). A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="Return_value_host_dhchap_ctrl_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_host_dhchap_ctrl_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_dhchap_ctrl_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_host_dhchap_ctrl_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_dhchap_ctrl_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_dhchap_dhgroup"></a>
<a id="Return_value_host_dhchap_dhgroup"></a>
##### dhchap_dhgroup

- Schema name: `Dhchap Dhgroup`
- Default: null

If selected, the DH (Diffie-Hellman) key exchange built on top of CHAP to be used for authentication.
<a id="Return_value_host_dhchap_dhgroup_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_host_dhchap_dhgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_dhchap_dhgroup_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "2048-BIT"
- "3072-BIT"
- "4096-BIT"
- "6144-BIT"
- "8192-BIT"

<a id="tab-pane_Return_value_host_dhchap_dhgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_dhchap_dhgroup_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_dhchap_hash"></a>
<a id="Return_value_host_dhchap_hash"></a>
##### dhchap_hash

- Schema name: `Dhchap Hash`
- Type: enum (of string)
- Default: "SHA-256"

HMAC (Hashed Message Authentication Code) to be used in conjunction if a `dhchap_dhgroup` is selected.
###### Must be one of:

- "SHA-256"
- "SHA-384"
- "SHA-512"

<a id="headingReturn_value_subsys"></a>
<a id="Return_value_subsys"></a>
#### subsys (required)

- Schema name: `NVMetSubsysEntry`
- Type: object

NVMe-oF subsystem that the host is authorized to access.
- No Additional Properties
<a id="headingReturn_value_subsys_id"></a>
<a id="Return_value_subsys_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF subsystem.

<a id="headingReturn_value_subsys_name"></a>
<a id="Return_value_subsys_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human readable name for the subsystem. If `subnqn` is not provided on creation, then this name will be appended to the `basenqn` from `nvmet.global.config` to generate a subnqn.
- Must be at least `1` characters long

<a id="headingReturn_value_subsys_subnqn"></a>
<a id="Return_value_subsys_subnqn"></a>
##### subnqn

- Schema name: `Subnqn`
- Default: null

NVMe Qualified Name (NQN) for the subsystem. If not provided during creation, will be auto-generated by appending the `name` to the `basenqn` from `nvmet.global.config`.
<a id="Return_value_subsys_subnqn_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_subnqn_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_subnqn_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_subsys_subnqn_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_subnqn_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_serial"></a>
<a id="Return_value_subsys_serial"></a>
##### serial (required)

- Schema name: `Serial`
- Type: string

Serial number assigned to the subsystem.

<a id="headingReturn_value_subsys_allow_any_host"></a>
<a id="Return_value_subsys_allow_any_host"></a>
##### allow_any_host

- Schema name: `Allow Any Host`
- Type: boolean
- Default: false

Any host can access the storage associated with this subsystem (i.e. no access control).

<a id="headingReturn_value_subsys_pi_enable"></a>
<a id="Return_value_subsys_pi_enable"></a>
##### pi_enable

- Schema name: `Pi Enable`
- Default: null

Enable Protection Information (PI) for data integrity checking.
<a id="Return_value_subsys_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_subsys_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_pi_enable_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_qid_max"></a>
<a id="Return_value_subsys_qid_max"></a>
##### qid_max

- Schema name: `Qid Max`
- Default: null

Maximum number of queue IDs allowed for this subsystem.
<a id="Return_value_subsys_qid_max_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_qid_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_qid_max_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_subsys_qid_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_qid_max_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_ieee_oui"></a>
<a id="Return_value_subsys_ieee_oui"></a>
##### ieee_oui

- Schema name: `Ieee Oui`
- Default: null

IEEE Organizationally Unique Identifier for the subsystem.
<a id="Return_value_subsys_ieee_oui_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_ieee_oui_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_ieee_oui_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_subsys_ieee_oui_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_ieee_oui_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_ana"></a>
<a id="Return_value_subsys_ana"></a>
##### ana

- Schema name: `Ana`
- Default: null

If set to either `True` or `False`, then *override* the global `ana` setting from `nvmet.global.config` for this subsystem only. If `null`, then the global `ana` setting will take effect.
<a id="Return_value_subsys_ana_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_ana_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_ana_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_subsys_ana_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_ana_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_hosts"></a>
<a id="Return_value_subsys_hosts"></a>
##### hosts

- Schema name: `Hosts`

List of host ids which have access to this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_subsys_hosts_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_hosts_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_hosts_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_subsys_hosts_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_subsys_hosts_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_hosts_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_namespaces"></a>
<a id="Return_value_subsys_namespaces"></a>
##### namespaces

- Schema name: `Namespaces`

List of namespaces ids in this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_subsys_namespaces_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_namespaces_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_namespaces_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_subsys_namespaces_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_subsys_namespaces_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_namespaces_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_ports"></a>
<a id="Return_value_subsys_ports"></a>
##### ports

- Schema name: `Ports`

List of ports ids on which this subsystem is available. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_subsys_ports_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_ports_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_ports_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_subsys_ports_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_subsys_ports_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_ports_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
