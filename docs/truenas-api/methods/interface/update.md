---
title: interface.update
kind: method
source_rst: _sources/api_methods_interface.update.rst.txt
source_html: api_methods_interface.update.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.update

## Summary

Update Interface of `id`.

.. examples(cli)::

Update network interface static IP:

> network interface update enp0s3 aliases="192.168.0.10"

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

ID of the interface to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Updated interface configuration data.
- No Additional Properties
##### name

- Schema name: `Name`
- Type: string

Generate a name if not provided based on `type`, e.g. "br0", "bond1", "vlan0".

##### description

- Schema name: `Description`
- Type: string

Human-readable description of the interface.

##### ipv4_dhcp

- Schema name: `Ipv4 Dhcp`
- Type: boolean

Enable IPv4 DHCP for automatic IP address assignment.

##### ipv6_auto

- Schema name: `Ipv6 Auto`
- Type: boolean

Enable IPv6 autoconfiguration.

##### aliases

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases to configure on the interface.
- All items must be unique
- No Additional Items

###### Each item of this array must be:

###### InterfaceCreateAlias

- Schema name: `InterfaceCreateAlias`
- Type: object
- No Additional Properties
####### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "INET"

The type of IP address (INET for IPv4, INET6 for IPv6).

####### address (required)

- Schema name: `Address`

The IP address for the failover alias.
######## Any of

######### Option 1

- Type: const

######### Option 2

- Type: string

####### netmask (required)

- Schema name: `Netmask`
- Type: integer

The network mask in CIDR notation.

##### failover_critical

- Schema name: `Failover Critical`
- Type: boolean

Whether this interface is critical for failover functionality. Critical interfaces are monitored for failover events and can trigger failover when they fail.

##### failover_group

- Schema name: `Failover Group`

Failover group identifier for clustering. Interfaces in the same group fail over together during failover events.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### failover_vhid

- Schema name: `Failover Vhid`

Virtual Host ID for VRRP failover configuration. Must be unique within the VRRP group and match between failover nodes.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `255`

####### Option 2

- Type: null

##### failover_aliases

- Schema name: `Failover Aliases`
- Type: array of object

List of IP aliases for failover configuration. These IPs are assigned to the interface during normal operation and migrate during failover.
- No Additional Items

###### Each item of this array must be:

###### InterfaceCreateFailoverAlias

- Schema name: `InterfaceCreateFailoverAlias`
- Type: object
- No Additional Properties
####### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "INET"

The type of IP address (INET for IPv4, INET6 for IPv6).

####### address (required)

- Schema name: `Address`

The IP address for the failover alias.
######## Any of

######### Option 1

- Type: const

######### Option 2

- Type: string

##### failover_virtual_aliases

- Schema name: `Failover Virtual Aliases`
- Type: array of object

List of virtual IP aliases for failover configuration. These are shared IPs that float between nodes during failover events.
- No Additional Items

###### Each item of this array must be:

###### InterfaceCreateFailoverAlias

- Schema name: `InterfaceCreateFailoverAlias`
- Type: object
- No Additional Properties
####### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "INET"

The type of IP address (INET for IPv4, INET6 for IPv6).

####### address (required)

- Schema name: `Address`

The IP address for the failover alias.
######## Any of

######### Option 1

- Type: const

######### Option 2

- Type: string

##### bridge_members

- Schema name: `Bridge Members`
- Type: array

List of interfaces to add as members of this bridge.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### enable_learning

- Schema name: `Enable Learning`
- Type: boolean

Enable MAC address learning for bridge interfaces. When enabled, the bridge learns MAC addresses from incoming frames and builds a forwarding table to optimize traffic flow.

##### stp

- Schema name: `Stp`
- Type: boolean

Enable Spanning Tree Protocol for bridge interfaces. STP prevents network loops by blocking redundant paths and enables automatic failover when the primary path fails.

##### lag_protocol

- Schema name: `Lag Protocol`
- Type: enum (of string)

Link aggregation protocol to use for bonding interfaces. LACP uses 802.3ad dynamic negotiation, FAILOVER provides active-backup, LOADBALANCE and ROUNDROBIN distribute traffic across links.

##### xmit_hash_policy

- Schema name: `Xmit Hash Policy`
- Type: enum (of null or string)

Transmit hash policy for load balancing in link aggregation. LAYER2 uses MAC addresses, LAYER2+3 adds IP addresses, and LAYER3+4 includes TCP/UDP ports for distribution.

