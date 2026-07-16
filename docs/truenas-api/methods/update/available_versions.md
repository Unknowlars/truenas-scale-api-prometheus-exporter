---
title: update.available_versions
kind: method
source_rst: _sources/api_methods_update.available_versions.rst.txt
source_html: api_methods_update.available_versions.html
required_roles:
  - SYSTEM_UPDATE_READ
---

# update.available_versions

## Summary

TrueNAS versions available for update.

## Required Roles

- `SYSTEM_UPDATE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of object

Array of available system update versions across all trains.
- No Additional Items

#### Each item of this array must be:

#### UpdateAvailableVersion

- Schema name: `UpdateAvailableVersion`
- Type: object
- No Additional Properties
##### train (required)

- Schema name: `Train`
- Type: string

Train that provides this version.

##### version (required)

- Schema name: `UpdateStatusNewVersion`
- Type: object

Detailed information about this available version.
- No Additional Properties
###### version (required)

- Schema name: `Version`
- Type: string

Newly available version number.

###### manifest (required)

- Schema name: `Manifest`
- Type: object

Object containing detailed version information and metadata.

###### release_notes (required)

- Schema name: `Release Notes`

Release notes.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### release_notes_url (required)

- Schema name: `Release Notes Url`
- Type: string

Release notes URL.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
