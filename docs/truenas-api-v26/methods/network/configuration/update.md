---
title: network.configuration.update
kind: method
source_rst: _sources/api_methods_network.configuration.update.rst.txt
source_html: api_methods_network.configuration.update.html
required_roles:
  - NETWORK_GENERAL_WRITE
---

# network.configuration.update

## Summary

Update Network Configuration Service configuration.

## Required Roles

- `NETWORK_GENERAL_WRITE`

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

Network configuration data to update.
- No Additional Properties
##### hostname

- Schema name: `Hostname`
- Type: string

System hostname.

##### domain

- Schema name: `Domain`
- Type: string

System domain name.

##### ipv4gateway

- Schema name: `Ipv4Gateway`

Used instead of the default gateway provided by DHCP.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### ipv6gateway

- Schema name: `Ipv6Gateway`

IPv6 default gateway address.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### nameserver1

- Schema name: `Nameserver1`

Primary DNS server.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### nameserver2

- Schema name: `Nameserver2`

Secondary DNS server.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### nameserver3

- Schema name: `Nameserver3`

Tertiary DNS server.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### httpproxy

- Schema name: `Httpproxy`
- Type: string

Must be provided if a proxy is to be used for network operations.

##### hosts

- Schema name: `Hosts`
- Type: array of string

Static host entries to add to the hosts file.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### domains

- Schema name: `Domains`
- Type: array of string

Additional domain names for DNS search.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### service_announcement

- Schema name: `ServiceAnnouncement`
- Type: object

Determines the broadcast protocols that will be used to advertise the server.
- No Additional Properties
###### netbios

- Schema name: `Netbios`
- Type: boolean

Enable the NetBIOS name server (NBNS) which starts concurrently with the SMB service. SMB clients will only perform NBNS lookups if SMB1 is enabled. NBNS may be required for legacy SMB clients.

###### mdns

- Schema name: `Mdns`
- Type: boolean

Enable multicast DNS service announcements for enabled services.

###### wsd

- Schema name: `Wsd`
- Type: boolean

Enable Web Service Discovery support.

##### activity

- Schema name: `NetworkConfigurationActivity`
- Type: object

Network activity filtering configuration.
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Whether to allow or deny the specified network activities.

###### activities

- Schema name: `Activities`
- Type: array of string
- Default: []

Array of network activity types to allow or deny.
- No Additional Items

####### Each item of this array must be:

- Type: string

##### hostname_b

- Schema name: `Hostname B`

Hostname for the second controller in HA configurations or `null`.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### hostname_virtual

- Schema name: `Hostname Virtual`

Virtual hostname for HA configurations or `null`.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

### Return value

- Type: object

The updated network configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
