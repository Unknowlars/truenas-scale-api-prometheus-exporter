---
title: docker.delete_backup
kind: method
source_rst: _sources/api_methods_docker.delete_backup.rst.txt
source_html: api_methods_docker.delete_backup.html
required_roles:
  - DOCKER_WRITE
---

# docker.delete_backup

## Summary

Delete `backup_name` app backup.

## Required Roles

- `DOCKER_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: backup_name

#### backup_name

- Schema name: `backup_name`
- Type: string

Name of the backup to delete.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the backup is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
