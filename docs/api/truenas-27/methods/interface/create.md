---
title: interface.create
kind: method
source_rst: _sources/api_methods_interface.create.rst.txt
source_html: api_methods_interface.create.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.create

## Summary

Create virtual interfaces (Link Aggregation, VLAN)

.. examples(cli)::

Create a bridge interface:

> network interface create name=br0 type=BRIDGE bridge_members=enp0s3,enp0s4 aliases="192.168.0.10"

Create a link aggregation interface that has multiple IP addresses in multiple subnets:

> network interface create name=bond0 type=LINK_AGGREGATION lag_protocol=LACP lag_ports=enp0s8,enp0s9 aliases="192.168.0.20/30","192.168.1.20/30"

Create a DHCP-enabled VLAN interface

> network interface create name=vlan0 type=VLAN vlan_parent_interface=enp0s10 vlan_tag=10 vlan_pcp=4 ipv4_dhcp=true ipv6_auto=true

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Configuration data for the new interface.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name

- Schema name: `Name`
- Type: string

Generate a name if not provided based on `type`, e.g. "br0", "bond1", "vlan0".

<a id="headingCall_parameters_items_i0_description"></a>
<a id="Call_parameters_items_i0_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Human-readable description of the interface.

<a id="headingCall_parameters_items_i0_type"></a>
<a id="Call_parameters_items_i0_type"></a>
##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of interface to create.
###### Must be one of:

- "BRIDGE"
- "LINK_AGGREGATION"
- "VLAN"

<a id="headingCall_parameters_items_i0_ipv4_dhcp"></a>
<a id="Call_parameters_items_i0_ipv4_dhcp"></a>
##### ipv4_dhcp

- Schema name: `Ipv4 Dhcp`
- Type: boolean
- Default: false

Enable IPv4 DHCP for automatic IP address assignment.

<a id="headingCall_parameters_items_i0_ipv6_auto"></a>
<a id="Call_parameters_items_i0_ipv6_auto"></a>
##### ipv6_auto

- Schema name: `Ipv6 Auto`
- Type: boolean
- Default: false

Enable IPv6 autoconfiguration.

<a id="headingCall_parameters_items_i0_aliases"></a>
<a id="Call_parameters_items_i0_aliases"></a>
##### aliases

- Schema name: `Aliases`
- Type: array of object
- Default: []

List of IP address aliases to configure on the interface.
- All items must be unique
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_aliases_items"></a>
###### InterfaceCreateAlias

- Schema name: `InterfaceCreateAlias`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_aliases_items_type"></a>
<a id="Call_parameters_items_i0_aliases_items_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "INET"

The type of IP address (INET for IPv4, INET6 for IPv6).
###### Must be one of:

- "INET"
- "INET6"

<a id="headingCall_parameters_items_i0_aliases_items_address"></a>
<a id="Call_parameters_items_i0_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`

The IP address for the failover alias.
<a id="Call_parameters_items_i0_aliases_items_address_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_aliases_items_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_aliases_items_address_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Call_parameters_items_i0_aliases_items_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_aliases_items_address_anyOf_i1)

- Type: string

<a id="headingCall_parameters_items_i0_aliases_items_netmask"></a>
<a id="Call_parameters_items_i0_aliases_items_netmask"></a>
###### netmask (required)

- Schema name: `Netmask`
- Type: integer

The network mask in CIDR notation.

<a id="headingCall_parameters_items_i0_failover_critical"></a>
<a id="Call_parameters_items_i0_failover_critical"></a>
##### failover_critical

- Schema name: `Failover Critical`
- Type: boolean
- Default: false

Whether this interface is critical for failover functionality. Critical interfaces are monitored for failover events and can trigger failover when they fail.

<a id="headingCall_parameters_items_i0_failover_group"></a>
<a id="Call_parameters_items_i0_failover_group"></a>
##### failover_group

- Schema name: `Failover Group`

Failover group identifier for clustering. Interfaces in the same group fail over together during failover events.
<a id="Call_parameters_items_i0_failover_group_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_failover_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_failover_group_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_failover_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_failover_group_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_failover_vhid"></a>
<a id="Call_parameters_items_i0_failover_vhid"></a>
##### failover_vhid

