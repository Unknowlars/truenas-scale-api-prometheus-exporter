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

JBOF configuration data for creation.
- No Additional Properties
<a id="headingCall_parameters_items_i0_description"></a>
<a id="Call_parameters_items_i0_description"></a>
##### description

- Schema name: `Description`
- Type: string

Optional description of the JBOF.

<a id="headingCall_parameters_items_i0_mgmt_ip1"></a>
<a id="Call_parameters_items_i0_mgmt_ip1"></a>
##### mgmt_ip1 (required)

- Schema name: `Mgmt Ip1`

IP of first Redfish management interface.
<a id="Call_parameters_items_i0_mgmt_ip1_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_mgmt_ip1_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_mgmt_ip1_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Call_parameters_items_i0_mgmt_ip1_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_mgmt_ip1_anyOf_i1)

- Type: string

<a id="headingCall_parameters_items_i0_mgmt_ip2"></a>
<a id="Call_parameters_items_i0_mgmt_ip2"></a>
##### mgmt_ip2

- Schema name: `Mgmt Ip2`

Optional IP of second Redfish management interface.
<a id="Call_parameters_items_i0_mgmt_ip2_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_mgmt_ip2_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_mgmt_ip2_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Call_parameters_items_i0_mgmt_ip2_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_mgmt_ip2_anyOf_i1)

- Type: string

<a id="headingCall_parameters_items_i0_mgmt_username"></a>
<a id="Call_parameters_items_i0_mgmt_username"></a>
##### mgmt_username (required)

- Schema name: `Mgmt Username`
- Type: string

Redfish administrative username.

<a id="headingCall_parameters_items_i0_mgmt_password"></a>
<a id="Call_parameters_items_i0_mgmt_password"></a>
##### mgmt_password (required)

- Schema name: `Mgmt Password`
- Type: string

Redfish administrative password.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `JBOFEntry`
- Type: object

The created JBOF configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the JBOF configuration.

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description

- Schema name: `Description`
- Type: string

Optional description of the JBOF.

<a id="headingReturn_value_mgmt_ip1"></a>
<a id="Return_value_mgmt_ip1"></a>
#### mgmt_ip1 (required)

- Schema name: `Mgmt Ip1`

IP of first Redfish management interface.
<a id="Return_value_mgmt_ip1_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_mgmt_ip1_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_mgmt_ip1_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_mgmt_ip1_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_mgmt_ip1_anyOf_i1)

- Type: string

<a id="headingReturn_value_mgmt_ip2"></a>
<a id="Return_value_mgmt_ip2"></a>
#### mgmt_ip2

- Schema name: `Mgmt Ip2`

Optional IP of second Redfish management interface.
<a id="Return_value_mgmt_ip2_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_mgmt_ip2_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_mgmt_ip2_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_mgmt_ip2_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_mgmt_ip2_anyOf_i1)

- Type: string

<a id="headingReturn_value_mgmt_username"></a>
<a id="Return_value_mgmt_username"></a>
#### mgmt_username (required)

- Schema name: `Mgmt Username`
- Type: string

Redfish administrative username.

<a id="headingReturn_value_mgmt_password"></a>
<a id="Return_value_mgmt_password"></a>
#### mgmt_password (required)

- Schema name: `Mgmt Password`
- Type: string

Redfish administrative password.

<a id="headingReturn_value_index"></a>
<a id="Return_value_index"></a>
#### index (required)

- Schema name: `Index`
- Type: integer

Index of the JBOF. Used to determine data plane IP addresses.

<a id="headingReturn_value_uuid"></a>
<a id="Return_value_uuid"></a>
#### uuid (required)

- Schema name: `Uuid`
- Type: string

UUID of the JBOF as reported by the enclosure firmware.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
