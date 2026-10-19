---
title: nvmet.port_subsys.query
kind: event
source_rst: _sources/api_events_nvmet.port_subsys.query.rst.txt
source_html: api_events_nvmet.port_subsys.query.html
required_roles:
  - SHARING_NVME_TARGET_READ
---

# nvmet.port_subsys.query

## Summary

Sent on nvmet.port_subsys changes.

## Required Roles

- `SHARING_NVME_TARGET_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `NVMetPortSubsysAddedEvent`
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

- Schema name: `NVMetPortSubsysEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the port-subsystem association.

<a id="headingADDED_fields_port"></a>
<a id="ADDED_fields_port"></a>
##### port (required)

- Schema name: `NVMetPortEntry`
- Type: object

NVMe-oF port that provides access to the subsystem.
- No Additional Properties
<a id="headingADDED_fields_port_id"></a>
<a id="ADDED_fields_port_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF port.

<a id="headingADDED_fields_port_index"></a>
<a id="ADDED_fields_port_index"></a>
###### index (required)

- Schema name: `Index`
- Type: integer

Index of the port, for internal use.

<a id="headingADDED_fields_port_addr_trtype"></a>
<a id="ADDED_fields_port_addr_trtype"></a>
###### addr_trtype (required)

- Schema name: `Addr Trtype`
- Type: enum (of string)

Fabric transport technology name.
###### Must be one of:

- "TCP"
- "RDMA"
- "FC"

<a id="headingADDED_fields_port_addr_trsvcid"></a>
<a id="ADDED_fields_port_addr_trsvcid"></a>
###### addr_trsvcid (required)

- Schema name: `Addr Trsvcid`

Transport-specific TRSVCID field. When configured for TCP/IP or RDMA this will be the port number.
<a id="ADDED_fields_port_addr_trsvcid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_port_addr_trsvcid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_port_addr_trsvcid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_port_addr_trsvcid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_port_addr_trsvcid_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_port_addr_trsvcid_anyOf_i2"></a>
###### [Option 3](#tab-pane_ADDED_fields_port_addr_trsvcid_anyOf_i2)

- Type: null

<a id="headingADDED_fields_port_addr_traddr"></a>
<a id="ADDED_fields_port_addr_traddr"></a>
###### addr_traddr (required)

- Schema name: `Addr Traddr`
- Type: string

A transport-specific field identifying the NVMe host port to use for the connection to the controller. For TCP or RDMA transports, this will be an IPv4 or IPv6 address.

<a id="headingADDED_fields_port_addr_adrfam"></a>
<a id="ADDED_fields_port_addr_adrfam"></a>
###### addr_adrfam (required)

- Schema name: `Addr Adrfam`
- Type: enum (of string)

Address family.
###### Must be one of:

- "IPV4"
- "IPV6"
- "FC"

<a id="headingADDED_fields_port_inline_data_size"></a>
<a id="ADDED_fields_port_inline_data_size"></a>
###### inline_data_size

- Schema name: `Inline Data Size`
- Default: null

Maximum size for inline data transfers or `null` for default.
<a id="ADDED_fields_port_inline_data_size_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_port_inline_data_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_port_inline_data_size_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_port_inline_data_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_port_inline_data_size_anyOf_i1)

- Type: null

<a id="headingADDED_fields_port_max_queue_size"></a>
<a id="ADDED_fields_port_max_queue_size"></a>
###### max_queue_size

- Schema name: `Max Queue Size`
- Default: null

Maximum number of queue entries or `null` for default.
<a id="ADDED_fields_port_max_queue_size_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_port_max_queue_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_port_max_queue_size_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_port_max_queue_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_port_max_queue_size_anyOf_i1)

- Type: null

<a id="headingADDED_fields_port_pi_enable"></a>
<a id="ADDED_fields_port_pi_enable"></a>
###### pi_enable

- Schema name: `Pi Enable`
- Default: null

Whether Protection Information (PI) is enabled or `null` for default.
<a id="ADDED_fields_port_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_port_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_port_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_port_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_port_pi_enable_anyOf_i1)

- Type: null

<a id="headingADDED_fields_port_enabled"></a>
<a id="ADDED_fields_port_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

<a id="headingADDED_fields_subsys"></a>
<a id="ADDED_fields_subsys"></a>
##### subsys (required)

