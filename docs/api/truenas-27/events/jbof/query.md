---
title: jbof.query
kind: event
source_rst: _sources/api_events_jbof.query.rst.txt
source_html: api_events_jbof.query.html
required_roles:
  - JBOF_READ
---

# jbof.query

## Summary

Sent on jbof changes.

## Required Roles

- `JBOF_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `JBOFAddedEvent`
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

- Schema name: `JBOFEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the JBOF configuration.

<a id="headingADDED_fields_description"></a>
<a id="ADDED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string

Optional description of the JBOF.

<a id="headingADDED_fields_mgmt_ip1"></a>
<a id="ADDED_fields_mgmt_ip1"></a>
##### mgmt_ip1 (required)

- Schema name: `Mgmt Ip1`

IP of first Redfish management interface.
<a id="ADDED_fields_mgmt_ip1_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_mgmt_ip1_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_mgmt_ip1_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_ADDED_fields_mgmt_ip1_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_mgmt_ip1_anyOf_i1)

- Type: string

<a id="headingADDED_fields_mgmt_ip2"></a>
<a id="ADDED_fields_mgmt_ip2"></a>
##### mgmt_ip2

- Schema name: `Mgmt Ip2`

Optional IP of second Redfish management interface.
<a id="ADDED_fields_mgmt_ip2_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_mgmt_ip2_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_mgmt_ip2_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_ADDED_fields_mgmt_ip2_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_mgmt_ip2_anyOf_i1)

- Type: string

<a id="headingADDED_fields_mgmt_username"></a>
<a id="ADDED_fields_mgmt_username"></a>
##### mgmt_username (required)

- Schema name: `Mgmt Username`
- Type: string

Redfish administrative username.

<a id="headingADDED_fields_mgmt_password"></a>
<a id="ADDED_fields_mgmt_password"></a>
##### mgmt_password (required)

- Schema name: `Mgmt Password`
- Type: string

Redfish administrative password.

<a id="headingADDED_fields_index"></a>
<a id="ADDED_fields_index"></a>
##### index (required)

- Schema name: `Index`
- Type: integer

Index of the JBOF. Used to determine data plane IP addresses.

<a id="headingADDED_fields_uuid"></a>
<a id="ADDED_fields_uuid"></a>
##### uuid (required)

- Schema name: `Uuid`
- Type: string

UUID of the JBOF as reported by the enclosure firmware.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `JBOFChangedEvent`
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

- Schema name: `JBOFEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the JBOF configuration.

<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string

Optional description of the JBOF.

<a id="headingCHANGED_fields_mgmt_ip1"></a>
<a id="CHANGED_fields_mgmt_ip1"></a>
##### mgmt_ip1 (required)

- Schema name: `Mgmt Ip1`

IP of first Redfish management interface.
<a id="CHANGED_fields_mgmt_ip1_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_mgmt_ip1_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_mgmt_ip1_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_CHANGED_fields_mgmt_ip1_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_mgmt_ip1_anyOf_i1)

- Type: string

<a id="headingCHANGED_fields_mgmt_ip2"></a>
<a id="CHANGED_fields_mgmt_ip2"></a>
##### mgmt_ip2

- Schema name: `Mgmt Ip2`

Optional IP of second Redfish management interface.
<a id="CHANGED_fields_mgmt_ip2_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_mgmt_ip2_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_mgmt_ip2_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_CHANGED_fields_mgmt_ip2_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_mgmt_ip2_anyOf_i1)

- Type: string

<a id="headingCHANGED_fields_mgmt_username"></a>
<a id="CHANGED_fields_mgmt_username"></a>
##### mgmt_username (required)

- Schema name: `Mgmt Username`
- Type: string

Redfish administrative username.

<a id="headingCHANGED_fields_mgmt_password"></a>
<a id="CHANGED_fields_mgmt_password"></a>
##### mgmt_password (required)

- Schema name: `Mgmt Password`
- Type: string

Redfish administrative password.

<a id="headingCHANGED_fields_index"></a>
<a id="CHANGED_fields_index"></a>
##### index (required)

- Schema name: `Index`
- Type: integer

Index of the JBOF. Used to determine data plane IP addresses.

<a id="headingCHANGED_fields_uuid"></a>
<a id="CHANGED_fields_uuid"></a>
##### uuid (required)

- Schema name: `Uuid`
- Type: string

UUID of the JBOF as reported by the enclosure firmware.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `JBOFRemovedEvent`
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
