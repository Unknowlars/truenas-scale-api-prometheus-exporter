---
title: lxc.update
kind: method
source_rst: _sources/api_methods_lxc.update.rst.txt
source_html: api_methods_lxc.update.html
required_roles:
  - LXC_CONFIG_WRITE
---

# lxc.update

## Summary

Update container config.

## Required Roles

- `LXC_CONFIG_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: lxc_config_update

#### lxc_config_update

- Schema name: `lxc_config_update`
- Type: object

LXCConfigUpdateArgs parameters.
- No Additional Properties
##### preferred_pool

- Schema name: `Preferred Pool`

Default pool used by containers and image datasets.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### bridge

- Schema name: `Bridge`

Network bridge interface for virtualized instance networking. `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### v4_network

- Schema name: `V4 Network`
- Type: string

IPv4 network CIDR for the container bridge network.

##### v6_network

- Schema name: `V6 Network`
- Type: string

IPv6 network CIDR for the container bridge network.

### Return value

- Schema name: `LXCConfigEntry`
- Type: object

Updated LXC configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Configuration ID.

#### preferred_pool

- Schema name: `Preferred Pool`
- Default: null

Default pool used by containers and image datasets.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### bridge

- Schema name: `Bridge`
- Default: null

Network bridge interface for virtualized instance networking. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### v4_network (required)

- Schema name: `V4 Network`
- Type: string

IPv4 network CIDR for the container bridge network.

#### v6_network (required)

- Schema name: `V6 Network`
- Type: string

IPv6 network CIDR for the container bridge network.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
