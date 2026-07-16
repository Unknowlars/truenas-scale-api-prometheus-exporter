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

Update the NFS service configuration.

At least one protocol must remain enabled in `protocols`; the `showmount` command is available only while NFSv3 is enabled. When `servers` is `null`, the number of nfsd is determined automatically from the system's capabilities (between 1 and 32); otherwise it is set to the requested value (1 to 256). The number of mountd processes is always one quarter of the number of nfsd. When `bindip` is empty, NFS listens on all active server addresses. NFS over RDMA, enabled with `rdma`, is only available on supported platforms with an RDMA-capable NIC and uses port 20049.

## Required Roles

- `SHARING_NFS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: nfs_update

#### nfs_update

- Schema name: `nfs_update`
- Type: object

NFSUpdateArgs parameters.
- No Additional Properties
##### servers

- Schema name: `Servers`

Specify the number of nfsd. Default: Number of nfsd is equal number of CPU.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `256`

####### Option 2

- Type: null

##### allow_nonroot

- Schema name: `Allow Nonroot`
- Type: boolean

Allow non-root mount requests. This equates to 'insecure' share option.

##### protocols

- Schema name: `Protocols`
- Type: array of enum (of string)

Specify supported NFS protocols: NFSv3, NFSv4 or both can be listed.
- No Additional Items

###### Each item of this array must be:

- Type: enum (of string)

##### v4_krb

- Schema name: `V4 Krb`
- Type: boolean

Force Kerberos authentication on NFS shares.

##### v4_domain

- Schema name: `V4 Domain`
- Type: string

Specify a DNS domain (NFSv4 only).

##### bindip

- Schema name: `Bindip`
- Type: array of string

Limit the server IP addresses available for NFS.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### mountd_port

- Schema name: `Mountd Port`

Specify the mountd port binding.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

####### Option 2

- Type: null

##### rpcstatd_port

- Schema name: `Rpcstatd Port`

Specify the rpc.statd port binding.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

####### Option 2

- Type: null

##### rpclockd_port

- Schema name: `Rpclockd Port`

Specify the rpc.lockd port binding.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

####### Option 2

- Type: null

##### mountd_log

- Schema name: `Mountd Log`
- Type: boolean

Enable or disable mountd logging.

##### statd_lockd_log

- Schema name: `Statd Lockd Log`
- Type: boolean

Enable or disable statd and lockd logging.

##### userd_manage_gids

- Schema name: `Userd Manage Gids`
- Type: boolean

Enable to allow server to manage gids.

##### rdma

- Schema name: `Rdma`
- Type: boolean

Enable or disable NFS over RDMA. Requires RDMA capable NIC.

### Return value

- Schema name: `NFSEntry`
- Type: object

The updated NFS service configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used as there is only one.

#### servers (required)

- Schema name: `Servers`

Specify the number of nfsd. Default: Number of nfsd is equal number of CPU.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `256`

###### Option 2

- Type: null

#### allow_nonroot (required)

- Schema name: `Allow Nonroot`
- Type: boolean

Allow non-root mount requests. This equates to 'insecure' share option.

#### protocols (required)

- Schema name: `Protocols`
- Type: array of enum (of string)

Specify supported NFS protocols: NFSv3, NFSv4 or both can be listed.
- No Additional Items

##### Each item of this array must be:

- Type: enum (of string)

#### v4_krb (required)

- Schema name: `V4 Krb`
- Type: boolean

Force Kerberos authentication on NFS shares.

#### v4_domain (required)

- Schema name: `V4 Domain`
- Type: string

Specify a DNS domain (NFSv4 only).

#### bindip

- Schema name: `Bindip`
- Type: array of string
- Default: []

Limit the server IP addresses available for NFS.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### mountd_port (required)

- Schema name: `Mountd Port`

Specify the mountd port binding.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

###### Option 2

- Type: null

#### rpcstatd_port (required)

- Schema name: `Rpcstatd Port`

Specify the rpc.statd port binding.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

###### Option 2

- Type: null

#### rpclockd_port (required)

- Schema name: `Rpclockd Port`

Specify the rpc.lockd port binding.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

###### Option 2

- Type: null

#### mountd_log (required)

- Schema name: `Mountd Log`
- Type: boolean

Enable or disable mountd logging.

#### statd_lockd_log (required)

- Schema name: `Statd Lockd Log`
- Type: boolean

Enable or disable statd and lockd logging.

#### v4_krb_enabled (required)

- Schema name: `V4 Krb Enabled`
- Type: boolean

Status of NFSv4 authentication requirement (status only).

#### userd_manage_gids (required)

- Schema name: `Userd Manage Gids`
- Type: boolean

Enable to allow server to manage gids.

#### keytab_has_nfs_spn (required)

- Schema name: `Keytab Has Nfs Spn`
- Type: boolean

Report status of NFS Principal Name in keytab (status only).

#### managed_nfsd (required)

- Schema name: `Managed Nfsd`
- Type: boolean

Report status of 'servers' field. If true, the number of nfsd is managed by the server (status only).

#### rdma (required)

- Schema name: `Rdma`
- Type: boolean

Enable or disable NFS over RDMA. Requires RDMA capable NIC.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
