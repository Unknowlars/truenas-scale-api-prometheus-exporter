---
title: container.image.query_registry
kind: method
source_rst: _sources/api_methods_container.image.query_registry.rst.txt
source_html: api_methods_container.image.query_registry.html
required_roles:
  - CONTAINER_IMAGE_READ
---

# container.image.query_registry

## Summary

Query images available in the images registry.

## Required Roles

- `CONTAINER_IMAGE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### ContainerImageQueryRegistryResultImage

- Schema name: `ContainerImageQueryRegistryResultImage`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Image name.

<a id="headingReturn_value_items_versions"></a>
<a id="Return_value_items_versions"></a>
##### versions (required)

- Schema name: `Versions`
- Type: array of object

Available image versions.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_versions_items"></a>
###### ContainerImageQueryRegistryResultImageVersion

- Schema name: `ContainerImageQueryRegistryResultImageVersion`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_versions_items_version"></a>
<a id="Return_value_items_versions_items_version"></a>
###### version (required)

- Schema name: `Version`
- Type: string

Image version name.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
