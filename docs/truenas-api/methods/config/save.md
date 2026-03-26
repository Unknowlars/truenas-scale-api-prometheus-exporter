---
title: config.save
kind: method
source_rst: _sources/api_methods_config.save.rst.txt
source_html: api_methods_config.save.html
required_roles:
  - FULL_ADMIN
---

# config.save

## Summary

Create a tar file of security-sensitive information. These options select which information is included in the tar file:

`secretseed` bool: When true, include password secret seed. `pool_keys` bool: IGNORED and DEPRECATED as it does not apply on SCALE systems. `root_authorized_keys` bool: When true, include "/root/.ssh/authorized_keys" file for the root user.

If none of these options are set, the tar file is not generated and the database file is returned.

This method is a job.

*This job MUST be used with* :doc:`core.download <api_methods_core.download>`.

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
  "secretseed": false,
  "pool_keys": false,
  "root_authorized_keys": false
}
```

Options controlling what data to include in the configuration backup.
- No Additional Properties
##### secretseed

- Schema name: `Secretseed`
- Type: boolean
- Default: false

Whether to include the secret seed in the configuration backup.

##### pool_keys

- Schema name: `Pool Keys`
- Type: boolean
- Default: false

Whether to include encryption keys for storage pools in the backup.

##### root_authorized_keys

- Schema name: `Root Authorized Keys`
- Type: boolean
- Default: false

Whether to include root user's SSH authorized keys in the backup.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the configuration backup is successfully created.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
