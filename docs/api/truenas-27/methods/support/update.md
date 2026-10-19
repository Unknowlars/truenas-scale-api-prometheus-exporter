---
title: support.update
kind: method
source_rst: _sources/api_methods_support.update.rst.txt
source_html: api_methods_support.update.html
required_roles:
  - SUPPORT_WRITE
---

# support.update

## Summary

Update Proactive Support settings.

## Required Roles

- `SUPPORT_WRITE`

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

Updated support configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i0_id"></a>
<a id="Call_parameters_items_i0_id"></a>
##### id

- Schema name: `Id`
- Type: integer

Unique identifier for the support configuration.

<a id="headingCall_parameters_items_i0_enabled"></a>
<a id="Call_parameters_items_i0_enabled"></a>
##### enabled

- Schema name: `Enabled`

Whether support is enabled. `null` if not available.
<a id="Call_parameters_items_i0_enabled_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_enabled_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_enabled_anyOf_i0)

- Type: boolean

<a id="tab-pane_Call_parameters_items_i0_enabled_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_enabled_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name

- Schema name: `Name`
- Type: string

Primary contact name for support.

<a id="headingCall_parameters_items_i0_title"></a>
<a id="Call_parameters_items_i0_title"></a>
##### title

- Schema name: `Title`
- Type: string

Primary contact title or role.

<a id="headingCall_parameters_items_i0_email"></a>
<a id="Call_parameters_items_i0_email"></a>
##### email

- Schema name: `Email`
- Type: string

Primary contact email address.

<a id="headingCall_parameters_items_i0_phone"></a>
<a id="Call_parameters_items_i0_phone"></a>
##### phone

- Schema name: `Phone`
- Type: string

Primary contact phone number.

<a id="headingCall_parameters_items_i0_secondary_name"></a>
<a id="Call_parameters_items_i0_secondary_name"></a>
##### secondary_name

- Schema name: `Secondary Name`
- Type: string

Secondary contact name for support.

<a id="headingCall_parameters_items_i0_secondary_title"></a>
<a id="Call_parameters_items_i0_secondary_title"></a>
##### secondary_title

- Schema name: `Secondary Title`
- Type: string

Secondary contact title or role.

<a id="headingCall_parameters_items_i0_secondary_email"></a>
<a id="Call_parameters_items_i0_secondary_email"></a>
##### secondary_email

- Schema name: `Secondary Email`
- Type: string

Secondary contact email address.

<a id="headingCall_parameters_items_i0_secondary_phone"></a>
<a id="Call_parameters_items_i0_secondary_phone"></a>
##### secondary_phone

- Schema name: `Secondary Phone`
- Type: string

Secondary contact phone number.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SupportEntry`
- Type: object

The updated support configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the support configuration.

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled (required)

- Schema name: `Enabled`

Whether support is enabled. `null` if not available.
<a id="Return_value_enabled_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_enabled_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_enabled_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_enabled_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_enabled_anyOf_i1)

- Type: null

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Primary contact name for support.

<a id="headingReturn_value_title"></a>
<a id="Return_value_title"></a>
#### title (required)

- Schema name: `Title`
- Type: string

Primary contact title or role.

<a id="headingReturn_value_email"></a>
<a id="Return_value_email"></a>
#### email (required)

- Schema name: `Email`
- Type: string

Primary contact email address.

<a id="headingReturn_value_phone"></a>
<a id="Return_value_phone"></a>
#### phone (required)

- Schema name: `Phone`
- Type: string

Primary contact phone number.

<a id="headingReturn_value_secondary_name"></a>
<a id="Return_value_secondary_name"></a>
#### secondary_name (required)

- Schema name: `Secondary Name`
- Type: string

Secondary contact name for support.

<a id="headingReturn_value_secondary_title"></a>
<a id="Return_value_secondary_title"></a>
#### secondary_title (required)

- Schema name: `Secondary Title`
- Type: string

Secondary contact title or role.

<a id="headingReturn_value_secondary_email"></a>
<a id="Return_value_secondary_email"></a>
#### secondary_email (required)

- Schema name: `Secondary Email`
- Type: string

Secondary contact email address.

<a id="headingReturn_value_secondary_phone"></a>
<a id="Return_value_secondary_phone"></a>
#### secondary_phone (required)

- Schema name: `Secondary Phone`
- Type: string

Secondary contact phone number.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
