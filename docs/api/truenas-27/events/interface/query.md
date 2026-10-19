---
title: interface.query
kind: event
source_rst: _sources/api_events_interface.query.rst.txt
source_html: api_events_interface.query.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# interface.query

## Summary

Sent on interface changes.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `InterfaceAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `InterfaceEntry`
- Type: object
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the network interface.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the network interface.

<a id="headingADDED_fields_fake"></a>
<a id="ADDED_fields_fake"></a>
##### fake (required)

- Schema name: `Fake`
- Type: boolean

Whether this is a fake/simulated interface for testing purposes.

<a id="headingADDED_fields_type"></a>
<a id="ADDED_fields_type"></a>
##### type (required)

- Schema name: `Type`
- Type: string

Type of interface (PHYSICAL, BRIDGE, LINK_AGGREGATION, VLAN, etc.).

<a id="headingADDED_fields_state"></a>
<a id="ADDED_fields_state"></a>
##### state (required)

- Schema name: `InterfaceEntryState`
- Type: object

Current runtime state information for the interface.
- No Additional Properties
<a id="headingADDED_fields_state_name"></a>
<a id="ADDED_fields_state_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Current name of the network interface.

<a id="headingADDED_fields_state_orig_name"></a>
<a id="ADDED_fields_state_orig_name"></a>
###### orig_name (required)

- Schema name: `Orig Name`
- Type: string

Original name of the network interface before any renaming.

<a id="headingADDED_fields_state_description"></a>
<a id="ADDED_fields_state_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the network interface.

<a id="headingADDED_fields_state_mtu"></a>
<a id="ADDED_fields_state_mtu"></a>
###### mtu (required)

- Schema name: `Mtu`
- Type: integer

Maximum transmission unit size for the interface.

<a id="headingADDED_fields_state_cloned"></a>
<a id="ADDED_fields_state_cloned"></a>
###### cloned (required)

- Schema name: `Cloned`
- Type: boolean

Whether the interface is a cloned/virtual interface.

<a id="headingADDED_fields_state_flags"></a>
<a id="ADDED_fields_state_flags"></a>
###### flags (required)

- Schema name: `Flags`
- Type: array of string

List of interface flags indicating various states and capabilities. Common flags include UP, DOWN, RUNNING, MULTICAST, BROADCAST, LOOPBACK, and POINTOPOINT.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_state_flags_items"></a>
- Type: string

<a id="headingADDED_fields_state_nd6_flags"></a>
<a id="ADDED_fields_state_nd6_flags"></a>
###### nd6_flags (required)

- Schema name: `Nd6 Flags`
- Type: array

IPv6 neighbor discovery flags. These control IPv6 autoconfiguration behavior and include flags like AUTO*LINKLOCAL, ACCEPT*RTADV, and PERFORMNUD.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_state_nd6_flags_items"></a>
- Type: object

<a id="headingADDED_fields_state_capabilities"></a>
<a id="ADDED_fields_state_capabilities"></a>
###### capabilities (required)

- Schema name: `Capabilities`
- Type: array

List of hardware capabilities supported by the interface. Common capabilities include VLAN*MTU, JUMBO*MTU, VLAN*HWTAGGING, VLAN*HWCSUM, and TSO4.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_state_capabilities_items"></a>
- Type: object

<a id="headingADDED_fields_state_link_state"></a>
<a id="ADDED_fields_state_link_state"></a>
###### link_state (required)

- Schema name: `Link State`
- Type: string

Current link state of the interface (up, down, etc.).

<a id="headingADDED_fields_state_media_type"></a>
<a id="ADDED_fields_state_media_type"></a>
###### media_type (required)

- Schema name: `Media Type`
- Type: string

Type of media/connection for the interface. Examples include Ethernet, 802.11, or loopback.

<a id="headingADDED_fields_state_media_subtype"></a>
<a id="ADDED_fields_state_media_subtype"></a>
###### media_subtype (required)

- Schema name: `Media Subtype`
- Type: string

Subtype of media/connection for the interface. Examples include 1000baseT, 100baseTX, or autoselect.

<a id="headingADDED_fields_state_active_media_type"></a>
<a id="ADDED_fields_state_active_media_type"></a>
###### active_media_type (required)

- Schema name: `Active Media Type`
- Type: string

Currently active media type. This may differ from configured media_type during autonegotiation.

<a id="headingADDED_fields_state_active_media_subtype"></a>
<a id="ADDED_fields_state_active_media_subtype"></a>
###### active_media_subtype (required)

- Schema name: `Active Media Subtype`
- Type: string

Currently active media subtype. This reflects the actual negotiated connection speed and type.

<a id="headingADDED_fields_state_supported_media"></a>
<a id="ADDED_fields_state_supported_media"></a>
###### supported_media (required)

- Schema name: `Supported Media`
- Type: array

List of supported media types for the interface. Contains media descriptors like '1000baseT <full-duplex>' or 'autoselect'.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_state_supported_media_items"></a>
- Type: object

<a id="headingADDED_fields_state_media_options"></a>
<a id="ADDED_fields_state_media_options"></a>
###### media_options (required)

- Schema name: `Media Options`

Available media options for the interface. Options may include 'full-duplex', 'half-duplex', 'flowcontrol', or 'rxpause'.
<a id="ADDED_fields_state_media_options_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_media_options_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_media_options_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_state_media_options_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_ADDED_fields_state_media_options_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_media_options_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state_link_address"></a>
<a id="ADDED_fields_state_link_address"></a>
###### link_address (required)

- Schema name: `Link Address`
- Type: string

MAC address of the interface.

<a id="headingADDED_fields_state_permanent_link_address"></a>
<a id="ADDED_fields_state_permanent_link_address"></a>
###### permanent_link_address (required)

- Schema name: `Permanent Link Address`

Permanent MAC address of the interface if different from current.
<a id="ADDED_fields_state_permanent_link_address_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_permanent_link_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_permanent_link_address_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_state_permanent_link_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_permanent_link_address_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state_hardware_link_address"></a>
<a id="ADDED_fields_state_hardware_link_address"></a>
###### hardware_link_address (required)

- Schema name: `Hardware Link Address`
- Type: string

Hardware MAC address of the interface.

<a id="headingADDED_fields_state_rx_queues"></a>
<a id="ADDED_fields_state_rx_queues"></a>
###### rx_queues

- Schema name: `Rx Queues`
- Type: integer

Number of receive queues configured for the interface.

<a id="headingADDED_fields_state_tx_queues"></a>
<a id="ADDED_fields_state_tx_queues"></a>
###### tx_queues

- Schema name: `Tx Queues`
- Type: integer

Number of transmit queues configured for the interface.

<a id="headingADDED_fields_state_aliases"></a>
<a id="ADDED_fields_state_aliases"></a>
###### aliases (required)

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases configured on the interface.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_state_aliases_items"></a>
###### InterfaceEntryStateAlias

- Schema name: `InterfaceEntryStateAlias`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_state_aliases_items_type"></a>
<a id="ADDED_fields_state_aliases_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

<a id="headingADDED_fields_state_aliases_items_address"></a>
<a id="ADDED_fields_state_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`
- Type: string

