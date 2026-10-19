---
title: docker.status
kind: method
source_rst: _sources/api_methods_docker.status.rst.txt
source_html: api_methods_docker.status.html
required_roles:
  - DOCKER_READ
---

# docker.status

## Summary

Returns the status of the docker service.

## Required Roles

- `DOCKER_READ`

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

- Schema name: `StatusResult`
- Type: object

Current Docker service status information.
- No Additional Properties
<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the current Docker service status.

<a id="headingReturn_value_status"></a>
<a id="Return_value_status"></a>
#### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current state of the Docker service.
##### Must be one of:

- "PENDING"
- "RUNNING"
- "STOPPED"
- "INITIALIZING"
- "STOPPING"
- "UNCONFIGURED"
- "FAILED"
- "MIGRATING"
- "MIGRATION_FAILED"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
