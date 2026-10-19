---
title: interface.query
kind: method
source_rst: _sources/api_methods_interface.query.rst.txt
source_html: api_methods_interface.query.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# interface.query

## Summary

Query Interfaces with `query-filters` and `query-options`

`options.extra.retrieve_names_only` (bool): Only return interface names.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Query options including pagination, ordering, and additional parameters.
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

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### InterfaceQueryResultItem

- Schema name: `InterfaceQueryResultItem`
- Type: object
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: string

Unique identifier for the network interface.

<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Name of the network interface.

<a id="headingReturn_value_anyOf_i0_items_fake"></a>
<a id="Return_value_anyOf_i0_items_fake"></a>
###### fake

- Schema name: `Fake`
- Type: boolean

Whether this is a fake/simulated interface for testing purposes.

<a id="headingReturn_value_anyOf_i0_items_type"></a>
<a id="Return_value_anyOf_i0_items_type"></a>
###### type

- Schema name: `Type`
- Type: string

Type of interface (PHYSICAL, BRIDGE, LINK_AGGREGATION, VLAN, etc.).

<a id="headingReturn_value_anyOf_i0_items_state"></a>
<a id="Return_value_anyOf_i0_items_state"></a>
###### state

- Schema name: `InterfaceEntryState`
- Type: object

Current runtime state information for the interface.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_state_name"></a>
<a id="Return_value_anyOf_i0_items_state_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Current name of the network interface.

<a id="headingReturn_value_anyOf_i0_items_state_orig_name"></a>
<a id="Return_value_anyOf_i0_items_state_orig_name"></a>
###### orig_name (required)

- Schema name: `Orig Name`
- Type: string

Original name of the network interface before any renaming.

<a id="headingReturn_value_anyOf_i0_items_state_description"></a>
<a id="Return_value_anyOf_i0_items_state_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the network interface.

<a id="headingReturn_value_anyOf_i0_items_state_mtu"></a>
<a id="Return_value_anyOf_i0_items_state_mtu"></a>
###### mtu (required)

- Schema name: `Mtu`
- Type: integer

Maximum transmission unit size for the interface.

<a id="headingReturn_value_anyOf_i0_items_state_cloned"></a>
<a id="Return_value_anyOf_i0_items_state_cloned"></a>
###### cloned (required)

- Schema name: `Cloned`
- Type: boolean

Whether the interface is a cloned/virtual interface.

<a id="headingReturn_value_anyOf_i0_items_state_flags"></a>
<a id="Return_value_anyOf_i0_items_state_flags"></a>
###### flags (required)

- Schema name: `Flags`
- Type: array of string

List of interface flags indicating various states and capabilities. Common flags include UP, DOWN, RUNNING, MULTICAST, BROADCAST, LOOPBACK, and POINTOPOINT.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_state_flags_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_state_nd6_flags"></a>
<a id="Return_value_anyOf_i0_items_state_nd6_flags"></a>
###### nd6_flags (required)

- Schema name: `Nd6 Flags`
- Type: array

IPv6 neighbor discovery flags. These control IPv6 autoconfiguration behavior and include flags like AUTO*LINKLOCAL, ACCEPT*RTADV, and PERFORMNUD.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_state_nd6_flags_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_state_capabilities"></a>
<a id="Return_value_anyOf_i0_items_state_capabilities"></a>
###### capabilities (required)

- Schema name: `Capabilities`
- Type: array

List of hardware capabilities supported by the interface. Common capabilities include VLAN*MTU, JUMBO*MTU, VLAN*HWTAGGING, VLAN*HWCSUM, and TSO4.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_state_capabilities_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_state_link_state"></a>
<a id="Return_value_anyOf_i0_items_state_link_state"></a>
###### link_state (required)

- Schema name: `Link State`
- Type: string

Current link state of the interface (up, down, etc.).

<a id="headingReturn_value_anyOf_i0_items_state_media_type"></a>
<a id="Return_value_anyOf_i0_items_state_media_type"></a>
###### media_type (required)

- Schema name: `Media Type`
- Type: string