The IP address value.

<a id="headingADDED_fields_state_aliases_items_netmask"></a>
<a id="ADDED_fields_state_aliases_items_netmask"></a>
###### netmask

- Schema name: `Netmask`

The network mask for the IP address, either as a string or CIDR notation integer.
<a id="ADDED_fields_state_aliases_items_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_aliases_items_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_aliases_items_netmask_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_state_aliases_items_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_aliases_items_netmask_anyOf_i1)

- Type: integer

<a id="headingADDED_fields_state_aliases_items_broadcast"></a>
<a id="ADDED_fields_state_aliases_items_broadcast"></a>
###### broadcast

- Schema name: `Broadcast`
- Type: string

Broadcast address for the network interface.

<a id="headingADDED_fields_state_vrrp_config"></a>
<a id="ADDED_fields_state_vrrp_config"></a>
###### vrrp_config

- Schema name: `Vrrp Config`
- Default: []

VRRP (Virtual Router Redundancy Protocol) configuration for the interface.
<a id="ADDED_fields_state_vrrp_config_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_vrrp_config_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_vrrp_config_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_state_vrrp_config_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_ADDED_fields_state_vrrp_config_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_vrrp_config_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state_protocol"></a>
<a id="ADDED_fields_state_protocol"></a>
###### protocol

- Schema name: `Protocol`

Link aggregation protocol used (LACP, FAILOVER, etc.).
<a id="ADDED_fields_state_protocol_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_protocol_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_protocol_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_state_protocol_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_protocol_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state_ports"></a>
<a id="ADDED_fields_state_ports"></a>
###### ports

