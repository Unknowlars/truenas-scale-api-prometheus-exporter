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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: image_pull

<a id="Call_parameters_items_i0"></a>
#### image_pull

- Schema name: `image_pull`
- Type: object

AppImagePullArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_auth_config"></a>
<a id="Call_parameters_items_i0_auth_config"></a>
##### auth_config

- Default: null

Authentication configuration for private registries or `null` for public images.
<a id="Call_parameters_items_i0_auth_config_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_auth_config_anyOf_i0"></a>
###### [AppImageAuthConfig](#tab-pane_Call_parameters_items_i0_auth_config_anyOf_i0)

- Schema name: `AppImageAuthConfig`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_auth_config_anyOf_i0_username"></a>
<a id="Call_parameters_items_i0_auth_config_anyOf_i0_username"></a>
###### username (required)

- Schema name: `Username`
- Type: string

Username for container registry authentication.

<a id="headingCall_parameters_items_i0_auth_config_anyOf_i0_password"></a>
<a id="Call_parameters_items_i0_auth_config_anyOf_i0_password"></a>
###### password (required)

- Schema name: `Password`
- Type: string

Password or access token for container registry authentication.

<a id="headingCall_parameters_items_i0_auth_config_anyOf_i0_registry_uri"></a>
<a id="Call_parameters_items_i0_auth_config_anyOf_i0_registry_uri"></a>
###### registry_uri

- Schema name: `Registry Uri`
- Default: null

Container registry URI or `null` to use default registry.
<a id="Call_parameters_items_i0_auth_config_anyOf_i0_registry_uri_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_auth_config_anyOf_i0_registry_uri_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_auth_config_anyOf_i0_registry_uri_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_auth_config_anyOf_i0_registry_uri_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_auth_config_anyOf_i0_registry_uri_anyOf_i1)

- Type: null

<a id="tab-pane_Call_parameters_items_i0_auth_config_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_auth_config_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_image"></a>
<a id="Call_parameters_items_i0_image"></a>
##### image (required)

- Schema name: `Image`
- Type: string

Container image reference to pull (registry/repository:tag).
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the image is successfully pulled.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
