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

#### nvidia (required)

- Schema name: `Nvidia`
- Type: boolean

Whether NVIDIA GPU support is enabled for containers.

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

#### secure_registry_mirrors (required)

- Schema name: `Secure Registry Mirrors`
- Type: array of string

Array of secure (HTTPS) registry mirror URLs.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

#### insecure_registry_mirrors (required)

- Schema name: `Insecure Registry Mirrors`
- Type: array of string

Array of insecure (HTTP) registry mirror URLs.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Type: Format: uri
- Must be at least `1` characters long
- Must be at most `2083` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
