---
title: jbof.create
kind: method
source_rst: _sources/api_methods_jbof.create.rst.txt
source_html: api_methods_jbof.create.html
required_roles:
  - JBOF_WRITE
---

# jbof.create

## Summary

Create a new JBOF.

This will use the supplied Redfish credentials to configure the data plane on the expansion shelf for direct connection to ROCE capable network cards on the TrueNAS head unit.

## Required Roles

- `JBOF_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

JBOF configuration data for creation.
- No Additional Properties
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

### Return value

- Schema name: `JBOFEntry`
- Type: object

The created JBOF configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the JBOF configuration.

#### description

- Schema name: `Description`
- Type: string

Optional description of the JBOF.

#### mgmt_ip1 (required)

- Schema name: `Mgmt Ip1`

IP of first Redfish management interface.
##### Any of

###### Option 1

- Type: const

###### Option 2

- Type: string

#### mgmt_ip2

- Schema name: `Mgmt Ip2`

Optional IP of second Redfish management interface.
##### Any of

###### Option 1

- Type: const

###### Option 2

- Type: string

#### mgmt_username (required)

- Schema name: `Mgmt Username`
- Type: string

Redfish administrative username.

#### mgmt_password (required)

- Schema name: `Mgmt Password`
- Type: string

Redfish administrative password.

#### index (required)

- Schema name: `Index`
- Type: integer

Index of the JBOF. Used to determine data plane IP addresses.

#### uuid (required)

- Schema name: `Uuid`
- Type: string

UUID of the JBOF as reported by the enclosure firmware.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
