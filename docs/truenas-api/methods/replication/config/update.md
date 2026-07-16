---
title: replication.config.update
kind: method
source_rst: _sources/api_methods_replication.config.update.rst.txt
source_html: api_methods_replication.config.update.html
required_roles:
  - REPLICATION_TASK_CONFIG_WRITE
---

# replication.config.update

## Required Roles

- `REPLICATION_TASK_CONFIG_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: replication_config_update

#### replication_config_update

- Schema name: `replication_config_update`
- Type: object

ReplicationConfigUpdateArgs parameters.
- No Additional Properties
##### max_parallel_replication_tasks

- Schema name: `Max Parallel Replication Tasks`

A maximum number of parallel replication tasks running.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1`

####### Option 2

- Type: null

### Return value

- Schema name: `ReplicationConfigEntry`
- Type: object

The updated replication configuration.
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
