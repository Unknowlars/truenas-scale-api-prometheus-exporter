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

### CHANGED

- Schema name: `DockerStateChangedEvent`
- Type: object
- No Additional Properties
#### fields (required)

- Schema name: `DockerStatusInfo`
- Type: object

Event fields.
- No Additional Properties
##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the current Docker service status.

##### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current state of the Docker service.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
