---
title: boot.environment.query
kind: event
source_rst: _sources/api_events_boot.environment.query.rst.txt
source_html: api_events_boot.environment.query.html
required_roles:
  - BOOT_ENV_READ
---

# boot.environment.query

## Summary

Sent on boot.environment changes.

## Required Roles

- `BOOT_ENV_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `BootEnvironmentAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `BootEnvironmentEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

The name of the boot environment referenced by the boot environment tool.
- Must be at least `1` characters long

<a id="headingADDED_fields_dataset"></a>
<a id="ADDED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

The name of the zfs dataset that represents the boot environment.
- Must be at least `1` characters long

<a id="headingADDED_fields_active"></a>
<a id="ADDED_fields_active"></a>
##### active (required)

- Schema name: `Active`
- Type: boolean

This is the currently running boot environment.

<a id="headingADDED_fields_activated"></a>
<a id="ADDED_fields_activated"></a>
##### activated (required)

- Schema name: `Activated`
- Type: boolean

Use this boot environment on next boot.

<a id="headingADDED_fields_created"></a>
<a id="ADDED_fields_created"></a>
##### created (required)

- Schema name: `Created`
- Type: string
- Type: Format: date-time

The date when the boot environment was created.

<a id="headingADDED_fields_used_bytes"></a>
<a id="ADDED_fields_used_bytes"></a>
##### used_bytes (required)

- Schema name: `Used Bytes`
- Type: integer

The total amount of bytes used by the boot environment.

<a id="headingADDED_fields_used"></a>
<a id="ADDED_fields_used"></a>
##### used (required)

- Schema name: `Used`
- Type: string

The boot environment's used space in human readable format.
- Must be at least `1` characters long

<a id="headingADDED_fields_keep"></a>
<a id="ADDED_fields_keep"></a>
##### keep (required)

- Schema name: `Keep`
- Type: boolean

When set to false, this makes the boot environment subject to automatic deletion if the TrueNAS updater needs space for an update. Otherwise, the updater will not delete this boot environment if it is set to true.

<a id="headingADDED_fields_can_activate"></a>
<a id="ADDED_fields_can_activate"></a>
##### can_activate (required)

- Schema name: `Can Activate`
- Type: boolean

The given boot environment may be activated.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `BootEnvironmentChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `BootEnvironmentEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

The name of the boot environment referenced by the boot environment tool.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_dataset"></a>
<a id="CHANGED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

The name of the zfs dataset that represents the boot environment.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_active"></a>
<a id="CHANGED_fields_active"></a>
##### active (required)

- Schema name: `Active`
- Type: boolean

This is the currently running boot environment.

<a id="headingCHANGED_fields_activated"></a>
<a id="CHANGED_fields_activated"></a>
##### activated (required)

- Schema name: `Activated`
- Type: boolean

Use this boot environment on next boot.

<a id="headingCHANGED_fields_created"></a>
<a id="CHANGED_fields_created"></a>
##### created (required)

- Schema name: `Created`
- Type: string
- Type: Format: date-time

The date when the boot environment was created.

<a id="headingCHANGED_fields_used_bytes"></a>
<a id="CHANGED_fields_used_bytes"></a>
##### used_bytes (required)

- Schema name: `Used Bytes`
- Type: integer

The total amount of bytes used by the boot environment.

<a id="headingCHANGED_fields_used"></a>
<a id="CHANGED_fields_used"></a>
##### used (required)

- Schema name: `Used`
- Type: string

The boot environment's used space in human readable format.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_keep"></a>
<a id="CHANGED_fields_keep"></a>
##### keep (required)

- Schema name: `Keep`
- Type: boolean

When set to false, this makes the boot environment subject to automatic deletion if the TrueNAS updater needs space for an update. Otherwise, the updater will not delete this boot environment if it is set to true.

<a id="headingCHANGED_fields_can_activate"></a>
<a id="CHANGED_fields_can_activate"></a>
##### can_activate (required)

- Schema name: `Can Activate`
- Type: boolean

The given boot environment may be activated.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `BootEnvironmentRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
