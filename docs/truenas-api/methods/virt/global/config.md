---
title: virt.global.config
kind: method
source_rst: _sources/api_methods_virt.global.config.rst.txt
source_html: api_methods_virt.global.config.html
required_roles:
  - VIRT_GLOBAL_READ
---

# virt.global.config

## Required Roles

- `VIRT_GLOBAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `VirtGlobalEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the virtualization global configuration.

#### pool

- Schema name: `Pool`
- Default: null

Default storage pool when creating new instances and volumes.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### dataset

- Schema name: `Dataset`
- Default: null

ZFS dataset path used for virtualization data storage. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### storage_pools

- Schema name: `Storage Pools`
- Default: null

ZFS pools to use as storage pools.
##### Any of

###### Option 1

- Type: array of string
- No Additional Items

####### Each item of this array must be:

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

#### v4_network

- Schema name: `V4 Network`
- Default: null

IPv4 network CIDR for the virtualization bridge network. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### v6_network

- Schema name: `V6 Network`
- Default: null

IPv6 network CIDR for the virtualization bridge network. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### state

- Schema name: `State`
- Default: null

Current operational state of the virtualization subsystem. `null` during initial setup.
##### Any of

###### Option 1

- Type: enum (of string)

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