- Schema name: `Failover Vhid`

Virtual Host ID for VRRP failover configuration. Must be unique within the VRRP group and match between failover nodes.
<a id="Call_parameters_items_i0_failover_vhid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_failover_vhid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_failover_vhid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `255`

<a id="tab-pane_Call_parameters_items_i0_failover_vhid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_failover_vhid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_failover_aliases"></a>
<a id="Call_parameters_items_i0_failover_aliases"></a>
##### failover_aliases

- Schema name: `Failover Aliases`
- Type: array of object
- Default: []

List of IP aliases for failover configuration. These IPs are assigned to the interface during normal operation and migrate during failover.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_failover_aliases_items"></a>
###### InterfaceCreateFailoverAlias

- Schema name: `InterfaceCreateFailoverAlias`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_failover_aliases_items_type"></a>
<a id="Call_parameters_items_i0_failover_aliases_items_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "INET"

The type of IP address (INET for IPv4, INET6 for IPv6).
###### Must be one of:

- "INET"
- "INET6"

<a id="headingCall_parameters_items_i0_failover_aliases_items_address"></a>
<a id="Call_parameters_items_i0_failover_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`

The IP address for the failover alias.
<a id="Call_parameters_items_i0_failover_aliases_items_address_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_failover_aliases_items_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_failover_aliases_items_address_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Call_parameters_items_i0_failover_aliases_items_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_failover_aliases_items_address_anyOf_i1)

- Type: string

<a id="headingCall_parameters_items_i0_failover_virtual_aliases"></a>
<a id="Call_parameters_items_i0_failover_virtual_aliases"></a>
##### failover_virtual_aliases

- Schema name: `Failover Virtual Aliases`
- Type: array of object
- Default: []

List of virtual IP aliases for failover configuration. These are shared IPs that float between nodes during failover events.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_failover_virtual_aliases_items"></a>
###### InterfaceCreateFailoverAlias

- Schema name: `InterfaceCreateFailoverAlias`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_failover_virtual_aliases_items_type"></a>
<a id="Call_parameters_items_i0_failover_virtual_aliases_items_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "INET"

The type of IP address (INET for IPv4, INET6 for IPv6).
###### Must be one of:

- "INET"
- "INET6"

<a id="headingCall_parameters_items_i0_failover_virtual_aliases_items_address"></a>
<a id="Call_parameters_items_i0_failover_virtual_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`

The IP address for the failover alias.
<a id="Call_parameters_items_i0_failover_virtual_aliases_items_address_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_failover_virtual_aliases_items_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_failover_virtual_aliases_items_address_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Call_parameters_items_i0_failover_virtual_aliases_items_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_failover_virtual_aliases_items_address_anyOf_i1)

- Type: string

<a id="headingCall_parameters_items_i0_bridge_members"></a>
<a id="Call_parameters_items_i0_bridge_members"></a>
##### bridge_members

- Schema name: `Bridge Members`
- Type: array
- Default: []

List of interfaces to add as members of this bridge.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_bridge_members_items"></a>
- Type: object

<a id="headingCall_parameters_items_i0_enable_learning"></a>
<a id="Call_parameters_items_i0_enable_learning"></a>
##### enable_learning

- Schema name: `Enable Learning`
- Type: boolean
- Default: true

Enable MAC address learning for bridge interfaces. When enabled, the bridge learns MAC addresses from incoming frames and builds a forwarding table to optimize traffic flow.

<a id="headingCall_parameters_items_i0_stp"></a>
<a id="Call_parameters_items_i0_stp"></a>
##### stp

- Schema name: `Stp`
- Type: boolean
- Default: true

Enable Spanning Tree Protocol for bridge interfaces. STP prevents network loops by blocking redundant paths and enables automatic failover when the primary path fails.

<a id="headingCall_parameters_items_i0_lag_protocol"></a>
<a id="Call_parameters_items_i0_lag_protocol"></a>
##### lag_protocol

- Schema name: `Lag Protocol`
- Type: enum (of string)

