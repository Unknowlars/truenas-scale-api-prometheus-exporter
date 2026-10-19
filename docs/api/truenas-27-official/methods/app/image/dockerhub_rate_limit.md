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

Returns the current rate-limit information for the Docker Hub registry.

Please refer to https://docs.docker.com/docker-hub/download-rate-limit/ for more information.

## Required Roles

- `APPS_READ`

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

- Schema name: `AppImageDockerhubRateLimitResult`
- Type: object

AppImageDockerhubRateLimitResult return fields.
- No Additional Properties
<a id="headingReturn_value_total_pull_limit"></a>
<a id="Return_value_total_pull_limit"></a>
#### total_pull_limit

- Schema name: `Total Pull Limit`
- Default: null

Total pull limit for Docker Hub registry.
<a id="Return_value_total_pull_limit_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_total_pull_limit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_total_pull_limit_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_total_pull_limit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_total_pull_limit_anyOf_i1)

- Type: null

<a id="headingReturn_value_total_time_limit_in_secs"></a>
<a id="Return_value_total_time_limit_in_secs"></a>
#### total_time_limit_in_secs

- Schema name: `Total Time Limit In Secs`
- Default: null

Total time limit in seconds for Docker Hub registry before the limit renews.
<a id="Return_value_total_time_limit_in_secs_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_total_time_limit_in_secs_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_total_time_limit_in_secs_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_total_time_limit_in_secs_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_total_time_limit_in_secs_anyOf_i1)

- Type: null

<a id="headingReturn_value_remaining_pull_limit"></a>
<a id="Return_value_remaining_pull_limit"></a>
#### remaining_pull_limit

- Schema name: `Remaining Pull Limit`
- Default: null

Remaining pull limit for Docker Hub registry.
<a id="Return_value_remaining_pull_limit_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_remaining_pull_limit_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_remaining_pull_limit_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_remaining_pull_limit_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_remaining_pull_limit_anyOf_i1)

- Type: null

<a id="headingReturn_value_remaining_time_limit_in_secs"></a>
<a id="Return_value_remaining_time_limit_in_secs"></a>
#### remaining_time_limit_in_secs

- Schema name: `Remaining Time Limit In Secs`
- Default: null

Remaining time limit in seconds for Docker Hub registry for the current pull limit to be renewed.
<a id="Return_value_remaining_time_limit_in_secs_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_remaining_time_limit_in_secs_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_remaining_time_limit_in_secs_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_remaining_time_limit_in_secs_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_remaining_time_limit_in_secs_anyOf_i1)

- Type: null

<a id="headingReturn_value_error"></a>
<a id="Return_value_error"></a>
#### error

- Schema name: `Error`
- Default: null

Error message if rate limit information could not be retrieved or `null` on success.
<a id="Return_value_error_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_error_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
