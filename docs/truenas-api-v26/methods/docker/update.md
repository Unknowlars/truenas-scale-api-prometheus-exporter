---
title: docker.update
kind: method
source_rst: _sources/api_methods_docker.update.rst.txt
source_html: api_methods_docker.update.html
required_roles:
  - DOCKER_WRITE
---

# docker.update

## Summary

Update Docker service configuration.

This method is a job.

## Required Roles

- `DOCKER_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: docker_update

#### docker_update

- Schema name: `docker_update`
- Type: object

DockerUpdateArgs parameters.
- No Additional Properties
##### enable_image_updates

- Schema name: `Enable Image Updates`
- Type: boolean

Whether automatic Docker image updates are enabled.

##### pool

- Schema name: `Pool`

Storage pool used for Docker or `null` if not configured.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### address_pools

- Schema name: `Address Pools`
- Type: array of object

Array of network address pools for container networking.
- No Additional Items

###### Each item of this array must be:

###### AddressPool

- Schema name: `AddressPool`
- Type: object
- No Additional Properties
####### base (required)

- Schema name: `Base`
- Type: string
- Type: Format: ipvanyinterface

Base network address with prefix for the pool.

####### size (required)

- Schema name: `Size`
- Type: integer

Subnet size for networks allocated from this pool.
- Value must be greater or equal to `1`

##### cidr_v6

- Schema name: `Cidr V6`
- Type: string
- Type: Format: ipvanyinterface

IPv6 CIDR block for Docker container networking.

##### registry_mirrors

- Schema name: `Registry Mirrors`
- Type: array of object

Array of registry mirrors.
- No Additional Items

###### Each item of this array must be:

###### RegistryMirror

- Schema name: `RegistryMirror`
- Type: object
- No Additional Properties
####### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

URL of the registry mirror.
- Must be at least `1` characters long
- Must be at most `2083` characters long

####### insecure (required)

- Schema name: `Insecure`
- Type: boolean

Whether the registry mirror uses an insecure (HTTP) connection.

##### migrate_applications

- Schema name: `Migrate Applications`
- Type: boolean

Whether to migrate existing applications when changing pools.

### Return value

- Schema name: `DockerEntry`
- Type: object

The updated Docker configuration.
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
