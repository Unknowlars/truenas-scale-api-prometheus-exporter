---
title: failover.become_passive
kind: method
source_rst: _sources/api_methods_failover.become_passive.rst.txt
source_html: api_methods_failover.become_passive.html
required_roles:
  - FAILOVER_WRITE
---

# failover.become_passive

## Summary

This method is only called manually by the end-user so we fully expect that they know what they're doing. Furthermore, this method will only run if failover has NOT been administratively disabled. The reason why we only allow this in that scenario is because the failover logic (on the other node) will ignore any failover "event" that comes in if failover has been administratively disabled. This immediately causes the HA system to go into a "faulted" state because the other node will get the VIPs but it will not import the zpool and it will not start `fenced`. Only way out of that situation is to manually fix things (import zpool, migrate VIPs, start `fenced`, etc).

.. warning::

The only "safe" way to "become passive" is to use the **STCNITH** method, or "Shoot The Current Node In The Head" (similar to **STONITH**). This ensures the current node gets out of the way *completely* so there is no chance of the zpool being imported on both nodes at the same time which can ultimately end in data corruption.

## Required Roles

- `FAILOVER_WRITE`

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

- Schema name: `Result`
- Type: null

Returns `null` when the node successfully becomes passive.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
