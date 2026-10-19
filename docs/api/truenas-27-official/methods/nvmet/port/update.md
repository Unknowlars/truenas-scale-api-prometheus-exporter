---
title: nvmet.port.update
kind: method
source_rst: _sources/api_methods_nvmet.port.update.rst.txt
source_html: api_methods_nvmet.port.update.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.port.update

## Summary

Update NVMe target `port` of `id`.

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

ID of the NVMe-oF port to update.

#### Parameter 2: nvmet_port_update

<a id="Call_parameters_items_i1"></a>
#### nvmet_port_update

- Schema name: `nvmet_port_update`

Updated NVMe-oF port configuration data.
<a id="Call_parameters_items_i1_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0"></a>
###### [NVMetPortUpdateRDMATCP](#tab-pane_Call_parameters_items_i1_anyOf_i0)

- Schema name: `NVMetPortUpdateRDMATCP`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_anyOf_i0_addr_trtype"></a>
<a id="Call_parameters_items_i1_anyOf_i0_addr_trtype"></a>
###### addr_trtype

- Schema name: `Addr Trtype`
- Type: enum (of string)

Fabric transport technology name.
###### Must be one of:

- "TCP"
- "RDMA"

<a id="headingCall_parameters_items_i1_anyOf_i0_addr_trsvcid"></a>
<a id="Call_parameters_items_i1_anyOf_i0_addr_trsvcid"></a>
###### addr_trsvcid

- Schema name: `Addr Trsvcid`
- Type: integer

Transport-specific TRSVCID field. When configured for TCP/IP or RDMA this will be the port number.
- Value must be greater or equal to `1024` and lesser or equal to `65535`

<a id="headingCall_parameters_items_i1_anyOf_i0_addr_traddr"></a>
<a id="Call_parameters_items_i1_anyOf_i0_addr_traddr"></a>
###### addr_traddr

- Schema name: `Addr Traddr`

A transport-specific field identifying the NVMe host port to use for the connection to the controller. For TCP or RDMA transports, this will be an IPv4 or IPv6 address.
<a id="Call_parameters_items_i1_anyOf_i0_addr_traddr_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0_addr_traddr_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i0_addr_traddr_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0_addr_traddr_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i0_addr_traddr_anyOf_i1)

- Type: string

<a id="headingCall_parameters_items_i1_anyOf_i0_inline_data_size"></a>
<a id="Call_parameters_items_i1_anyOf_i0_inline_data_size"></a>
###### inline_data_size

- Schema name: `Inline Data Size`

Maximum size for inline data transfers or `null` for default.
<a id="Call_parameters_items_i1_anyOf_i0_inline_data_size_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0_inline_data_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i0_inline_data_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0_inline_data_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i0_inline_data_size_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_anyOf_i0_max_queue_size"></a>
<a id="Call_parameters_items_i1_anyOf_i0_max_queue_size"></a>
###### max_queue_size

- Schema name: `Max Queue Size`

Maximum number of queue entries or `null` for default.
<a id="Call_parameters_items_i1_anyOf_i0_max_queue_size_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0_max_queue_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i0_max_queue_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0_max_queue_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i0_max_queue_size_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_anyOf_i0_pi_enable"></a>
<a id="Call_parameters_items_i1_anyOf_i0_pi_enable"></a>
###### pi_enable

- Schema name: `Pi Enable`

Whether Protection Information (PI) is enabled or `null` for default.
<a id="Call_parameters_items_i1_anyOf_i0_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i0_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i0_pi_enable_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_anyOf_i0_enabled"></a>
<a id="Call_parameters_items_i1_anyOf_i0_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1"></a>
###### [NVMetPortUpdateFC](#tab-pane_Call_parameters_items_i1_anyOf_i1)

- Schema name: `NVMetPortUpdateFC`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_anyOf_i1_addr_trtype"></a>
<a id="Call_parameters_items_i1_anyOf_i1_addr_trtype"></a>
###### addr_trtype

- Schema name: `Addr Trtype`
- Type: const

Fabric transport technology name.
- Specific value: `"FC"`

<a id="headingCall_parameters_items_i1_anyOf_i1_addr_traddr"></a>
<a id="Call_parameters_items_i1_anyOf_i1_addr_traddr"></a>
###### addr_traddr