##### lacpdu_rate

- Schema name: `Lacpdu Rate`
- Type: enum (of null or string)

LACP data unit transmission rate. SLOW sends LACPDUs every 30 seconds, FAST sends every 1 second for quicker link failure detection.

##### lag_ports

- Schema name: `Lag Ports`
- Type: array of string

List of interface names to include in the link aggregation group.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### vlan_parent_interface

- Schema name: `Vlan Parent Interface`
- Type: string

Parent interface for VLAN configuration.

##### vlan_tag

- Schema name: `Vlan Tag`
- Type: integer

VLAN tag number (1-4094).

##### vlan_pcp

- Schema name: `Vlan Pcp`

Priority Code Point for VLAN traffic prioritization (0-7). Values 0-7 map to different QoS priority levels, with 0 being lowest and 7 highest priority.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `7`

####### Option 2

- Type: null

##### mtu

- Schema name: `Mtu`

Maximum transmission unit size for the interface (68-9216 bytes).
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `68` and lesser or equal to `9216`

####### Option 2

- Type: null

### Return value

- Schema name: `InterfaceEntry`
- Type: object

The updated interface configuration.
#### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the network interface.

#### name (required)

- Schema name: `Name`
- Type: string

Name of the network interface.

#### fake (required)

- Schema name: `Fake`
- Type: boolean

Whether this is a fake/simulated interface for testing purposes.

#### type (required)

- Schema name: `Type`
- Type: string

Type of interface (PHYSICAL, BRIDGE, LINK_AGGREGATION, VLAN, etc.).

#### state (required)

- Schema name: `InterfaceEntryState`
- Type: object

Current runtime state information for the interface.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Current name of the network interface.

##### orig_name (required)

- Schema name: `Orig Name`
- Type: string

Original name of the network interface before any renaming.

##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the network interface.

##### mtu (required)

- Schema name: `Mtu`
- Type: integer

Maximum transmission unit size for the interface.

##### cloned (required)

- Schema name: `Cloned`
- Type: boolean

Whether the interface is a cloned/virtual interface.

##### flags (required)

- Schema name: `Flags`
- Type: array of string

List of interface flags indicating various states and capabilities. Common flags include UP, DOWN, RUNNING, MULTICAST, BROADCAST, LOOPBACK, and POINTOPOINT.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### nd6_flags (required)

- Schema name: `Nd6 Flags`
- Type: array

IPv6 neighbor discovery flags. These control IPv6 autoconfiguration behavior and include flags like AUTO*LINKLOCAL, ACCEPT*RTADV, and PERFORMNUD.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### capabilities (required)

- Schema name: `Capabilities`
- Type: array

List of hardware capabilities supported by the interface. Common capabilities include VLAN*MTU, JUMBO*MTU, VLAN*HWTAGGING, VLAN*HWCSUM, and TSO4.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### link_state (required)

- Schema name: `Link State`
- Type: string

Current link state of the interface (up, down, etc.).

##### media_type (required)

- Schema name: `Media Type`
- Type: string

Type of media/connection for the interface. Examples include Ethernet, 802.11, or loopback.

##### media_subtype (required)

- Schema name: `Media Subtype`
- Type: string

Subtype of media/connection for the interface. Examples include 1000baseT, 100baseTX, or autoselect.

##### active_media_type (required)

- Schema name: `Active Media Type`
- Type: string

Currently active media type. This may differ from configured media_type during autonegotiation.

##### active_media_subtype (required)

- Schema name: `Active Media Subtype`
- Type: string

Currently active media subtype. This reflects the actual negotiated connection speed and type.

##### supported_media (required)

- Schema name: `Supported Media`
- Type: array

List of supported media types for the interface. Contains media descriptors like '1000baseT <full-duplex>' or 'autoselect'.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### media_options (required)

- Schema name: `Media Options`

Available media options for the interface. Options may include 'full-duplex', 'half-duplex', 'flowcontrol', or 'rxpause'.
###### Any of

####### Option 1

- Type: array
- No Additional Items

######## Each item of this array must be:

- Type: object

####### Option 2

- Type: null

##### link_address (required)

- Schema name: `Link Address`
- Type: string

MAC address of the interface.

##### permanent_link_address (required)

- Schema name: `Permanent Link Address`

Permanent MAC address of the interface if different from current.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### hardware_link_address (required)

- Schema name: `Hardware Link Address`
- Type: string

