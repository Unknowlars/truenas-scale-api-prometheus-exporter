---
title: failover.reboot.info
kind: method
source_rst: _sources/api_methods_failover.reboot.info.rst.txt
source_html: api_methods_failover.reboot.info.html
required_roles:
  - FAILOVER_READ
---

# failover.reboot.info

## Summary

Return reboot information for both nodes of the failover pair.

The response reports, for the local node and for the other node, whether a reboot is required and the reasons for it. The `other_node` field is `null` when the remote node cannot be reached.

## Required Roles

- `FAILOVER_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `FailoverRebootInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_this_node"></a>
<a id="Return_value_this_node"></a>
#### this_node (required)

- Schema name: `RebootInfo`
- Type: object

Reboot information for the current node.
- No Additional Properties
<a id="headingReturn_value_this_node_boot_id"></a>
<a id="Return_value_this_node_boot_id"></a>
##### boot_id (required)

- Schema name: `Boot Id`
- Type: string

Unique identifier for the current boot session.

<a id="headingReturn_value_this_node_reboot_required_reasons"></a>
<a id="Return_value_this_node_reboot_required_reasons"></a>
##### reboot_required_reasons (required)

- Schema name: `Reboot Required Reasons`
- Type: array of object

Array of reasons why a system reboot is required.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_this_node_reboot_required_reasons_items"></a>
###### RebootRequiredReason

- Schema name: `RebootRequiredReason`
- Type: object
- No Additional Properties
<a id="headingReturn_value_this_node_reboot_required_reasons_items_code"></a>
<a id="Return_value_this_node_reboot_required_reasons_items_code"></a>
###### code (required)

- Schema name: `Code`
- Type: string

Code identifying the reason for required reboot.

<a id="headingReturn_value_this_node_reboot_required_reasons_items_reason"></a>
<a id="Return_value_this_node_reboot_required_reasons_items_reason"></a>
###### reason (required)

- Schema name: `Reason`
- Type: string

Human-readable description of why a reboot is required.

<a id="headingReturn_value_other_node"></a>
<a id="Return_value_other_node"></a>
#### other_node (required)

Reboot information for the other node in the failover pair or `null` if not available.
<a id="Return_value_other_node_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_other_node_anyOf_i0"></a>
###### [RebootInfo](#tab-pane_Return_value_other_node_anyOf_i0)

- Schema name: `RebootInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_other_node_anyOf_i0_boot_id"></a>
<a id="Return_value_other_node_anyOf_i0_boot_id"></a>
###### boot_id (required)

- Schema name: `Boot Id`
- Type: string

Unique identifier for the current boot session.

<a id="headingReturn_value_other_node_anyOf_i0_reboot_required_reasons"></a>
<a id="Return_value_other_node_anyOf_i0_reboot_required_reasons"></a>
###### reboot_required_reasons (required)

- Schema name: `Reboot Required Reasons`
- Type: array

Array of reasons why a system reboot is required.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_other_node_anyOf_i0_reboot_required_reasons_items"></a>
- Type: object

<a id="tab-pane_Return_value_other_node_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_other_node_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
