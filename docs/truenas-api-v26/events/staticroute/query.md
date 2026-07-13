---
title: staticroute.query
kind: event
source_rst: _sources/api_events_staticroute.query.rst.txt
source_html: api_events_staticroute.query.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# staticroute.query

## Summary

Sent on staticroute changes.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

### ADDED

- Schema name: `StaticRouteAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `StaticRouteEntry`
- Type: object
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

##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this static route.

### CHANGED

- Schema name: `StaticRouteChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `StaticRouteEntry`
- Type: object
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

##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this static route.

### REMOVED

- Schema name: `StaticRouteRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