Link aggregation protocol to use for bonding interfaces. LACP uses 802.3ad dynamic negotiation, FAILOVER provides active-backup, LOADBALANCE and ROUNDROBIN distribute traffic across links.
###### Must be one of:

- "LACP"
- "FAILOVER"
- "LOADBALANCE"
- "ROUNDROBIN"
- "NONE"

<a id="headingCall_parameters_items_i0_xmit_hash_policy"></a>
<a id="Call_parameters_items_i0_xmit_hash_policy"></a>
##### xmit_hash_policy

- Schema name: `Xmit Hash Policy`
- Type: enum (of null or string)
- Default: null

Transmit hash policy for load balancing in link aggregation. LAYER2 uses MAC addresses, LAYER2+3 adds IP addresses, and LAYER3+4 includes TCP/UDP ports for distribution.
###### Must be one of:

- "LAYER2"
- "LAYER2+3"
- "LAYER3+4"
- null

<a id="headingCall_parameters_items_i0_lacpdu_rate"></a>
<a id="Call_parameters_items_i0_lacpdu_rate"></a>
##### lacpdu_rate

- Schema name: `Lacpdu Rate`
- Type: enum (of null or string)
- Default: null

LACP data unit transmission rate. SLOW sends LACPDUs every 30 seconds, FAST sends every 1 second for quicker link failure detection.
###### Must be one of:

- "SLOW"
- "FAST"
- null

<a id="headingCall_parameters_items_i0_lag_ports"></a>
<a id="Call_parameters_items_i0_lag_ports"></a>
##### lag_ports

- Schema name: `Lag Ports`
- Type: array of string
- Default: []

List of interface names to include in the link aggregation group.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_lag_ports_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_vlan_parent_interface"></a>
<a id="Call_parameters_items_i0_vlan_parent_interface"></a>
##### vlan_parent_interface

- Schema name: `Vlan Parent Interface`
- Type: string

Parent interface for VLAN configuration.

<a id="headingCall_parameters_items_i0_vlan_tag"></a>
<a id="Call_parameters_items_i0_vlan_tag"></a>
##### vlan_tag

- Schema name: `Vlan Tag`
- Type: integer

VLAN tag number (1-4094).

<a id="headingCall_parameters_items_i0_vlan_pcp"></a>
<a id="Call_parameters_items_i0_vlan_pcp"></a>
##### vlan_pcp

- Schema name: `Vlan Pcp`

Priority Code Point for VLAN traffic prioritization (0-7). Values 0-7 map to different QoS priority levels, with 0 being lowest and 7 highest priority.
<a id="Call_parameters_items_i0_vlan_pcp_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_vlan_pcp_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_vlan_pcp_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `7`

<a id="tab-pane_Call_parameters_items_i0_vlan_pcp_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_vlan_pcp_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_mtu"></a>
<a id="Call_parameters_items_i0_mtu"></a>
##### mtu

- Schema name: `Mtu`
- Default: null

Maximum transmission unit size for the interface (68-9216 bytes).
<a id="Call_parameters_items_i0_mtu_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_mtu_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_mtu_anyOf_i0)

- Type: integer
- Value must be greater or equal to `68` and lesser or equal to `9216`

<a id="tab-pane_Call_parameters_items_i0_mtu_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_mtu_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `InterfaceEntry`
- Type: object

The created interface configuration.
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the network interface.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Name of the network interface.

<a id="headingReturn_value_fake"></a>
<a id="Return_value_fake"></a>
#### fake (required)

- Schema name: `Fake`
- Type: boolean

Whether this is a fake/simulated interface for testing purposes.

<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type (required)

- Schema name: `Type`
- Type: string

Type of interface (PHYSICAL, BRIDGE, LINK_AGGREGATION, VLAN, etc.).

<a id="headingReturn_value_state"></a>
<a id="Return_value_state"></a>
#### state (required)

- Schema name: `InterfaceEntryState`
- Type: object

Current runtime state information for the interface.
- No Additional Properties
<a id="headingReturn_value_state_name"></a>
<a id="Return_value_state_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Current name of the network interface.

