---
title: fc.fc_host.update
kind: method
source_rst: _sources/api_methods_fc.fc_host.update.rst.txt
source_html: api_methods_fc.fc_host.update.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# fc.fc_host.update

## Summary

Update FC host `id`.

`alias` is a user-readable name for FC host port.

`wwpn` is the WWPN in naa format (Controller A if HA)

`wwpn_b` is the WWPN in naa format (Controller B, only applicable for HA)

`npiv` is the number of NPIV hosts to allow for this FC host.

## Required Roles

- `SHARING_ISCSI_TARGET_WRITE`

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

ID of the Fibre Channel host to update.

#### Parameter 2: fc_host_update

#### fc_host_update

- Schema name: `fc_host_update`
- Type: object

Updated Fibre Channel host configuration data.
- No Additional Properties
##### alias

- Schema name: `Alias`
- Type: string

Human-readable alias for the Fibre Channel host.
- Must be at least `1` characters long
- Must be at most `32` characters long

##### wwpn

- Schema name: `Wwpn`

World Wide Port Name for port A or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### wwpn_b

- Schema name: `Wwpn B`

World Wide Port Name for port B or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### npiv

- Schema name: `Npiv`
- Type: integer

Number of N_Port ID Virtualization (NPIV) virtual ports to create.

### Return value

- Schema name: `FCHostEntry`
- Type: object

The updated Fibre Channel host configuration.
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
