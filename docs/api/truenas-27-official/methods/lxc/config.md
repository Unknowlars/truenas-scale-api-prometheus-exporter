---
title: lxc.config
kind: method
source_rst: _sources/api_methods_lxc.config.rst.txt
source_html: api_methods_lxc.config.html
required_roles:
  - LXC_CONFIG_READ
---

# lxc.config

## Required Roles

- `LXC_CONFIG_READ`

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

- Schema name: `LXCConfigEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Configuration ID.

<a id="headingReturn_value_preferred_pool"></a>
<a id="Return_value_preferred_pool"></a>
#### preferred_pool

- Schema name: `Preferred Pool`
- Default: null

Default pool used by containers and image datasets.
<a id="Return_value_preferred_pool_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_preferred_pool_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_preferred_pool_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_preferred_pool_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_preferred_pool_anyOf_i1)

- Type: null

<a id="headingReturn_value_bridge"></a>
<a id="Return_value_bridge"></a>
#### bridge

- Schema name: `Bridge`
- Default: null

Network bridge interface for virtualized instance networking. `null` if not configured.
<a id="Return_value_bridge_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_bridge_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_bridge_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_bridge_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_bridge_anyOf_i1)

- Type: null

<a id="headingReturn_value_v4_network"></a>
<a id="Return_value_v4_network"></a>
#### v4_network (required)

- Schema name: `V4 Network`
- Type: string

IPv4 network CIDR for the container bridge network.

<a id="headingReturn_value_v6_network"></a>
<a id="Return_value_v6_network"></a>
#### v6_network (required)

- Schema name: `V6 Network`
- Type: string

IPv6 network CIDR for the container bridge network.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
