---
title: failover.reboot.info
kind: method
source_rst: _sources/api_methods_failover.reboot.info.rst.txt
source_html: api_methods_failover.reboot.info.html
required_roles:
  - FAILOVER_READ
---

# failover.reboot.info

## Required Roles

- `FAILOVER_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `FailoverRebootInfoResult`
- Type: object

FailoverRebootInfoResult return fields.
- No Additional Properties
#### this_node (required)

- Schema name: `RebootInfo`
- Type: object

Reboot information for the current node.
- No Additional Properties
##### boot_id (required)

- Schema name: `Boot Id`
- Type: string

Unique identifier for the current boot session.

##### reboot_required_reasons (required)

- Schema name: `Reboot Required Reasons`
- Type: array of object

Array of reasons why a system reboot is required.
- No Additional Items

###### Each item of this array must be:

###### RebootRequiredReason

- Schema name: `RebootRequiredReason`
- Type: object
- No Additional Properties
####### code (required)

- Schema name: `Code`
- Type: string

Code identifying the reason for required reboot.

####### reason (required)

- Schema name: `Reason`
- Type: string

Human-readable description of why a reboot is required.

#### other_node (required)

Reboot information for the other node in the failover pair or `null` if not available.
##### Any of

###### RebootInfo

- Schema name: `RebootInfo`
- Type: object
- No Additional Properties
####### boot_id (required)

- Schema name: `Boot Id`
- Type: string

Unique identifier for the current boot session.

####### reboot_required_reasons (required)

- Schema name: `Reboot Required Reasons`
- Type: array

Array of reasons why a system reboot is required.
- No Additional Items

######## Each item of this array must be:

- Type: object

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
