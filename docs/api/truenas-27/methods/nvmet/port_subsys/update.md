---
title: nvmet.port_subsys.update
kind: method
source_rst: _sources/api_methods_nvmet.port_subsys.update.rst.txt
source_html: api_methods_nvmet.port_subsys.update.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.port_subsys.update

## Summary

Update `port`/`subsys` association of `id`.

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

ID of the port-subsystem association to update.

#### Parameter 2: nvmet_port_subsys_update

<a id="Call_parameters_items_i1"></a>
#### nvmet_port_subsys_update

- Schema name: `nvmet_port_subsys_update`
- Type: object

Updated port-subsystem association configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_port_id"></a>
<a id="Call_parameters_items_i1_port_id"></a>
##### port_id

- Schema name: `Port Id`
- Type: integer

ID of the NVMe-oF port to associate.

<a id="headingCall_parameters_items_i1_subsys_id"></a>
<a id="Call_parameters_items_i1_subsys_id"></a>
##### subsys_id

- Schema name: `Subsys Id`
- Type: integer

ID of the NVMe-oF subsystem to make accessible.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NVMetPortSubsysEntry`
- Type: object

The updated port-subsystem association.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the port-subsystem association.

<a id="headingReturn_value_port"></a>
<a id="Return_value_port"></a>
#### port (required)

- Schema name: `NVMetPortEntry`
- Type: object

NVMe-oF port that provides access to the subsystem.
- No Additional Properties
<a id="headingReturn_value_port_id"></a>
<a id="Return_value_port_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF port.

<a id="headingReturn_value_port_index"></a>
<a id="Return_value_port_index"></a>
##### index (required)

- Schema name: `Index`
- Type: integer

Index of the port, for internal use.

<a id="headingReturn_value_port_addr_trtype"></a>
<a id="Return_value_port_addr_trtype"></a>
##### addr_trtype (required)

- Schema name: `Addr Trtype`
- Type: enum (of string)

Fabric transport technology name.
###### Must be one of:

- "TCP"
- "RDMA"
- "FC"

<a id="headingReturn_value_port_addr_trsvcid"></a>
<a id="Return_value_port_addr_trsvcid"></a>
##### addr_trsvcid (required)

- Schema name: `Addr Trsvcid`

Transport-specific TRSVCID field. When configured for TCP/IP or RDMA this will be the port number.
<a id="Return_value_port_addr_trsvcid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_port_addr_trsvcid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_port_addr_trsvcid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_port_addr_trsvcid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_port_addr_trsvcid_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_port_addr_trsvcid_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_port_addr_trsvcid_anyOf_i2)

- Type: null

<a id="headingReturn_value_port_addr_traddr"></a>
<a id="Return_value_port_addr_traddr"></a>
##### addr_traddr (required)

- Schema name: `Addr Traddr`
- Type: string

A transport-specific field identifying the NVMe host port to use for the connection to the controller. For TCP or RDMA transports, this will be an IPv4 or IPv6 address.

<a id="headingReturn_value_port_addr_adrfam"></a>
<a id="Return_value_port_addr_adrfam"></a>
##### addr_adrfam (required)

- Schema name: `Addr Adrfam`
- Type: enum (of string)

Address family.
###### Must be one of:

- "IPV4"
- "IPV6"
- "FC"

<a id="headingReturn_value_port_inline_data_size"></a>
<a id="Return_value_port_inline_data_size"></a>
##### inline_data_size

- Schema name: `Inline Data Size`
- Default: null

Maximum size for inline data transfers or `null` for default.
<a id="Return_value_port_inline_data_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_port_inline_data_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_port_inline_data_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_port_inline_data_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_port_inline_data_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_port_max_queue_size"></a>
<a id="Return_value_port_max_queue_size"></a>
##### max_queue_size

- Schema name: `Max Queue Size`
- Default: null

Maximum number of queue entries or `null` for default.
<a id="Return_value_port_max_queue_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_port_max_queue_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_port_max_queue_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_port_max_queue_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_port_max_queue_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_port_pi_enable"></a>
<a id="Return_value_port_pi_enable"></a>
##### pi_enable

- Schema name: `Pi Enable`
- Default: null

Whether Protection Information (PI) is enabled or `null` for default.
<a id="Return_value_port_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_port_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_port_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_port_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_port_pi_enable_anyOf_i1)

- Type: null

<a id="headingReturn_value_port_enabled"></a>
<a id="Return_value_port_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

<a id="headingReturn_value_subsys"></a>
<a id="Return_value_subsys"></a>
#### subsys (required)

- Schema name: `NVMetSubsysEntry`
- Type: object

NVMe-oF subsystem that is accessible through the port.
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