Type of media/connection for the interface. Examples include Ethernet, 802.11, or loopback.

<a id="headingReturn_value_anyOf_i0_items_state_media_subtype"></a>
<a id="Return_value_anyOf_i0_items_state_media_subtype"></a>
###### media_subtype (required)

- Schema name: `Media Subtype`
- Type: string

Subtype of media/connection for the interface. Examples include 1000baseT, 100baseTX, or autoselect.

<a id="headingReturn_value_anyOf_i0_items_state_active_media_type"></a>
<a id="Return_value_anyOf_i0_items_state_active_media_type"></a>
###### active_media_type (required)

- Schema name: `Active Media Type`
- Type: string

Currently active media type. This may differ from configured media_type during autonegotiation.

<a id="headingReturn_value_anyOf_i0_items_state_active_media_subtype"></a>
<a id="Return_value_anyOf_i0_items_state_active_media_subtype"></a>
###### active_media_subtype (required)

- Schema name: `Active Media Subtype`
- Type: string

Currently active media subtype. This reflects the actual negotiated connection speed and type.

<a id="headingReturn_value_anyOf_i0_items_state_supported_media"></a>
<a id="Return_value_anyOf_i0_items_state_supported_media"></a>
###### supported_media (required)

- Schema name: `Supported Media`
- Type: array

List of supported media types for the interface. Contains media descriptors like '1000baseT <full-duplex>' or 'autoselect'.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_state_supported_media_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_state_media_options"></a>
<a id="Return_value_anyOf_i0_items_state_media_options"></a>
###### media_options (required)

- Schema name: `Media Options`

Available media options for the interface. Options may include 'full-duplex', 'half-duplex', 'flowcontrol', or 'rxpause'.
<a id="Return_value_anyOf_i0_items_state_media_options_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_media_options_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_media_options_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_state_media_options_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_Return_value_anyOf_i0_items_state_media_options_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_media_options_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state_link_address"></a>
<a id="Return_value_anyOf_i0_items_state_link_address"></a>
###### link_address (required)

- Schema name: `Link Address`
- Type: string

MAC address of the interface.

<a id="headingReturn_value_anyOf_i0_items_state_permanent_link_address"></a>
<a id="Return_value_anyOf_i0_items_state_permanent_link_address"></a>
###### permanent_link_address (required)

- Schema name: `Permanent Link Address`

Permanent MAC address of the interface if different from current.
<a id="Return_value_anyOf_i0_items_state_permanent_link_address_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_permanent_link_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_permanent_link_address_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_state_permanent_link_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_permanent_link_address_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state_hardware_link_address"></a>
<a id="Return_value_anyOf_i0_items_state_hardware_link_address"></a>
###### hardware_link_address (required)

- Schema name: `Hardware Link Address`
- Type: string

Hardware MAC address of the interface.

<a id="headingReturn_value_anyOf_i0_items_state_rx_queues"></a>
<a id="Return_value_anyOf_i0_items_state_rx_queues"></a>
###### rx_queues

- Schema name: `Rx Queues`
- Type: integer

Number of receive queues configured for the interface.

<a id="headingReturn_value_anyOf_i0_items_state_tx_queues"></a>
<a id="Return_value_anyOf_i0_items_state_tx_queues"></a>
###### tx_queues

- Schema name: `Tx Queues`
- Type: integer

Number of transmit queues configured for the interface.

<a id="headingReturn_value_anyOf_i0_items_state_aliases"></a>
<a id="Return_value_anyOf_i0_items_state_aliases"></a>
###### aliases (required)

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases configured on the interface.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_state_aliases_items"></a>
###### InterfaceEntryStateAlias

- Schema name: `InterfaceEntryStateAlias`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_state_aliases_items_type"></a>
<a id="Return_value_anyOf_i0_items_state_aliases_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

<a id="headingReturn_value_anyOf_i0_items_state_aliases_items_address"></a>
<a id="Return_value_anyOf_i0_items_state_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`
- Type: string

The IP address value.

