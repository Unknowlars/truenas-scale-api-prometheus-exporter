---
title: nfs.update
kind: method
source_rst: _sources/api_methods_nfs.update.rst.txt
source_html: api_methods_nfs.update.html
required_roles:
  - SHARING_NFS_WRITE
---

# nfs.update

## Summary

Update NFS Service Configuration.

`servers` - Represents number of servers to create. By default, the number of nfsd is determined by the capabilities of the system. To specify the number of nfsd, set a value between 1 and 256. 'Unset' the field to return to default. This field will always report the number of nfsd to start.

INPUT: 1 .. 256 or 'unset' where unset will enable the automatic determination and 1 ..256 will set the number of nfsd Default: Number of nfsd is automatically determined and will be no less than 1 and no more than 32

The number of mountd will be 1/4 the number of reported nfsd.

`allow_nonroot` - If 'enabled' it allows non-root mount requests to be served.

INPUT: enable/disable (True/False) Default: disabled

`bindip` - Limit the server IP addresses available for NFS By default, NFS will listen on all IP addresses that are active on the server. To specify the server interface or a set of interfaces provide a list of IP's. If the field is unset/empty, NFS listens on all available server addresses.

INPUT: list of IP addresses available configured on the server Default: Use all available addresses (empty list)

`protocols` - enable/disable NFSv3, NFSv4 Both can be enabled or NFSv4 or NFSv4 by themselves. At least one must be enabled. Note: The 'showmount' command is available only if NFSv3 is enabled.

INPUT: Select NFSv3 or NFSv4 or NFSv3,NFSv4 Default: NFSv3,NFSv4

`v4_krb` - Force Kerberos authentication on NFS shares If enabled, NFS shares will fail if the Kerberos ticket is unavilable

INPUT: enable/disable Default: disabled

`v4_domain` - Specify a DNS domain (NFSv4 only) If set, the value will be used to override the default DNS domain name for NFSv4. Specifies the 'Domain' idmapd.conf setting.

INPUT: a string Default: unset, i.e. an empty string.

`mountd_port` - mountd port binding The value set specifies the port mountd(8) binds to.

INPUT: unset or an integer between 1 .. 65535 Default: unset

`rpcstatd_port` - statd port binding The value set specifies the port rpc.statd(8) binds to.

INPUT: unset or an integer between 1 .. 65535 Default: unset

`rpclockd_port` - lockd port binding The value set specifies the port rpclockd_port(8) binds to.

INPUT: unset or an integer between 1 .. 65535 Default: unset

`rdma` - Enable/Disable NFS over RDMA support Available on supported platforms and requires an installed and RDMA capable NIC. NFS over RDMA uses port 20040.

INPUT: Enable/Disable Default: Disable

## Required Roles

