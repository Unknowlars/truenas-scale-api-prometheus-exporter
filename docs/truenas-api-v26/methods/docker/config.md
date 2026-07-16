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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `DockerEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Docker configuration.

#### enable_image_updates (required)

- Schema name: `Enable Image Updates`
- Type: boolean

Whether automatic Docker image updates are enabled.

#### dataset (required)

- Schema name: `Dataset`

ZFS dataset used for Docker data storage or `null`.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### pool (required)

- Schema name: `Pool`

Storage pool used for Docker or `null` if not configured.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### address_pools (required)

- Schema name: `Address Pools`
- Type: array of object

Array of network address pools for container networking.
- No Additional Items

##### Each item of this array must be:

- Type: object

#### cidr_v6 (required)

- Schema name: `Cidr V6`
- Type: string

IPv6 CIDR block for Docker container networking.

#### registry_mirrors (required)

- Schema name: `Registry Mirrors`
- Type: array of object

Array of registry mirrors.
- No Additional Items

##### Each item of this array must be:

##### RegistryMirror

- Schema name: `RegistryMirror`
- Type: object
- No Additional Properties
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

URL of the registry mirror.
- Must be at least `1` characters long
- Must be at most `2083` characters long

###### insecure (required)

- Schema name: `Insecure`
- Type: boolean

Whether the registry mirror uses an insecure (HTTP) connection.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
