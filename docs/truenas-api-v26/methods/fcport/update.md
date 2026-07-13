---
title: fcport.update
kind: method
source_rst: _sources/api_methods_fcport.update.rst.txt
source_html: api_methods_fcport.update.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# fcport.update

## Summary

Update FC port mapping `id`.

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

ID of the Fibre Channel port to update.

#### Parameter 2: fc_Port_update

#### fc_Port_update

- Schema name: `fc_Port_update`
- Type: object

Updated Fibre Channel port configuration data.
- No Additional Properties
##### port

- Schema name: `Port`
- Type: string

Alias name for the Fibre Channel port.
- Must be at least `1` characters long
- Must be at most `40` characters long

##### target_id

- Schema name: `Target Id`
- Type: integer

ID of the target to associate with this FC port.

### Return value

- Schema name: `FCPortEntry`
- Type: object

The updated Fibre Channel port configuration.
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