- Schema name: `Ports`
- Type: array of object
- Default: []

List of ports that are members of this link aggregation group.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_state_ports_items"></a>
###### InterfaceEntryStatePort

- Schema name: `InterfaceEntryStatePort`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_state_ports_items_name"></a>
<a id="ADDED_fields_state_ports_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

The name of the port interface.

<a id="headingADDED_fields_state_ports_items_flags"></a>
<a id="ADDED_fields_state_ports_items_flags"></a>
###### flags (required)

- Schema name: `Flags`
- Type: array of string

List of flags associated with the port.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_state_ports_items_flags_items"></a>
- Type: string

<a id="headingADDED_fields_state_xmit_hash_policy"></a>
<a id="ADDED_fields_state_xmit_hash_policy"></a>
###### xmit_hash_policy

- Schema name: `Xmit Hash Policy`
- Default: null

Transmit hash policy for load balancing in link aggregation. LAYER2 uses MAC addresses, LAYER2+3 adds IP addresses, and LAYER3+4 includes TCP/UDP ports for distribution.
<a id="ADDED_fields_state_xmit_hash_policy_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_xmit_hash_policy_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_xmit_hash_policy_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_state_xmit_hash_policy_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_xmit_hash_policy_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state_lacpdu_rate"></a>
<a id="ADDED_fields_state_lacpdu_rate"></a>
###### lacpdu_rate

- Schema name: `Lacpdu Rate`
- Default: null

LACP data unit transmission rate. SLOW sends LACPDUs every 30 seconds, FAST sends every 1 second for quicker link failure detection.
<a id="ADDED_fields_state_lacpdu_rate_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_lacpdu_rate_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_lacpdu_rate_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_state_lacpdu_rate_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_lacpdu_rate_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state_parent"></a>
<a id="ADDED_fields_state_parent"></a>
###### parent

- Schema name: `Parent`

Parent interface for VLAN configuration.
<a id="ADDED_fields_state_parent_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_parent_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_parent_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_state_parent_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_parent_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state_tag"></a>
<a id="ADDED_fields_state_tag"></a>
###### tag

- Schema name: `Tag`

VLAN tag number.
<a id="ADDED_fields_state_tag_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_tag_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_tag_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_state_tag_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_tag_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state_pcp"></a>
<a id="ADDED_fields_state_pcp"></a>
###### pcp

- Schema name: `Pcp`

Priority Code Point for VLAN traffic prioritization. Values 0-7 map to different QoS priority levels, with 0 being lowest and 7 highest priority.
<a id="ADDED_fields_state_pcp_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_pcp_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_pcp_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_state_pcp_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_pcp_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state_fec_mode"></a>
<a id="ADDED_fields_state_fec_mode"></a>
###### fec_mode

- Schema name: `Fec Mode`

Currently active Forward Error Correction mode from the hardware. Only present for physical interfaces. "AUTO": Selects the best FEC mode based on cable/port capabilities "RS": RS-FEC (Reed-Solomon), often used for 25GbE/100GbE+ NICs "BASER": BaseR-FEC (FireCode) "OFF": Disables FEC "LLRS": Low Latency Reed-Solomon FEC, used for 25GBASE-KR/CR `null`: FEC not supported or mode cannot be determined
<a id="ADDED_fields_state_fec_mode_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_state_fec_mode_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_state_fec_mode_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "AUTO"
- "OFF"
- "RS"
- "BASER"
- "LLRS"

<a id="tab-pane_ADDED_fields_state_fec_mode_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_state_fec_mode_anyOf_i1)

- Type: null

<a id="headingADDED_fields_aliases"></a>
<a id="ADDED_fields_aliases"></a>
##### aliases (required)

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases configured on the interface.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_aliases_items"></a>
###### InterfaceEntryAlias

- Schema name: `InterfaceEntryAlias`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_aliases_items_type"></a>
<a id="ADDED_fields_aliases_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

<a id="headingADDED_fields_aliases_items_address"></a>
<a id="ADDED_fields_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`
- Type: string

The IP address value.

<a id="headingADDED_fields_aliases_items_netmask"></a>
<a id="ADDED_fields_aliases_items_netmask"></a>
###### netmask (required)

- Schema name: `Netmask`

