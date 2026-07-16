---
title: app.image.pull
kind: method
source_rst: _sources/api_methods_app.image.pull.rst.txt
source_html: api_methods_app.image.pull.html
required_roles:
  - APPS_WRITE
---

# app.image.pull

## Summary

`image` is the name of the image to pull. Format for the name is "registry/repo/image:v1.2.3" where registry may be omitted and it will default to docker registry in this case. It can or cannot contain the tag - this will be passed as is to docker so this should be analogous to what `docker pull` expects.

`auth_config` should be specified if image to be retrieved is under a private repository.

This method is a job.

## Required Roles

- `APPS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: image_pull

#### image_pull

- Schema name: `image_pull`
- Type: object

AppImagePullArgs parameters.
- No Additional Properties
##### auth_config

- Default: null

Authentication configuration for private registries or `null` for public images.
###### Any of

####### AppImageAuthConfig

- Schema name: `AppImageAuthConfig`
- Type: object
- No Additional Properties
######## username (required)

- Schema name: `Username`
- Type: string

Username for container registry authentication.

######## password (required)

- Schema name: `Password`
- Type: string

Password or access token for container registry authentication.

######## registry_uri

- Schema name: `Registry Uri`
- Default: null

Container registry URI or `null` to use default registry.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: null

##### image (required)

- Schema name: `Image`
- Type: string

Container image reference to pull (registry/repository:tag).
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the image is successfully pulled.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
