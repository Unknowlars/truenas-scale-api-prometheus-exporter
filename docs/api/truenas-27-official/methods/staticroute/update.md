---
title: staticroute.update
kind: method
source_rst: _sources/api_methods_staticroute.update.rst.txt
source_html: api_methods_staticroute.update.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# staticroute.update

## Summary

Update Static Route of `id`.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the static route to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Updated configuration for the static route.
- No Additional Properties
<a id="headingCall_parameters_items_i1_destination"></a>
<a id="Call_parameters_items_i1_destination"></a>
##### destination

- Schema name: `Destination`
- Type: string

Destination network or host for this static route.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_gateway"></a>
<a id="Call_parameters_items_i1_gateway"></a>
##### gateway

- Schema name: `Gateway`
- Type: string

Gateway IP address for this static route.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_description"></a>
<a id="Call_parameters_items_i1_description"></a>
##### description

- Schema name: `Description`
- Type: string

Optional description for this static route.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `StaticRouteEntry`
- Type: object

The updated static route configuration.
- No Additional Properties
<a id="headingReturn_value_destination"></a>
<a id="Return_value_destination"></a>
#### destination (required)

- Schema name: `Destination`
- Type: string

Destination network or host for this static route.
- Must be at least `1` characters long

<a id="headingReturn_value_gateway"></a>
<a id="Return_value_gateway"></a>
#### gateway (required)

- Schema name: `Gateway`
- Type: string

Gateway IP address for this static route.
- Must be at least `1` characters long

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description for this static route.

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this static route.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