The network mask for the IP address, either as a string or CIDR notation integer.
<a id="ADDED_fields_aliases_items_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_aliases_items_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_aliases_items_netmask_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_aliases_items_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_aliases_items_netmask_anyOf_i1)

- Type: integer

<a id="headingADDED_fields_ipv4_dhcp"></a>
<a id="ADDED_fields_ipv4_dhcp"></a>
##### ipv4_dhcp (required)

- Schema name: `Ipv4 Dhcp`
- Type: boolean

Whether IPv4 DHCP is enabled for automatic IP address assignment.

<a id="headingADDED_fields_ipv6_auto"></a>
<a id="ADDED_fields_ipv6_auto"></a>
##### ipv6_auto (required)

- Schema name: `Ipv6 Auto`
- Type: boolean

Whether IPv6 autoconfiguration is enabled.

<a id="headingADDED_fields_description"></a>
<a id="ADDED_fields_description"></a>
##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the interface.

<a id="headingADDED_fields_mtu"></a>
<a id="ADDED_fields_mtu"></a>
##### mtu (required)

- Schema name: `Mtu`

Maximum transmission unit size for the interface.
<a id="ADDED_fields_mtu_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_mtu_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_mtu_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_mtu_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_mtu_anyOf_i1)

- Type: null

<a id="headingADDED_fields_fec_mode"></a>
<a id="ADDED_fields_fec_mode"></a>
##### fec_mode

- Schema name: `Fec Mode`
- Type: enum (of string)

Forward Error Correction (FEC) mode. Only valid for physical interfaces. "AUTO": Selects the best FEC mode based on cable/port capabilities "RS": RS-FEC (Reed-Solomon), often used for 25GbE/100GbE+ NICs "BASER": BaseR-FEC (FireCode) "OFF": Disables FEC "LLRS": Low Latency Reed-Solomon FEC, used for 25GBASE-KR/CR
###### Must be one of:

- "AUTO"
- "OFF"
- "RS"
- "BASER"
- "LLRS"

<a id="headingADDED_fields_vlan_parent_interface"></a>
<a id="ADDED_fields_vlan_parent_interface"></a>
##### vlan_parent_interface

- Schema name: `Vlan Parent Interface`

Parent interface for VLAN configuration.
<a id="ADDED_fields_vlan_parent_interface_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_vlan_parent_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_vlan_parent_interface_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_vlan_parent_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_vlan_parent_interface_anyOf_i1)

- Type: null

<a id="headingADDED_fields_vlan_tag"></a>
<a id="ADDED_fields_vlan_tag"></a>
##### vlan_tag

- Schema name: `Vlan Tag`

VLAN tag number for VLAN interfaces.
<a id="ADDED_fields_vlan_tag_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_vlan_tag_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_vlan_tag_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_vlan_tag_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_vlan_tag_anyOf_i1)

- Type: null

<a id="headingADDED_fields_vlan_pcp"></a>
<a id="ADDED_fields_vlan_pcp"></a>
##### vlan_pcp

- Schema name: `Vlan Pcp`

Priority Code Point for VLAN traffic prioritization.
<a id="ADDED_fields_vlan_pcp_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_vlan_pcp_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_vlan_pcp_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_vlan_pcp_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_vlan_pcp_anyOf_i1)

- Type: null

<a id="headingADDED_fields_lag_protocol"></a>
<a id="ADDED_fields_lag_protocol"></a>
##### lag_protocol

- Schema name: `Lag Protocol`
- Type: string

Link aggregation protocol (LACP, FAILOVER, LOADBALANCE, etc.).

<a id="headingADDED_fields_lag_ports"></a>
<a id="ADDED_fields_lag_ports"></a>
##### lag_ports

- Schema name: `Lag Ports`
- Type: array of string
- Default: []

List of interface names that are members of this link aggregation group.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_lag_ports_items"></a>
- Type: string

<a id="headingADDED_fields_bridge_members"></a>
<a id="ADDED_fields_bridge_members"></a>
##### bridge_members

- Schema name: `Bridge Members`
- Type: array of string
- Default: []

List of interface names that are members of this bridge.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_bridge_members_items"></a>
- Type: string

<a id="headingADDED_fields_enable_learning"></a>
<a id="ADDED_fields_enable_learning"></a>
##### enable_learning

- Schema name: `Enable Learning`
- Type: boolean

Whether MAC address learning is enabled for bridge interfaces.

