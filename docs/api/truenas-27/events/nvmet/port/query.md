---
title: nvmet.port.query
kind: event
source_rst: _sources/api_events_nvmet.port.query.rst.txt
source_html: api_events_nvmet.port.query.html
required_roles:
  - SHARING_NVME_TARGET_READ
---

# nvmet.port.query

## Summary

Sent on nvmet.port changes.

## Required Roles

- `SHARING_NVME_TARGET_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `NVMetPortAddedEvent`
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

- Schema name: `NVMetPortEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF port.

<a id="headingADDED_fields_index"></a>
<a id="ADDED_fields_index"></a>
##### index (required)

- Schema name: `Index`
- Type: integer

Index of the port, for internal use.

<a id="headingADDED_fields_addr_trtype"></a>
<a id="ADDED_fields_addr_trtype"></a>
##### addr_trtype (required)

- Schema name: `Addr Trtype`
- Type: enum (of string)

Fabric transport technology name.
###### Must be one of:

- "TCP"
- "RDMA"
- "FC"

<a id="headingADDED_fields_addr_trsvcid"></a>
<a id="ADDED_fields_addr_trsvcid"></a>
##### addr_trsvcid (required)

- Schema name: `Addr Trsvcid`

Transport-specific TRSVCID field. When configured for TCP/IP or RDMA this will be the port number.
<a id="ADDED_fields_addr_trsvcid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_addr_trsvcid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_addr_trsvcid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_addr_trsvcid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_addr_trsvcid_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_addr_trsvcid_anyOf_i2"></a>
###### [Option 3](#tab-pane_ADDED_fields_addr_trsvcid_anyOf_i2)

- Type: null

<a id="headingADDED_fields_addr_traddr"></a>
<a id="ADDED_fields_addr_traddr"></a>
##### addr_traddr (required)

- Schema name: `Addr Traddr`
- Type: string

A transport-specific field identifying the NVMe host port to use for the connection to the controller. For TCP or RDMA transports, this will be an IPv4 or IPv6 address.

<a id="headingADDED_fields_addr_adrfam"></a>
<a id="ADDED_fields_addr_adrfam"></a>
##### addr_adrfam (required)

- Schema name: `Addr Adrfam`
- Type: enum (of string)

Address family.
###### Must be one of:

- "IPV4"
- "IPV6"
- "FC"

<a id="headingADDED_fields_inline_data_size"></a>
<a id="ADDED_fields_inline_data_size"></a>
##### inline_data_size

- Schema name: `Inline Data Size`
- Default: null

Maximum size for inline data transfers or `null` for default.
<a id="ADDED_fields_inline_data_size_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_inline_data_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_inline_data_size_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_inline_data_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_inline_data_size_anyOf_i1)

- Type: null

<a id="headingADDED_fields_max_queue_size"></a>
<a id="ADDED_fields_max_queue_size"></a>
##### max_queue_size

- Schema name: `Max Queue Size`
- Default: null

Maximum number of queue entries or `null` for default.
<a id="ADDED_fields_max_queue_size_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_max_queue_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_max_queue_size_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_max_queue_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_max_queue_size_anyOf_i1)

- Type: null

<a id="headingADDED_fields_pi_enable"></a>
<a id="ADDED_fields_pi_enable"></a>
##### pi_enable

- Schema name: `Pi Enable`
- Default: null

Whether Protection Information (PI) is enabled or `null` for default.
<a id="ADDED_fields_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_pi_enable_anyOf_i1)

- Type: null

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `NVMetPortChangedEvent`
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

- Schema name: `NVMetPortEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF port.

<a id="headingCHANGED_fields_index"></a>
<a id="CHANGED_fields_index"></a>
##### index (required)

- Schema name: `Index`
- Type: integer

Index of the port, for internal use.

<a id="headingCHANGED_fields_addr_trtype"></a>
<a id="CHANGED_fields_addr_trtype"></a>
##### addr_trtype (required)

- Schema name: `Addr Trtype`
- Type: enum (of string)

Fabric transport technology name.
###### Must be one of:

- "TCP"
- "RDMA"
- "FC"

<a id="headingCHANGED_fields_addr_trsvcid"></a>
<a id="CHANGED_fields_addr_trsvcid"></a>
##### addr_trsvcid (required)

- Schema name: `Addr Trsvcid`

Transport-specific TRSVCID field. When configured for TCP/IP or RDMA this will be the port number.
<a id="CHANGED_fields_addr_trsvcid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_addr_trsvcid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_addr_trsvcid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_addr_trsvcid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_addr_trsvcid_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_addr_trsvcid_anyOf_i2"></a>
###### [Option 3](#tab-pane_CHANGED_fields_addr_trsvcid_anyOf_i2)

- Type: null

<a id="headingCHANGED_fields_addr_traddr"></a>
<a id="CHANGED_fields_addr_traddr"></a>
##### addr_traddr (required)

- Schema name: `Addr Traddr`
- Type: string

A transport-specific field identifying the NVMe host port to use for the connection to the controller. For TCP or RDMA transports, this will be an IPv4 or IPv6 address.

<a id="headingCHANGED_fields_addr_adrfam"></a>
<a id="CHANGED_fields_addr_adrfam"></a>
##### addr_adrfam (required)

- Schema name: `Addr Adrfam`
- Type: enum (of string)

Address family.
###### Must be one of:

- "IPV4"
- "IPV6"
- "FC"

<a id="headingCHANGED_fields_inline_data_size"></a>
<a id="CHANGED_fields_inline_data_size"></a>
##### inline_data_size

- Schema name: `Inline Data Size`
- Default: null

Maximum size for inline data transfers or `null` for default.
<a id="CHANGED_fields_inline_data_size_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_inline_data_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_inline_data_size_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_inline_data_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_inline_data_size_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_max_queue_size"></a>
<a id="CHANGED_fields_max_queue_size"></a>
##### max_queue_size

- Schema name: `Max Queue Size`
- Default: null

Maximum number of queue entries or `null` for default.
<a id="CHANGED_fields_max_queue_size_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_max_queue_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_max_queue_size_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_max_queue_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_max_queue_size_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_pi_enable"></a>
<a id="CHANGED_fields_pi_enable"></a>
##### pi_enable

- Schema name: `Pi Enable`
- Default: null

Whether Protection Information (PI) is enabled or `null` for default.
<a id="CHANGED_fields_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_pi_enable_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `NVMetPortRemovedEvent`
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
