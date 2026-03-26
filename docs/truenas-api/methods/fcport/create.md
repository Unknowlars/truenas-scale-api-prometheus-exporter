---
title: fcport.create
kind: method
source_rst: _sources/api_methods_fcport.create.rst.txt
source_html: api_methods_fcport.create.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# fcport.create

## Summary

Creates mapping between a FC port and a target.

`port` is a FC host port `alias`, or `alias/number` for a NPIV port.

`target_id` is the `id` of the target to be associated with the FC port.

## Required Roles

- `SHARING_ISCSI_TARGET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: fc_Port_create

#### fc_Port_create

- Schema name: `fc_Port_create`
- Type: object

Fibre Channel port configuration data for the new port.
- No Additional Properties
##### port (required)

- Schema name: `Port`
- Type: string

Alias name for the Fibre Channel port.
- Must be at least `1` characters long
- Must be at most `40` characters long

##### target_id (required)

- Schema name: `Target Id`
- Type: integer

ID of the target to associate with this FC port.

### Return value

- Schema name: `FCPortEntry`
- Type: object

The created Fibre Channel port configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel port configuration.

#### port (required)

- Schema name: `Port`
- Type: string

Alias name for the Fibre Channel port.
- Must be at least `1` characters long
- Must be at most `40` characters long

#### wwpn (required)

- Schema name: `Wwpn`

World Wide Port Name for port A or `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### wwpn_b (required)

- Schema name: `Wwpn B`

World Wide Port Name for port B or `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### target (required)

- Schema name: `Target`

Target configuration object or `null` if not configured.
##### Any of

###### Option 1

- Type: object

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
