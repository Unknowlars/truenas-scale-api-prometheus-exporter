---
title: docker.backup_to_pool
kind: method
source_rst: _sources/api_methods_docker.backup_to_pool.rst.txt
source_html: api_methods_docker.backup_to_pool.html
required_roles:
  - DOCKER_WRITE
---

# docker.backup_to_pool

## Summary

Create a backup of existing apps on `target_pool`.

This creates a backup of existing apps on the `target_pool` specified. If this is executed multiple times, in the next iteration it will incrementally backup the apps that have changed since the last backup.

Note: This will stop the docker service (which means current active apps will be stopped) and then start it again after snapshot has been taken of the current apps dataset.

This method is a job.

## Required Roles

- `DOCKER_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: target_pool

#### target_pool

- Schema name: `target_pool`
- Type: string

Name of the storage pool to backup Docker data to.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the pool backup is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
