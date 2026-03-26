---
title: docker.network.query
kind: event
source_rst: _sources/api_events_docker.network.query.rst.txt
source_html: api_events_docker.network.query.html
required_roles:
  - DOCKER_READ
---

# docker.network.query

## Summary

Sent on docker.network changes.

## Required Roles

- `DOCKER_READ`

## Schema

- Type: object

### ADDED

- Schema name: `DockerNetworkAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### fields (required)

- Schema name: `DockerNetworkEntry`
- Type: object
- No Additional Properties
##### ipam (required)

- Schema name: `Ipam`

IP Address Management configuration for the network or `null`.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

##### labels (required)

- Schema name: `Labels`

Metadata labels attached to the network or `null`.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

##### created (required)

- Schema name: `Created`

Timestamp when the network was created or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### driver (required)

- Schema name: `Driver`

Network driver type (bridge, host, overlay, etc.) or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### id (required)

- Schema name: `Id`

Full network identifier or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### name (required)

- Schema name: `Name`

Human-readable name of the network or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### scope (required)

- Schema name: `Scope`

Network scope (local, global, swarm) or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### short_id (required)

- Schema name: `Short Id`

Shortened network identifier or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

### CHANGED

- Schema name: `DockerNetworkChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### fields (required)

- Schema name: `DockerNetworkEntry`
- Type: object
- No Additional Properties
##### ipam (required)

- Schema name: `Ipam`

IP Address Management configuration for the network or `null`.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

##### labels (required)

- Schema name: `Labels`

Metadata labels attached to the network or `null`.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

##### created (required)

- Schema name: `Created`

Timestamp when the network was created or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### driver (required)

- Schema name: `Driver`

Network driver type (bridge, host, overlay, etc.) or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### id (required)

- Schema name: `Id`

Full network identifier or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### name (required)

- Schema name: `Name`

Human-readable name of the network or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### scope (required)

- Schema name: `Scope`

Network scope (local, global, swarm) or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### short_id (required)

- Schema name: `Short Id`

Shortened network identifier or `null`.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

### REMOVED

- Schema name: `DockerNetworkRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
