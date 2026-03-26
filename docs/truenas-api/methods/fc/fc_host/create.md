---
title: fc.fc_host.create
kind: method
source_rst: _sources/api_methods_fc.fc_host.create.rst.txt
source_html: api_methods_fc.fc_host.create.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# fc.fc_host.create

## Summary

Creates FC host (pairing).

This will associate an `alias` with a corresponding Fibre Channel WWPN. For HA sytems the alias will be associated with a pair of WWPNs, one per node.

`alias` is a user-readable name for FC host (pairing).

`wwpn` is the WWPN in naa format (Controller A if HA)

`wwpn_b` is the WWPN in naa format (Controller B, only applicable for HA)

`npiv` is the number of NPIV hosts to create for this FC host.

## Required Roles

- `SHARING_ISCSI_TARGET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: fc_host_create

#### fc_host_create

- Schema name: `fc_host_create`
- Type: object

Fibre Channel host configuration data for the new host.
- No Additional Properties
##### alias (required)

- Schema name: `Alias`
- Type: string

Human-readable alias for the Fibre Channel host.
- Must be at least `1` characters long
- Must be at most `32` characters long

##### wwpn

- Schema name: `Wwpn`
- Default: null

World Wide Port Name for port A or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### wwpn_b

- Schema name: `Wwpn B`
- Default: null

World Wide Port Name for port B or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### npiv

- Schema name: `Npiv`
- Type: integer
- Default: 0

Number of N_Port ID Virtualization (NPIV) virtual ports to create.

### Return value

- Schema name: `FCHostEntry`
- Type: object

The created Fibre Channel host configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel host configuration.

#### alias (required)

- Schema name: `Alias`
- Type: string

Human-readable alias for the Fibre Channel host.
- Must be at least `1` characters long
- Must be at most `32` characters long

#### wwpn

- Schema name: `Wwpn`
- Default: null

World Wide Port Name for port A or `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### wwpn_b

- Schema name: `Wwpn B`
- Default: null

World Wide Port Name for port B or `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### npiv

- Schema name: `Npiv`
- Type: integer
- Default: 0

Number of N_Port ID Virtualization (NPIV) virtual ports to create.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
