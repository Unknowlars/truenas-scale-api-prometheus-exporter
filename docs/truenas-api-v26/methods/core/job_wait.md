---
title: core.job_wait
kind: method
source_rst: _sources/api_methods_core.job_wait.rst.txt
source_html: api_methods_core.job_wait.html
required_roles:
  []
---

# core.job_wait

## Summary

Wait for the job identified by `id` to finish and return its result.

This method is itself a job that wraps the target job, so it mirrors the target's progress and final state (success, failure, or abort).

This method is a job.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the job to wait for completion.

### Return value

- Schema name: `Result`
- Type: object

The result data returned by the completed job.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
