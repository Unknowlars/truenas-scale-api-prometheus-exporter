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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `ReplicationConfigEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the replication configuration.

#### max_parallel_replication_tasks (required)

- Schema name: `Max Parallel Replication Tasks`

A maximum number of parallel replication tasks running.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `1`

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
