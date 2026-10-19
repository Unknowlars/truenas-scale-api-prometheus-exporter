---
title: container.delete
kind: method
source_rst: _sources/api_methods_container.delete.rst.txt
source_html: api_methods_container.delete.html
required_roles:
  - CONTAINER_WRITE
---

# container.delete

## Summary

Delete a Container.

A container whose dataset has child datasets or snapshots is refused unless `recursive` is set, which destroys them along with any clones of those snapshots - data that cannot be recovered afterwards.

This method is a job.

## Required Roles

- `CONTAINER_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

Container ID.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {"force": false, "recursive": false}

Container deletion options.
- No Additional Properties
<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force deletion of a container that is not stopped (running or suspended) by stopping it first.

<a id="headingCall_parameters_items_i1_recursive"></a>
<a id="Call_parameters_items_i1_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Destroy everything the container's dataset carries along with the container: its child datasets and snapshots, any clones of those snapshots wherever in the pool they live, and any holds held on them - releasing a hold can break a replication task that depends on it. Deleting a container whose dataset has child datasets or snapshots fails without this. None of what is destroyed can be recovered afterwards.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
