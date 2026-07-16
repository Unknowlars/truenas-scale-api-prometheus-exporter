---
title: vmware.get_datastores
kind: method
source_rst: _sources/api_methods_vmware.get_datastores.rst.txt
source_html: api_methods_vmware.get_datastores.html
required_roles:
  - READONLY_ADMIN
---

# vmware.get_datastores

## Summary

Get datastores from VMWare.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vmware-creds

#### vmware-creds

- Schema name: `vmware-creds`
- Type: object

VMWareGetDatastoresArgs parameters.
- No Additional Properties
##### hostname (required)

- Schema name: `Hostname`
- Type: string

IP address or hostname of the VMware host or vCenter server.

##### username (required)

- Schema name: `Username`
- Type: string

Username for VMware host authentication.

##### password (required)

- Schema name: `Password`
- Type: string

Password for VMware host authentication.

### Return value

- Schema name: `Result`
- Type: array of string

Array of available datastore names on the VMware host.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