<a id="headingADDED_fields_additionalProperties"></a>
<a id="ADDED_fields_additionalProperties"></a>
##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `InterfaceChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `InterfaceEntry`
- Type: object
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the network interface.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the network interface.

<a id="headingCHANGED_fields_fake"></a>
<a id="CHANGED_fields_fake"></a>
##### fake (required)

- Schema name: `Fake`
- Type: boolean

Whether this is a fake/simulated interface for testing purposes.

<a id="headingCHANGED_fields_type"></a>
<a id="CHANGED_fields_type"></a>
##### type (required)

- Schema name: `Type`
- Type: string

Type of interface (PHYSICAL, BRIDGE, LINK_AGGREGATION, VLAN, etc.).

<a id="headingCHANGED_fields_state"></a>
<a id="CHANGED_fields_state"></a>
##### state (required)

- Schema name: `InterfaceEntryState`
- Type: object

Current runtime state information for the interface.
- No Additional Properties
<a id="headingCHANGED_fields_state_name"></a>
<a id="CHANGED_fields_state_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Current name of the network interface.

<a id="headingCHANGED_fields_state_orig_name"></a>
<a id="CHANGED_fields_state_orig_name"></a>
###### orig_name (required)

- Schema name: `Orig Name`
- Type: string

Original name of the network interface before any renaming.

<a id="headingCHANGED_fields_state_description"></a>
<a id="CHANGED_fields_state_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the network interface.

<a id="headingCHANGED_fields_state_mtu"></a>
<a id="CHANGED_fields_state_mtu"></a>
###### mtu (required)

- Schema name: `Mtu`
- Type: integer

Maximum transmission unit size for the interface.

<a id="headingCHANGED_fields_state_cloned"></a>
<a id="CHANGED_fields_state_cloned"></a>
###### cloned (required)

- Schema name: `Cloned`
- Type: boolean

Whether the interface is a cloned/virtual interface.

<a id="headingCHANGED_fields_state_flags"></a>
<a id="CHANGED_fields_state_flags"></a>
###### flags (required)

- Schema name: `Flags`
- Type: array of string

List of interface flags indicating various states and capabilities. Common flags include UP, DOWN, RUNNING, MULTICAST, BROADCAST, LOOPBACK, and POINTOPOINT.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_state_flags_items"></a>
- Type: string

<a id="headingCHANGED_fields_state_nd6_flags"></a>
<a id="CHANGED_fields_state_nd6_flags"></a>
###### nd6_flags (required)

- Schema name: `Nd6 Flags`
- Type: array

IPv6 neighbor discovery flags. These control IPv6 autoconfiguration behavior and include flags like AUTO*LINKLOCAL, ACCEPT*RTADV, and PERFORMNUD.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_state_nd6_flags_items"></a>
- Type: object

<a id="headingCHANGED_fields_state_capabilities"></a>
<a id="CHANGED_fields_state_capabilities"></a>
###### capabilities (required)

- Schema name: `Capabilities`
- Type: array

List of hardware capabilities supported by the interface. Common capabilities include VLAN*MTU, JUMBO*MTU, VLAN*HWTAGGING, VLAN*HWCSUM, and TSO4.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_state_capabilities_items"></a>
- Type: object

<a id="headingCHANGED_fields_state_link_state"></a>
<a id="CHANGED_fields_state_link_state"></a>
###### link_state (required)

- Schema name: `Link State`
- Type: string

Current link state of the interface (up, down, etc.).

<a id="headingCHANGED_fields_state_media_type"></a>
<a id="CHANGED_fields_state_media_type"></a>
###### media_type (required)

- Schema name: `Media Type`
- Type: string

Type of media/connection for the interface. Examples include Ethernet, 802.11, or loopback.

<a id="headingCHANGED_fields_state_media_subtype"></a>
<a id="CHANGED_fields_state_media_subtype"></a>
###### media_subtype (required)

- Schema name: `Media Subtype`
- Type: string

Subtype of media/connection for the interface. Examples include 1000baseT, 100baseTX, or autoselect.

<a id="headingCHANGED_fields_state_active_media_type"></a>
<a id="CHANGED_fields_state_active_media_type"></a>
###### active_media_type (required)

- Schema name: `Active Media Type`
- Type: string

Currently active media type. This may differ from configured media_type during autonegotiation.

