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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `StatusResult`
- Type: object

Current Docker service status information.
- No Additional Properties
#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the current Docker service status.

#### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current state of the Docker service.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
