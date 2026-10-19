---
title: docker.network.query
kind: event
source_rst: _sources/api_events_docker.network.query.rst.txt
source_html: api_events_docker.network.query.html
required_roles:
  - DOCKER_READ
---

# docker.network.query

## Summary

Sent on docker.network changes.

## Required Roles

- `DOCKER_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `DockerNetworkAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
<a id="ADDED_id_anyOf"></a>
##### Any of

<a id="tab-pane_ADDED_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_id_anyOf_i1)

- Type: null

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `DockerNetworkEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_ipam"></a>
<a id="ADDED_fields_ipam"></a>
##### ipam (required)

- Schema name: `Ipam`

IP Address Management configuration for the network or `null`.
<a id="ADDED_fields_ipam_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_ipam_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_ipam_anyOf_i0)

- Type: object

<a id="tab-pane_ADDED_fields_ipam_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_ipam_anyOf_i1)

- Type: null

<a id="headingADDED_fields_labels"></a>
<a id="ADDED_fields_labels"></a>
##### labels (required)

- Schema name: `Labels`

Metadata labels attached to the network or `null`.
<a id="ADDED_fields_labels_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_labels_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_labels_anyOf_i0)

- Type: object

<a id="tab-pane_ADDED_fields_labels_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_labels_anyOf_i1)

- Type: null

<a id="headingADDED_fields_created"></a>
<a id="ADDED_fields_created"></a>
##### created (required)

- Schema name: `Created`

Timestamp when the network was created or `null`.
<a id="ADDED_fields_created_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_created_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_created_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_created_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_created_anyOf_i1)

- Type: null

<a id="headingADDED_fields_driver"></a>
<a id="ADDED_fields_driver"></a>
##### driver (required)

- Schema name: `Driver`

Network driver type (bridge, host, overlay, etc.) or `null`.
<a id="ADDED_fields_driver_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_driver_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_driver_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_driver_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_driver_anyOf_i1)

- Type: null

<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`

Full network identifier or `null`.
<a id="ADDED_fields_id_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_id_anyOf_i1)

- Type: null

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`

Human-readable name of the network or `null`.
<a id="ADDED_fields_name_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_name_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_name_anyOf_i1)

- Type: null

<a id="headingADDED_fields_scope"></a>
<a id="ADDED_fields_scope"></a>
##### scope (required)

- Schema name: `Scope`

Network scope (local, global, swarm) or `null`.
<a id="ADDED_fields_scope_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_scope_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_scope_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_scope_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_scope_anyOf_i1)

- Type: null

<a id="headingADDED_fields_short_id"></a>
<a id="ADDED_fields_short_id"></a>
##### short_id (required)

- Schema name: `Short Id`

Shortened network identifier or `null`.
<a id="ADDED_fields_short_id_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_short_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_short_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_short_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_short_id_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `DockerNetworkChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
<a id="CHANGED_id_anyOf"></a>
##### Any of

<a id="tab-pane_CHANGED_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_id_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `DockerNetworkEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_ipam"></a>
<a id="CHANGED_fields_ipam"></a>
##### ipam (required)

- Schema name: `Ipam`

IP Address Management configuration for the network or `null`.
<a id="CHANGED_fields_ipam_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_ipam_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_ipam_anyOf_i0)

- Type: object

<a id="tab-pane_CHANGED_fields_ipam_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_ipam_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_labels"></a>
<a id="CHANGED_fields_labels"></a>
##### labels (required)

- Schema name: `Labels`

Metadata labels attached to the network or `null`.
<a id="CHANGED_fields_labels_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_labels_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_labels_anyOf_i0)

- Type: object

<a id="tab-pane_CHANGED_fields_labels_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_labels_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_created"></a>
<a id="CHANGED_fields_created"></a>
##### created (required)

- Schema name: `Created`

Timestamp when the network was created or `null`.
<a id="CHANGED_fields_created_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_created_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_created_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_created_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_created_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_driver"></a>
<a id="CHANGED_fields_driver"></a>
##### driver (required)

- Schema name: `Driver`

Network driver type (bridge, host, overlay, etc.) or `null`.
<a id="CHANGED_fields_driver_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_driver_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_driver_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_driver_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_driver_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`

Full network identifier or `null`.
<a id="CHANGED_fields_id_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_id_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`

Human-readable name of the network or `null`.
<a id="CHANGED_fields_name_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_name_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_name_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_scope"></a>
<a id="CHANGED_fields_scope"></a>
##### scope (required)

- Schema name: `Scope`

Network scope (local, global, swarm) or `null`.
<a id="CHANGED_fields_scope_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_scope_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_scope_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_scope_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_scope_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_short_id"></a>
<a id="CHANGED_fields_short_id"></a>
##### short_id (required)

- Schema name: `Short Id`

Shortened network identifier or `null`.
<a id="CHANGED_fields_short_id_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_short_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_short_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_short_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_short_id_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `DockerNetworkRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
<a id="REMOVED_id_anyOf"></a>
##### Any of

<a id="tab-pane_REMOVED_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_REMOVED_id_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_REMOVED_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_REMOVED_id_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
