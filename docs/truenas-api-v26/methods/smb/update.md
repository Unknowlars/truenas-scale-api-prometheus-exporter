---
title: smb.update
kind: method
source_rst: _sources/api_methods_smb.update.rst.txt
source_html: api_methods_smb.update.html
required_roles:
  - SHARING_SMB_WRITE
---

# smb.update

## Summary

Update the SMB service configuration.

The group specified as the SMB `admin_group` is automatically added as a foreign group member of `S-1-5-32-544` (the builtin administrators group), affording the group all privileges granted to a local administrator. Any SMB group may be selected, including Active Directory groups.

Mandatory SMB encryption (`encryption` set to `REQUIRED`) is not compatible with `SMB1` server support.

.. note::

`workgroup` and `netbiosname` must have different values.

.. important::

`smb_options` are raw `smb.conf` parameters that are not covered by the supported configuration options. Not all options are tested or supported, and their behavior may change between releases. Stability of `smb.conf` options is not guaranteed.

## Required Roles

- `SHARING_SMB_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: smb_update

#### smb_update

- Schema name: `smb_update`
- Type: object

SMBUpdateArgs parameters.
- No Additional Properties
##### netbiosname

- Schema name: `Netbiosname`
- Type: string

The NetBIOS name of this server.

##### netbiosalias

- Schema name: `Netbiosalias`
- Type: array of string

Alternative netbios names of the TrueNAS server. These names are announced through NetBIOS name server and registered in Active Directory when TrueNAS joins the domain.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### workgroup

- Schema name: `Workgroup`
- Type: string

Workgroup name. When TrueNAS joins active directory, it automatically changes this value to match the NetBIOS domain of the Active Directory domain.

##### description

- Schema name: `Description`
- Type: string

Description of the SMB server. SMB clients may see this description during some operations.

##### minimum_protocol

- Schema name: `Minimum Protocol`
- Type: enum (of string)

Minimum SMB protocol version permitted for client connections. `SMB1` enables legacy client support (not recommended). `SMB2` is the default. `SMB3` restricts access to modern clients only. NOTE: SMB2 and SMB3 are dialects of the same protocol family; setting `SMB3` as the minimum may break access for networked embedded devices that only support SMB2.

##### unixcharset

- Schema name: `Unixcharset`
- Type: enum (of string)

Select character set for file names on local filesystem. Use this option only if you know the names are not UTF-8.

##### localmaster

- Schema name: `Localmaster`
- Type: boolean

When set to `true` the NetBIOS name server in TrueNAS participates in elections for the local master browser. When set to `false` the NetBIOS name server does not attempt to become a local master browser on a subnet and loses all browsing elections. NOTE: This parameter has no effect if the NetBIOS name server is disabled.

##### syslog

- Schema name: `Syslog`
- Type: boolean

Send log messages to syslog. Enable this option if you want SMB server error logs to be included in information sent to a remote syslog server. NOTE: This requires that remote syslog is globally configured on TrueNAS.

##### aapl_extensions

- Schema name: `Aapl Extensions`
- Type: boolean

Enable support for SMB2/3 AAPL protocol extensions. This setting makes the TrueNAS server advertise support for Apple protocol extensions as a MacOS server. Enabling this is required for Time Machine support.

##### search_protocols

- Schema name: `Search Protocols`
- Type: array of string

List of enabled search protocols for the SMB server. Currently the only support search protocol is SPOTLIGHT for MacOS clients. When SPOTLIGHT search protocol support is enabled, MacOS clients can send spotlight protocol requests to the TrueNAS samba server and receive results from indexed paths.
- No Additional Items

###### Each item of this array must be:

- Type: const

##### admin_group

- Schema name: `Admin Group`

The selected group has full administrator privileges on TrueNAS via the SMB protocol.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### guest

- Schema name: `Guest`
- Type: string

SMB guest account username. This username provides access to legacy SMB shares with guest access enabled. It must be a valid, existing local user account.
- Must be at least `1` characters long

##### filemask

- Schema name: `Filemask`

`smb.conf` create mask. DEFAULT applies current server default which is 664.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: const

##### dirmask

- Schema name: `Dirmask`

`smb.conf` directory mask. DEFAULT applies current server default which is 775.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: const

##### ntlmv1_auth

- Schema name: `Ntlmv1 Auth`
- Type: boolean

Enable legacy and very insecure NTLMv1 authentication. This should never be done except in extreme edge cases and may be against regulations in non-home environments.

##### multichannel

- Schema name: `Multichannel`
- Type: boolean

Enable SMB3 multi-channel support.

##### encryption

- Schema name: `Encryption`
- Type: enum (of string)

SMB2/3 transport encryption setting for the TrueNAS SMB server. `NEGOTIATE`: Enable negotiation of data encryption. Encrypt data only if the client explicitly requests it. `DESIRED`: Enable negotiation of data encryption. Encrypt data on sessions and share connections for clients that support it. `REQUIRED`: Require data encryption for sessions and share connections. NOTE: Clients that do not support encryption cannot access SMB shares. `DEFAULT`: Use the TrueNAS SMB server default encryption settings. Currently, this is the same as `NEGOTIATE`.

##### bindip

- Schema name: `Bindip`
- Type: array of string

List of IP addresses used by the TrueNAS SMB server.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Type: Format: ipvanyinterface

##### server_sid

- Schema name: `Server Sid`

The unique identifier for the TrueNAS SMB server. It also serves as the domain SID for all local SMB user and group accounts.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### smb_options

- Schema name: `Smb Options`
- Type: string

Additional unvalidated and unsupported configuration options for the SMB server. WARNING: Using `smb_options` may produce unexpected server behavior.

##### debug

- Schema name: `Debug`
- Type: boolean

Set SMB log levels to debug. Use this setting only when troubleshooting a specific SMB issue. Do not use it in production environments.

##### stateful_failover

- Schema name: `Stateful Failover`
- Type: boolean

Enterprise feature to ensure SMB state consistency across HA failover events. This feature is incompatible with the following share purposes: MULTIPROTOCOL*SHARE, LEGACY*SHARE. This feature is also incompatible with `minimum_protocol` set to `SMB1`.

### Return value

- Schema name: `SMBEntry`
- Type: object

The updated SMB service configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the SMB service configuration.

#### netbiosname (required)

- Schema name: `Netbiosname`
- Type: string

The NetBIOS name of this server.

#### netbiosalias (required)

- Schema name: `Netbiosalias`
- Type: array of string

Alternative netbios names of the TrueNAS server. These names are announced through NetBIOS name server and registered in Active Directory when TrueNAS joins the domain.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### workgroup (required)

- Schema name: `Workgroup`
- Type: string

Workgroup name. When TrueNAS joins active directory, it automatically changes this value to match the NetBIOS domain of the Active Directory domain.

#### description (required)

- Schema name: `Description`
- Type: string

Description of the SMB server. SMB clients may see this description during some operations.

#### minimum_protocol (required)

- Schema name: `Minimum Protocol`
- Type: enum (of string)

Minimum SMB protocol version permitted for client connections. `SMB1` enables legacy client support (not recommended). `SMB2` is the default. `SMB3` restricts access to modern clients only. NOTE: SMB2 and SMB3 are dialects of the same protocol family; setting `SMB3` as the minimum may break access for networked embedded devices that only support SMB2.

#### unixcharset (required)

- Schema name: `Unixcharset`
- Type: enum (of string)

Select character set for file names on local filesystem. Use this option only if you know the names are not UTF-8.

#### localmaster (required)

- Schema name: `Localmaster`
- Type: boolean

When set to `true` the NetBIOS name server in TrueNAS participates in elections for the local master browser. When set to `false` the NetBIOS name server does not attempt to become a local master browser on a subnet and loses all browsing elections. NOTE: This parameter has no effect if the NetBIOS name server is disabled.

#### syslog (required)

- Schema name: `Syslog`
- Type: boolean

Send log messages to syslog. Enable this option if you want SMB server error logs to be included in information sent to a remote syslog server. NOTE: This requires that remote syslog is globally configured on TrueNAS.

#### aapl_extensions (required)

- Schema name: `Aapl Extensions`
- Type: boolean

Enable support for SMB2/3 AAPL protocol extensions. This setting makes the TrueNAS server advertise support for Apple protocol extensions as a MacOS server. Enabling this is required for Time Machine support.

#### search_protocols

- Schema name: `Search Protocols`
- Type: array of string
- Default: []

List of enabled search protocols for the SMB server. Currently the only support search protocol is SPOTLIGHT for MacOS clients. When SPOTLIGHT search protocol support is enabled, MacOS clients can send spotlight protocol requests to the TrueNAS samba server and receive results from indexed paths.
- No Additional Items

##### Each item of this array must be:

- Type: const

#### admin_group (required)

- Schema name: `Admin Group`

The selected group has full administrator privileges on TrueNAS via the SMB protocol.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### guest (required)

- Schema name: `Guest`
- Type: string

SMB guest account username. This username provides access to legacy SMB shares with guest access enabled. It must be a valid, existing local user account.
- Must be at least `1` characters long

#### filemask (required)

- Schema name: `Filemask`

`smb.conf` create mask. DEFAULT applies current server default which is 664.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: const

#### dirmask (required)

- Schema name: `Dirmask`

`smb.conf` directory mask. DEFAULT applies current server default which is 775.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: const

#### ntlmv1_auth (required)

- Schema name: `Ntlmv1 Auth`
- Type: boolean

Enable legacy and very insecure NTLMv1 authentication. This should never be done except in extreme edge cases and may be against regulations in non-home environments.

#### multichannel (required)

- Schema name: `Multichannel`
- Type: boolean

Enable SMB3 multi-channel support.

#### encryption (required)

- Schema name: `Encryption`
- Type: enum (of string)

SMB2/3 transport encryption setting for the TrueNAS SMB server. `NEGOTIATE`: Enable negotiation of data encryption. Encrypt data only if the client explicitly requests it. `DESIRED`: Enable negotiation of data encryption. Encrypt data on sessions and share connections for clients that support it. `REQUIRED`: Require data encryption for sessions and share connections. NOTE: Clients that do not support encryption cannot access SMB shares. `DEFAULT`: Use the TrueNAS SMB server default encryption settings. Currently, this is the same as `NEGOTIATE`.

#### bindip (required)

- Schema name: `Bindip`
- Type: array of string

List of IP addresses used by the TrueNAS SMB server.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Type: Format: ipvanyinterface

#### server_sid (required)

- Schema name: `Server Sid`

The unique identifier for the TrueNAS SMB server. It also serves as the domain SID for all local SMB user and group accounts.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### smb_options (required)

- Schema name: `Smb Options`
- Type: string

Additional unvalidated and unsupported configuration options for the SMB server. WARNING: Using `smb_options` may produce unexpected server behavior.

#### debug (required)

- Schema name: `Debug`
- Type: boolean

Set SMB log levels to debug. Use this setting only when troubleshooting a specific SMB issue. Do not use it in production environments.

#### stateful_failover (required)

- Schema name: `Stateful Failover`
- Type: boolean

Enterprise feature to ensure SMB state consistency across HA failover events. This feature is incompatible with the following share purposes: MULTIPROTOCOL*SHARE, LEGACY*SHARE. This feature is also incompatible with `minimum_protocol` set to `SMB1`.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
