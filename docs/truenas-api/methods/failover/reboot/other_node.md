---
title: failover.reboot.other_node
kind: method
source_rst: _sources/api_methods_failover.reboot.other_node.rst.txt
source_html: api_methods_failover.reboot.other_node.html
required_roles:
  - FULL_ADMIN
---

# failover.reboot.other_node

## Summary

Reboot the other node and wait for it to come back online.

NOTE: This makes very few checks on HA systems. You need to know what you're doing before calling this.

This method is a job.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "reason": "System upgrade",
  "graceful": false
}
```

Options for rebooting the other node.
- No Additional Properties
##### reason

- Schema name: `Reason`
- Type: string
- Default: "System upgrade"

Reason for the system reboot.
- Must be at least `1` characters long

##### graceful

- Schema name: `Graceful`
- Type: boolean
- Default: false

If set, call `system.reboot` to gracefully reboot the other node. By default, `failover.become_passive` will be called on the other node to forcefully reboot and simulate a failover event unless there were changes in the other node's boot environment.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the other node reboot is successfully initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