- Schema name: `NVMetSubsysEntry`
- Type: object

NVMe-oF subsystem that is accessible through the port.
- No Additional Properties
<a id="headingADDED_fields_subsys_id"></a>
<a id="ADDED_fields_subsys_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF subsystem.

<a id="headingADDED_fields_subsys_name"></a>
<a id="ADDED_fields_subsys_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human readable name for the subsystem. If `subnqn` is not provided on creation, then this name will be appended to the `basenqn` from `nvmet.global.config` to generate a subnqn.
- Must be at least `1` characters long

<a id="headingADDED_fields_subsys_subnqn"></a>
<a id="ADDED_fields_subsys_subnqn"></a>
###### subnqn

- Schema name: `Subnqn`
- Default: null

NVMe Qualified Name (NQN) for the subsystem. If not provided during creation, will be auto-generated by appending the `name` to the `basenqn` from `nvmet.global.config`.
<a id="ADDED_fields_subsys_subnqn_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_subsys_subnqn_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_subsys_subnqn_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_subsys_subnqn_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_subsys_subnqn_anyOf_i1)

- Type: null

<a id="headingADDED_fields_subsys_serial"></a>
<a id="ADDED_fields_subsys_serial"></a>
###### serial (required)

- Schema name: `Serial`
- Type: string

Serial number assigned to the subsystem.

<a id="headingADDED_fields_subsys_allow_any_host"></a>
<a id="ADDED_fields_subsys_allow_any_host"></a>
###### allow_any_host

- Schema name: `Allow Any Host`
- Type: boolean
- Default: false

Any host can access the storage associated with this subsystem (i.e. no access control).

<a id="headingADDED_fields_subsys_pi_enable"></a>
<a id="ADDED_fields_subsys_pi_enable"></a>
###### pi_enable

- Schema name: `Pi Enable`
- Default: null

Enable Protection Information (PI) for data integrity checking.
<a id="ADDED_fields_subsys_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_subsys_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_subsys_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_subsys_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_subsys_pi_enable_anyOf_i1)

- Type: null

<a id="headingADDED_fields_subsys_qid_max"></a>
<a id="ADDED_fields_subsys_qid_max"></a>
###### qid_max

- Schema name: `Qid Max`
- Default: null

Maximum number of queue IDs allowed for this subsystem.
<a id="ADDED_fields_subsys_qid_max_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_subsys_qid_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_subsys_qid_max_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_subsys_qid_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_subsys_qid_max_anyOf_i1)

- Type: null

<a id="headingADDED_fields_subsys_ieee_oui"></a>
<a id="ADDED_fields_subsys_ieee_oui"></a>
###### ieee_oui

- Schema name: `Ieee Oui`
- Default: null

IEEE Organizationally Unique Identifier for the subsystem.
<a id="ADDED_fields_subsys_ieee_oui_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_subsys_ieee_oui_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_subsys_ieee_oui_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_subsys_ieee_oui_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_subsys_ieee_oui_anyOf_i1)

- Type: null

<a id="headingADDED_fields_subsys_ana"></a>
<a id="ADDED_fields_subsys_ana"></a>
###### ana

- Schema name: `Ana`
- Default: null

If set to either `True` or `False`, then *override* the global `ana` setting from `nvmet.global.config` for this subsystem only. If `null`, then the global `ana` setting will take effect.
<a id="ADDED_fields_subsys_ana_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_subsys_ana_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_subsys_ana_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_subsys_ana_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_subsys_ana_anyOf_i1)

- Type: null

<a id="headingADDED_fields_subsys_hosts"></a>
<a id="ADDED_fields_subsys_hosts"></a>
###### hosts

- Schema name: `Hosts`

List of host ids which have access to this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="ADDED_fields_subsys_hosts_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_subsys_hosts_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_subsys_hosts_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_subsys_hosts_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_ADDED_fields_subsys_hosts_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_subsys_hosts_anyOf_i1)

- Type: null

<a id="headingADDED_fields_subsys_namespaces"></a>
<a id="ADDED_fields_subsys_namespaces"></a>
###### namespaces

- Schema name: `Namespaces`

List of namespaces ids in this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="ADDED_fields_subsys_namespaces_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_subsys_namespaces_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_subsys_namespaces_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_subsys_namespaces_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_ADDED_fields_subsys_namespaces_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_subsys_namespaces_anyOf_i1)

