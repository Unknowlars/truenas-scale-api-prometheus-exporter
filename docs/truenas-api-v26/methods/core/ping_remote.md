---
title: core.ping_remote
kind: method
source_rst: _sources/api_methods_core.ping_remote.rst.txt
source_html: api_methods_core.ping_remote.html
required_roles:
  - FULL_ADMIN
---

# core.ping_remote

## Summary

Method that will send an ICMP echo request to "hostname" and will wait up to "timeout" for a reply.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`
- Type: object

CorePingRemoteArgs parameters.
- No Additional Properties
##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "ICMP"

Ping protocol type to use. `ICMP`: Auto-detect IPv4 or IPv6 based on hostname `ICMPV4`: Force IPv4 ping `ICMPV6`: Force IPv6 ping

##### hostname (required)

- Schema name: `Hostname`
- Type: string

Target hostname or IP address to ping.

##### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 4

Timeout in seconds for each ping attempt.
- Value must be greater or equal to `1` and lesser or equal to `60`

##### count

- Schema name: `Count`
- Default: null

Number of ping packets to send or `null` for default.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### interface

- Schema name: `Interface`
- Default: null

Network interface to use for pinging or `null` for default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### interval

- Schema name: `Interval`
- Default: null

Interval between ping packets or `null` for default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if the remote host responded to ping, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