<a id="headingCHANGED_fields_state_active_media_subtype"></a>
<a id="CHANGED_fields_state_active_media_subtype"></a>
###### active_media_subtype (required)

- Schema name: `Active Media Subtype`
- Type: string

Currently active media subtype. This reflects the actual negotiated connection speed and type.

<a id="headingCHANGED_fields_state_supported_media"></a>
<a id="CHANGED_fields_state_supported_media"></a>
###### supported_media (required)

- Schema name: `Supported Media`
- Type: array

List of supported media types for the interface. Contains media descriptors like '1000baseT <full-duplex>' or 'autoselect'.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_state_supported_media_items"></a>
- Type: object

<a id="headingCHANGED_fields_state_media_options"></a>
<a id="CHANGED_fields_state_media_options"></a>
###### media_options (required)

- Schema name: `Media Options`

Available media options for the interface. Options may include 'full-duplex', 'half-duplex', 'flowcontrol', or 'rxpause'.
<a id="CHANGED_fields_state_media_options_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_media_options_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_media_options_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_state_media_options_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_CHANGED_fields_state_media_options_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_media_options_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state_link_address"></a>
<a id="CHANGED_fields_state_link_address"></a>
###### link_address (required)

- Schema name: `Link Address`
- Type: string

MAC address of the interface.

<a id="headingCHANGED_fields_state_permanent_link_address"></a>
<a id="CHANGED_fields_state_permanent_link_address"></a>
###### permanent_link_address (required)

- Schema name: `Permanent Link Address`

Permanent MAC address of the interface if different from current.
<a id="CHANGED_fields_state_permanent_link_address_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_permanent_link_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_permanent_link_address_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_state_permanent_link_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_permanent_link_address_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state_hardware_link_address"></a>
<a id="CHANGED_fields_state_hardware_link_address"></a>
###### hardware_link_address (required)

- Schema name: `Hardware Link Address`
- Type: string

Hardware MAC address of the interface.

<a id="headingCHANGED_fields_state_rx_queues"></a>
<a id="CHANGED_fields_state_rx_queues"></a>
###### rx_queues

- Schema name: `Rx Queues`
- Type: integer

Number of receive queues configured for the interface.

<a id="headingCHANGED_fields_state_tx_queues"></a>
<a id="CHANGED_fields_state_tx_queues"></a>
###### tx_queues

- Schema name: `Tx Queues`
- Type: integer

Number of transmit queues configured for the interface.

<a id="headingCHANGED_fields_state_aliases"></a>
<a id="CHANGED_fields_state_aliases"></a>
###### aliases (required)

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases configured on the interface.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_state_aliases_items"></a>
###### InterfaceEntryStateAlias

- Schema name: `InterfaceEntryStateAlias`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_state_aliases_items_type"></a>
<a id="CHANGED_fields_state_aliases_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

<a id="headingCHANGED_fields_state_aliases_items_address"></a>
<a id="CHANGED_fields_state_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`
- Type: string

The IP address value.

<a id="headingCHANGED_fields_state_aliases_items_netmask"></a>
<a id="CHANGED_fields_state_aliases_items_netmask"></a>
###### netmask

- Schema name: `Netmask`

The network mask for the IP address, either as a string or CIDR notation integer.
<a id="CHANGED_fields_state_aliases_items_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_aliases_items_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_aliases_items_netmask_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_state_aliases_items_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_aliases_items_netmask_anyOf_i1)

- Type: integer

<a id="headingCHANGED_fields_state_aliases_items_broadcast"></a>
<a id="CHANGED_fields_state_aliases_items_broadcast"></a>
###### broadcast

- Schema name: `Broadcast`
- Type: string

Broadcast address for the network interface.

<a id="headingCHANGED_fields_state_vrrp_config"></a>
<a id="CHANGED_fields_state_vrrp_config"></a>
###### vrrp_config

- Schema name: `Vrrp Config`
- Default: []

VRRP (Virtual Router Redundancy Protocol) configuration for the interface.
<a id="CHANGED_fields_state_vrrp_config_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_vrrp_config_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_vrrp_config_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_state_vrrp_config_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_CHANGED_fields_state_vrrp_config_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_vrrp_config_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state_protocol"></a>
<a id="CHANGED_fields_state_protocol"></a>
###### protocol

- Schema name: `Protocol`

