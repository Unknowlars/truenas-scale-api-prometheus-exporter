---
title: kerberos.realm.update
kind: method
source_rst: _sources/api_methods_kerberos.realm.update.rst.txt
source_html: api_methods_kerberos.realm.update.html
required_roles:
  - DIRECTORY_SERVICE_WRITE
---

# kerberos.realm.update

## Summary

Update a kerberos realm by id. This will be automatically populated during the domain join process in an Active Directory environment. Kerberos realm names are case-sensitive, but convention is to only use upper-case.

## Required Roles

- `DIRECTORY_SERVICE_WRITE`

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

ID of the Kerberos realm to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Updated Kerberos realm configuration data.
- No Additional Properties
##### realm

- Schema name: `Realm`
- Type: string

Kerberos realm name. This is external to TrueNAS and is case-sensitive. The general convention for kerberos realms is that they are upper-case.
- Must be at least `1` characters long

##### primary_kdc

- Schema name: `Primary Kdc`

The master Kerberos domain controller for this realm. TrueNAS uses this as a fallback if it cannot get credentials because of an invalid password. This can help in environments where the domain uses a hub-and-spoke topology. Use this setting to reduce credential errors after TrueNAS automatically changes its machine password.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### kdc

- Schema name: `Kdc`
- Type: array of string

List of kerberos domain controllers. If the list is empty then the kerberos libraries will use DNS to look up KDCs. In some situations this is undesirable as kerberos libraries are, for intance, not active directory site aware and so may be suboptimal.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### admin_server

- Schema name: `Admin Server`
- Type: array of string

List of kerberos admin servers. If the list is empty then the kerberos libraries will use DNS to look them up.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### kpasswd_server

- Schema name: `Kpasswd Server`
- Type: array of string

List of kerberos kpasswd servers. If the list is empty then DNS will be used to look them up if needed.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

### Return value

- Schema name: `KerberosRealmEntry`
- Type: object

The updated Kerberos realm configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos realm configuration.

#### realm (required)

- Schema name: `Realm`
- Type: string

Kerberos realm name. This is external to TrueNAS and is case-sensitive. The general convention for kerberos realms is that they are upper-case.
- Must be at least `1` characters long

#### primary_kdc

- Schema name: `Primary Kdc`
- Default: null

The master Kerberos domain controller for this realm. TrueNAS uses this as a fallback if it cannot get credentials because of an invalid password. This can help in environments where the domain uses a hub-and-spoke topology. Use this setting to reduce credential errors after TrueNAS automatically changes its machine password.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### kdc

- Schema name: `Kdc`
- Type: array of string
- Default: []

List of kerberos domain controllers. If the list is empty then the kerberos libraries will use DNS to look up KDCs. In some situations this is undesirable as kerberos libraries are, for intance, not active directory site aware and so may be suboptimal.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### admin_server

- Schema name: `Admin Server`
- Type: array of string
- Default: []

List of kerberos admin servers. If the list is empty then the kerberos libraries will use DNS to look them up.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### kpasswd_server

- Schema name: `Kpasswd Server`
- Type: array of string
- Default: []

List of kerberos kpasswd servers. If the list is empty then DNS will be used to look them up if needed.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
