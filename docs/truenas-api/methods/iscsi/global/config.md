---
title: iscsi.global.config
kind: method
source_rst: _sources/api_methods_iscsi.global.config.rst.txt
source_html: api_methods_iscsi.global.config.html
required_roles:
  - SHARING_ISCSI_GLOBAL_READ
---

# iscsi.global.config

## Required Roles

- `SHARING_ISCSI_GLOBAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `IscsiGlobalEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the global iSCSI configuration.

#### basename (required)

- Schema name: `Basename`
- Type: string

Base name prefix for iSCSI target IQNs.

#### isns_servers (required)

- Schema name: `Isns Servers`
- Type: array of string

Array of iSNS (Internet Storage Name Service) server addresses.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### listen_port

- Schema name: `Listen Port`
- Type: integer
- Default: 3260

TCP port number for iSCSI connections.
- Value must be greater or equal to `1025` and lesser or equal to `65535`

#### pool_avail_threshold

- Schema name: `Pool Avail Threshold`
- Default: null

Pool available space threshold percentage or `null` to disable.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `99`

###### Option 2

- Type: null

#### alua (required)

- Schema name: `Alua`
- Type: boolean

Whether Asymmetric Logical Unit Access (ALUA) is enabled. Enabling is limited to TrueNAS Enterprise-licensed high availability systems. ALUA only works when configured on both the client and server.

#### iser (required)

- Schema name: `Iser`
- Type: boolean

Whether iSCSI Extensions for RDMA (iSER) are enabled. Enabling is limited to TrueNAS Enterprise-licensed systems and requires the system and network environment have Remote Direct Memory Access (RDMA)-capable hardware.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
