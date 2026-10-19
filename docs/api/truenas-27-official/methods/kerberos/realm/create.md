---
title: kerberos.realm.create
kind: method
source_rst: _sources/api_methods_kerberos.realm.create.rst.txt
source_html: api_methods_kerberos.realm.create.html
required_roles:
  - DIRECTORY_SERVICE_WRITE
---

# kerberos.realm.create

## Summary

Create a new kerberos realm. This will be automatically populated during the domain join process in an Active Directory environment. Kerberos realm names are case-sensitive, but convention is to only use upper-case.

Entries for kdc, admin_server, and kpasswd_server are not required. If they are unpopulated, then kerberos will use DNS srv records to discover the correct servers. The option to hard-code them is provided due to AD site discovery. Kerberos has no concept of Active Directory sites. This means that middleware performs the site discovery and sets the kerberos configuration based on the AD site.

## Required Roles

- `DIRECTORY_SERVICE_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Kerberos realm configuration data for creation.
- No Additional Properties
<a id="headingCall_parameters_items_i0_realm"></a>
<a id="Call_parameters_items_i0_realm"></a>
##### realm (required)

- Schema name: `Realm`
- Type: string

Kerberos realm name. This is external to TrueNAS and is case-sensitive. The general convention for kerberos realms is that they are upper-case.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_primary_kdc"></a>
<a id="Call_parameters_items_i0_primary_kdc"></a>
##### primary_kdc

- Schema name: `Primary Kdc`
- Default: null

The master Kerberos domain controller for this realm. TrueNAS uses this as a fallback if it cannot get credentials because of an invalid password. This can help in environments where the domain uses a hub-and-spoke topology. Use this setting to reduce credential errors after TrueNAS automatically changes its machine password.
<a id="Call_parameters_items_i0_primary_kdc_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_primary_kdc_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_primary_kdc_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_primary_kdc_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_primary_kdc_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_kdc"></a>
<a id="Call_parameters_items_i0_kdc"></a>
##### kdc

- Schema name: `Kdc`
- Type: array of string
- Default: []

List of kerberos domain controllers. If the list is empty then the kerberos libraries will use DNS to look up KDCs. In some situations this is undesirable as kerberos libraries are, for intance, not active directory site aware and so may be suboptimal.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_kdc_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_admin_server"></a>
<a id="Call_parameters_items_i0_admin_server"></a>
##### admin_server

- Schema name: `Admin Server`
- Type: array of string
- Default: []

List of kerberos admin servers. If the list is empty then the kerberos libraries will use DNS to look them up.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_admin_server_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_kpasswd_server"></a>
<a id="Call_parameters_items_i0_kpasswd_server"></a>
##### kpasswd_server

- Schema name: `Kpasswd Server`
- Type: array of string
- Default: []

List of kerberos kpasswd servers. If the list is empty then DNS will be used to look them up if needed.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_kpasswd_server_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `KerberosRealmEntry`
- Type: object

The created Kerberos realm configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos realm configuration.

<a id="headingReturn_value_realm"></a>
<a id="Return_value_realm"></a>
#### realm (required)

- Schema name: `Realm`
- Type: string

Kerberos realm name. This is external to TrueNAS and is case-sensitive. The general convention for kerberos realms is that they are upper-case.
- Must be at least `1` characters long

<a id="headingReturn_value_primary_kdc"></a>
<a id="Return_value_primary_kdc"></a>
#### primary_kdc

- Schema name: `Primary Kdc`
- Default: null

The master Kerberos domain controller for this realm. TrueNAS uses this as a fallback if it cannot get credentials because of an invalid password. This can help in environments where the domain uses a hub-and-spoke topology. Use this setting to reduce credential errors after TrueNAS automatically changes its machine password.
<a id="Return_value_primary_kdc_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_primary_kdc_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_primary_kdc_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_primary_kdc_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_primary_kdc_anyOf_i1)

- Type: null

<a id="headingReturn_value_kdc"></a>
<a id="Return_value_kdc"></a>
#### kdc

- Schema name: `Kdc`
- Type: array of string
- Default: []

List of kerberos domain controllers. If the list is empty then the kerberos libraries will use DNS to look up KDCs. In some situations this is undesirable as kerberos libraries are, for intance, not active directory site aware and so may be suboptimal.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_kdc_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_admin_server"></a>
<a id="Return_value_admin_server"></a>
#### admin_server

- Schema name: `Admin Server`
- Type: array of string
- Default: []

List of kerberos admin servers. If the list is empty then the kerberos libraries will use DNS to look them up.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_admin_server_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_kpasswd_server"></a>
<a id="Return_value_kpasswd_server"></a>
#### kpasswd_server

- Schema name: `Kpasswd Server`
- Type: array of string
- Default: []

List of kerberos kpasswd servers. If the list is empty then DNS will be used to look them up if needed.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_kpasswd_server_items"></a>
- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
