---
title: fcport.port_choices
kind: method
source_rst: _sources/api_methods_fcport.port_choices.rst.txt
source_html: api_methods_fcport.port_choices.html
required_roles:
  - READONLY_ADMIN | SHARING_ISCSI_TARGET_READ
---

# fcport.port_choices

## Required Roles

- `READONLY_ADMIN | SHARING_ISCSI_TARGET_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: include_used

#### include_used

- Schema name: `include_used`
- Type: boolean
- Default: true

Whether to include FC ports that are already in use.

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
#### FCPortChoiceEntry

All properties whose name matches the following regular expression must respect the following conditions
- Schema name: `FCPortChoiceEntry`
- Type: object
- No Additional Properties
##### wwpn (required)

- Schema name: `Wwpn`

World Wide Port Name for port A or `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### wwpn_b (required)

- Schema name: `Wwpn B`

World Wide Port Name for port B or `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
