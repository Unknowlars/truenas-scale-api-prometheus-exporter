---
title: nvmet.port.query
kind: event
source_rst: _sources/api_events_nvmet.port.query.rst.txt
source_html: api_events_nvmet.port.query.html
required_roles:
  - SHARING_NVME_TARGET_READ
---

# nvmet.port.query

## Summary

Sent on nvmet.port changes.

## Required Roles

- `SHARING_NVME_TARGET_READ`

## Schema

- Type: object

### ADDED

- Schema name: `NVMetPortAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `NVMetPortEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF port.

##### index (required)

- Schema name: `Index`
- Type: integer

Index of the port, for internal use.

##### addr_trtype (required)

- Schema name: `Addr Trtype`
- Type: enum (of string)

Fabric transport technology name.

##### addr_trsvcid (required)

- Schema name: `Addr Trsvcid`

Transport-specific TRSVCID field. When configured for TCP/IP or RDMA this will be the port number.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 3

- Type: null

##### addr_traddr (required)

- Schema name: `Addr Traddr`
- Type: string

A transport-specific field identifying the NVMe host port to use for the connection to the controller. For TCP or RDMA transports, this will be an IPv4 or IPv6 address.

##### addr_adrfam (required)

- Schema name: `Addr Adrfam`
- Type: enum (of string)

Address family.

##### inline_data_size

- Schema name: `Inline Data Size`
- Default: null

Maximum size for inline data transfers or `null` for default.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### max_queue_size

- Schema name: `Max Queue Size`
- Default: null

Maximum number of queue entries or `null` for default.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### pi_enable

- Schema name: `Pi Enable`
- Default: null

Whether Protection Information (PI) is enabled or `null` for default.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

### CHANGED

- Schema name: `NVMetPortChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `NVMetPortEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF port.

##### index (required)

- Schema name: `Index`
- Type: integer

Index of the port, for internal use.

##### addr_trtype (required)

- Schema name: `Addr Trtype`
- Type: enum (of string)

Fabric transport technology name.

##### addr_trsvcid (required)

- Schema name: `Addr Trsvcid`

Transport-specific TRSVCID field. When configured for TCP/IP or RDMA this will be the port number.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 3

- Type: null

##### addr_traddr (required)

- Schema name: `Addr Traddr`
- Type: string

A transport-specific field identifying the NVMe host port to use for the connection to the controller. For TCP or RDMA transports, this will be an IPv4 or IPv6 address.

##### addr_adrfam (required)

- Schema name: `Addr Adrfam`
- Type: enum (of string)

Address family.

##### inline_data_size

- Schema name: `Inline Data Size`
- Default: null

Maximum size for inline data transfers or `null` for default.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### max_queue_size

- Schema name: `Max Queue Size`
- Default: null

Maximum number of queue entries or `null` for default.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### pi_enable

- Schema name: `Pi Enable`
- Default: null

Whether Protection Information (PI) is enabled or `null` for default.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

### REMOVED

- Schema name: `NVMetPortRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
