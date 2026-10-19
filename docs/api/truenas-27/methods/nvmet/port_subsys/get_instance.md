---
title: nvmet.port_subsys.get_instance
kind: method
source_rst: _sources/api_methods_nvmet.port_subsys.get_instance.rst.txt
source_html: api_methods_nvmet.port_subsys.get_instance.html
required_roles:
  - SHARING_NVME_TARGET_READ
---

# nvmet.port_subsys.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `SHARING_NVME_TARGET_READ`

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

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NVMetPortSubsysEntry`
- Type: object
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
