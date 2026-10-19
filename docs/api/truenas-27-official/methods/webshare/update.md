---
title: webshare.update
kind: method
source_rst: _sources/api_methods_webshare.update.rst.txt
source_html: api_methods_webshare.update.html
required_roles:
  - SHARING_WEBSHARE_WRITE
---

# webshare.update

## Summary

Update Webshare Service Configuration.

## Required Roles

- `SHARING_WEBSHARE_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: webshare_update

<a id="Call_parameters_items_i0"></a>
#### webshare_update

- Schema name: `webshare_update`
- Type: object

Updated webshare configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i0_bindip"></a>
<a id="Call_parameters_items_i0_bindip"></a>
##### bindip

- Schema name: `Bindip`
- Type: array of string

List of IP addresses used by the TrueNAS Webshare server.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_bindip_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_search"></a>
<a id="Call_parameters_items_i0_search"></a>
##### search

- Schema name: `Search`
- Type: boolean

Search indexing is enabled.

<a id="headingCall_parameters_items_i0_passkey"></a>
<a id="Call_parameters_items_i0_passkey"></a>
##### passkey

- Schema name: `Passkey`
- Type: enum (of string)

Passkey authentication mode.
###### Must be one of:

- "ENABLED"
- "DISABLED"
- "REQUIRED"

<a id="headingCall_parameters_items_i0_groups"></a>
<a id="Call_parameters_items_i0_groups"></a>
##### groups

- Schema name: `Groups`
- Type: array of string

A list of AD/LDAP group names whose members will be granted access to Webshare.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_groups_items"></a>
- Type: string

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `WebshareEntry`
- Type: object

The updated Webshare service configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Webshare service configuration.

<a id="headingReturn_value_bindip"></a>
<a id="Return_value_bindip"></a>
#### bindip (required)

- Schema name: `Bindip`
- Type: array of string

List of IP addresses used by the TrueNAS Webshare server.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_bindip_items"></a>
- Type: string

<a id="headingReturn_value_search"></a>
<a id="Return_value_search"></a>
#### search (required)

- Schema name: `Search`
- Type: boolean

Search indexing is enabled.

<a id="headingReturn_value_passkey"></a>
<a id="Return_value_passkey"></a>
#### passkey (required)

- Schema name: `Passkey`
- Type: enum (of string)

Passkey authentication mode.
##### Must be one of:

- "ENABLED"
- "DISABLED"
- "REQUIRED"

<a id="headingReturn_value_groups"></a>
<a id="Return_value_groups"></a>
#### groups (required)

- Schema name: `Groups`
- Type: array of string

A list of AD/LDAP group names whose members will be granted access to Webshare.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_groups_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
