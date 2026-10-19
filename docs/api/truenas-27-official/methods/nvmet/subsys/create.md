---
title: nvmet.subsys.create
kind: method
source_rst: _sources/api_methods_nvmet.subsys.create.rst.txt
source_html: api_methods_nvmet.subsys.create.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.subsys.create

## Summary

Create a NVMe target subsystem (`subsys`).

When a `subsys` contains one of more `namespaces`, and is associated with one or more `ports` then clients may access the storage using NVMe-oF.

All clients may access the subsystem if the `allow_any_host` attribute is set. Otherwise, access is only permitted to `hosts` who have been associated with the subsystem.

See [nvmet.host.create](../host/create.md) and [nvmet.host_subsys.create](../host_subsys/create.md).

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

#### Parameter 1: nvmet_subsys_create

<a id="Call_parameters_items_i0"></a>
#### nvmet_subsys_create

- Schema name: `nvmet_subsys_create`
- Type: object

Configuration data for creating a new NVMe-oF subsystem.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human readable name for the subsystem. If `subnqn` is not provided on creation, then this name will be appended to the `basenqn` from `nvmet.global.config` to generate a subnqn.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_subnqn"></a>
<a id="Call_parameters_items_i0_subnqn"></a>
##### subnqn

- Schema name: `Subnqn`
- Default: null

NVMe Qualified Name (NQN) for the subsystem. Must be a valid NQN format if provided.
<a id="Call_parameters_items_i0_subnqn_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_subnqn_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_subnqn_anyOf_i0)

- Type: string
- Must be at least `11` characters long
- Must be at most `223` characters long

<a id="tab-pane_Call_parameters_items_i0_subnqn_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_subnqn_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_allow_any_host"></a>
<a id="Call_parameters_items_i0_allow_any_host"></a>
##### allow_any_host

- Schema name: `Allow Any Host`
- Type: boolean
- Default: false

Any host can access the storage associated with this subsystem (i.e. no access control).

<a id="headingCall_parameters_items_i0_pi_enable"></a>
<a id="Call_parameters_items_i0_pi_enable"></a>
##### pi_enable

- Schema name: `Pi Enable`
- Default: null

Enable Protection Information (PI) for data integrity checking.
<a id="Call_parameters_items_i0_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_pi_enable_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_qid_max"></a>
<a id="Call_parameters_items_i0_qid_max"></a>
##### qid_max

- Schema name: `Qid Max`
- Default: null

Maximum number of queue IDs allowed for this subsystem.
<a id="Call_parameters_items_i0_qid_max_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_qid_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_qid_max_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_qid_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_qid_max_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_ieee_oui"></a>
<a id="Call_parameters_items_i0_ieee_oui"></a>
##### ieee_oui

- Schema name: `Ieee Oui`
- Default: null

IEEE Organizationally Unique Identifier for the subsystem.
<a id="Call_parameters_items_i0_ieee_oui_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_ieee_oui_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_ieee_oui_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_ieee_oui_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_ieee_oui_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_ana"></a>
<a id="Call_parameters_items_i0_ana"></a>
##### ana

- Schema name: `Ana`
- Default: null

If set to either `True` or `False`, then *override* the global `ana` setting from `nvmet.global.config` for this subsystem only. If `null`, then the global `ana` setting will take effect.
<a id="Call_parameters_items_i0_ana_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_ana_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_ana_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_ana_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_ana_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NVMetSubsysEntry`
- Type: object

The newly created NVMe-oF subsystem configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF subsystem.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Human readable name for the subsystem. If `subnqn` is not provided on creation, then this name will be appended to the `basenqn` from `nvmet.global.config` to generate a subnqn.
- Must be at least `1` characters long

<a id="headingReturn_value_subnqn"></a>
<a id="Return_value_subnqn"></a>
#### subnqn

- Schema name: `Subnqn`
- Default: null

NVMe Qualified Name (NQN) for the subsystem. If not provided during creation, will be auto-generated by appending the `name` to the `basenqn` from `nvmet.global.config`.
<a id="Return_value_subnqn_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_subnqn_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subnqn_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_subnqn_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subnqn_anyOf_i1)

- Type: null

<a id="headingReturn_value_serial"></a>
<a id="Return_value_serial"></a>
#### serial (required)

- Schema name: `Serial`
- Type: string

Serial number assigned to the subsystem.

<a id="headingReturn_value_allow_any_host"></a>
<a id="Return_value_allow_any_host"></a>
#### allow_any_host

- Schema name: `Allow Any Host`
- Type: boolean
- Default: false

Any host can access the storage associated with this subsystem (i.e. no access control).

<a id="headingReturn_value_pi_enable"></a>
<a id="Return_value_pi_enable"></a>
#### pi_enable

- Schema name: `Pi Enable`
- Default: null

Enable Protection Information (PI) for data integrity checking.
<a id="Return_value_pi_enable_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pi_enable_anyOf_i1)

- Type: null

<a id="headingReturn_value_qid_max"></a>
<a id="Return_value_qid_max"></a>
#### qid_max

- Schema name: `Qid Max`
- Default: null

Maximum number of queue IDs allowed for this subsystem.
<a id="Return_value_qid_max_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_qid_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_qid_max_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_qid_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_qid_max_anyOf_i1)

- Type: null

<a id="headingReturn_value_ieee_oui"></a>
<a id="Return_value_ieee_oui"></a>
#### ieee_oui

- Schema name: `Ieee Oui`
- Default: null

IEEE Organizationally Unique Identifier for the subsystem.
<a id="Return_value_ieee_oui_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_ieee_oui_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ieee_oui_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_ieee_oui_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ieee_oui_anyOf_i1)

- Type: null

<a id="headingReturn_value_ana"></a>
<a id="Return_value_ana"></a>
#### ana

- Schema name: `Ana`
- Default: null

If set to either `True` or `False`, then *override* the global `ana` setting from `nvmet.global.config` for this subsystem only. If `null`, then the global `ana` setting will take effect.
<a id="Return_value_ana_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_ana_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ana_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_ana_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ana_anyOf_i1)

- Type: null

<a id="headingReturn_value_hosts"></a>
<a id="Return_value_hosts"></a>
#### hosts

- Schema name: `Hosts`

List of host ids which have access to this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_hosts_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_hosts_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_hosts_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_hosts_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_hosts_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_hosts_anyOf_i1)

- Type: null

<a id="headingReturn_value_namespaces"></a>
<a id="Return_value_namespaces"></a>
#### namespaces

- Schema name: `Namespaces`

List of namespaces ids in this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_namespaces_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_namespaces_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_namespaces_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_namespaces_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_namespaces_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_namespaces_anyOf_i1)

- Type: null

<a id="headingReturn_value_ports"></a>
<a id="Return_value_ports"></a>
#### ports

- Schema name: `Ports`

List of ports ids on which this subsystem is available. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_ports_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_ports_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ports_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_ports_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_ports_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ports_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
