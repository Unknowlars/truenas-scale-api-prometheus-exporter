---
title: docker.config
kind: method
source_rst: _sources/api_methods_docker.config.rst.txt
source_html: api_methods_docker.config.html
required_roles:
  - DOCKER_READ
---

# docker.config

## Required Roles

- `DOCKER_READ`

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

- Schema name: `DockerEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Docker configuration.

<a id="headingReturn_value_enable_image_updates"></a>
<a id="Return_value_enable_image_updates"></a>
#### enable_image_updates (required)

- Schema name: `Enable Image Updates`
- Type: boolean

Whether automatic Docker image updates are enabled.

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`

ZFS dataset used for Docker data storage or `null`.
<a id="Return_value_dataset_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dataset_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_pool"></a>
<a id="Return_value_pool"></a>
#### pool (required)

- Schema name: `Pool`

Storage pool used for Docker or `null` if not configured.
<a id="Return_value_pool_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_pool_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pool_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_pool_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pool_anyOf_i1)

- Type: null

<a id="headingReturn_value_address_pools"></a>
<a id="Return_value_address_pools"></a>
#### address_pools (required)

- Schema name: `Address Pools`
- Type: array of object

Array of network address pools for container networking.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_address_pools_items"></a>
- Type: object

<a id="headingReturn_value_cidr_v6"></a>
<a id="Return_value_cidr_v6"></a>
#### cidr_v6 (required)

- Schema name: `Cidr V6`
- Type: string

IPv6 CIDR block for Docker container networking.

<a id="headingReturn_value_registry_mirrors"></a>
<a id="Return_value_registry_mirrors"></a>
#### registry_mirrors (required)

- Schema name: `Registry Mirrors`
- Type: array of object

Array of registry mirrors.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_registry_mirrors_items"></a>
##### RegistryMirror

- Schema name: `RegistryMirror`
- Type: object
- No Additional Properties
<a id="headingReturn_value_registry_mirrors_items_url"></a>
<a id="Return_value_registry_mirrors_items_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

URL of the registry mirror.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingReturn_value_registry_mirrors_items_insecure"></a>
<a id="Return_value_registry_mirrors_items_insecure"></a>
###### insecure (required)

- Schema name: `Insecure`
- Type: boolean

Whether the registry mirror uses an insecure (HTTP) connection.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
