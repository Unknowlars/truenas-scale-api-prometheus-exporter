---
title: fcport.port_choices
kind: method
source_rst: _sources/api_methods_fcport.port_choices.rst.txt
source_html: api_methods_fcport.port_choices.html
required_roles:
  - READONLY_ADMIN
  - SHARING_ISCSI_TARGET_READ
---

# fcport.port_choices

## Required Roles

- `READONLY_ADMIN`
- `SHARING_ISCSI_TARGET_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: include_used

<a id="Call_parameters_items_i0"></a>
#### include_used

- Schema name: `include_used`
- Type: boolean
- Default: true

Whether to include FC ports that are already in use.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object
Examples:

```json
{
    "fc0": {
        "wwpn": "naa.2100001122334455",
        "wwpn_b": "naa.210000AABBCCDDEEFF"
    },
    "fc0/1": {
        "wwpn": "naa.2200001122334455",
        "wwpn_b": "naa.220000AABBCCDDEEFF"
    }
}
```
<a id="headingReturn_value_pattern1"></a>
<a id="Return_value_pattern1"></a>
#### FCPortChoiceEntry

All properties whose name matches the following regular expression must respect the following conditions
- Property name regular expression: `^[a-zA-Z0-9,\-_:]+(/[1-9][0-9]*)?$`
- Schema name: `FCPortChoiceEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_pattern1_wwpn"></a>
<a id="Return_value_pattern1_wwpn"></a>
##### wwpn (required)

- Schema name: `Wwpn`

World Wide Port Name for port A or `null` if not available.
<a id="Return_value_pattern1_wwpn_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_pattern1_wwpn_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pattern1_wwpn_anyOf_i0)

- Type: string
- Must match regular expression: `^naa.[0-9a-fA-F]{16}$`

<a id="tab-pane_Return_value_pattern1_wwpn_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pattern1_wwpn_anyOf_i1)

- Type: null

<a id="headingReturn_value_pattern1_wwpn_b"></a>
<a id="Return_value_pattern1_wwpn_b"></a>
##### wwpn_b (required)

- Schema name: `Wwpn B`

World Wide Port Name for port B or `null` if not available.
<a id="Return_value_pattern1_wwpn_b_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_pattern1_wwpn_b_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pattern1_wwpn_b_anyOf_i0)

- Type: string
- Must match regular expression: `^naa.[0-9a-fA-F]{16}$`

<a id="tab-pane_Return_value_pattern1_wwpn_b_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pattern1_wwpn_b_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
