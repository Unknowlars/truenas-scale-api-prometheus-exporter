---
title: directoryservices.status
kind: method
source_rst: _sources/api_methods_directoryservices.status.rst.txt
source_html: api_methods_directoryservices.status.html
required_roles:
  []
---

# directoryservices.status

## Summary

Provide the type and status of the currently-enabled directory service.

## Required Roles

- None documented.

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

- Schema name: `DirectoryServicesStatus`
- Type: object
- No Additional Properties
<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type (required)

- Schema name: `Type`

The type of enabled directory service.
<a id="Return_value_type_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_type_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "ACTIVEDIRECTORY"
- "IPA"
- "LDAP"

<a id="tab-pane_Return_value_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_status"></a>
<a id="Return_value_status"></a>
#### status

- Schema name: `Status`
- Default: null

This field shows the directory service status from the last health check. The status is null if directory services are disabled.
<a id="Return_value_status_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_status_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_status_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "DISABLED"
- "FAULTED"
- "LEAVING"
- "JOINING"
- "HEALTHY"

<a id="tab-pane_Return_value_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_status_anyOf_i1)

- Type: null

<a id="headingReturn_value_status_msg"></a>
<a id="Return_value_status_msg"></a>
#### status_msg

- Schema name: `Status Msg`
- Default: null

This field shows the reason why the directory service is FAULTED after a failed health check. If the directory service is not faulted, the field is null.
<a id="Return_value_status_msg_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_status_msg_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_status_msg_anyOf_i0)

- Type: string
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_status_msg_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_status_msg_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