Link aggregation protocol used (LACP, FAILOVER, etc.).
<a id="CHANGED_fields_state_protocol_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_protocol_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_protocol_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_state_protocol_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_protocol_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state_ports"></a>
<a id="CHANGED_fields_state_ports"></a>
###### ports

- Schema name: `Ports`
- Type: array of object
- Default: []

List of ports that are members of this link aggregation group.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_state_ports_items"></a>
###### InterfaceEntryStatePort

- Schema name: `InterfaceEntryStatePort`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_state_ports_items_name"></a>
<a id="CHANGED_fields_state_ports_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

The name of the port interface.

<a id="headingCHANGED_fields_state_ports_items_flags"></a>
<a id="CHANGED_fields_state_ports_items_flags"></a>
###### flags (required)

- Schema name: `Flags`
- Type: array of string

List of flags associated with the port.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_state_ports_items_flags_items"></a>
- Type: string

<a id="headingCHANGED_fields_state_xmit_hash_policy"></a>
<a id="CHANGED_fields_state_xmit_hash_policy"></a>
###### xmit_hash_policy

- Schema name: `Xmit Hash Policy`
- Default: null

Transmit hash policy for load balancing in link aggregation. LAYER2 uses MAC addresses, LAYER2+3 adds IP addresses, and LAYER3+4 includes TCP/UDP ports for distribution.
<a id="CHANGED_fields_state_xmit_hash_policy_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_xmit_hash_policy_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_xmit_hash_policy_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_state_xmit_hash_policy_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_xmit_hash_policy_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state_lacpdu_rate"></a>
<a id="CHANGED_fields_state_lacpdu_rate"></a>
###### lacpdu_rate

- Schema name: `Lacpdu Rate`
- Default: null

LACP data unit transmission rate. SLOW sends LACPDUs every 30 seconds, FAST sends every 1 second for quicker link failure detection.
<a id="CHANGED_fields_state_lacpdu_rate_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_lacpdu_rate_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_lacpdu_rate_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_state_lacpdu_rate_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_lacpdu_rate_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state_parent"></a>
<a id="CHANGED_fields_state_parent"></a>
###### parent

- Schema name: `Parent`

Parent interface for VLAN configuration.
<a id="CHANGED_fields_state_parent_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_parent_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_parent_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_state_parent_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_parent_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state_tag"></a>
<a id="CHANGED_fields_state_tag"></a>
###### tag

- Schema name: `Tag`

VLAN tag number.
<a id="CHANGED_fields_state_tag_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_tag_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_tag_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_state_tag_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_tag_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state_pcp"></a>
<a id="CHANGED_fields_state_pcp"></a>
###### pcp

- Schema name: `Pcp`

Priority Code Point for VLAN traffic prioritization. Values 0-7 map to different QoS priority levels, with 0 being lowest and 7 highest priority.
<a id="CHANGED_fields_state_pcp_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_pcp_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_pcp_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_state_pcp_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_pcp_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state_fec_mode"></a>
<a id="CHANGED_fields_state_fec_mode"></a>
###### fec_mode

- Schema name: `Fec Mode`

Currently active Forward Error Correction mode from the hardware. Only present for physical interfaces. "AUTO": Selects the best FEC mode based on cable/port capabilities "RS": RS-FEC (Reed-Solomon), often used for 25GbE/100GbE+ NICs "BASER": BaseR-FEC (FireCode) "OFF": Disables FEC "LLRS": Low Latency Reed-Solomon FEC, used for 25GBASE-KR/CR `null`: FEC not supported or mode cannot be determined
<a id="CHANGED_fields_state_fec_mode_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_state_fec_mode_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_state_fec_mode_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "AUTO"
- "OFF"
- "RS"
- "BASER"
- "LLRS"

<a id="tab-pane_CHANGED_fields_state_fec_mode_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_state_fec_mode_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_aliases"></a>
<a id="CHANGED_fields_aliases"></a>
##### aliases (required)

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases configured on the interface.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_aliases_items"></a>
###### InterfaceEntryAlias

- Schema name: `InterfaceEntryAlias`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_aliases_items_type"></a>
<a id="CHANGED_fields_aliases_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

<a id="headingCHANGED_fields_aliases_items_address"></a>
<a id="CHANGED_fields_aliases_items_address"></a>
###### address (required)

- Schema name: `Address`
- Type: string

The IP address value.

<a id="headingCHANGED_fields_aliases_items_netmask"></a>
<a id="CHANGED_fields_aliases_items_netmask"></a>
###### netmask (required)

