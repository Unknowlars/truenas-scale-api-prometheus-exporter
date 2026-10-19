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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `VMWareAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `VMWareEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VMware configuration.

<a id="headingADDED_fields_datastore"></a>
<a id="ADDED_fields_datastore"></a>
##### datastore (required)

- Schema name: `Datastore`
- Type: string

Valid datastore name which exists on the VMWare host.

<a id="headingADDED_fields_filesystem"></a>
<a id="ADDED_fields_filesystem"></a>
##### filesystem (required)

- Schema name: `Filesystem`
- Type: string

ZFS filesystem or dataset to use for VMware storage.

<a id="headingADDED_fields_hostname"></a>
<a id="ADDED_fields_hostname"></a>
##### hostname (required)

- Schema name: `Hostname`
- Type: string

Valid IP address / hostname of a VMWare host. When clustering, this is the vCenter server for the cluster.

<a id="headingADDED_fields_username"></a>
<a id="ADDED_fields_username"></a>
##### username (required)

- Schema name: `Username`
- Type: string

Credentials used to authorize access to the VMWare host.

<a id="headingADDED_fields_password"></a>
<a id="ADDED_fields_password"></a>
##### password (required)

- Schema name: `Password`
- Type: string

Password for VMware host authentication.

<a id="headingADDED_fields_state"></a>
<a id="ADDED_fields_state"></a>
##### state (required)

- Schema name: `VMWareEntryState`
- Type: object

Current connection and synchronization state with the VMware host.
- No Additional Properties
<a id="headingADDED_fields_state_state"></a>
<a id="ADDED_fields_state_state"></a>
###### state

- Schema name: `State`
- Type: enum (of string)

VMware host state. `PENDING`: No snapshot operation on the host was performed yet `SUCCESS`: The last snapshot operation on the host was successful `ERROR`: The last snapshot operation on the host failed `BLOCKED`: Network activity is blocked
###### Must be one of:

- "PENDING"
- "SUCCESS"
- "ERROR"
- "BLOCKED"

<a id="headingADDED_fields_state_error"></a>
<a id="ADDED_fields_state_error"></a>
###### error

- Schema name: `Error`
- Type: string

Error text (if any).

<a id="headingADDED_fields_state_datetime"></a>
<a id="ADDED_fields_state_datetime"></a>
###### datetime

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

State update datetime.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `VMWareChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `VMWareEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VMware configuration.

<a id="headingCHANGED_fields_datastore"></a>
<a id="CHANGED_fields_datastore"></a>
##### datastore (required)

- Schema name: `Datastore`
- Type: string

Valid datastore name which exists on the VMWare host.

<a id="headingCHANGED_fields_filesystem"></a>
<a id="CHANGED_fields_filesystem"></a>
##### filesystem (required)

- Schema name: `Filesystem`
- Type: string

ZFS filesystem or dataset to use for VMware storage.

<a id="headingCHANGED_fields_hostname"></a>
<a id="CHANGED_fields_hostname"></a>
##### hostname (required)

- Schema name: `Hostname`
- Type: string

Valid IP address / hostname of a VMWare host. When clustering, this is the vCenter server for the cluster.

<a id="headingCHANGED_fields_username"></a>
<a id="CHANGED_fields_username"></a>
##### username (required)

- Schema name: `Username`
- Type: string

Credentials used to authorize access to the VMWare host.

<a id="headingCHANGED_fields_password"></a>
<a id="CHANGED_fields_password"></a>
##### password (required)

- Schema name: `Password`
- Type: string

Password for VMware host authentication.

<a id="headingCHANGED_fields_state"></a>
<a id="CHANGED_fields_state"></a>
##### state (required)

- Schema name: `VMWareEntryState`
- Type: object

Current connection and synchronization state with the VMware host.
- No Additional Properties
<a id="headingCHANGED_fields_state_state"></a>
<a id="CHANGED_fields_state_state"></a>
###### state

- Schema name: `State`
- Type: enum (of string)

VMware host state. `PENDING`: No snapshot operation on the host was performed yet `SUCCESS`: The last snapshot operation on the host was successful `ERROR`: The last snapshot operation on the host failed `BLOCKED`: Network activity is blocked
###### Must be one of:

- "PENDING"
- "SUCCESS"
- "ERROR"
- "BLOCKED"

<a id="headingCHANGED_fields_state_error"></a>
<a id="CHANGED_fields_state_error"></a>
###### error

- Schema name: `Error`
- Type: string

Error text (if any).

<a id="headingCHANGED_fields_state_datetime"></a>
<a id="CHANGED_fields_state_datetime"></a>
###### datetime

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

State update datetime.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `VMWareRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
