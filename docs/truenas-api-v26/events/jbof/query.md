---
title: jbof.query
kind: event
source_rst: _sources/api_events_jbof.query.rst.txt
source_html: api_events_jbof.query.html
required_roles:
  - JBOF_READ
---

# jbof.query

## Summary

Sent on jbof changes.

## Required Roles

- `JBOF_READ`

## Schema

- Type: object

### ADDED

- Schema name: `JBOFAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `JBOFEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the JBOF configuration.

##### description

- Schema name: `Description`
- Type: string

Optional description of the JBOF.

##### mgmt_ip1 (required)

- Schema name: `Mgmt Ip1`

IP of first Redfish management interface.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### mgmt_ip2

- Schema name: `Mgmt Ip2`

Optional IP of second Redfish management interface.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### mgmt_username (required)

- Schema name: `Mgmt Username`
- Type: string

Redfish administrative username.

##### mgmt_password (required)

- Schema name: `Mgmt Password`
- Type: string

Redfish administrative password.

##### index (required)

- Schema name: `Index`
- Type: integer

Index of the JBOF. Used to determine data plane IP addresses.

##### uuid (required)

- Schema name: `Uuid`
- Type: string

UUID of the JBOF as reported by the enclosure firmware.

### CHANGED

- Schema name: `JBOFChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `JBOFEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the JBOF configuration.

##### description

- Schema name: `Description`
- Type: string

Optional description of the JBOF.

##### mgmt_ip1 (required)

- Schema name: `Mgmt Ip1`

IP of first Redfish management interface.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### mgmt_ip2

- Schema name: `Mgmt Ip2`

Optional IP of second Redfish management interface.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### mgmt_username (required)

- Schema name: `Mgmt Username`
- Type: string

Redfish administrative username.

##### mgmt_password (required)

- Schema name: `Mgmt Password`
- Type: string

Redfish administrative password.

##### index (required)

- Schema name: `Index`
- Type: integer

Index of the JBOF. Used to determine data plane IP addresses.

##### uuid (required)

- Schema name: `Uuid`
- Type: string

UUID of the JBOF as reported by the enclosure firmware.

### REMOVED

- Schema name: `JBOFRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
