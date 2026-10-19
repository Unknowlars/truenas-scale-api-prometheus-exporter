---
title: ipmi.sel.clear
kind: method
source_rst: _sources/api_methods_ipmi.sel.clear.rst.txt
source_html: api_methods_ipmi.sel.clear.html
required_roles:
  - IPMI_WRITE
---

# ipmi.sel.clear

## Summary

Clear all entries from the IPMI System Event Log (SEL).

This method is a job.

## Required Roles

- `IPMI_WRITE`

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

Returns `null` when the SEL clear operation completes successfully.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
