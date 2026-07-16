---
title: staticroute.update
kind: method
source_rst: _sources/api_methods_staticroute.update.rst.txt
source_html: api_methods_staticroute.update.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# staticroute.update

## Summary

Update Static Route of `id`.

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
- Type: integer

ID of the static route to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Updated configuration for the static route.
- No Additional Properties
##### destination

- Schema name: `Destination`
- Type: string

Destination network or host for this static route.
- Must be at least `1` characters long

##### gateway

- Schema name: `Gateway`
- Type: string

Gateway IP address for this static route.
- Must be at least `1` characters long

##### description

- Schema name: `Description`
- Type: string

Optional description for this static route.

### Return value

- Schema name: `StaticRouteEntry`
- Type: object

The updated static route configuration.
- No Additional Properties
#### destination (required)

- Schema name: `Destination`
- Type: string

Destination network or host for this static route.
- Must be at least `1` characters long

#### gateway (required)

- Schema name: `Gateway`
- Type: string

Gateway IP address for this static route.
- Must be at least `1` characters long

#### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description for this static route.

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this static route.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