<a id="headingReturn_value_anyOf_i0_items_state_aliases_items_netmask"></a>
<a id="Return_value_anyOf_i0_items_state_aliases_items_netmask"></a>
###### netmask

- Schema name: `Netmask`

The network mask for the IP address, either as a string or CIDR notation integer.
<a id="Return_value_anyOf_i0_items_state_aliases_items_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_aliases_items_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_aliases_items_netmask_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_state_aliases_items_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_aliases_items_netmask_anyOf_i1)

- Type: integer

<a id="headingReturn_value_anyOf_i0_items_state_aliases_items_broadcast"></a>
<a id="Return_value_anyOf_i0_items_state_aliases_items_broadcast"></a>
###### broadcast

- Schema name: `Broadcast`
- Type: string

Broadcast address for the network interface.

<a id="headingReturn_value_anyOf_i0_items_state_vrrp_config"></a>
<a id="Return_value_anyOf_i0_items_state_vrrp_config"></a>
###### vrrp_config

- Schema name: `Vrrp Config`
- Default: []

VRRP (Virtual Router Redundancy Protocol) configuration for the interface.
<a id="Return_value_anyOf_i0_items_state_vrrp_config_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_vrrp_config_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_vrrp_config_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_state_vrrp_config_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_Return_value_anyOf_i0_items_state_vrrp_config_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_vrrp_config_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state_protocol"></a>
<a id="Return_value_anyOf_i0_items_state_protocol"></a>
###### protocol

- Schema name: `Protocol`

Link aggregation protocol used (LACP, FAILOVER, etc.).
<a id="Return_value_anyOf_i0_items_state_protocol_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_protocol_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_protocol_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_state_protocol_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_protocol_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state_ports"></a>
<a id="Return_value_anyOf_i0_items_state_ports"></a>
###### ports

- Schema name: `Ports`
- Type: array of object
- Default: []

List of ports that are members of this link aggregation group.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_state_ports_items"></a>
###### InterfaceEntryStatePort

- Schema name: `InterfaceEntryStatePort`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_state_ports_items_name"></a>
<a id="Return_value_anyOf_i0_items_state_ports_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

The name of the port interface.

<a id="headingReturn_value_anyOf_i0_items_state_ports_items_flags"></a>
<a id="Return_value_anyOf_i0_items_state_ports_items_flags"></a>
###### flags (required)

- Schema name: `Flags`
- Type: array of string

List of flags associated with the port.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_state_ports_items_flags_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_state_xmit_hash_policy"></a>
<a id="Return_value_anyOf_i0_items_state_xmit_hash_policy"></a>
###### xmit_hash_policy

- Schema name: `Xmit Hash Policy`
- Default: null

Transmit hash policy for load balancing in link aggregation. LAYER2 uses MAC addresses, LAYER2+3 adds IP addresses, and LAYER3+4 includes TCP/UDP ports for distribution.
<a id="Return_value_anyOf_i0_items_state_xmit_hash_policy_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_xmit_hash_policy_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_xmit_hash_policy_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_state_xmit_hash_policy_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_xmit_hash_policy_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state_lacpdu_rate"></a>
<a id="Return_value_anyOf_i0_items_state_lacpdu_rate"></a>
###### lacpdu_rate

- Schema name: `Lacpdu Rate`
- Default: null

LACP data unit transmission rate. SLOW sends LACPDUs every 30 seconds, FAST sends every 1 second for quicker link failure detection.
<a id="Return_value_anyOf_i0_items_state_lacpdu_rate_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_lacpdu_rate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_lacpdu_rate_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_state_lacpdu_rate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_lacpdu_rate_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state_parent"></a>
<a id="Return_value_anyOf_i0_items_state_parent"></a>
###### parent

- Schema name: `Parent`

Parent interface for VLAN configuration.
<a id="Return_value_anyOf_i0_items_state_parent_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_parent_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_parent_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_state_parent_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_parent_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state_tag"></a>
<a id="Return_value_anyOf_i0_items_state_tag"></a>
###### tag

- Schema name: `Tag`