- Type: null

<a id="headingADDED_fields_subsys_ports"></a>
<a id="ADDED_fields_subsys_ports"></a>
###### ports

- Schema name: `Ports`

List of ports ids on which this subsystem is available. Only populated on query if `extra.options.verbose` is set.
<a id="ADDED_fields_subsys_ports_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_subsys_ports_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_subsys_ports_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_subsys_ports_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_ADDED_fields_subsys_ports_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_subsys_ports_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `NVMetPortSubsysChangedEvent`
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

- Schema name: `NVMetPortSubsysEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the port-subsystem association.

<a id="headingCHANGED_fields_port"></a>
<a id="CHANGED_fields_port"></a>
##### port (required)

- Schema name: `NVMetPortEntry`
- Type: object

NVMe-oF port that provides access to the subsystem.
- No Additional Properties
<a id="headingCHANGED_fields_port_id"></a>
<a id="CHANGED_fields_port_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF port.

<a id="headingCHANGED_fields_port_index"></a>
<a id="CHANGED_fields_port_index"></a>
###### index (required)

- Schema name: `Index`
- Type: integer

Index of the port, for internal use.

<a id="headingCHANGED_fields_port_addr_trtype"></a>
<a id="CHANGED_fields_port_addr_trtype"></a>
###### addr_trtype (required)

- Schema name: `Addr Trtype`
- Type: enum (of string)

Fabric transport technology name.
###### Must be one of:

- "TCP"
- "RDMA"
- "FC"

<a id="headingCHANGED_fields_port_addr_trsvcid"></a>
<a id="CHANGED_fields_port_addr_trsvcid"></a>
###### addr_trsvcid (required)

- Schema name: `Addr Trsvcid`

Transport-specific TRSVCID field. When configured for TCP/IP or RDMA this will be the port number.
<a id="CHANGED_fields_port_addr_trsvcid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_port_addr_trsvcid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_port_addr_trsvcid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_port_addr_trsvcid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_port_addr_trsvcid_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_port_addr_trsvcid_anyOf_i2"></a>
###### [Option 3](#tab-pane_CHANGED_fields_port_addr_trsvcid_anyOf_i2)

- Type: null

<a id="headingCHANGED_fields_port_addr_traddr"></a>
<a id="CHANGED_fields_port_addr_traddr"></a>
###### addr_traddr (required)

- Schema name: `Addr Traddr`
- Type: string

A transport-specific field identifying the NVMe host port to use for the connection to the controller. For TCP or RDMA transports, this will be an IPv4 or IPv6 address.

<a id="headingCHANGED_fields_port_addr_adrfam"></a>
<a id="CHANGED_fields_port_addr_adrfam"></a>
###### addr_adrfam (required)

- Schema name: `Addr Adrfam`
- Type: enum (of string)

Address family.
###### Must be one of:

- "IPV4"
- "IPV6"
- "FC"

<a id="headingCHANGED_fields_port_inline_data_size"></a>
<a id="CHANGED_fields_port_inline_data_size"></a>
###### inline_data_size

- Schema name: `Inline Data Size`
- Default: null

Maximum size for inline data transfers or `null` for default.
<a id="CHANGED_fields_port_inline_data_size_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_port_inline_data_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_port_inline_data_size_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_port_inline_data_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_port_inline_data_size_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_port_max_queue_size"></a>
<a id="CHANGED_fields_port_max_queue_size"></a>
###### max_queue_size

- Schema name: `Max Queue Size`
- Default: null

Maximum number of queue entries or `null` for default.
<a id="CHANGED_fields_port_max_queue_size_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_port_max_queue_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_port_max_queue_size_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_port_max_queue_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_port_max_queue_size_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_port_pi_enable"></a>
<a id="CHANGED_fields_port_pi_enable"></a>
###### pi_enable

- Schema name: `Pi Enable`
- Default: null

Whether Protection Information (PI) is enabled or `null` for default.
<a id="CHANGED_fields_port_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_port_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_port_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_port_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_port_pi_enable_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_port_enabled"></a>
<a id="CHANGED_fields_port_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

<a id="headingCHANGED_fields_subsys"></a>
<a id="CHANGED_fields_subsys"></a>
##### subsys (required)

- Schema name: `NVMetSubsysEntry`
- Type: object

NVMe-oF subsystem that is accessible through the port.
- No Additional Properties
<a id="headingCHANGED_fields_subsys_id"></a>
<a id="CHANGED_fields_subsys_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF subsystem.

<a id="headingCHANGED_fields_subsys_name"></a>
<a id="CHANGED_fields_subsys_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human readable name for the subsystem. If `subnqn` is not provided on creation, then this name will be appended to the `basenqn` from `nvmet.global.config` to generate a subnqn.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_subsys_subnqn"></a>
<a id="CHANGED_fields_subsys_subnqn"></a>
###### subnqn

- Schema name: `Subnqn`
- Default: null

NVMe Qualified Name (NQN) for the subsystem. If not provided during creation, will be auto-generated by appending the `name` to the `basenqn` from `nvmet.global.config`.
<a id="CHANGED_fields_subsys_subnqn_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_subsys_subnqn_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_subsys_subnqn_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_subsys_subnqn_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_subsys_subnqn_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_subsys_serial"></a>
<a id="CHANGED_fields_subsys_serial"></a>
###### serial (required)

- Schema name: `Serial`
- Type: string

Serial number assigned to the subsystem.

<a id="headingCHANGED_fields_subsys_allow_any_host"></a>
<a id="CHANGED_fields_subsys_allow_any_host"></a>
###### allow_any_host

- Schema name: `Allow Any Host`
- Type: boolean
- Default: false

Any host can access the storage associated with this subsystem (i.e. no access control).

<a id="headingCHANGED_fields_subsys_pi_enable"></a>
<a id="CHANGED_fields_subsys_pi_enable"></a>
###### pi_enable

- Schema name: `Pi Enable`
- Default: null

Enable Protection Information (PI) for data integrity checking.
<a id="CHANGED_fields_subsys_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_subsys_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_subsys_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_subsys_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_subsys_pi_enable_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_subsys_qid_max"></a>
<a id="CHANGED_fields_subsys_qid_max"></a>
###### qid_max

- Schema name: `Qid Max`
- Default: null

Maximum number of queue IDs allowed for this subsystem.
<a id="CHANGED_fields_subsys_qid_max_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_subsys_qid_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_subsys_qid_max_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_subsys_qid_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_subsys_qid_max_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_subsys_ieee_oui"></a>
<a id="CHANGED_fields_subsys_ieee_oui"></a>
###### ieee_oui

- Schema name: `Ieee Oui`
- Default: null

IEEE Organizationally Unique Identifier for the subsystem.
<a id="CHANGED_fields_subsys_ieee_oui_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_subsys_ieee_oui_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_subsys_ieee_oui_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_subsys_ieee_oui_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_subsys_ieee_oui_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_subsys_ana"></a>
<a id="CHANGED_fields_subsys_ana"></a>
###### ana

- Schema name: `Ana`
- Default: null

If set to either `True` or `False`, then *override* the global `ana` setting from `nvmet.global.config` for this subsystem only. If `null`, then the global `ana` setting will take effect.
<a id="CHANGED_fields_subsys_ana_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_subsys_ana_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_subsys_ana_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_subsys_ana_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_subsys_ana_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_subsys_hosts"></a>
<a id="CHANGED_fields_subsys_hosts"></a>
###### hosts

- Schema name: `Hosts`

List of host ids which have access to this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="CHANGED_fields_subsys_hosts_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_subsys_hosts_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_subsys_hosts_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_subsys_hosts_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_CHANGED_fields_subsys_hosts_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_subsys_hosts_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_subsys_namespaces"></a>
<a id="CHANGED_fields_subsys_namespaces"></a>
###### namespaces

- Schema name: `Namespaces`

List of namespaces ids in this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="CHANGED_fields_subsys_namespaces_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_subsys_namespaces_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_subsys_namespaces_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_subsys_namespaces_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_CHANGED_fields_subsys_namespaces_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_subsys_namespaces_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_subsys_ports"></a>
<a id="CHANGED_fields_subsys_ports"></a>
###### ports

- Schema name: `Ports`

List of ports ids on which this subsystem is available. Only populated on query if `extra.options.verbose` is set.
<a id="CHANGED_fields_subsys_ports_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_subsys_ports_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_subsys_ports_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_subsys_ports_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_CHANGED_fields_subsys_ports_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_subsys_ports_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `NVMetPortSubsysRemovedEvent`
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
