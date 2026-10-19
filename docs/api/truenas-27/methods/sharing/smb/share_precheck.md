---
title: sharing.smb.share_precheck
kind: method
source_rst: _sources/api_methods_sharing.smb.share_precheck.rst.txt
source_html: api_methods_sharing.smb.share_precheck.html
required_roles:
  - READONLY_ADMIN
---

# sharing.smb.share_precheck

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: smb_share_precheck

<a id="Call_parameters_items_i0"></a>
#### smb_share_precheck

- Schema name: `smb_share_precheck`
- Type: object

SharingSMBSharePrecheckArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name

- Schema name: `Name`
- Default: null

Name of the SMB share to validate (optional).
<a id="Call_parameters_items_i0_name_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_name_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_name_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the SMB share configuration passes validation checks.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
