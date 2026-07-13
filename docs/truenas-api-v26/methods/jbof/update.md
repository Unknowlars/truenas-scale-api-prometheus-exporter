---
title: jbof.update
kind: method
source_rst: _sources/api_methods_jbof.update.rst.txt
source_html: api_methods_jbof.update.html
required_roles:
  - JBOF_WRITE
---

# jbof.update

## Summary

Update JBOF of `id`.

## Required Roles

- `JBOF_WRITE`

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

ID of the JBOF to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Updated JBOF configuration data.
- No Additional Properties
##### description

- Schema name: `Description`
- Type: string

Optional description of the JBOF.

##### mgmt_ip1

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

##### mgmt_username

- Schema name: `Mgmt Username`
- Type: string

Redfish administrative username.

##### mgmt_password

- Schema name: `Mgmt Password`
- Type: string

Redfish administrative password.

### Return value

- Type: object

The updated JBOF configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
