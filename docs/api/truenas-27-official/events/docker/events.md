---
title: docker.events
kind: event
source_rst: _sources/api_events_docker.events.rst.txt
source_html: api_events_docker.events.html
required_roles:
  - DOCKER_READ
---

# docker.events

## Summary

Docker container events

## Required Roles

- `DOCKER_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `DockerEventsAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

App name.

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `Fields`
- Type: object

Event fields.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
