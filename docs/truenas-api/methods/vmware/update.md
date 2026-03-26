---
title: vmware.update
kind: method
source_rst: _sources/api_methods_vmware.update.rst.txt
source_html: api_methods_vmware.update.html
required_roles:
  - SNAPSHOT_TASK_WRITE
---

# vmware.update

## Summary

Update VMWare snapshot of `id`.

## Required Roles

- `SNAPSHOT_TASK_WRITE`

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

ID of the VMware configuration to update.

#### Parameter 2: vmware_update

#### vmware_update

- Schema name: `vmware_update`
- Type: object

Updated configuration for the VMware integration.
- No Additional Properties
##### datastore

- Schema name: `Datastore`
- Type: string

Valid datastore name which exists on the VMWare host.

##### filesystem

- Schema name: `Filesystem`
- Type: string

ZFS filesystem or dataset to use for VMware storage.

##### hostname

- Schema name: `Hostname`
- Type: string

Valid IP address / hostname of a VMWare host. When clustering, this is the vCenter server for the cluster.

##### username

- Schema name: `Username`
- Type: string

Credentials used to authorize access to the VMWare host.

##### password

- Schema name: `Password`
- Type: string

Password for VMware host authentication.

### Return value

- Schema name: `VMWareEntry`
- Type: object

The updated VMware integration configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VMware configuration.

#### datastore (required)

- Schema name: `Datastore`
- Type: string

Valid datastore name which exists on the VMWare host.

#### filesystem (required)

- Schema name: `Filesystem`
- Type: string

ZFS filesystem or dataset to use for VMware storage.

#### hostname (required)

- Schema name: `Hostname`
- Type: string

Valid IP address / hostname of a VMWare host. When clustering, this is the vCenter server for the cluster.

#### username (required)

- Schema name: `Username`
- Type: string

Credentials used to authorize access to the VMWare host.

#### password (required)

- Schema name: `Password`
- Type: string

Password for VMware host authentication.

#### state (required)

- Schema name: `State`
- Type: object

Current connection and synchronization state with the VMware host.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