- `SHARING_NFS_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: nfs_update

<a id="Call_parameters_items_i0"></a>
#### nfs_update

- Schema name: `nfs_update`
- Type: object

NFSUpdateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_servers"></a>
<a id="Call_parameters_items_i0_servers"></a>
##### servers

- Schema name: `Servers`

Specify the number of nfsd. Default: Number of nfsd is equal number of CPU.
<a id="Call_parameters_items_i0_servers_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_servers_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_servers_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `256`

<a id="tab-pane_Call_parameters_items_i0_servers_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_servers_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_allow_nonroot"></a>
<a id="Call_parameters_items_i0_allow_nonroot"></a>
##### allow_nonroot

- Schema name: `Allow Nonroot`
- Type: boolean

Allow non-root mount requests. This equates to 'insecure' share option.

<a id="headingCall_parameters_items_i0_protocols"></a>
<a id="Call_parameters_items_i0_protocols"></a>
##### protocols

- Schema name: `Protocols`
- Type: array of enum (of string)

Specify supported NFS protocols: NFSv3, NFSv4 or both can be listed.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_protocols_items"></a>
- Type: enum (of string)
###### Must be one of:

- "NFSV3"
- "NFSV4"

<a id="headingCall_parameters_items_i0_v4_krb"></a>
<a id="Call_parameters_items_i0_v4_krb"></a>
##### v4_krb

- Schema name: `V4 Krb`
- Type: boolean

Force Kerberos authentication on NFS shares.

<a id="headingCall_parameters_items_i0_v4_domain"></a>
<a id="Call_parameters_items_i0_v4_domain"></a>
##### v4_domain

- Schema name: `V4 Domain`
- Type: string

Specify a DNS domain (NFSv4 only).

<a id="headingCall_parameters_items_i0_bindip"></a>
<a id="Call_parameters_items_i0_bindip"></a>
##### bindip

- Schema name: `Bindip`
- Type: array of string

Limit the server IP addresses available for NFS.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_bindip_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_mountd_port"></a>
<a id="Call_parameters_items_i0_mountd_port"></a>
##### mountd_port

- Schema name: `Mountd Port`

Specify the mountd port binding.
<a id="Call_parameters_items_i0_mountd_port_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_mountd_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_mountd_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="tab-pane_Call_parameters_items_i0_mountd_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_mountd_port_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_rpcstatd_port"></a>
<a id="Call_parameters_items_i0_rpcstatd_port"></a>
##### rpcstatd_port

- Schema name: `Rpcstatd Port`

Specify the rpc.statd port binding.
<a id="Call_parameters_items_i0_rpcstatd_port_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_rpcstatd_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_rpcstatd_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="tab-pane_Call_parameters_items_i0_rpcstatd_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_rpcstatd_port_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_rpclockd_port"></a>
<a id="Call_parameters_items_i0_rpclockd_port"></a>
##### rpclockd_port

- Schema name: `Rpclockd Port`

Specify the rpc.lockd port binding.
<a id="Call_parameters_items_i0_rpclockd_port_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_rpclockd_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_rpclockd_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="tab-pane_Call_parameters_items_i0_rpclockd_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_rpclockd_port_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_mountd_log"></a>
<a id="Call_parameters_items_i0_mountd_log"></a>
##### mountd_log

- Schema name: `Mountd Log`
- Type: boolean

Enable or disable mountd logging.

<a id="headingCall_parameters_items_i0_statd_lockd_log"></a>
<a id="Call_parameters_items_i0_statd_lockd_log"></a>
##### statd_lockd_log

- Schema name: `Statd Lockd Log`
- Type: boolean

Enable or disable statd and lockd logging.

<a id="headingCall_parameters_items_i0_userd_manage_gids"></a>
<a id="Call_parameters_items_i0_userd_manage_gids"></a>
##### userd_manage_gids

- Schema name: `Userd Manage Gids`
- Type: boolean

Enable to allow server to manage gids.

<a id="headingCall_parameters_items_i0_rdma"></a>
<a id="Call_parameters_items_i0_rdma"></a>
##### rdma

- Schema name: `Rdma`
- Type: boolean

Enable or disable NFS over RDMA. Requires RDMA capable NIC.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NFSEntry`
- Type: object

The updated NFS service configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used as there is only one.

<a id="headingReturn_value_servers"></a>
<a id="Return_value_servers"></a>
#### servers (required)

- Schema name: `Servers`

Specify the number of nfsd. Default: Number of nfsd is equal number of CPU.
<a id="Return_value_servers_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_servers_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_servers_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `256`

<a id="tab-pane_Return_value_servers_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_servers_anyOf_i1)

- Type: null

<a id="headingReturn_value_allow_nonroot"></a>
<a id="Return_value_allow_nonroot"></a>
#### allow_nonroot (required)

- Schema name: `Allow Nonroot`
- Type: boolean

Allow non-root mount requests. This equates to 'insecure' share option.

<a id="headingReturn_value_protocols"></a>
<a id="Return_value_protocols"></a>
#### protocols (required)

- Schema name: `Protocols`
- Type: array of enum (of string)

