---
title: update.status
kind: event
source_rst: _sources/api_events_update.status.rst.txt
source_html: api_events_update.status.html
required_roles:
  - SYSTEM_UPDATE_READ
---

# update.status

## Summary

Updated on update status changes.

## Required Roles

- `SYSTEM_UPDATE_READ`

## Schema

- Type: object

### CHANGED

- Schema name: `UpdateStatusChangedEvent`
- Type: object
- No Additional Properties
#### status (required)

- Schema name: `UpdateStatus`
- Type: object

Updated system update status information.
- No Additional Properties
##### code (required)

- Schema name: `Code`
- Type: enum (of string)

Status code: * NORMAL - normal status, see `status` dictionary for details. * ERROR - an error occurred, see `error` for details.

##### status (required)

Detailed update status information. `null` if code is ERROR.
###### Any of

####### UpdateStatusStatus

- Schema name: `UpdateStatusStatus`
- Type: object
- No Additional Properties
######## current_version (required)

- Schema name: `UpdateStatusCurrentVersion`
- Type: object

Currently running system version information.
- No Additional Properties
######### train (required)

- Schema name: `Train`
- Type: string

Train name.

######### profile (required)

- Schema name: `Profile`
- Type: string

Update profile assigned for the version.

######### matches_profile (required)

- Schema name: `Matches Profile`
- Type: boolean

Whether the system version running matches the configured update profile.

######## new_version (required)

New system version information (or `null` if no new system version is available).
######### Any of

########## UpdateStatusNewVersion

- Schema name: `UpdateStatusNewVersion`
- Type: object
- No Additional Properties
########### version (required)

- Schema name: `Version`
- Type: string

Newly available version number.

########### manifest (required)

- Schema name: `Manifest`
- Type: object

Object containing detailed version information and metadata.

########### release_notes (required)

- Schema name: `Release Notes`

Release notes.
############ Any of

############# Option 1

- Type: string

############# Option 2

- Type: null

########### release_notes_url (required)

- Schema name: `Release Notes Url`
- Type: string

Release notes URL.

########## Option 2

- Type: string

########## Option 1

- Type: null

########## Option 2

- Type: null

####### Option 2

- Schema name: `UpdateStatusNewVersion`
- Type: object
- No Additional Properties
######## version (required)

- Schema name: `Version`
- Type: string

Newly available version number.

######## manifest (required)

- Schema name: `Manifest`
- Type: object

Object containing detailed version information and metadata.

######## release_notes (required)

- Schema name: `Release Notes`

Release notes.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## release_notes_url (required)

- Schema name: `Release Notes Url`
- Type: string

Release notes URL.

####### UpdateStatusNewVersion

- Type: string

####### Option 2

- Type: null

####### Option 1

- Type: null

####### Option 2

- Type: null

##### error (required)

Error message if code is ERROR. `null` otherwise.
###### Any of

####### UpdateStatusError

- Schema name: `UpdateStatusError`
- Type: object
- No Additional Properties
######## errname (required)

- Schema name: `Errname`
- Type: string

Error code (i.e. ENONET).

######## reason (required)

- Schema name: `Reason`
- Type: string

Error text.

####### Option 2

- Type: null

##### update_download_progress (required)

Current update download progress.
###### Any of

####### UpdateDownloadProgress

- Schema name: `UpdateDownloadProgress`
- Type: object
- No Additional Properties
######## percent (required)

- Schema name: `Percent`
- Type: number

Download completion percentage (0.0 to 100.0).

######## description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the current download activity.

######## version (required)

- Schema name: `Version`
- Type: string

Version number being downloaded.

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
