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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `AppImageAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `AppImageEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container image (usually SHA256 hash).
- Must be at least `1` characters long

<a id="headingADDED_fields_repo_tags"></a>
<a id="ADDED_fields_repo_tags"></a>
##### repo_tags (required)

- Schema name: `Repo Tags`
- Type: array of string

Array of repository tags associated with this image.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_repo_tags_items"></a>
- Type: string

<a id="headingADDED_fields_repo_digests"></a>
<a id="ADDED_fields_repo_digests"></a>
##### repo_digests (required)

- Schema name: `Repo Digests`
- Type: array of string

Array of repository digests (content-addressable identifiers) for this image.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_repo_digests_items"></a>
- Type: string

<a id="headingADDED_fields_size"></a>
<a id="ADDED_fields_size"></a>
##### size (required)

- Schema name: `Size`
- Type: integer

Size of the container image in bytes.

<a id="headingADDED_fields_dangling"></a>
<a id="ADDED_fields_dangling"></a>
##### dangling (required)

- Schema name: `Dangling`
- Type: boolean

Whether this is a dangling image (no tags or references).

<a id="headingADDED_fields_update_available"></a>
<a id="ADDED_fields_update_available"></a>
##### update_available (required)

- Schema name: `Update Available`
- Type: boolean

Whether a newer version of this image is available for download.

<a id="headingADDED_fields_created"></a>
<a id="ADDED_fields_created"></a>
##### created (required)

- Schema name: `Created`

Timestamp when the container image was created (ISO format) or `null` if not available.
<a id="ADDED_fields_created_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_created_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_created_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_created_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_created_anyOf_i1)

- Type: null

<a id="headingADDED_fields_author"></a>
<a id="ADDED_fields_author"></a>
##### author (required)

- Schema name: `Author`

Author or maintainer of the container image or `null` if not specified.
<a id="ADDED_fields_author_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_author_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_author_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_author_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_author_anyOf_i1)

- Type: null

<a id="headingADDED_fields_comment"></a>
<a id="ADDED_fields_comment"></a>
##### comment (required)

- Schema name: `Comment`

Comment or description provided by the image author or `null` if not provided.
<a id="ADDED_fields_comment_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_comment_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_comment_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_comment_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_comment_anyOf_i1)

- Type: null

<a id="headingADDED_fields_parsed_repo_tags"></a>
<a id="ADDED_fields_parsed_repo_tags"></a>
##### parsed_repo_tags

- Schema name: `Parsed Repo Tags`
- Default: null

Parsed repository tag information or `null` if not available.
<a id="ADDED_fields_parsed_repo_tags_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_parsed_repo_tags_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_parsed_repo_tags_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_parsed_repo_tags_anyOf_i0_items"></a>
###### AppImageParsedRepoTags

- Schema name: `AppImageParsedRepoTags`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_parsed_repo_tags_anyOf_i0_items_reference"></a>
<a id="ADDED_fields_parsed_repo_tags_anyOf_i0_items_reference"></a>
###### reference (required)

- Schema name: `Reference`
- Type: string

Full reference to the container image (registry/repository:tag).

<a id="headingADDED_fields_parsed_repo_tags_anyOf_i0_items_image"></a>
<a id="ADDED_fields_parsed_repo_tags_anyOf_i0_items_image"></a>
###### image (required)

- Schema name: `Image`
- Type: string

Container image name without registry or tag.

<a id="headingADDED_fields_parsed_repo_tags_anyOf_i0_items_tag"></a>
<a id="ADDED_fields_parsed_repo_tags_anyOf_i0_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: string

Image tag (version) or digest identifier.

<a id="headingADDED_fields_parsed_repo_tags_anyOf_i0_items_registry"></a>
<a id="ADDED_fields_parsed_repo_tags_anyOf_i0_items_registry"></a>
###### registry (required)

- Schema name: `Registry`
- Type: string

Container registry hostname (e.g., docker.io, quay.io).

<a id="headingADDED_fields_parsed_repo_tags_anyOf_i0_items_complete_tag"></a>
<a id="ADDED_fields_parsed_repo_tags_anyOf_i0_items_complete_tag"></a>
###### complete_tag (required)

- Schema name: `Complete Tag`
- Type: string

Complete image reference including registry, image name, and tag.

<a id="headingADDED_fields_parsed_repo_tags_anyOf_i0_items_reference_is_digest"></a>
<a id="ADDED_fields_parsed_repo_tags_anyOf_i0_items_reference_is_digest"></a>
###### reference_is_digest (required)

- Schema name: `Reference Is Digest`
- Type: boolean

Whether the reference uses a digest hash instead of a tag name.

