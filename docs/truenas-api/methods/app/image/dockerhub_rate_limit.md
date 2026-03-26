---
title: app.image.dockerhub_rate_limit
kind: method
source_rst: _sources/api_methods_app.image.dockerhub_rate_limit.rst.txt
source_html: api_methods_app.image.dockerhub_rate_limit.html
required_roles:
  - APPS_READ
---

# app.image.dockerhub_rate_limit

## Summary

Returns the current rate limit information for Docker Hub registry.

Please refer to https://docs.docker.com/docker-hub/download-rate-limit/ for more information.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `ContainerImagesDockerhubRateLimitResult`
- Type: object

ContainerImagesDockerhubRateLimitResult return fields.
- No Additional Properties
#### total_pull_limit

- Schema name: `Total Pull Limit`
- Default: null

Total pull limit for Docker Hub registry.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### total_time_limit_in_secs

- Schema name: `Total Time Limit In Secs`
- Default: null

Total time limit in seconds for Docker Hub registry before the limit renews.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### remaining_pull_limit

- Schema name: `Remaining Pull Limit`
- Default: null

Remaining pull limit for Docker Hub registry.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### remaining_time_limit_in_secs

- Schema name: `Remaining Time Limit In Secs`
- Default: null

Remaining time limit in seconds for Docker Hub registry for the current pull limit to be renewed.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### error

- Schema name: `Error`
- Default: null

Error message if rate limit information could not be retrieved or `null` on success.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
