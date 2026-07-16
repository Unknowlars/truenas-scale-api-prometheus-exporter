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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vmware-creds

#### vmware-creds

- Schema name: `vmware-creds`
- Type: object

VMWareMatchDatastoresWithDatasetsArgs parameters.
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

- Schema name: `VMWareMatchDatastoresWithDatasetsResult`
- Type: object

VMWareMatchDatastoresWithDatasetsResult return fields.
- No Additional Properties
#### datastores (required)

- Schema name: `Datastores`
- Type: array of object

Array of VMware datastores with their matching local filesystems.
- No Additional Items

##### Each item of this array must be:

##### VMWareMatchDatastoresWithDatasetsResultDatastore

- Schema name: `VMWareMatchDatastoresWithDatasetsResultDatastore`
- Type: object
- No Additional Properties
###### name (required)

- Schema name: `Name`
- Type: string

Name of the VMware datastore.

###### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the datastore.

###### filesystems (required)

- Schema name: `Filesystems`
- Type: array of string

Array of local filesystem names that can provide storage for this datastore.
- No Additional Items

####### Each item of this array must be:

- Type: string

#### filesystems (required)

- Schema name: `Filesystems`
- Type: array of object

Array of local filesystems that can be used for VMware storage.
- No Additional Items

##### Each item of this array must be:

##### VMWareMatchDatastoresWithDatasetsResultFilesystem

- Schema name: `VMWareMatchDatastoresWithDatasetsResultFilesystem`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of storage - FILESYSTEM for ZFS datasets, VOLUME for ZFS volumes.

###### name (required)

- Schema name: `Name`
- Type: string

Name of the local filesystem or volume.

###### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the filesystem or volume.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