<a id="headingReturn_value_state_orig_name"></a>
<a id="Return_value_state_orig_name"></a>
##### orig_name (required)

- Schema name: `Orig Name`
- Type: string

Original name of the network interface before any renaming.

<a id="headingReturn_value_state_description"></a>
<a id="Return_value_state_description"></a>
##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the network interface.

<a id="headingReturn_value_state_mtu"></a>
<a id="Return_value_state_mtu"></a>
##### mtu (required)

- Schema name: `Mtu`
- Type: integer

Maximum transmission unit size for the interface.

<a id="headingReturn_value_state_cloned"></a>
<a id="Return_value_state_cloned"></a>
##### cloned (required)

- Schema name: `Cloned`
- Type: boolean

Whether the interface is a cloned/virtual interface.

<a id="headingReturn_value_state_flags"></a>
<a id="Return_value_state_flags"></a>
##### flags (required)

- Schema name: `Flags`
- Type: array of string

List of interface flags indicating various states and capabilities. Common flags include UP, DOWN, RUNNING, MULTICAST, BROADCAST, LOOPBACK, and POINTOPOINT.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_state_flags_items"></a>
- Type: string

<a id="headingReturn_value_state_nd6_flags"></a>
<a id="Return_value_state_nd6_flags"></a>
##### nd6_flags (required)

- Schema name: `Nd6 Flags`
- Type: array

IPv6 neighbor discovery flags. These control IPv6 autoconfiguration behavior and include flags like AUTO*LINKLOCAL, ACCEPT*RTADV, and PERFORMNUD.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_state_nd6_flags_items"></a>
- Type: object

<a id="headingReturn_value_state_capabilities"></a>
<a id="Return_value_state_capabilities"></a>
##### capabilities (required)

- Schema name: `Capabilities`
- Type: array

List of hardware capabilities supported by the interface. Common capabilities include VLAN*MTU, JUMBO*MTU, VLAN*HWTAGGING, VLAN*HWCSUM, and TSO4.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_state_capabilities_items"></a>
- Type: object

<a id="headingReturn_value_state_link_state"></a>
<a id="Return_value_state_link_state"></a>
##### link_state (required)

- Schema name: `Link State`
- Type: string

Current link state of the interface (up, down, etc.).

<a id="headingReturn_value_state_media_type"></a>
<a id="Return_value_state_media_type"></a>
##### media_type (required)

- Schema name: `Media Type`
- Type: string

Type of media/connection for the interface. Examples include Ethernet, 802.11, or loopback.

<a id="headingReturn_value_state_media_subtype"></a>
<a id="Return_value_state_media_subtype"></a>
##### media_subtype (required)

- Schema name: `Media Subtype`
- Type: string

Subtype of media/connection for the interface. Examples include 1000baseT, 100baseTX, or autoselect.

<a id="headingReturn_value_state_active_media_type"></a>
<a id="Return_value_state_active_media_type"></a>
##### active_media_type (required)

- Schema name: `Active Media Type`
- Type: string

Currently active media type. This may differ from configured media_type during autonegotiation.

<a id="headingReturn_value_state_active_media_subtype"></a>
<a id="Return_value_state_active_media_subtype"></a>
##### active_media_subtype (required)

- Schema name: `Active Media Subtype`
- Type: string

Currently active media subtype. This reflects the actual negotiated connection speed and type.

<a id="headingReturn_value_state_supported_media"></a>
<a id="Return_value_state_supported_media"></a>
##### supported_media (required)

- Schema name: `Supported Media`
- Type: array

List of supported media types for the interface. Contains media descriptors like '1000baseT <full-duplex>' or 'autoselect'.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_state_supported_media_items"></a>
- Type: object

<a id="headingReturn_value_state_media_options"></a>
<a id="Return_value_state_media_options"></a>
##### media_options (required)

- Schema name: `Media Options`

Available media options for the interface. Options may include 'full-duplex', 'half-duplex', 'flowcontrol', or 'rxpause'.
<a id="Return_value_state_media_options_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_media_options_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_media_options_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_state_media_options_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_Return_value_state_media_options_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_media_options_anyOf_i1)

