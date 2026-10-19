---
title: kerberos.realm.query
kind: event
source_rst: _sources/api_events_kerberos.realm.query.rst.txt
source_html: api_events_kerberos.realm.query.html
required_roles:
  - DIRECTORY_SERVICE_READ
---

# kerberos.realm.query

## Summary

Sent on kerberos.realm changes.

## Required Roles

- `DIRECTORY_SERVICE_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `KerberosRealmAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `KerberosRealmEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos realm configuration.

<a id="headingADDED_fields_realm"></a>
<a id="ADDED_fields_realm"></a>
##### realm (required)

- Schema name: `Realm`
- Type: string

Kerberos realm name. This is external to TrueNAS and is case-sensitive. The general convention for kerberos realms is that they are upper-case.
- Must be at least `1` characters long

<a id="headingADDED_fields_primary_kdc"></a>
<a id="ADDED_fields_primary_kdc"></a>
##### primary_kdc

- Schema name: `Primary Kdc`
- Default: null

The master Kerberos domain controller for this realm. TrueNAS uses this as a fallback if it cannot get credentials because of an invalid password. This can help in environments where the domain uses a hub-and-spoke topology. Use this setting to reduce credential errors after TrueNAS automatically changes its machine password.
<a id="ADDED_fields_primary_kdc_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_primary_kdc_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_primary_kdc_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_primary_kdc_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_primary_kdc_anyOf_i1)

- Type: null

<a id="headingADDED_fields_kdc"></a>
<a id="ADDED_fields_kdc"></a>
##### kdc

- Schema name: `Kdc`
- Type: array of string
- Default: []

List of kerberos domain controllers. If the list is empty then the kerberos libraries will use DNS to look up KDCs. In some situations this is undesirable as kerberos libraries are, for intance, not active directory site aware and so may be suboptimal.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_kdc_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_admin_server"></a>
<a id="ADDED_fields_admin_server"></a>
##### admin_server

- Schema name: `Admin Server`
- Type: array of string
- Default: []

List of kerberos admin servers. If the list is empty then the kerberos libraries will use DNS to look them up.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_admin_server_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_kpasswd_server"></a>
<a id="ADDED_fields_kpasswd_server"></a>
##### kpasswd_server

- Schema name: `Kpasswd Server`
- Type: array of string
- Default: []

List of kerberos kpasswd servers. If the list is empty then DNS will be used to look them up if needed.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_kpasswd_server_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `KerberosRealmChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `KerberosRealmEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos realm configuration.

<a id="headingCHANGED_fields_realm"></a>
<a id="CHANGED_fields_realm"></a>
##### realm (required)

- Schema name: `Realm`
- Type: string

Kerberos realm name. This is external to TrueNAS and is case-sensitive. The general convention for kerberos realms is that they are upper-case.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_primary_kdc"></a>
<a id="CHANGED_fields_primary_kdc"></a>
##### primary_kdc

- Schema name: `Primary Kdc`
- Default: null

The master Kerberos domain controller for this realm. TrueNAS uses this as a fallback if it cannot get credentials because of an invalid password. This can help in environments where the domain uses a hub-and-spoke topology. Use this setting to reduce credential errors after TrueNAS automatically changes its machine password.
<a id="CHANGED_fields_primary_kdc_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_primary_kdc_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_primary_kdc_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_primary_kdc_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_primary_kdc_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_kdc"></a>
<a id="CHANGED_fields_kdc"></a>
##### kdc

- Schema name: `Kdc`
- Type: array of string
- Default: []

List of kerberos domain controllers. If the list is empty then the kerberos libraries will use DNS to look up KDCs. In some situations this is undesirable as kerberos libraries are, for intance, not active directory site aware and so may be suboptimal.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_kdc_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_admin_server"></a>
<a id="CHANGED_fields_admin_server"></a>
##### admin_server

- Schema name: `Admin Server`
- Type: array of string
- Default: []

List of kerberos admin servers. If the list is empty then the kerberos libraries will use DNS to look them up.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_admin_server_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_kpasswd_server"></a>
<a id="CHANGED_fields_kpasswd_server"></a>
##### kpasswd_server

- Schema name: `Kpasswd Server`
- Type: array of string
- Default: []

List of kerberos kpasswd servers. If the list is empty then DNS will be used to look them up if needed.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_kpasswd_server_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `KerberosRealmRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
