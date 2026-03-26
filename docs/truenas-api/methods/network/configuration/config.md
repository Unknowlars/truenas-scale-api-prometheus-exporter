---
title: network.configuration.config
kind: method
source_rst: _sources/api_methods_network.configuration.config.rst.txt
source_html: api_methods_network.configuration.config.html
required_roles:
  - NETWORK_GENERAL_READ
---

# network.configuration.config

## Required Roles

- `NETWORK_GENERAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `NetworkConfigurationEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the network configuration.

#### hostname (required)

- Schema name: `Hostname`
- Type: string

System hostname.

#### domain (required)

- Schema name: `Domain`
- Type: string

System domain name.

#### ipv4gateway (required)

- Schema name: `Ipv4Gateway`

Used instead of the default gateway provided by DHCP.
##### Any of

###### Option 1

- Type: const

###### Option 2

- Type: string

#### ipv6gateway (required)

- Schema name: `Ipv6Gateway`

IPv6 default gateway address.
##### Any of

###### Option 1

- Type: const

###### Option 2

- Type: string

#### nameserver1 (required)

- Schema name: `Nameserver1`

Primary DNS server.
##### Any of

###### Option 1

- Type: const

###### Option 2

- Type: string

#### nameserver2 (required)

- Schema name: `Nameserver2`

Secondary DNS server.
##### Any of

###### Option 1

- Type: const

###### Option 2

- Type: string

#### nameserver3 (required)

- Schema name: `Nameserver3`

Tertiary DNS server.
##### Any of

###### Option 1

- Type: const

###### Option 2

- Type: string

#### httpproxy (required)

- Schema name: `Httpproxy`
- Type: string

Must be provided if a proxy is to be used for network operations.

#### hosts (required)

- Schema name: `Hosts`
- Type: array of string

Static host entries to add to the hosts file.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### domains (required)

- Schema name: `Domains`
- Type: array of string

Additional domain names for DNS search.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### service_announcement (required)

- Schema name: `ServiceAnnouncement`
- Type: object

Determines the broadcast protocols that will be used to advertise the server.
- No Additional Properties
##### netbios

- Schema name: `Netbios`
- Type: boolean

Enable the NetBIOS name server (NBNS) which starts concurrently with the SMB service. SMB clients will only perform NBNS lookups if SMB1 is enabled. NBNS may be required for legacy SMB clients.

##### mdns

- Schema name: `Mdns`
- Type: boolean

Enable multicast DNS service announcements for enabled services.

##### wsd

- Schema name: `Wsd`
- Type: boolean

Enable Web Service Discovery support.

#### activity (required)

- Schema name: `NetworkConfigurationActivity`
- Type: object

Network activity filtering configuration.
- No Additional Properties
##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Whether to allow or deny the specified network activities.

##### activities

- Schema name: `Activities`
- Type: array of string
- Default: []

Array of network activity types to allow or deny.
- No Additional Items

###### Each item of this array must be:

- Type: string

#### hostname_local (required)

- Schema name: `Hostname Local`
- Type: string

Local hostname for this system.

#### hostname_b

- Schema name: `Hostname B`

Hostname for the second controller in HA configurations or `null`.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### hostname_virtual

- Schema name: `Hostname Virtual`

Virtual hostname for HA configurations or `null`.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### state (required)

- Schema name: `NetWorkConfigurationState`
- Type: object

Current network configuration state.
- No Additional Properties
##### ipv4gateway (required)

- Schema name: `Ipv4Gateway`

Current IPv4 default gateway address.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### ipv6gateway (required)

- Schema name: `Ipv6Gateway`

Current IPv6 default gateway address.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### nameserver1 (required)

- Schema name: `Nameserver1`

Current primary DNS server address.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### nameserver2 (required)

- Schema name: `Nameserver2`

Current secondary DNS server address.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### nameserver3 (required)

- Schema name: `Nameserver3`

Current tertiary DNS server address.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### hosts (required)

- Schema name: `Hosts`
- Type: array of string

Current hosts file entries.
- No Additional Items

###### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