- Type: null

<a id="headingReturn_value_state_link_address"></a>
<a id="Return_value_state_link_address"></a>
##### link_address (required)

- Schema name: `Link Address`
- Type: string

MAC address of the interface.

<a id="headingReturn_value_state_permanent_link_address"></a>
<a id="Return_value_state_permanent_link_address"></a>
##### permanent_link_address (required)

- Schema name: `Permanent Link Address`

Permanent MAC address of the interface if different from current.
<a id="Return_value_state_permanent_link_address_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_permanent_link_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_permanent_link_address_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_state_permanent_link_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_permanent_link_address_anyOf_i1)

- Type: null

<a id="headingReturn_value_state_hardware_link_address"></a>
<a id="Return_value_state_hardware_link_address"></a>
##### hardware_link_address (required)

- Schema name: `Hardware Link Address`
- Type: string

Hardware MAC address of the interface.

<a id="headingReturn_value_state_rx_queues"></a>
<a id="Return_value_state_rx_queues"></a>
##### rx_queues

- Schema name: `Rx Queues`
- Type: integer

Number of receive queues configured for the interface.

<a id="headingReturn_value_state_tx_queues"></a>
<a id="Return_value_state_tx_queues"></a>
##### tx_queues

- Schema name: `Tx Queues`
- Type: integer

Number of transmit queues configured for the interface.

<a id="headingReturn_value_state_aliases"></a>
<a id="Return_value_state_aliases"></a>
##### aliases (required)

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases configured on the interface.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_state_aliases_items"></a>
###### InterfaceEntryStateAlias

- Schema name: `InterfaceEntryStateAlias`
- Type: object
- No Additional Properties
<a id="headingReturn_value_state_aliases_items_type"></a>
<a id="Return_value_state_aliases_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

<a id="headingReturn_value_state_aliases_items_address"></a>
<a id="Return_value_state_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`
- Type: string

The IP address value.

<a id="headingReturn_value_state_aliases_items_netmask"></a>
<a id="Return_value_state_aliases_items_netmask"></a>
###### netmask

- Schema name: `Netmask`

The network mask for the IP address, either as a string or CIDR notation integer.
<a id="Return_value_state_aliases_items_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_aliases_items_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_aliases_items_netmask_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_state_aliases_items_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_aliases_items_netmask_anyOf_i1)

- Type: integer

<a id="headingReturn_value_state_aliases_items_broadcast"></a>
<a id="Return_value_state_aliases_items_broadcast"></a>
###### broadcast

- Schema name: `Broadcast`
- Type: string

Broadcast address for the network interface.

<a id="headingReturn_value_state_vrrp_config"></a>
<a id="Return_value_state_vrrp_config"></a>
##### vrrp_config

- Schema name: `Vrrp Config`
- Default: []

VRRP (Virtual Router Redundancy Protocol) configuration for the interface.
<a id="Return_value_state_vrrp_config_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_vrrp_config_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_vrrp_config_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_state_vrrp_config_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_Return_value_state_vrrp_config_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_vrrp_config_anyOf_i1)

- Type: null

<a id="headingReturn_value_state_protocol"></a>
<a id="Return_value_state_protocol"></a>
##### protocol

- Schema name: `Protocol`

Link aggregation protocol used (LACP, FAILOVER, etc.).
<a id="Return_value_state_protocol_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_protocol_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_protocol_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_state_protocol_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_protocol_anyOf_i1)

- Type: null

<a id="headingReturn_value_state_ports"></a>
<a id="Return_value_state_ports"></a>
##### ports

- Schema name: `Ports`
- Type: array of object
- Default: []

List of ports that are members of this link aggregation group.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_state_ports_items"></a>
###### InterfaceEntryStatePort

- Schema name: `InterfaceEntryStatePort`
- Type: object
- No Additional Properties
<a id="headingReturn_value_state_ports_items_name"></a>
<a id="Return_value_state_ports_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

The name of the port interface.

<a id="headingReturn_value_state_ports_items_flags"></a>
<a id="Return_value_state_ports_items_flags"></a>
###### flags (required)

