---
title: iscsi.global.config
kind: method
source_rst: _sources/api_methods_iscsi.global.config.rst.txt
source_html: api_methods_iscsi.global.config.html
required_roles:
  - SHARING_ISCSI_GLOBAL_READ
---

# iscsi.global.config

## Required Roles

- `SHARING_ISCSI_GLOBAL_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ISCSIGlobalEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the global iSCSI configuration.

<a id="headingReturn_value_basename"></a>
<a id="Return_value_basename"></a>
#### basename (required)

- Schema name: `Basename`
- Type: string

Base name prefix for iSCSI target IQNs.

<a id="headingReturn_value_isns_servers"></a>
<a id="Return_value_isns_servers"></a>
#### isns_servers (required)

- Schema name: `Isns Servers`
- Type: array of string

Array of iSNS (Internet Storage Name Service) server addresses.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_isns_servers_items"></a>
- Type: string

<a id="headingReturn_value_listen_port"></a>
<a id="Return_value_listen_port"></a>
#### listen_port

- Schema name: `Listen Port`
- Type: integer
- Default: 3260

TCP port number for iSCSI connections.
- Value must be greater or equal to `1025` and lesser or equal to `65535`

<a id="headingReturn_value_pool_avail_threshold"></a>
<a id="Return_value_pool_avail_threshold"></a>
#### pool_avail_threshold

- Schema name: `Pool Avail Threshold`
- Default: null

Pool available space threshold percentage or `null` to disable.
<a id="Return_value_pool_avail_threshold_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_pool_avail_threshold_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pool_avail_threshold_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `99`

<a id="tab-pane_Return_value_pool_avail_threshold_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pool_avail_threshold_anyOf_i1)

- Type: null

<a id="headingReturn_value_alua"></a>
<a id="Return_value_alua"></a>
#### alua (required)

- Schema name: `Alua`
- Type: boolean

Whether Asymmetric Logical Unit Access (ALUA) is enabled. Enabling is limited to TrueNAS Enterprise-licensed high availability systems. ALUA only works when configured on both the client and server.

<a id="headingReturn_value_iser"></a>
<a id="Return_value_iser"></a>
#### iser (required)

- Schema name: `Iser`
- Type: boolean

Whether iSCSI Extensions for RDMA (iSER) are enabled. Enabling is limited to TrueNAS Enterprise-licensed systems and requires the system and network environment have Remote Direct Memory Access (RDMA)-capable hardware.

<a id="headingReturn_value_direct_config"></a>
<a id="Return_value_direct_config"></a>
#### direct_config (required)

- Schema name: `Direct Config`

Whether configuration is written into the kernel directly by middlewared.
<a id="Return_value_direct_config_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_direct_config_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_direct_config_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_direct_config_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_direct_config_anyOf_i1)

- Type: null

<a id="headingReturn_value_mode"></a>
<a id="Return_value_mode"></a>
#### mode (required)

- Schema name: `Mode`
- Type: integer

Internal iSCSI operational mode.
- Value must be greater or equal to `0` and lesser or equal to `1`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