- Schema name: `Netmask`

The network mask for the IP address, either as a string or CIDR notation integer.
<a id="CHANGED_fields_aliases_items_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_aliases_items_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_aliases_items_netmask_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_aliases_items_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_aliases_items_netmask_anyOf_i1)

- Type: integer

<a id="headingCHANGED_fields_ipv4_dhcp"></a>
<a id="CHANGED_fields_ipv4_dhcp"></a>
##### ipv4_dhcp (required)

- Schema name: `Ipv4 Dhcp`
- Type: boolean

Whether IPv4 DHCP is enabled for automatic IP address assignment.

<a id="headingCHANGED_fields_ipv6_auto"></a>
<a id="CHANGED_fields_ipv6_auto"></a>
##### ipv6_auto (required)

- Schema name: `Ipv6 Auto`
- Type: boolean

Whether IPv6 autoconfiguration is enabled.

<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the interface.

<a id="headingCHANGED_fields_mtu"></a>
<a id="CHANGED_fields_mtu"></a>
##### mtu (required)

- Schema name: `Mtu`

Maximum transmission unit size for the interface.
<a id="CHANGED_fields_mtu_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_mtu_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_mtu_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_mtu_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_mtu_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_fec_mode"></a>
<a id="CHANGED_fields_fec_mode"></a>
##### fec_mode

- Schema name: `Fec Mode`
- Type: enum (of string)

Forward Error Correction (FEC) mode. Only valid for physical interfaces. "AUTO": Selects the best FEC mode based on cable/port capabilities "RS": RS-FEC (Reed-Solomon), often used for 25GbE/100GbE+ NICs "BASER": BaseR-FEC (FireCode) "OFF": Disables FEC "LLRS": Low Latency Reed-Solomon FEC, used for 25GBASE-KR/CR
###### Must be one of:

- "AUTO"
- "OFF"
- "RS"
- "BASER"
- "LLRS"

<a id="headingCHANGED_fields_vlan_parent_interface"></a>
<a id="CHANGED_fields_vlan_parent_interface"></a>
##### vlan_parent_interface

- Schema name: `Vlan Parent Interface`

Parent interface for VLAN configuration.
<a id="CHANGED_fields_vlan_parent_interface_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_vlan_parent_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_vlan_parent_interface_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_vlan_parent_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_vlan_parent_interface_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_vlan_tag"></a>
<a id="CHANGED_fields_vlan_tag"></a>
##### vlan_tag

- Schema name: `Vlan Tag`

VLAN tag number for VLAN interfaces.
<a id="CHANGED_fields_vlan_tag_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_vlan_tag_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_vlan_tag_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_vlan_tag_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_vlan_tag_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_vlan_pcp"></a>
<a id="CHANGED_fields_vlan_pcp"></a>
##### vlan_pcp

- Schema name: `Vlan Pcp`

Priority Code Point for VLAN traffic prioritization.
<a id="CHANGED_fields_vlan_pcp_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_vlan_pcp_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_vlan_pcp_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_vlan_pcp_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_vlan_pcp_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_lag_protocol"></a>
<a id="CHANGED_fields_lag_protocol"></a>
##### lag_protocol

- Schema name: `Lag Protocol`
- Type: string

Link aggregation protocol (LACP, FAILOVER, LOADBALANCE, etc.).

<a id="headingCHANGED_fields_lag_ports"></a>
<a id="CHANGED_fields_lag_ports"></a>
##### lag_ports

- Schema name: `Lag Ports`
- Type: array of string
- Default: []

List of interface names that are members of this link aggregation group.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_lag_ports_items"></a>
- Type: string

<a id="headingCHANGED_fields_bridge_members"></a>
<a id="CHANGED_fields_bridge_members"></a>
##### bridge_members

- Schema name: `Bridge Members`
- Type: array of string
- Default: []

List of interface names that are members of this bridge.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_bridge_members_items"></a>
- Type: string

<a id="headingCHANGED_fields_enable_learning"></a>
<a id="CHANGED_fields_enable_learning"></a>
##### enable_learning

- Schema name: `Enable Learning`
- Type: boolean

Whether MAC address learning is enabled for bridge interfaces.

<a id="headingCHANGED_fields_additionalProperties"></a>
<a id="CHANGED_fields_additionalProperties"></a>
##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `InterfaceRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