VLAN tag number.
<a id="Return_value_anyOf_i0_items_state_tag_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_tag_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_tag_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_state_tag_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_tag_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state_pcp"></a>
<a id="Return_value_anyOf_i0_items_state_pcp"></a>
###### pcp

- Schema name: `Pcp`

Priority Code Point for VLAN traffic prioritization. Values 0-7 map to different QoS priority levels, with 0 being lowest and 7 highest priority.
<a id="Return_value_anyOf_i0_items_state_pcp_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_pcp_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_pcp_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_state_pcp_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_pcp_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state_fec_mode"></a>
<a id="Return_value_anyOf_i0_items_state_fec_mode"></a>
###### fec_mode

- Schema name: `Fec Mode`

Currently active Forward Error Correction mode from the hardware. Only present for physical interfaces. "AUTO": Selects the best FEC mode based on cable/port capabilities "RS": RS-FEC (Reed-Solomon), often used for 25GbE/100GbE+ NICs "BASER": BaseR-FEC (FireCode) "OFF": Disables FEC "LLRS": Low Latency Reed-Solomon FEC, used for 25GBASE-KR/CR `null`: FEC not supported or mode cannot be determined
<a id="Return_value_anyOf_i0_items_state_fec_mode_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_state_fec_mode_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_state_fec_mode_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "AUTO"
- "OFF"
- "RS"
- "BASER"
- "LLRS"

<a id="tab-pane_Return_value_anyOf_i0_items_state_fec_mode_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_state_fec_mode_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_aliases"></a>
<a id="Return_value_anyOf_i0_items_aliases"></a>
###### aliases

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases configured on the interface.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_aliases_items"></a>
###### InterfaceEntryAlias

- Schema name: `InterfaceEntryAlias`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_aliases_items_type"></a>
<a id="Return_value_anyOf_i0_items_aliases_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

<a id="headingReturn_value_anyOf_i0_items_aliases_items_address"></a>
<a id="Return_value_anyOf_i0_items_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`
- Type: string

The IP address value.

<a id="headingReturn_value_anyOf_i0_items_aliases_items_netmask"></a>
<a id="Return_value_anyOf_i0_items_aliases_items_netmask"></a>
###### netmask (required)

- Schema name: `Netmask`

The network mask for the IP address, either as a string or CIDR notation integer.
<a id="Return_value_anyOf_i0_items_aliases_items_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_aliases_items_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_aliases_items_netmask_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_aliases_items_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_aliases_items_netmask_anyOf_i1)

- Type: integer

<a id="headingReturn_value_anyOf_i0_items_ipv4_dhcp"></a>
<a id="Return_value_anyOf_i0_items_ipv4_dhcp"></a>
###### ipv4_dhcp

- Schema name: `Ipv4 Dhcp`
- Type: boolean

Whether IPv4 DHCP is enabled for automatic IP address assignment.

<a id="headingReturn_value_anyOf_i0_items_ipv6_auto"></a>
<a id="Return_value_anyOf_i0_items_ipv6_auto"></a>
###### ipv6_auto

- Schema name: `Ipv6 Auto`
- Type: boolean

Whether IPv6 autoconfiguration is enabled.

<a id="headingReturn_value_anyOf_i0_items_description"></a>
<a id="Return_value_anyOf_i0_items_description"></a>
###### description

- Schema name: `Description`
- Type: string

Human-readable description of the interface.

<a id="headingReturn_value_anyOf_i0_items_mtu"></a>
<a id="Return_value_anyOf_i0_items_mtu"></a>
###### mtu

- Schema name: `Mtu`

Maximum transmission unit size for the interface.
<a id="Return_value_anyOf_i0_items_mtu_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_mtu_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_mtu_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_mtu_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_mtu_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_fec_mode"></a>
<a id="Return_value_anyOf_i0_items_fec_mode"></a>
###### fec_mode

- Schema name: `Fec Mode`
- Type: enum (of string)

