---
title: interface.get_instance
kind: method
source_rst: _sources/api_methods_interface.get_instance.rst.txt
source_html: api_methods_interface.get_instance.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# interface.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `NETWORK_INTERFACE_READ`

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

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
- No Additional Properties
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `InterfaceEntry`
- Type: object
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
