---
title: system.reboot.info
kind: event
source_rst: _sources/api_events_system.reboot.info.rst.txt
source_html: api_events_system.reboot.info.html
required_roles:
  - SYSTEM_GENERAL_READ
---

# system.reboot.info

## Summary

Sent when a system reboot is required.

## Required Roles

- `SYSTEM_GENERAL_READ`

## Schema

- Type: object

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `SystemRebootInfoChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: null

Always `null`.

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `RebootInfo`
- Type: object

Event fields.
- No Additional Properties
<a id="headingCHANGED_fields_boot_id"></a>
<a id="CHANGED_fields_boot_id"></a>
##### boot_id (required)

- Schema name: `Boot Id`
- Type: string

Unique identifier for the current boot session.

<a id="headingCHANGED_fields_reboot_required_reasons"></a>
<a id="CHANGED_fields_reboot_required_reasons"></a>
##### reboot_required_reasons (required)

- Schema name: `Reboot Required Reasons`
- Type: array of object

Array of reasons why a system reboot is required.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_reboot_required_reasons_items"></a>
###### RebootRequiredReason

- Schema name: `RebootRequiredReason`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_reboot_required_reasons_items_code"></a>
<a id="CHANGED_fields_reboot_required_reasons_items_code"></a>
###### code (required)

- Schema name: `Code`
- Type: string

Code identifying the reason for required reboot.

<a id="headingCHANGED_fields_reboot_required_reasons_items_reason"></a>
<a id="CHANGED_fields_reboot_required_reasons_items_reason"></a>
###### reason (required)

- Schema name: `Reason`
- Type: string

Human-readable description of why a reboot is required.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
