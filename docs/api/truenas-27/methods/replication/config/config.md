---
title: replication.config.config
kind: method
source_rst: _sources/api_methods_replication.config.config.rst.txt
source_html: api_methods_replication.config.config.html
required_roles:
  - REPLICATION_TASK_CONFIG_READ
---

# replication.config.config

## Required Roles

- `REPLICATION_TASK_CONFIG_READ`

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

- Schema name: `ReplicationConfigEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the replication configuration.

<a id="headingReturn_value_max_parallel_replication_tasks"></a>
<a id="Return_value_max_parallel_replication_tasks"></a>
#### max_parallel_replication_tasks (required)

- Schema name: `Max Parallel Replication Tasks`

A maximum number of parallel replication tasks running.
<a id="Return_value_max_parallel_replication_tasks_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_max_parallel_replication_tasks_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_max_parallel_replication_tasks_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1`

<a id="tab-pane_Return_value_max_parallel_replication_tasks_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_max_parallel_replication_tasks_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
