---
title: app.outdated_docker_images
kind: method
source_rst: _sources/api_methods_app.outdated_docker_images.rst.txt
source_html: api_methods_app.outdated_docker_images.html
required_roles:
  - APPS_READ
---

# app.outdated_docker_images

## Summary

Returns a list of outdated docker images for the specified app `name`.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: app_name

#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to check for outdated Docker images.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: array of string

Array of Docker image names that have updates available.
- No Additional Items

#### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
