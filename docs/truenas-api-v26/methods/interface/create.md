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

Create virtual interfaces (Link Aggregation, VLAN).

Create a bridge interface::

{ "jsonrpc": "2.0", "id": 1, "method": "interface.create", "params": [{ "name": "br0", "type": "BRIDGE", "bridge_members": ["enp0s3", "enp0s4"], "aliases": ["192.168.0.10"] }] }

Create a link aggregation interface that has multiple IP addresses in multiple subnets::

{ "jsonrpc": "2.0", "id": 1, "method": "interface.create", "params": [{ "name": "bond0", "type": "LINK_AGGREGATION", "lag_protocol": "LACP", "lag_ports": ["enp0s8", "enp0s9"], "aliases": ["192.168.0.20/30", "192.168.1.20/30"] }] }

Create a DHCP-enabled VLAN interface::

{ "jsonrpc": "2.0", "id": 1, "method": "interface.create", "params": [{ "name": "vlan0", "type": "VLAN", "vlan_parent_interface": "enp0s10", "vlan_tag": 10, "vlan_pcp": 4, "ipv4_dhcp": true, "ipv6_auto": true }] }

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Configuration data for the new interface.
- No Additional Properties
##### name

- Schema name: `Name`
- Type: string

Generate a name if not provided based on `type`, e.g. "br0", "bond1", "vlan0".

##### description

- Schema name: `Description`
- Type: string
- Default: ""

Human-readable description of the interface.

##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of interface to create.

##### ipv4_dhcp

- Schema name: `Ipv4 Dhcp`
- Type: boolean
- Default: false

Enable IPv4 DHCP for automatic IP address assignment.

##### ipv6_auto

- Schema name: `Ipv6 Auto`
- Type: boolean
- Default: false

Enable IPv6 autoconfiguration.

##### aliases

- Schema name: `Aliases`
- Type: array of object
- Default: []

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
- Default: false

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
- Default: []

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
- Default: []

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
- Default: []

List of interfaces to add as members of this bridge.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### enable_learning

- Schema name: `Enable Learning`
- Type: boolean
- Default: true

Enable MAC address learning for bridge interfaces. When enabled, the bridge learns MAC addresses from incoming frames and builds a forwarding table to optimize traffic flow.

##### stp

- Schema name: `Stp`
- Type: boolean
- Default: true

Enable Spanning Tree Protocol for bridge interfaces. STP prevents network loops by blocking redundant paths and enables automatic failover when the primary path fails.

##### lag_protocol

- Schema name: `Lag Protocol`
- Type: enum (of string)

Link aggregation protocol to use for bonding interfaces. LACP uses 802.3ad dynamic negotiation, FAILOVER provides active-backup, LOADBALANCE and ROUNDROBIN distribute traffic across links.

##### xmit_hash_policy

- Schema name: `Xmit Hash Policy`
- Type: enum (of null or string)
- Default: null

Transmit hash policy for load balancing in link aggregation. LAYER2 uses MAC addresses, LAYER2+3 adds IP addresses, and LAYER3+4 includes TCP/UDP ports for distribution.

##### lacpdu_rate

- Schema name: `Lacpdu Rate`
- Type: enum (of null or string)
- Default: null

LACP data unit transmission rate. SLOW sends LACPDUs every 30 seconds, FAST sends every 1 second for quicker link failure detection.

##### lag_ports

- Schema name: `Lag Ports`
- Type: array of string
- Default: []

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
- Value must be greater or equal to `1` and lesser or equal to `4094`

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
- Default: null

Maximum transmission unit size for the interface (68-9216 bytes).
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `68` and lesser or equal to `9216`

####### Option 2

- Type: null

### Return value

- Type: object

The created interface configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