- Schema name: `Flags`
- Type: array of string

List of flags associated with the port.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_state_ports_items_flags_items"></a>
- Type: string

<a id="headingReturn_value_state_xmit_hash_policy"></a>
<a id="Return_value_state_xmit_hash_policy"></a>
##### xmit_hash_policy

- Schema name: `Xmit Hash Policy`
- Default: null

Transmit hash policy for load balancing in link aggregation. LAYER2 uses MAC addresses, LAYER2+3 adds IP addresses, and LAYER3+4 includes TCP/UDP ports for distribution.
<a id="Return_value_state_xmit_hash_policy_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_xmit_hash_policy_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_xmit_hash_policy_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_state_xmit_hash_policy_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_xmit_hash_policy_anyOf_i1)

- Type: null

<a id="headingReturn_value_state_lacpdu_rate"></a>
<a id="Return_value_state_lacpdu_rate"></a>
##### lacpdu_rate

- Schema name: `Lacpdu Rate`
- Default: null

LACP data unit transmission rate. SLOW sends LACPDUs every 30 seconds, FAST sends every 1 second for quicker link failure detection.
<a id="Return_value_state_lacpdu_rate_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_lacpdu_rate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_lacpdu_rate_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_state_lacpdu_rate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_lacpdu_rate_anyOf_i1)

- Type: null

<a id="headingReturn_value_state_parent"></a>
<a id="Return_value_state_parent"></a>
##### parent

- Schema name: `Parent`

Parent interface for VLAN configuration.
<a id="Return_value_state_parent_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_parent_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_parent_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_state_parent_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_parent_anyOf_i1)

- Type: null

<a id="headingReturn_value_state_tag"></a>
<a id="Return_value_state_tag"></a>
##### tag

- Schema name: `Tag`

VLAN tag number.
<a id="Return_value_state_tag_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_tag_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_tag_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_state_tag_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_tag_anyOf_i1)

- Type: null

<a id="headingReturn_value_state_pcp"></a>
<a id="Return_value_state_pcp"></a>
##### pcp

- Schema name: `Pcp`

Priority Code Point for VLAN traffic prioritization. Values 0-7 map to different QoS priority levels, with 0 being lowest and 7 highest priority.
<a id="Return_value_state_pcp_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_pcp_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_pcp_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_state_pcp_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_pcp_anyOf_i1)

- Type: null

<a id="headingReturn_value_state_fec_mode"></a>
<a id="Return_value_state_fec_mode"></a>
##### fec_mode

- Schema name: `Fec Mode`

Currently active Forward Error Correction mode from the hardware. Only present for physical interfaces. "AUTO": Selects the best FEC mode based on cable/port capabilities "RS": RS-FEC (Reed-Solomon), often used for 25GbE/100GbE+ NICs "BASER": BaseR-FEC (FireCode) "OFF": Disables FEC "LLRS": Low Latency Reed-Solomon FEC, used for 25GBASE-KR/CR `null`: FEC not supported or mode cannot be determined
<a id="Return_value_state_fec_mode_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_fec_mode_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_fec_mode_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "AUTO"
- "OFF"
- "RS"
- "BASER"
- "LLRS"

<a id="tab-pane_Return_value_state_fec_mode_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_fec_mode_anyOf_i1)

- Type: null

<a id="headingReturn_value_aliases"></a>
<a id="Return_value_aliases"></a>
#### aliases (required)

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases configured on the interface.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_aliases_items"></a>
##### InterfaceEntryAlias

- Schema name: `InterfaceEntryAlias`
- Type: object
- No Additional Properties
<a id="headingReturn_value_aliases_items_type"></a>
<a id="Return_value_aliases_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

<a id="headingReturn_value_aliases_items_address"></a>
<a id="Return_value_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`
- Type: string

The IP address value.

<a id="headingReturn_value_aliases_items_netmask"></a>
<a id="Return_value_aliases_items_netmask"></a>
###### netmask (required)

- Schema name: `Netmask`