Forward Error Correction (FEC) mode. Only valid for physical interfaces. "AUTO": Selects the best FEC mode based on cable/port capabilities "RS": RS-FEC (Reed-Solomon), often used for 25GbE/100GbE+ NICs "BASER": BaseR-FEC (FireCode) "OFF": Disables FEC "LLRS": Low Latency Reed-Solomon FEC, used for 25GBASE-KR/CR
###### Must be one of:

- "AUTO"
- "OFF"
- "RS"
- "BASER"
- "LLRS"

<a id="headingReturn_value_anyOf_i0_items_vlan_parent_interface"></a>
<a id="Return_value_anyOf_i0_items_vlan_parent_interface"></a>
###### vlan_parent_interface

- Schema name: `Vlan Parent Interface`

Parent interface for VLAN configuration.
<a id="Return_value_anyOf_i0_items_vlan_parent_interface_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_vlan_parent_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_vlan_parent_interface_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_vlan_parent_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_vlan_parent_interface_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_vlan_tag"></a>
<a id="Return_value_anyOf_i0_items_vlan_tag"></a>
###### vlan_tag

- Schema name: `Vlan Tag`

VLAN tag number for VLAN interfaces.
<a id="Return_value_anyOf_i0_items_vlan_tag_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_vlan_tag_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_vlan_tag_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_vlan_tag_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_vlan_tag_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_vlan_pcp"></a>
<a id="Return_value_anyOf_i0_items_vlan_pcp"></a>
###### vlan_pcp

- Schema name: `Vlan Pcp`

Priority Code Point for VLAN traffic prioritization.
<a id="Return_value_anyOf_i0_items_vlan_pcp_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_vlan_pcp_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_vlan_pcp_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_vlan_pcp_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_vlan_pcp_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_lag_protocol"></a>
<a id="Return_value_anyOf_i0_items_lag_protocol"></a>
###### lag_protocol

- Schema name: `Lag Protocol`
- Type: string

Link aggregation protocol (LACP, FAILOVER, LOADBALANCE, etc.).

<a id="headingReturn_value_anyOf_i0_items_lag_ports"></a>
<a id="Return_value_anyOf_i0_items_lag_ports"></a>
###### lag_ports

- Schema name: `Lag Ports`
- Type: array of string

List of interface names that are members of this link aggregation group.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_lag_ports_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_bridge_members"></a>
<a id="Return_value_anyOf_i0_items_bridge_members"></a>
###### bridge_members

- Schema name: `Bridge Members`
- Type: array of string

List of interface names that are members of this bridge.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_bridge_members_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_enable_learning"></a>
<a id="Return_value_anyOf_i0_items_enable_learning"></a>
###### enable_learning

- Schema name: `Enable Learning`
- Type: boolean

Whether MAC address learning is enabled for bridge interfaces.

<a id="headingReturn_value_anyOf_i0_items_additionalProperties"></a>
<a id="Return_value_anyOf_i0_items_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [InterfaceQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `InterfaceQueryResultItem`
- Type: object
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: string

Unique identifier for the network interface.

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name

- Schema name: `Name`
- Type: string

Name of the network interface.

<a id="headingReturn_value_anyOf_i1_fake"></a>
<a id="Return_value_anyOf_i1_fake"></a>
###### fake

- Schema name: `Fake`
- Type: boolean

Whether this is a fake/simulated interface for testing purposes.

<a id="headingReturn_value_anyOf_i1_type"></a>
<a id="Return_value_anyOf_i1_type"></a>
###### type

- Schema name: `Type`
- Type: string

Type of interface (PHYSICAL, BRIDGE, LINK_AGGREGATION, VLAN, etc.).

<a id="headingReturn_value_anyOf_i1_state"></a>
<a id="Return_value_anyOf_i1_state"></a>
###### state

- Type: object

Current runtime state information for the interface.

<a id="headingReturn_value_anyOf_i1_aliases"></a>
<a id="Return_value_anyOf_i1_aliases"></a>
###### aliases

- Schema name: `Aliases`
- Type: array

List of IP address aliases configured on the interface.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_aliases_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i1_ipv4_dhcp"></a>
<a id="Return_value_anyOf_i1_ipv4_dhcp"></a>
###### ipv4_dhcp

