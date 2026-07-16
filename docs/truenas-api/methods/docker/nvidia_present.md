---
title: docker.nvidia_present
kind: method
source_rst: _sources/api_methods_docker.nvidia_present.rst.txt
source_html: api_methods_docker.nvidia_present.html
required_roles:
  - DOCKER_READ
---

# docker.nvidia_present

## Required Roles

- `DOCKER_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if NVIDIA GPU hardware is present and supported, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
