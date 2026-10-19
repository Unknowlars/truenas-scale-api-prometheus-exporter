---
title: iscsi.target.validate_name
kind: method
source_rst: _sources/api_methods_iscsi.target.validate_name.rst.txt
source_html: api_methods_iscsi.target.validate_name.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# iscsi.target.validate_name

## Summary

Returns validation error for iSCSI target name :param name: name to be validated :param existing_id: id of an existing iSCSI target that will receive this name (or `None` if a new target is being created) :return: error message (or `None` if there is no error)

## Required Roles

- `SHARING_ISCSI_TARGET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: name

<a id="Call_parameters_items_i0"></a>
#### name

- Schema name: `name`
- Type: string

Target name to validate.

#### Parameter 2: existing_id

<a id="Call_parameters_items_i1"></a>
#### existing_id

- Schema name: `existing_id`
- Default: null

ID of existing target to exclude from validation or `null` for new targets.
<a id="Call_parameters_items_i1_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

Error message if name is invalid or `null` if name is valid.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
