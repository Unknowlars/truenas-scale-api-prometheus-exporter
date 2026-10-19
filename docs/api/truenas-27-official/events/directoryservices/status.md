---
title: directoryservices.status
kind: event
source_rst: _sources/api_events_directoryservices.status.rst.txt
source_html: api_events_directoryservices.status.html
required_roles:
  - DIRECTORY_SERVICE_READ
---

# directoryservices.status

## Summary

Sent on directory service state changes.

## Required Roles

- `DIRECTORY_SERVICE_READ`

## Schema

- Type: object

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `DirectoryServicesStatusChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `DirectoryServicesStatus`
- Type: object

Event fields.
- No Additional Properties
<a id="headingCHANGED_fields_type"></a>
<a id="CHANGED_fields_type"></a>
##### type (required)

- Schema name: `Type`

The type of enabled directory service.
<a id="CHANGED_fields_type_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_type_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "ACTIVEDIRECTORY"
- "IPA"
- "LDAP"

<a id="tab-pane_CHANGED_fields_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_type_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_status"></a>
<a id="CHANGED_fields_status"></a>
##### status

- Schema name: `Status`
- Default: null

This field shows the directory service status from the last health check. The status is null if directory services are disabled.
<a id="CHANGED_fields_status_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_status_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "DISABLED"
- "FAULTED"
- "LEAVING"
- "JOINING"
- "HEALTHY"

<a id="tab-pane_CHANGED_fields_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_status_msg"></a>
<a id="CHANGED_fields_status_msg"></a>
##### status_msg

- Schema name: `Status Msg`
- Default: null

This field shows the reason why the directory service is FAULTED after a failed health check. If the directory service is not faulted, the field is null.
<a id="CHANGED_fields_status_msg_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_msg_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_status_msg_anyOf_i0)

- Type: string
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_CHANGED_fields_status_msg_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_msg_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
