---
title: staticroute.create
kind: method
source_rst: _sources/api_methods_staticroute.create.rst.txt
source_html: api_methods_staticroute.create.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# staticroute.create

## Summary

Create a Static Route.

Address families of `gateway` and `destination` should match when creating a static route.

`description` is an optional attribute for any notes regarding the static route.

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

Configuration for the new static route.
- No Additional Properties
##### destination (required)

- Schema name: `Destination`
- Type: string

Destination network or host for this static route.
- Must be at least `1` characters long

##### gateway (required)

- Schema name: `Gateway`
- Type: string

Gateway IP address for this static route.
- Must be at least `1` characters long

##### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description for this static route.

### Return value

- Schema name: `StaticRouteEntry`
- Type: object

The newly created static route configuration.
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