Specify supported NFS protocols: NFSv3, NFSv4 or both can be listed.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_protocols_items"></a>
- Type: enum (of string)
###### Must be one of:

- "NFSV3"
- "NFSV4"

<a id="headingReturn_value_v4_krb"></a>
<a id="Return_value_v4_krb"></a>
#### v4_krb (required)

- Schema name: `V4 Krb`
- Type: boolean

Force Kerberos authentication on NFS shares.

<a id="headingReturn_value_v4_domain"></a>
<a id="Return_value_v4_domain"></a>
#### v4_domain (required)

- Schema name: `V4 Domain`
- Type: string

Specify a DNS domain (NFSv4 only).

<a id="headingReturn_value_bindip"></a>
<a id="Return_value_bindip"></a>
#### bindip

- Schema name: `Bindip`
- Type: array of string
- Default: []

Limit the server IP addresses available for NFS.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_bindip_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_mountd_port"></a>
<a id="Return_value_mountd_port"></a>
#### mountd_port (required)

- Schema name: `Mountd Port`

Specify the mountd port binding.
<a id="Return_value_mountd_port_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_mountd_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_mountd_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="tab-pane_Return_value_mountd_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_mountd_port_anyOf_i1)

- Type: null

<a id="headingReturn_value_rpcstatd_port"></a>
<a id="Return_value_rpcstatd_port"></a>
#### rpcstatd_port (required)

- Schema name: `Rpcstatd Port`

Specify the rpc.statd port binding.
<a id="Return_value_rpcstatd_port_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_rpcstatd_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_rpcstatd_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="tab-pane_Return_value_rpcstatd_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_rpcstatd_port_anyOf_i1)

- Type: null

<a id="headingReturn_value_rpclockd_port"></a>
<a id="Return_value_rpclockd_port"></a>
#### rpclockd_port (required)

- Schema name: `Rpclockd Port`

Specify the rpc.lockd port binding.
<a id="Return_value_rpclockd_port_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_rpclockd_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_rpclockd_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="tab-pane_Return_value_rpclockd_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_rpclockd_port_anyOf_i1)

- Type: null

<a id="headingReturn_value_mountd_log"></a>
<a id="Return_value_mountd_log"></a>
#### mountd_log (required)

- Schema name: `Mountd Log`
- Type: boolean

Enable or disable mountd logging.

<a id="headingReturn_value_statd_lockd_log"></a>
<a id="Return_value_statd_lockd_log"></a>
#### statd_lockd_log (required)

- Schema name: `Statd Lockd Log`
- Type: boolean

Enable or disable statd and lockd logging.

<a id="headingReturn_value_v4_krb_enabled"></a>
<a id="Return_value_v4_krb_enabled"></a>
#### v4_krb_enabled (required)

- Schema name: `V4 Krb Enabled`
- Type: boolean

Status of NFSv4 authentication requirement (status only).

<a id="headingReturn_value_userd_manage_gids"></a>
<a id="Return_value_userd_manage_gids"></a>
#### userd_manage_gids (required)

- Schema name: `Userd Manage Gids`
- Type: boolean

Enable to allow server to manage gids.

<a id="headingReturn_value_keytab_has_nfs_spn"></a>
<a id="Return_value_keytab_has_nfs_spn"></a>
#### keytab_has_nfs_spn (required)

- Schema name: `Keytab Has Nfs Spn`
- Type: boolean

Report status of NFS Principal Name in keytab (status only).

<a id="headingReturn_value_managed_nfsd"></a>
<a id="Return_value_managed_nfsd"></a>
#### managed_nfsd (required)

- Schema name: `Managed Nfsd`
- Type: boolean

Report status of 'servers' field. If true, the number of nfsd is managed by the server (status only).

<a id="headingReturn_value_rdma"></a>
<a id="Return_value_rdma"></a>
#### rdma (required)

- Schema name: `Rdma`
- Type: boolean

Enable or disable NFS over RDMA. Requires RDMA capable NIC.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
