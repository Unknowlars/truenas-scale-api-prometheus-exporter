---
title: failover.update
kind: method
source_rst: _sources/api_methods_failover.update.rst.txt
source_html: api_methods_failover.update.html
required_roles:
  - FAILOVER_WRITE
---

# failover.update

## Summary

Update failover configuration.

## Required Roles

- `FAILOVER_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Updated failover configuration data.
- No Additional Properties
##### disabled

- Schema name: `Disabled`
- Type: boolean

When true, HA will be administratively disabled.

##### master

- Schema name: `Master`
- Type: boolean

Marks the particular node in the chassis as the master node. The standby node will have the opposite value.

##### timeout

- Schema name: `Timeout`
- Type: integer

The time to WAIT (in seconds) until a failover occurs when a network event occurs on an interface that is marked critical for failover AND HA is enabled and working appropriately. The default time to wait is 2 seconds. **NOTE: This setting does NOT effect the `disabled` or `master` parameters.**

### Return value

- Schema name: `FailoverEntry`
- Type: object

The updated failover configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the failover configuration.

#### disabled (required)

- Schema name: `Disabled`
- Type: boolean

When true, HA will be administratively disabled.

#### master (required)

- Schema name: `Master`
- Type: boolean

Marks the particular node in the chassis as the master node. The standby node will have the opposite value.

#### timeout (required)

- Schema name: `Timeout`
- Type: integer

The time to WAIT (in seconds) until a failover occurs when a network event occurs on an interface that is marked critical for failover AND HA is enabled and working appropriately. The default time to wait is 2 seconds. **NOTE: This setting does NOT effect the `disabled` or `master` parameters.**

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
