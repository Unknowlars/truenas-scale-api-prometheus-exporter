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

Provide the type and status of the currently-enabled directory service

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `DirectoryServicesStatusResult`
- Type: object

DirectoryServicesStatusResult return fields.
- No Additional Properties
#### type (required)

- Schema name: `Type`

The type of enabled directory service.
##### Any of

###### Option 1

- Type: enum (of string)

###### Option 2

- Type: null

#### status

- Schema name: `Status`
- Default: null

This field shows the directory service status from the last health check. The status is null if directory services are disabled.
##### Any of

###### Option 1

- Type: enum (of string)

###### Option 2

- Type: null

#### status_msg

- Schema name: `Status Msg`
- Default: null

This field shows the reason why the directory service is FAULTED after a failed health check. If the directory service is not faulted, the field is null.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
