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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the VMware configuration to update.

#### Parameter 2: vmware_update

<a id="Call_parameters_items_i1"></a>
#### vmware_update

- Schema name: `vmware_update`
- Type: object

Updated configuration for the VMware integration.
- No Additional Properties
<a id="headingCall_parameters_items_i1_datastore"></a>
<a id="Call_parameters_items_i1_datastore"></a>
##### datastore

- Schema name: `Datastore`
- Type: string

Valid datastore name which exists on the VMWare host.

<a id="headingCall_parameters_items_i1_filesystem"></a>
<a id="Call_parameters_items_i1_filesystem"></a>
##### filesystem

- Schema name: `Filesystem`
- Type: string

ZFS filesystem or dataset to use for VMware storage.

<a id="headingCall_parameters_items_i1_hostname"></a>
<a id="Call_parameters_items_i1_hostname"></a>
##### hostname

- Schema name: `Hostname`
- Type: string

Valid IP address / hostname of a VMWare host. When clustering, this is the vCenter server for the cluster.

<a id="headingCall_parameters_items_i1_username"></a>
<a id="Call_parameters_items_i1_username"></a>
##### username

- Schema name: `Username`
- Type: string

Credentials used to authorize access to the VMWare host.

<a id="headingCall_parameters_items_i1_password"></a>
<a id="Call_parameters_items_i1_password"></a>
##### password

- Schema name: `Password`
- Type: string

Password for VMware host authentication.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `VMWareEntry`
- Type: object

The updated VMware integration configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VMware configuration.

<a id="headingReturn_value_datastore"></a>
<a id="Return_value_datastore"></a>
#### datastore (required)

- Schema name: `Datastore`
- Type: string

Valid datastore name which exists on the VMWare host.

<a id="headingReturn_value_filesystem"></a>
<a id="Return_value_filesystem"></a>
#### filesystem (required)

- Schema name: `Filesystem`
- Type: string

ZFS filesystem or dataset to use for VMware storage.

<a id="headingReturn_value_hostname"></a>
<a id="Return_value_hostname"></a>
#### hostname (required)

- Schema name: `Hostname`
- Type: string

Valid IP address / hostname of a VMWare host. When clustering, this is the vCenter server for the cluster.

<a id="headingReturn_value_username"></a>
<a id="Return_value_username"></a>
#### username (required)

- Schema name: `Username`
- Type: string

Credentials used to authorize access to the VMWare host.

<a id="headingReturn_value_password"></a>
<a id="Return_value_password"></a>
#### password (required)

- Schema name: `Password`
- Type: string

Password for VMware host authentication.

<a id="headingReturn_value_state"></a>
<a id="Return_value_state"></a>
#### state (required)

- Schema name: `VMWareEntryState`
- Type: object

Current connection and synchronization state with the VMware host.
- No Additional Properties
<a id="headingReturn_value_state_state"></a>
<a id="Return_value_state_state"></a>
##### state

- Schema name: `State`
- Type: enum (of string)

VMware host state. `PENDING`: No snapshot operation on the host was performed yet `SUCCESS`: The last snapshot operation on the host was successful `ERROR`: The last snapshot operation on the host failed `BLOCKED`: Network activity is blocked
###### Must be one of:

- "PENDING"
- "SUCCESS"
- "ERROR"
- "BLOCKED"

<a id="headingReturn_value_state_error"></a>
<a id="Return_value_state_error"></a>
##### error

- Schema name: `Error`
- Type: string

Error text (if any).

<a id="headingReturn_value_state_datetime"></a>
<a id="Return_value_state_datetime"></a>
##### datetime

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

State update datetime.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
