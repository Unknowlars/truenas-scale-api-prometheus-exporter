---
title: virt.global.update
kind: method
source_rst: _sources/api_methods_virt.global.update.rst.txt
source_html: api_methods_virt.global.update.html
required_roles:
  - VIRT_GLOBAL_WRITE
---

# virt.global.update

## Summary

Update global virtualization settings.

`pool` which pool to use to store instances. None will disable the service.

`bridge` which bridge interface to use by default. None means it will automatically create one.

This method is a job.

## Required Roles

- `VIRT_GLOBAL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: virt_global_update

#### virt_global_update

- Schema name: `virt_global_update`
- Type: object

VirtGlobalUpdateArgs parameters.
- No Additional Properties
##### pool

- Schema name: `Pool`

Default storage pool when creating new instances and volumes.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### bridge

- Schema name: `Bridge`

Network bridge interface for virtualized instance networking. `null` to disable.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### storage_pools

- Schema name: `Storage Pools`

ZFS pools to use as storage pools.
###### Any of

####### Option 1

- Type: array of string
- No Additional Items

######## Each item of this array must be:

- Type: string

####### Option 2

- Type: null

##### v4_network

- Schema name: `V4 Network`

IPv4 network CIDR for the virtualization bridge network. `null` to use default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### v6_network

- Schema name: `V6 Network`

IPv6 network CIDR for the virtualization bridge network. `null` to use default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

### Return value

- Schema name: `VirtGlobalEntry`
- Type: object

The updated virtualization global configuration.
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