The network mask for the IP address, either as a string or CIDR notation integer.
<a id="Return_value_aliases_items_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_aliases_items_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_aliases_items_netmask_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_aliases_items_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_aliases_items_netmask_anyOf_i1)

- Type: integer

<a id="headingReturn_value_ipv4_dhcp"></a>
<a id="Return_value_ipv4_dhcp"></a>
#### ipv4_dhcp (required)

- Schema name: `Ipv4 Dhcp`
- Type: boolean

Whether IPv4 DHCP is enabled for automatic IP address assignment.

<a id="headingReturn_value_ipv6_auto"></a>
<a id="Return_value_ipv6_auto"></a>
#### ipv6_auto (required)

- Schema name: `Ipv6 Auto`
- Type: boolean

Whether IPv6 autoconfiguration is enabled.

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the interface.

<a id="headingReturn_value_mtu"></a>
<a id="Return_value_mtu"></a>
#### mtu (required)

- Schema name: `Mtu`

Maximum transmission unit size for the interface.
<a id="Return_value_mtu_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_mtu_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_mtu_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_mtu_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_mtu_anyOf_i1)

- Type: null

<a id="headingReturn_value_fec_mode"></a>
<a id="Return_value_fec_mode"></a>
#### fec_mode

- Schema name: `Fec Mode`
- Type: enum (of string)

Forward Error Correction (FEC) mode. Only valid for physical interfaces. "AUTO": Selects the best FEC mode based on cable/port capabilities "RS": RS-FEC (Reed-Solomon), often used for 25GbE/100GbE+ NICs "BASER": BaseR-FEC (FireCode) "OFF": Disables FEC "LLRS": Low Latency Reed-Solomon FEC, used for 25GBASE-KR/CR
##### Must be one of:

- "AUTO"
- "OFF"
- "RS"
- "BASER"
- "LLRS"

<a id="headingReturn_value_vlan_parent_interface"></a>
<a id="Return_value_vlan_parent_interface"></a>
#### vlan_parent_interface

- Schema name: `Vlan Parent Interface`

Parent interface for VLAN configuration.
<a id="Return_value_vlan_parent_interface_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_vlan_parent_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_vlan_parent_interface_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_vlan_parent_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_vlan_parent_interface_anyOf_i1)

- Type: null

<a id="headingReturn_value_vlan_tag"></a>
<a id="Return_value_vlan_tag"></a>
#### vlan_tag

- Schema name: `Vlan Tag`

VLAN tag number for VLAN interfaces.
<a id="Return_value_vlan_tag_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_vlan_tag_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_vlan_tag_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_vlan_tag_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_vlan_tag_anyOf_i1)

- Type: null

<a id="headingReturn_value_vlan_pcp"></a>
<a id="Return_value_vlan_pcp"></a>
#### vlan_pcp

- Schema name: `Vlan Pcp`

Priority Code Point for VLAN traffic prioritization.
<a id="Return_value_vlan_pcp_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_vlan_pcp_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_vlan_pcp_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_vlan_pcp_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_vlan_pcp_anyOf_i1)

- Type: null

<a id="headingReturn_value_lag_protocol"></a>
<a id="Return_value_lag_protocol"></a>
#### lag_protocol

- Schema name: `Lag Protocol`
- Type: string

Link aggregation protocol (LACP, FAILOVER, LOADBALANCE, etc.).

<a id="headingReturn_value_lag_ports"></a>
<a id="Return_value_lag_ports"></a>
#### lag_ports

- Schema name: `Lag Ports`
- Type: array of string
- Default: []

List of interface names that are members of this link aggregation group.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_lag_ports_items"></a>
- Type: string

<a id="headingReturn_value_bridge_members"></a>
<a id="Return_value_bridge_members"></a>
#### bridge_members

- Schema name: `Bridge Members`
- Type: array of string
- Default: []

List of interface names that are members of this bridge.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_bridge_members_items"></a>
- Type: string

<a id="headingReturn_value_enable_learning"></a>
<a id="Return_value_enable_learning"></a>
#### enable_learning

- Schema name: `Enable Learning`
- Type: boolean

Whether MAC address learning is enabled for bridge interfaces.

<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
