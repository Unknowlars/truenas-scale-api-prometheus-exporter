---
title: docker.backup
kind: method
source_rst: _sources/api_methods_docker.backup.rst.txt
source_html: api_methods_docker.backup.html
required_roles:
  - DOCKER_WRITE
---

# docker.backup

## Summary

Create a backup of existing apps.

This creates a backup of existing apps on the same pool in which docker is initialized.

This method is a job.

## Required Roles

- `DOCKER_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: backup_name

<a id="Call_parameters_items_i0"></a>
#### backup_name

- Schema name: `backup_name`
- Default: null

Name for the backup or `null` to generate a timestamp-based name.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: string

Name of the created backup.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
