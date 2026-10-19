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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vmware-creds

<a id="Call_parameters_items_i0"></a>
#### vmware-creds

- Schema name: `vmware-creds`
- Type: object

VMWareGetDatastoresArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_hostname"></a>
<a id="Call_parameters_items_i0_hostname"></a>
##### hostname (required)

- Schema name: `Hostname`
- Type: string

IP address or hostname of the VMware host or vCenter server.

<a id="headingCall_parameters_items_i0_username"></a>
<a id="Call_parameters_items_i0_username"></a>
##### username (required)

- Schema name: `Username`
- Type: string

Username for VMware host authentication.

<a id="headingCall_parameters_items_i0_password"></a>
<a id="Call_parameters_items_i0_password"></a>
##### password (required)

- Schema name: `Password`
- Type: string

Password for VMware host authentication.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of string

Array of available datastore names on the VMware host.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