Hardware MAC address of the interface.

##### rx_queues

- Schema name: `Rx Queues`
- Type: integer

Number of receive queues configured for the interface.

##### tx_queues

- Schema name: `Tx Queues`
- Type: integer

Number of transmit queues configured for the interface.

##### aliases (required)

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases configured on the interface.
- No Additional Items

###### Each item of this array must be:

###### InterfaceEntryStateAlias

- Schema name: `InterfaceEntryStateAlias`
- Type: object
- No Additional Properties
####### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

####### address (required)

- Schema name: `Address`
- Type: string

The IP address value.

####### netmask

- Schema name: `Netmask`

The network mask for the IP address, either as a string or CIDR notation integer.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: integer

####### broadcast

- Schema name: `Broadcast`
- Type: string

Broadcast address for the network interface.

##### vrrp_config

- Schema name: `Vrrp Config`
- Default: []

VRRP (Virtual Router Redundancy Protocol) configuration for the interface.
###### Any of

####### Option 1

- Type: array
- No Additional Items

######## Each item of this array must be:

- Type: object

####### Option 2

- Type: null

##### protocol

- Schema name: `Protocol`

Link aggregation protocol used (LACP, FAILOVER, etc.).
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### ports

- Schema name: `Ports`
- Type: array of object
- Default: []

List of ports that are members of this link aggregation group.
- No Additional Items

###### Each item of this array must be:

###### InterfaceEntryStatePort

- Schema name: `InterfaceEntryStatePort`
- Type: object
- No Additional Properties
####### name (required)

- Schema name: `Name`
- Type: string

The name of the port interface.

####### flags (required)

- Schema name: `Flags`
- Type: array of string

List of flags associated with the port.
- No Additional Items

######## Each item of this array must be:

- Type: string

##### xmit_hash_policy

- Schema name: `Xmit Hash Policy`
- Default: null

Transmit hash policy for load balancing in link aggregation. LAYER2 uses MAC addresses, LAYER2+3 adds IP addresses, and LAYER3+4 includes TCP/UDP ports for distribution.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### lacpdu_rate

- Schema name: `Lacpdu Rate`
- Default: null

LACP data unit transmission rate. SLOW sends LACPDUs every 30 seconds, FAST sends every 1 second for quicker link failure detection.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### parent

- Schema name: `Parent`

Parent interface for VLAN configuration.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### tag

- Schema name: `Tag`

VLAN tag number.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### pcp

- Schema name: `Pcp`

Priority Code Point for VLAN traffic prioritization. Values 0-7 map to different QoS priority levels, with 0 being lowest and 7 highest priority.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

#### aliases (required)

- Schema name: `Aliases`
- Type: array of object

List of IP address aliases configured on the interface.
- No Additional Items

##### Each item of this array must be:

##### InterfaceEntryAlias

- Schema name: `InterfaceEntryAlias`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

###### address (required)

- Schema name: `Address`
- Type: string

The IP address value.

###### netmask (required)

- Schema name: `Netmask`

The network mask for the IP address, either as a string or CIDR notation integer.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: integer

#### ipv4_dhcp (required)

- Schema name: `Ipv4 Dhcp`
- Type: boolean

Whether IPv4 DHCP is enabled for automatic IP address assignment.

#### ipv6_auto (required)

- Schema name: `Ipv6 Auto`
- Type: boolean

Whether IPv6 autoconfiguration is enabled.

#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the interface.

#### mtu (required)

- Schema name: `Mtu`

Maximum transmission unit size for the interface.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### vlan_parent_interface

- Schema name: `Vlan Parent Interface`

Parent interface for VLAN configuration.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### vlan_tag

- Schema name: `Vlan Tag`

VLAN tag number for VLAN interfaces.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### vlan_pcp

- Schema name: `Vlan Pcp`

Priority Code Point for VLAN traffic prioritization.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### lag_protocol

- Schema name: `Lag Protocol`
- Type: string

Link aggregation protocol (LACP, FAILOVER, LOADBALANCE, etc.).

#### lag_ports

- Schema name: `Lag Ports`
- Type: array of string
- Default: []

List of interface names that are members of this link aggregation group.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### bridge_members

- Schema name: `Bridge Members`
- Type: array of string
- Default: []

List of interface names that are members of this bridge.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### enable_learning

- Schema name: `Enable Learning`
- Type: boolean

Whether MAC address learning is enabled for bridge interfaces.

#### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
