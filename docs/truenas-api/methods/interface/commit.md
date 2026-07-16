---
title: interface.commit
kind: method
source_rst: _sources/api_methods_interface.commit.rst.txt
source_html: api_methods_interface.commit.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.commit

## Summary

Commit/apply pending interfaces changes.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

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

Options for committing interface changes.
- No Additional Properties
##### rollback

- Schema name: `Rollback`
- Type: boolean
- Default: true

Roll back changes in case they fail to apply.

##### checkin_timeout

- Schema name: `Checkin Timeout`
- Type: integer
- Default: 60

Number of seconds to wait for the checkin call to acknowledge the interface changes happened as planned from the user. If checkin does not happen within this period of time, the changes will get reverted.

### Return value

- Schema name: `Result`
- Type: null

No return value for successful commit operation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
