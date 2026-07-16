---
title: nvmet.port.create
kind: method
source_rst: _sources/api_methods_nvmet.port.create.rst.txt
source_html: api_methods_nvmet.port.create.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.port.create

## Summary

Create a NVMe target `port`.

`ports` are the means through which subsystems (`subsys`) are made available to clients (`hosts`).

## Required Roles

- `SHARING_NVME_TARGET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: nvmet_port_create

#### nvmet_port_create

- Schema name: `nvmet_port_create`

NVMe-oF port configuration data for creation (TCP/RDMA or Fibre Channel).

### Return value

- Schema name: `NVMetPortEntry`
- Type: object

The created NVMe-oF port configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF port.

#### index (required)

- Schema name: `Index`
- Type: integer

Index of the port, for internal use.

#### addr_trtype (required)

- Schema name: `Addr Trtype`
- Type: enum (of string)

Fabric transport technology name.

#### addr_trsvcid (required)

- Schema name: `Addr Trsvcid`

Transport-specific TRSVCID field. When configured for TCP/IP or RDMA this will be the port number.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: string
- Must be at least `1` characters long

###### Option 3

- Type: null

#### addr_traddr (required)

- Schema name: `Addr Traddr`
- Type: string

A transport-specific field identifying the NVMe host port to use for the connection to the controller. For TCP or RDMA transports, this will be an IPv4 or IPv6 address.

#### addr_adrfam (required)

- Schema name: `Addr Adrfam`
- Type: enum (of string)

Address family.

#### inline_data_size

- Schema name: `Inline Data Size`
- Default: null

Maximum size for inline data transfers or `null` for default.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### max_queue_size

- Schema name: `Max Queue Size`
- Default: null

Maximum number of queue entries or `null` for default.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### pi_enable

- Schema name: `Pi Enable`
- Default: null

Whether Protection Information (PI) is enabled or `null` for default.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Port enabled. When NVMe target is running, cannot make changes to an enabled port.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