- Schema name: `Addr Traddr`
- Type: string

A transport-specific field identifying the NVMe host port to use for the connection to the controller.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_anyOf_i1_inline_data_size"></a>
<a id="Call_parameters_items_i1_anyOf_i1_inline_data_size"></a>
###### inline_data_size

- Schema name: `Inline Data Size`

Maximum size for inline data transfers or `null` for default.
<a id="Call_parameters_items_i1_anyOf_i1_inline_data_size_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1_inline_data_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i1_inline_data_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1_inline_data_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i1_inline_data_size_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_anyOf_i1_max_queue_size"></a>
<a id="Call_parameters_items_i1_anyOf_i1_max_queue_size"></a>
###### max_queue_size

- Schema name: `Max Queue Size`

Maximum number of queue entries or `null` for default.
<a id="Call_parameters_items_i1_anyOf_i1_max_queue_size_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1_max_queue_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i1_max_queue_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1_max_queue_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i1_max_queue_size_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_anyOf_i1_pi_enable"></a>
<a id="Call_parameters_items_i1_anyOf_i1_pi_enable"></a>
###### pi_enable

- Schema name: `Pi Enable`

Whether Protection Information (PI) is enabled or `null` for default.
<a id="Call_parameters_items_i1_anyOf_i1_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i1_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i1_pi_enable_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_anyOf_i1_enabled"></a>
<a id="Call_parameters_items_i1_anyOf_i1_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NVMetPortEntry`
- Type: object

The updated NVMe-oF port configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF port.

<a id="headingReturn_value_index"></a>
<a id="Return_value_index"></a>
#### index (required)

- Schema name: `Index`
- Type: integer

Index of the port, for internal use.

<a id="headingReturn_value_addr_trtype"></a>
<a id="Return_value_addr_trtype"></a>
#### addr_trtype (required)

- Schema name: `Addr Trtype`
- Type: enum (of string)

Fabric transport technology name.
##### Must be one of:

- "TCP"
- "RDMA"
- "FC"

<a id="headingReturn_value_addr_trsvcid"></a>
<a id="Return_value_addr_trsvcid"></a>
#### addr_trsvcid (required)

- Schema name: `Addr Trsvcid`

Transport-specific TRSVCID field. When configured for TCP/IP or RDMA this will be the port number.
<a id="Return_value_addr_trsvcid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_addr_trsvcid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_addr_trsvcid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_addr_trsvcid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_addr_trsvcid_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_addr_trsvcid_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_addr_trsvcid_anyOf_i2)

- Type: null

<a id="headingReturn_value_addr_traddr"></a>
<a id="Return_value_addr_traddr"></a>
#### addr_traddr (required)

- Schema name: `Addr Traddr`
- Type: string

A transport-specific field identifying the NVMe host port to use for the connection to the controller. For TCP or RDMA transports, this will be an IPv4 or IPv6 address.

<a id="headingReturn_value_addr_adrfam"></a>
<a id="Return_value_addr_adrfam"></a>
#### addr_adrfam (required)

- Schema name: `Addr Adrfam`
- Type: enum (of string)

Address family.
##### Must be one of:

- "IPV4"
- "IPV6"
- "FC"

<a id="headingReturn_value_inline_data_size"></a>
<a id="Return_value_inline_data_size"></a>
#### inline_data_size

- Schema name: `Inline Data Size`
- Default: null

Maximum size for inline data transfers or `null` for default.
<a id="Return_value_inline_data_size_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_inline_data_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_inline_data_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_inline_data_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_inline_data_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_max_queue_size"></a>
<a id="Return_value_max_queue_size"></a>
#### max_queue_size

- Schema name: `Max Queue Size`
- Default: null

Maximum number of queue entries or `null` for default.
<a id="Return_value_max_queue_size_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_max_queue_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_max_queue_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_max_queue_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_max_queue_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_pi_enable"></a>
<a id="Return_value_pi_enable"></a>
#### pi_enable

- Schema name: `Pi Enable`
- Default: null

Whether Protection Information (PI) is enabled or `null` for default.
<a id="Return_value_pi_enable_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pi_enable_anyOf_i1)

- Type: null

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
