---
title: vmware.create
kind: method
source_rst: _sources/api_methods_vmware.create.rst.txt
source_html: api_methods_vmware.create.html
required_roles:
  - SNAPSHOT_TASK_WRITE
---

# vmware.create

## Summary

Create VMWare snapshot.

## Required Roles

- `SNAPSHOT_TASK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vmware_create

#### vmware_create

- Schema name: `vmware_create`
- Type: object

Configuration for creating a new VMware integration.
- No Additional Properties
##### datastore (required)

- Schema name: `Datastore`
- Type: string

Valid datastore name which exists on the VMWare host.

##### filesystem (required)

- Schema name: `Filesystem`
- Type: string

ZFS filesystem or dataset to use for VMware storage.

##### hostname (required)

- Schema name: `Hostname`
- Type: string

Valid IP address / hostname of a VMWare host. When clustering, this is the vCenter server for the cluster.

##### username (required)

- Schema name: `Username`
- Type: string

Credentials used to authorize access to the VMWare host.

##### password (required)

- Schema name: `Password`
- Type: string

Password for VMware host authentication.

### Return value

- Schema name: `VMWareEntry`
- Type: object

The newly created VMware integration configuration.
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
