---
title: staticroute.query
kind: event
source_rst: _sources/api_events_staticroute.query.rst.txt
source_html: api_events_staticroute.query.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# staticroute.query

## Summary

Sent on staticroute changes.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `StaticRouteAddedEvent`
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

- Schema name: `StaticRouteEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_destination"></a>
<a id="ADDED_fields_destination"></a>
##### destination (required)

- Schema name: `Destination`
- Type: string

Destination network or host for this static route.
- Must be at least `1` characters long

<a id="headingADDED_fields_gateway"></a>
<a id="ADDED_fields_gateway"></a>
##### gateway (required)

- Schema name: `Gateway`
- Type: string

Gateway IP address for this static route.
- Must be at least `1` characters long

<a id="headingADDED_fields_description"></a>
<a id="ADDED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description for this static route.

<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this static route.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `StaticRouteChangedEvent`
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

- Schema name: `StaticRouteEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_destination"></a>
<a id="CHANGED_fields_destination"></a>
##### destination (required)

- Schema name: `Destination`
- Type: string

Destination network or host for this static route.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_gateway"></a>
<a id="CHANGED_fields_gateway"></a>
##### gateway (required)

- Schema name: `Gateway`
- Type: string

Gateway IP address for this static route.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description for this static route.

<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this static route.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `StaticRouteRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
