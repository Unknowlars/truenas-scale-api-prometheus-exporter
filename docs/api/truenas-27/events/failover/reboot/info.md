---
title: failover.reboot.info
kind: event
source_rst: _sources/api_events_failover.reboot.info.rst.txt
source_html: api_events_failover.reboot.info.html
required_roles:
  - FAILOVER_READ
---

# failover.reboot.info

## Summary

Sent when a system reboot is required.

## Required Roles

- `FAILOVER_READ`

## Schema

- Type: object

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `FailoverRebootInfoChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: null

Always null.

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `FailoverRebootInfo`
- Type: object

Event fields.
- No Additional Properties
<a id="headingCHANGED_fields_this_node"></a>
<a id="CHANGED_fields_this_node"></a>
##### this_node (required)

- Schema name: `RebootInfo`
- Type: object

Reboot information for the current node.
- No Additional Properties
<a id="headingCHANGED_fields_this_node_boot_id"></a>
<a id="CHANGED_fields_this_node_boot_id"></a>
###### boot_id (required)

- Schema name: `Boot Id`
- Type: string

Unique identifier for the current boot session.

<a id="headingCHANGED_fields_this_node_reboot_required_reasons"></a>
<a id="CHANGED_fields_this_node_reboot_required_reasons"></a>
###### reboot_required_reasons (required)

- Schema name: `Reboot Required Reasons`
- Type: array of object

Array of reasons why a system reboot is required.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_this_node_reboot_required_reasons_items"></a>
###### RebootRequiredReason

- Schema name: `RebootRequiredReason`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_this_node_reboot_required_reasons_items_code"></a>
<a id="CHANGED_fields_this_node_reboot_required_reasons_items_code"></a>
###### code (required)

- Schema name: `Code`
- Type: string

Code identifying the reason for required reboot.

<a id="headingCHANGED_fields_this_node_reboot_required_reasons_items_reason"></a>
<a id="CHANGED_fields_this_node_reboot_required_reasons_items_reason"></a>
###### reason (required)

- Schema name: `Reason`
- Type: string

Human-readable description of why a reboot is required.

<a id="headingCHANGED_fields_other_node"></a>
<a id="CHANGED_fields_other_node"></a>
##### other_node (required)

Reboot information for the other node in the failover pair or `null` if not available.
<a id="CHANGED_fields_other_node_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_other_node_anyOf_i0"></a>
###### [RebootInfo](#tab-pane_CHANGED_fields_other_node_anyOf_i0)

- Schema name: `RebootInfo`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_other_node_anyOf_i0_boot_id"></a>
<a id="CHANGED_fields_other_node_anyOf_i0_boot_id"></a>
###### boot_id (required)

- Schema name: `Boot Id`
- Type: string

Unique identifier for the current boot session.

<a id="headingCHANGED_fields_other_node_anyOf_i0_reboot_required_reasons"></a>
<a id="CHANGED_fields_other_node_anyOf_i0_reboot_required_reasons"></a>
###### reboot_required_reasons (required)

- Schema name: `Reboot Required Reasons`
- Type: array

Array of reasons why a system reboot is required.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_other_node_anyOf_i0_reboot_required_reasons_items"></a>
- Type: object

<a id="tab-pane_CHANGED_fields_other_node_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_other_node_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
