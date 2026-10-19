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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NetworkConfigurationEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the network configuration.

<a id="headingReturn_value_hostname"></a>
<a id="Return_value_hostname"></a>
#### hostname (required)

- Schema name: `Hostname`
- Type: string

System hostname.

<a id="headingReturn_value_domain"></a>
<a id="Return_value_domain"></a>
#### domain (required)

- Schema name: `Domain`
- Type: string

System domain name.

<a id="headingReturn_value_ipv4gateway"></a>
<a id="Return_value_ipv4gateway"></a>
#### ipv4gateway (required)

- Schema name: `Ipv4Gateway`

Used instead of the default gateway provided by DHCP.
<a id="Return_value_ipv4gateway_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_ipv4gateway_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ipv4gateway_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_ipv4gateway_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ipv4gateway_anyOf_i1)

- Type: string

<a id="headingReturn_value_ipv6gateway"></a>
<a id="Return_value_ipv6gateway"></a>
#### ipv6gateway (required)

- Schema name: `Ipv6Gateway`

IPv6 default gateway address.
<a id="Return_value_ipv6gateway_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_ipv6gateway_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ipv6gateway_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_ipv6gateway_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ipv6gateway_anyOf_i1)

- Type: string

<a id="headingReturn_value_nameserver1"></a>
<a id="Return_value_nameserver1"></a>
#### nameserver1 (required)

- Schema name: `Nameserver1`

Primary DNS server.
<a id="Return_value_nameserver1_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_nameserver1_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_nameserver1_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_nameserver1_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_nameserver1_anyOf_i1)

- Type: string

<a id="headingReturn_value_nameserver2"></a>
<a id="Return_value_nameserver2"></a>
#### nameserver2 (required)

- Schema name: `Nameserver2`

Secondary DNS server.
<a id="Return_value_nameserver2_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_nameserver2_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_nameserver2_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_nameserver2_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_nameserver2_anyOf_i1)

- Type: string

<a id="headingReturn_value_nameserver3"></a>
<a id="Return_value_nameserver3"></a>
#### nameserver3 (required)

- Schema name: `Nameserver3`

Tertiary DNS server.
<a id="Return_value_nameserver3_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_nameserver3_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_nameserver3_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_nameserver3_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_nameserver3_anyOf_i1)

- Type: string

<a id="headingReturn_value_httpproxy"></a>
<a id="Return_value_httpproxy"></a>
#### httpproxy (required)

- Schema name: `Httpproxy`
- Type: string

Must be provided if a proxy is to be used for network operations.

<a id="headingReturn_value_hosts"></a>
<a id="Return_value_hosts"></a>
#### hosts (required)

- Schema name: `Hosts`
- Type: array of string

Static host entries to add to the hosts file.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_hosts_items"></a>
- Type: string

<a id="headingReturn_value_domains"></a>
<a id="Return_value_domains"></a>
#### domains (required)

- Schema name: `Domains`
- Type: array of string

Additional domain names for DNS search.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_domains_items"></a>
- Type: string

<a id="headingReturn_value_service_announcement"></a>
<a id="Return_value_service_announcement"></a>
#### service_announcement (required)

- Schema name: `ServiceAnnouncement`
- Type: object

Determines the broadcast protocols that will be used to advertise the server.
- No Additional Properties
<a id="headingReturn_value_service_announcement_netbios"></a>
<a id="Return_value_service_announcement_netbios"></a>
##### netbios

- Schema name: `Netbios`
- Type: boolean

Enable the NetBIOS name server (NBNS) which starts concurrently with the SMB service. SMB clients will only perform NBNS lookups if SMB1 is enabled. NBNS may be required for legacy SMB clients.

<a id="headingReturn_value_service_announcement_mdns"></a>
<a id="Return_value_service_announcement_mdns"></a>
##### mdns

- Schema name: `Mdns`
- Type: boolean

Enable multicast DNS service announcements for enabled services.

<a id="headingReturn_value_service_announcement_wsd"></a>
<a id="Return_value_service_announcement_wsd"></a>
##### wsd

- Schema name: `Wsd`
- Type: boolean

Enable Web Service Discovery support.

