---
title: boot.set_scrub_interval
kind: method
source_rst: _sources/api_methods_boot.set_scrub_interval.rst.txt
source_html: api_methods_boot.set_scrub_interval.html
required_roles:
  - BOOT_ENV_WRITE
---

# boot.set_scrub_interval

## Summary

Set Automatic Scrub Interval value in days.

## Required Roles

- `BOOT_ENV_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: interval

#### interval

- Schema name: `interval`
- Type: integer

Scrub interval in days (must be a positive integer).
- Value must be strictly greater than `0`

### Return value

- Schema name: `Result`
- Type: integer

The updated scrub interval in days.
- Value must be strictly greater than `0`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
