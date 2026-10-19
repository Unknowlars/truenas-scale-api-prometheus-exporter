---
title: alert.list_categories
kind: method
source_rst: _sources/api_methods_alert.list_categories.rst.txt
source_html: api_methods_alert.list_categories.html
required_roles:
  - ALERT_LIST_READ
---

# alert.list_categories

## Summary

List all types of alerts which the system can issue.

## Required Roles

- `ALERT_LIST_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

<a id="Call_parameters_items_i0"></a>
#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "include_all_products": false,
  "include_hidden_classes": false
}
```

List options.
- No Additional Properties
<a id="headingCall_parameters_items_i0_include_all_products"></a>
<a id="Call_parameters_items_i0_include_all_products"></a>
##### include_all_products

- Schema name: `Include All Products`
- Type: boolean
- Default: false

Include every alert class, including those that do not apply to this system's hardware or license.

<a id="headingCall_parameters_items_i0_include_hidden_classes"></a>
<a id="Call_parameters_items_i0_include_hidden_classes"></a>
##### include_hidden_classes

- Schema name: `Include Hidden Classes`
- Type: boolean
- Default: false

Include hidden alert classes.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of available alert categories and their classes.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### AlertCategory

- Schema name: `AlertCategory`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_id"></a>
<a id="Return_value_items_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the alert category.

<a id="headingReturn_value_items_title"></a>
<a id="Return_value_items_title"></a>
##### title (required)

- Schema name: `Title`
- Type: string

Human-readable title for the alert category.

<a id="headingReturn_value_items_classes"></a>
<a id="Return_value_items_classes"></a>
##### classes (required)

- Schema name: `Classes`
- Type: array of object

Array of alert classes within this category.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_classes_items"></a>
###### AlertCategoryClass

- Schema name: `AlertCategoryClass`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_classes_items_id"></a>
<a id="Return_value_items_classes_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the alert class.

<a id="headingReturn_value_items_classes_items_title"></a>
<a id="Return_value_items_classes_items_title"></a>
###### title (required)

- Schema name: `Title`
- Type: string

Human-readable title for the alert class.

<a id="headingReturn_value_items_classes_items_level"></a>
<a id="Return_value_items_classes_items_level"></a>
###### level (required)

- Schema name: `Level`
- Type: string

Default severity level for alerts in this class.

<a id="headingReturn_value_items_classes_items_proactive_support"></a>
<a id="Return_value_items_classes_items_proactive_support"></a>
###### proactive_support (required)

- Schema name: `Proactive Support`
- Type: boolean

Whether this alert class is included in proactive support monitoring.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