<a id="headingReturn_value_activity"></a>
<a id="Return_value_activity"></a>
#### activity (required)

- Schema name: `NetworkConfigurationActivity`
- Type: object

Network activity filtering configuration.
- No Additional Properties
<a id="headingReturn_value_activity_type"></a>
<a id="Return_value_activity_type"></a>
##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Whether to allow or deny the specified network activities.
###### Must be one of:

- "ALLOW"
- "DENY"

<a id="headingReturn_value_activity_activities"></a>
<a id="Return_value_activity_activities"></a>
##### activities

- Schema name: `Activities`
- Type: array of string
- Default: []

Array of network activity types to allow or deny.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_activity_activities_items"></a>
- Type: string

<a id="headingReturn_value_hostname_local"></a>
<a id="Return_value_hostname_local"></a>
#### hostname_local (required)

- Schema name: `Hostname Local`
- Type: string

Local hostname for this system.

<a id="headingReturn_value_hostname_b"></a>
<a id="Return_value_hostname_b"></a>
#### hostname_b

- Schema name: `Hostname B`

Hostname for the second controller in HA configurations or `null`.
<a id="Return_value_hostname_b_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_hostname_b_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_hostname_b_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_hostname_b_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_hostname_b_anyOf_i1)

- Type: null

<a id="headingReturn_value_hostname_virtual"></a>
<a id="Return_value_hostname_virtual"></a>
#### hostname_virtual

- Schema name: `Hostname Virtual`

Virtual hostname for HA configurations or `null`.
<a id="Return_value_hostname_virtual_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_hostname_virtual_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_hostname_virtual_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_hostname_virtual_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_hostname_virtual_anyOf_i1)

- Type: null

<a id="headingReturn_value_state"></a>
<a id="Return_value_state"></a>
#### state (required)

- Schema name: `NetWorkConfigurationState`
- Type: object

Current network configuration state.
- No Additional Properties
<a id="headingReturn_value_state_ipv4gateway"></a>
<a id="Return_value_state_ipv4gateway"></a>
##### ipv4gateway (required)

- Schema name: `Ipv4Gateway`

Current IPv4 default gateway address.
<a id="Return_value_state_ipv4gateway_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_ipv4gateway_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_ipv4gateway_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_state_ipv4gateway_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_ipv4gateway_anyOf_i1)

- Type: string

<a id="headingReturn_value_state_ipv6gateway"></a>
<a id="Return_value_state_ipv6gateway"></a>
##### ipv6gateway (required)

- Schema name: `Ipv6Gateway`

Current IPv6 default gateway address.
<a id="Return_value_state_ipv6gateway_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_ipv6gateway_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_ipv6gateway_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_state_ipv6gateway_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_ipv6gateway_anyOf_i1)

- Type: string

<a id="headingReturn_value_state_nameserver1"></a>
<a id="Return_value_state_nameserver1"></a>
##### nameserver1 (required)

- Schema name: `Nameserver1`

Current primary DNS server address.
<a id="Return_value_state_nameserver1_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_nameserver1_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_nameserver1_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_state_nameserver1_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_nameserver1_anyOf_i1)

- Type: string

<a id="headingReturn_value_state_nameserver2"></a>
<a id="Return_value_state_nameserver2"></a>
##### nameserver2 (required)

- Schema name: `Nameserver2`

Current secondary DNS server address.
<a id="Return_value_state_nameserver2_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_nameserver2_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_nameserver2_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_state_nameserver2_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_nameserver2_anyOf_i1)

- Type: string

<a id="headingReturn_value_state_nameserver3"></a>
<a id="Return_value_state_nameserver3"></a>
##### nameserver3 (required)

- Schema name: `Nameserver3`

Current tertiary DNS server address.
<a id="Return_value_state_nameserver3_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_state_nameserver3_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_state_nameserver3_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_state_nameserver3_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_state_nameserver3_anyOf_i1)

- Type: string

<a id="headingReturn_value_state_hosts"></a>
<a id="Return_value_state_hosts"></a>
##### hosts (required)

- Schema name: `Hosts`
- Type: array of string

Current hosts file entries.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_state_hosts_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
