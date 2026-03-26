---
title: system.reboot.info
kind: method
source_rst: _sources/api_methods_system.reboot.info.rst.txt
source_html: api_methods_system.reboot.info.html
required_roles:
  - SYSTEM_GENERAL_READ
---

# system.reboot.info

## Required Roles

- `SYSTEM_GENERAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `RebootInfo`
- Type: object

Information about the current boot session and reboot requirements.
- No Additional Properties
#### boot_id (required)

- Schema name: `Boot Id`
- Type: string

Unique identifier for the current boot session.

#### reboot_required_reasons (required)

- Schema name: `Reboot Required Reasons`
- Type: array of object

Array of reasons why a system reboot is required.
- No Additional Items

##### Each item of this array must be:

##### RebootRequiredReason

- Schema name: `RebootRequiredReason`
- Type: object
- No Additional Properties
###### code (required)

- Schema name: `Code`
- Type: string

Code identifying the reason for required reboot.

###### reason (required)

- Schema name: `Reason`
- Type: string

Human-readable description of why a reboot is required.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
