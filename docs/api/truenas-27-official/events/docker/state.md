---
title: docker.state
kind: event
source_rst: _sources/api_events_docker.state.rst.txt
source_html: api_events_docker.state.html
required_roles:
  - DOCKER_READ
---

# docker.state

## Summary

Docker state events

## Required Roles

- `DOCKER_READ`

## Schema

- Type: object

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `DockerStateChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `DockerStatusInfo`
- Type: object

Event fields.
- No Additional Properties
<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the current Docker service status.

<a id="headingCHANGED_fields_status"></a>
<a id="CHANGED_fields_status"></a>
##### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current state of the Docker service.
###### Must be one of:

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
