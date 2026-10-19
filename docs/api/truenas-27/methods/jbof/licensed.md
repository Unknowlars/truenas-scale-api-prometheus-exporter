---
title: jbof.licensed
kind: method
source_rst: _sources/api_methods_jbof.licensed.rst.txt
source_html: api_methods_jbof.licensed.html
required_roles:
  - JBOF_READ
---

# jbof.licensed

## Summary

Return a count of the number of JBOF units licensed.

## Required Roles

- `JBOF_READ`

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
- Type: integer

Number of JBOF units licensed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
