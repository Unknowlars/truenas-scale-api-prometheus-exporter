---
title: vmware.query
kind: event
source_rst: _sources/api_events_vmware.query.rst.txt
source_html: api_events_vmware.query.html
required_roles:
  - SNAPSHOT_TASK_READ
---

# vmware.query

## Summary

Sent on vmware changes.

## Required Roles

- `SNAPSHOT_TASK_READ`

## Schema

- Type: object

### ADDED

- Schema name: `VMWareAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `VMWareEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VMware configuration.

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

##### state (required)

- Schema name: `State`
- Type: object

Current connection and synchronization state with the VMware host.

### CHANGED

- Schema name: `VMWareChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `VMWareEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VMware configuration.

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

##### state (required)

- Schema name: `State`
- Type: object

Current connection and synchronization state with the VMware host.

### REMOVED

- Schema name: `VMWareRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
