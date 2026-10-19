---
title: vmware.match_datastores_with_datasets
kind: method
source_rst: _sources/api_methods_vmware.match_datastores_with_datasets.rst.txt
source_html: api_methods_vmware.match_datastores_with_datasets.html
required_roles:
  - READONLY_ADMIN
---

# vmware.match_datastores_with_datasets

## Summary

Requests datastores from vCenter server and tries to match them with local filesystems.

Returns a list of datastores, a list of local filesystems and guessed relationship between them.

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

VMWareMatchDatastoresWithDatasetsArgs parameters.
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

- Schema name: `VMWareMatchDatastoresWithDatasetsResult`
- Type: object

VMWareMatchDatastoresWithDatasetsResult return fields.
- No Additional Properties
<a id="headingReturn_value_datastores"></a>
<a id="Return_value_datastores"></a>
#### datastores (required)

- Schema name: `Datastores`
- Type: array of object

Array of VMware datastores with their matching local filesystems.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_datastores_items"></a>
##### VMWareMatchDatastoresWithDatasetsResultDatastore

- Schema name: `VMWareMatchDatastoresWithDatasetsResultDatastore`
- Type: object
- No Additional Properties
<a id="headingReturn_value_datastores_items_name"></a>
<a id="Return_value_datastores_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the VMware datastore.

<a id="headingReturn_value_datastores_items_description"></a>
<a id="Return_value_datastores_items_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the datastore.

<a id="headingReturn_value_datastores_items_filesystems"></a>
<a id="Return_value_datastores_items_filesystems"></a>
###### filesystems (required)

- Schema name: `Filesystems`
- Type: array of string

Array of local filesystem names that can provide storage for this datastore.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_datastores_items_filesystems_items"></a>
- Type: string

<a id="headingReturn_value_filesystems"></a>
<a id="Return_value_filesystems"></a>
#### filesystems (required)

- Schema name: `Filesystems`
- Type: array of object

Array of local filesystems that can be used for VMware storage.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_filesystems_items"></a>
##### VMWareMatchDatastoresWithDatasetsResultFilesystem

- Schema name: `VMWareMatchDatastoresWithDatasetsResultFilesystem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_filesystems_items_type"></a>
<a id="Return_value_filesystems_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of storage - FILESYSTEM for ZFS datasets, VOLUME for ZFS volumes.
###### Must be one of:

- "FILESYSTEM"
- "VOLUME"

<a id="headingReturn_value_filesystems_items_name"></a>
<a id="Return_value_filesystems_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the local filesystem or volume.

<a id="headingReturn_value_filesystems_items_description"></a>
<a id="Return_value_filesystems_items_description"></a>
###### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the filesystem or volume.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