<a id="tab-pane_ADDED_fields_parsed_repo_tags_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_parsed_repo_tags_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `AppImageChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `AppImageEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container image (usually SHA256 hash).
- Must be at least `1` characters long

<a id="headingCHANGED_fields_repo_tags"></a>
<a id="CHANGED_fields_repo_tags"></a>
##### repo_tags (required)

- Schema name: `Repo Tags`
- Type: array of string

Array of repository tags associated with this image.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_repo_tags_items"></a>
- Type: string

<a id="headingCHANGED_fields_repo_digests"></a>
<a id="CHANGED_fields_repo_digests"></a>
##### repo_digests (required)

- Schema name: `Repo Digests`
- Type: array of string

Array of repository digests (content-addressable identifiers) for this image.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_repo_digests_items"></a>
- Type: string

<a id="headingCHANGED_fields_size"></a>
<a id="CHANGED_fields_size"></a>
##### size (required)

- Schema name: `Size`
- Type: integer

Size of the container image in bytes.

<a id="headingCHANGED_fields_dangling"></a>
<a id="CHANGED_fields_dangling"></a>
##### dangling (required)

- Schema name: `Dangling`
- Type: boolean

Whether this is a dangling image (no tags or references).

<a id="headingCHANGED_fields_update_available"></a>
<a id="CHANGED_fields_update_available"></a>
##### update_available (required)

- Schema name: `Update Available`
- Type: boolean

Whether a newer version of this image is available for download.

<a id="headingCHANGED_fields_created"></a>
<a id="CHANGED_fields_created"></a>
##### created (required)

- Schema name: `Created`

Timestamp when the container image was created (ISO format) or `null` if not available.
<a id="CHANGED_fields_created_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_created_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_created_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_created_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_created_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_author"></a>
<a id="CHANGED_fields_author"></a>
##### author (required)

- Schema name: `Author`

Author or maintainer of the container image or `null` if not specified.
<a id="CHANGED_fields_author_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_author_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_author_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_author_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_author_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_comment"></a>
<a id="CHANGED_fields_comment"></a>
##### comment (required)

- Schema name: `Comment`

Comment or description provided by the image author or `null` if not provided.
<a id="CHANGED_fields_comment_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_comment_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_comment_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_comment_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_comment_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_parsed_repo_tags"></a>
<a id="CHANGED_fields_parsed_repo_tags"></a>
##### parsed_repo_tags

- Schema name: `Parsed Repo Tags`
- Default: null

Parsed repository tag information or `null` if not available.
<a id="CHANGED_fields_parsed_repo_tags_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_parsed_repo_tags_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_parsed_repo_tags_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_parsed_repo_tags_anyOf_i0_items"></a>
###### AppImageParsedRepoTags

- Schema name: `AppImageParsedRepoTags`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_parsed_repo_tags_anyOf_i0_items_reference"></a>
<a id="CHANGED_fields_parsed_repo_tags_anyOf_i0_items_reference"></a>
###### reference (required)

- Schema name: `Reference`
- Type: string

Full reference to the container image (registry/repository:tag).

<a id="headingCHANGED_fields_parsed_repo_tags_anyOf_i0_items_image"></a>
<a id="CHANGED_fields_parsed_repo_tags_anyOf_i0_items_image"></a>
###### image (required)

- Schema name: `Image`
- Type: string

Container image name without registry or tag.

<a id="headingCHANGED_fields_parsed_repo_tags_anyOf_i0_items_tag"></a>
<a id="CHANGED_fields_parsed_repo_tags_anyOf_i0_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: string

Image tag (version) or digest identifier.

<a id="headingCHANGED_fields_parsed_repo_tags_anyOf_i0_items_registry"></a>
<a id="CHANGED_fields_parsed_repo_tags_anyOf_i0_items_registry"></a>
###### registry (required)

- Schema name: `Registry`
- Type: string

Container registry hostname (e.g., docker.io, quay.io).

<a id="headingCHANGED_fields_parsed_repo_tags_anyOf_i0_items_complete_tag"></a>
<a id="CHANGED_fields_parsed_repo_tags_anyOf_i0_items_complete_tag"></a>
###### complete_tag (required)

- Schema name: `Complete Tag`
- Type: string

Complete image reference including registry, image name, and tag.

<a id="headingCHANGED_fields_parsed_repo_tags_anyOf_i0_items_reference_is_digest"></a>
<a id="CHANGED_fields_parsed_repo_tags_anyOf_i0_items_reference_is_digest"></a>
###### reference_is_digest (required)

- Schema name: `Reference Is Digest`
- Type: boolean

Whether the reference uses a digest hash instead of a tag name.

<a id="tab-pane_CHANGED_fields_parsed_repo_tags_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_parsed_repo_tags_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `AppImageRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