- Schema name: `Ipv4 Dhcp`
- Type: boolean

Whether IPv4 DHCP is enabled for automatic IP address assignment.

<a id="headingReturn_value_anyOf_i1_ipv6_auto"></a>
<a id="Return_value_anyOf_i1_ipv6_auto"></a>
###### ipv6_auto

- Schema name: `Ipv6 Auto`
- Type: boolean

Whether IPv6 autoconfiguration is enabled.

<a id="headingReturn_value_anyOf_i1_description"></a>
<a id="Return_value_anyOf_i1_description"></a>
###### description

- Schema name: `Description`
- Type: string

Human-readable description of the interface.

<a id="headingReturn_value_anyOf_i1_mtu"></a>
<a id="Return_value_anyOf_i1_mtu"></a>
###### mtu

- Schema name: `Mtu`

Maximum transmission unit size for the interface.
<a id="Return_value_anyOf_i1_mtu_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_mtu_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_mtu_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_mtu_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_mtu_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_fec_mode"></a>
<a id="Return_value_anyOf_i1_fec_mode"></a>
###### fec_mode

- Schema name: `Fec Mode`
- Type: enum (of string)

Forward Error Correction (FEC) mode. Only valid for physical interfaces. "AUTO": Selects the best FEC mode based on cable/port capabilities "RS": RS-FEC (Reed-Solomon), often used for 25GbE/100GbE+ NICs "BASER": BaseR-FEC (FireCode) "OFF": Disables FEC "LLRS": Low Latency Reed-Solomon FEC, used for 25GBASE-KR/CR
###### Must be one of:

- "AUTO"
- "OFF"
- "RS"
- "BASER"
- "LLRS"

<a id="headingReturn_value_anyOf_i1_vlan_parent_interface"></a>
<a id="Return_value_anyOf_i1_vlan_parent_interface"></a>
###### vlan_parent_interface

- Schema name: `Vlan Parent Interface`

Parent interface for VLAN configuration.
<a id="Return_value_anyOf_i1_vlan_parent_interface_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_vlan_parent_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_vlan_parent_interface_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_vlan_parent_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_vlan_parent_interface_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_vlan_tag"></a>
<a id="Return_value_anyOf_i1_vlan_tag"></a>
###### vlan_tag

- Schema name: `Vlan Tag`

VLAN tag number for VLAN interfaces.
<a id="Return_value_anyOf_i1_vlan_tag_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_vlan_tag_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_vlan_tag_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_vlan_tag_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_vlan_tag_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_vlan_pcp"></a>
<a id="Return_value_anyOf_i1_vlan_pcp"></a>
###### vlan_pcp

- Schema name: `Vlan Pcp`

Priority Code Point for VLAN traffic prioritization.
<a id="Return_value_anyOf_i1_vlan_pcp_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_vlan_pcp_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_vlan_pcp_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_vlan_pcp_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_vlan_pcp_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_lag_protocol"></a>
<a id="Return_value_anyOf_i1_lag_protocol"></a>
###### lag_protocol

- Schema name: `Lag Protocol`
- Type: string

Link aggregation protocol (LACP, FAILOVER, LOADBALANCE, etc.).

<a id="headingReturn_value_anyOf_i1_lag_ports"></a>
<a id="Return_value_anyOf_i1_lag_ports"></a>
###### lag_ports

- Schema name: `Lag Ports`
- Type: array of string

List of interface names that are members of this link aggregation group.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_lag_ports_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i1_bridge_members"></a>
<a id="Return_value_anyOf_i1_bridge_members"></a>
###### bridge_members

- Schema name: `Bridge Members`
- Type: array of string

List of interface names that are members of this bridge.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_bridge_members_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i1_enable_learning"></a>
<a id="Return_value_anyOf_i1_enable_learning"></a>
###### enable_learning

- Schema name: `Enable Learning`
- Type: boolean

Whether MAC address learning is enabled for bridge interfaces.

<a id="headingReturn_value_anyOf_i1_additionalProperties"></a>
<a id="Return_value_anyOf_i1_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
