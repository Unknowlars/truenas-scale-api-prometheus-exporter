---
title: docker.restore_backup
kind: method
source_rst: _sources/api_methods_docker.restore_backup.rst.txt
source_html: api_methods_docker.restore_backup.html
required_roles:
  - DOCKER_WRITE
---

# docker.restore_backup

## Summary

Restore a backup of existing apps.

This method is a job.

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

Name of the backup to restore.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the backup restore is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
