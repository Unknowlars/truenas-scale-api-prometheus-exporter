---
title: core.arp
kind: method
source_rst: _sources/api_methods_core.arp.rst.txt
source_html: api_methods_core.arp.html
required_roles:
  - FULL_ADMIN
---

# core.arp

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`
- Type: object

CoreArpArgs parameters.
- No Additional Properties
##### ip

- Schema name: `Ip`
- Default: null

IP address to look up in ARP table or `null` for all entries.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### interface

- Schema name: `Interface`
- Default: null

Network interface to query or `null` for all interfaces.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: object

Object mapping IP addresses to MAC addresses from the ARP table.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
