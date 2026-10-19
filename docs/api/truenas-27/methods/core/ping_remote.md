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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

<a id="Call_parameters_items_i0"></a>
#### options

- Schema name: `options`
- Type: object

CorePingRemoteArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_type"></a>
<a id="Call_parameters_items_i0_type"></a>
##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "ICMP"

Ping protocol type to use. `ICMP`: Auto-detect IPv4 or IPv6 based on hostname `ICMPV4`: Force IPv4 ping `ICMPV6`: Force IPv6 ping
###### Must be one of:

- "ICMP"
- "ICMPV4"
- "ICMPV6"

<a id="headingCall_parameters_items_i0_hostname"></a>
<a id="Call_parameters_items_i0_hostname"></a>
##### hostname (required)

- Schema name: `Hostname`
- Type: string

Target hostname or IP address to ping.

<a id="headingCall_parameters_items_i0_timeout"></a>
<a id="Call_parameters_items_i0_timeout"></a>
##### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 4

Timeout in seconds for each ping attempt.
- Value must be greater or equal to `1` and lesser or equal to `60`

<a id="headingCall_parameters_items_i0_count"></a>
<a id="Call_parameters_items_i0_count"></a>
##### count

- Schema name: `Count`
- Default: null

Number of ping packets to send or `null` for default.
<a id="Call_parameters_items_i0_count_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_count_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_count_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_count_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_count_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_interface"></a>
<a id="Call_parameters_items_i0_interface"></a>
##### interface

- Schema name: `Interface`
- Default: null

Network interface to use for pinging or `null` for default.
<a id="Call_parameters_items_i0_interface_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_interface_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_interface_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_interval"></a>
<a id="Call_parameters_items_i0_interval"></a>
##### interval

- Schema name: `Interval`
- Default: null

Interval between ping packets or `null` for default.
<a id="Call_parameters_items_i0_interval_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_interval_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_interval_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_interval_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_interval_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if the remote host responded to ping, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
