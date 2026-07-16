---
title: app.image.query
kind: event
source_rst: _sources/api_events_app.image.query.rst.txt
source_html: api_events_app.image.query.html
required_roles:
  - APPS_READ
---

# app.image.query

## Summary

Sent on app.image changes.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

### ADDED

- Schema name: `AppImageAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `AppImageEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container image (usually SHA256 hash).
- Must be at least `1` characters long

##### repo_tags (required)

- Schema name: `Repo Tags`
- Type: array of string

Array of repository tags associated with this image.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### repo_digests (required)

- Schema name: `Repo Digests`
- Type: array of string

Array of repository digests (content-addressable identifiers) for this image.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### size (required)

- Schema name: `Size`
- Type: integer

Size of the container image in bytes.

##### dangling (required)

- Schema name: `Dangling`
- Type: boolean

Whether this is a dangling image (no tags or references).

##### update_available (required)

- Schema name: `Update Available`
- Type: boolean

Whether a newer version of this image is available for download.

##### created (required)

- Schema name: `Created`
- Type: string

Timestamp when the container image was created (ISO format).

##### author (required)

- Schema name: `Author`
- Type: string

Author or maintainer of the container image.

##### comment (required)

- Schema name: `Comment`
- Type: string

Comment or description provided by the image author.

##### parsed_repo_tags

- Schema name: `Parsed Repo Tags`
- Default: null

Parsed repository tag information or `null` if not available.
###### Any of

####### Option 1

- Type: array of object
- No Additional Items

######## Each item of this array must be:

######## AppImageParsedRepoTags

- Schema name: `AppImageParsedRepoTags`
- Type: object
- No Additional Properties
######### reference (required)

- Schema name: `Reference`
- Type: string

Full reference to the container image (registry/repository:tag).

######### image (required)

- Schema name: `Image`
- Type: string

Container image name without registry or tag.

######### tag (required)

- Schema name: `Tag`
- Type: string

Image tag (version) or digest identifier.

######### registry (required)

- Schema name: `Registry`
- Type: string

Container registry hostname (e.g., docker.io, quay.io).

######### complete_tag (required)

- Schema name: `Complete Tag`
- Type: string

Complete image reference including registry, image name, and tag.

######### reference_is_digest (required)

- Schema name: `Reference Is Digest`
- Type: boolean

Whether the reference uses a digest hash instead of a tag name.

####### Option 2

- Type: null

### CHANGED

- Schema name: `AppImageChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `AppImageEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container image (usually SHA256 hash).
- Must be at least `1` characters long

##### repo_tags (required)

- Schema name: `Repo Tags`
- Type: array of string

Array of repository tags associated with this image.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### repo_digests (required)

- Schema name: `Repo Digests`
- Type: array of string

Array of repository digests (content-addressable identifiers) for this image.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### size (required)

- Schema name: `Size`
- Type: integer

Size of the container image in bytes.

##### dangling (required)

- Schema name: `Dangling`
- Type: boolean

Whether this is a dangling image (no tags or references).

##### update_available (required)

- Schema name: `Update Available`
- Type: boolean

Whether a newer version of this image is available for download.

##### created (required)

- Schema name: `Created`
- Type: string

Timestamp when the container image was created (ISO format).

##### author (required)

- Schema name: `Author`
- Type: string

Author or maintainer of the container image.

##### comment (required)

- Schema name: `Comment`
- Type: string

Comment or description provided by the image author.

##### parsed_repo_tags

- Schema name: `Parsed Repo Tags`
- Default: null

Parsed repository tag information or `null` if not available.
###### Any of

####### Option 1

- Type: array of object
- No Additional Items

######## Each item of this array must be:

######## AppImageParsedRepoTags

- Schema name: `AppImageParsedRepoTags`
- Type: object
- No Additional Properties
######### reference (required)

- Schema name: `Reference`
- Type: string

Full reference to the container image (registry/repository:tag).

######### image (required)

- Schema name: `Image`
- Type: string

Container image name without registry or tag.

######### tag (required)

- Schema name: `Tag`
- Type: string

Image tag (version) or digest identifier.

######### registry (required)

- Schema name: `Registry`
- Type: string

Container registry hostname (e.g., docker.io, quay.io).

######### complete_tag (required)

- Schema name: `Complete Tag`
- Type: string

Complete image reference including registry, image name, and tag.

######### reference_is_digest (required)

- Schema name: `Reference Is Digest`
- Type: boolean

Whether the reference uses a digest hash instead of a tag name.

####### Option 2

- Type: null

### REMOVED

- Schema name: `AppImageRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
