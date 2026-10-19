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

Update SMB Service Configuration.

`netbiosname` defaults to the original hostname of the system.

`netbiosalias` a list of netbios aliases. If Server is joined to an AD domain, additional Kerberos Service Principal Names will be generated for these aliases.

`workgroup` specifies the NetBIOS workgroup to which the TrueNAS server belongs. This will be automatically set to the correct value during the process of joining an AD domain. NOTE: `workgroup` and `netbiosname` should have different values.

`minimum_protocol` sets the minimum SMB protocol version permitted for client connections.

`aapl_extensions` enables support for SMB2 protocol extensions for MacOS clients. This is not a requirement for MacOS support, but is currently a requirement for time machine support.

`localmaster` when set, determines if the system participates in a browser election.

`guest` attribute is specified to select the account to be used for guest access. It defaults to "nobody".

The group specified as the SMB `admin_group` will be automatically added as a foreign group member of S-1-5-32-544 (builtin\admins). This will afford the group all privileges granted to a local admin. Any SMB group may be selected (including AD groups).

`ntlmv1_auth` enables a legacy and insecure authentication method, which may be required for legacy or poorly-implemented SMB clients.

`encryption` set global server behavior with regard to SMB encrpytion. Options are DEFAULT (which follows the upstream defaults -- currently identical to NEGOTIATE), NEGOTIATE encrypts SMB transport only if requested by the SMB client, DESIRED encrypts SMB transport if supported by the SMB client, REQUIRED only allows encrypted transport to the SMB server. Mandatory SMB encryption is not compatible with SMB1 server support in TrueNAS.

`smb_options` smb.conf parameters that are not covered by the above supported configuration options may be added as an smb_option. Not all options are tested or supported, and behavior of smb_options may change between releases. Stability of smb.conf options is not guaranteed.

## Required Roles

- `SHARING_SMB_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: smb_update

<a id="Call_parameters_items_i0"></a>
#### smb_update

- Schema name: `smb_update`
- Type: object

SMBUpdateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_netbiosname"></a>
<a id="Call_parameters_items_i0_netbiosname"></a>
##### netbiosname

- Schema name: `Netbiosname`
- Type: string

The NetBIOS name of this server.

<a id="headingCall_parameters_items_i0_netbiosalias"></a>
<a id="Call_parameters_items_i0_netbiosalias"></a>
##### netbiosalias

- Schema name: `Netbiosalias`
- Type: array of string

Alternative netbios names of the TrueNAS server. These names are announced through NetBIOS name server and registered in Active Directory when TrueNAS joins the domain.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_netbiosalias_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_workgroup"></a>
<a id="Call_parameters_items_i0_workgroup"></a>
##### workgroup

- Schema name: `Workgroup`
- Type: string

Workgroup name. When TrueNAS joins active directory, it automatically changes this value to match the NetBIOS domain of the Active Directory domain.

<a id="headingCall_parameters_items_i0_description"></a>
<a id="Call_parameters_items_i0_description"></a>
##### description

- Schema name: `Description`
- Type: string

Description of the SMB server. SMB clients may see this description during some operations.

<a id="headingCall_parameters_items_i0_minimum_protocol"></a>
<a id="Call_parameters_items_i0_minimum_protocol"></a>
##### minimum_protocol

- Schema name: `Minimum Protocol`
- Type: enum (of string)

Minimum SMB protocol version permitted for client connections. `SMB1` enables legacy client support (not recommended). `SMB2` is the default. `SMB3` restricts access to modern clients only. NOTE: SMB2 and SMB3 are dialects of the same protocol family; setting `SMB3` as the minimum may break access for networked embedded devices that only support SMB2.
###### Must be one of:

- "SMB1"
- "SMB2"
- "SMB3"

<a id="headingCall_parameters_items_i0_unixcharset"></a>
<a id="Call_parameters_items_i0_unixcharset"></a>
##### unixcharset

- Schema name: `Unixcharset`
- Type: enum (of string)

Select character set for file names on local filesystem. Use this option only if you know the names are not UTF-8.
###### Must be one of:

- "UTF-8"
- "GB2312"
- "HZ-GB-2312"
- "CP1361"
- "BIG5"
- "BIG5HKSCS"
- "CP037"
- "CP273"
- "CP424"
- "CP437"
- "CP500"
- "CP775"
- "CP850"
- "CP852"
- "CP855"
- "CP857"
- "CP858"
- "CP860"
- "CP861"
- "CP862"
- "CP863"
- "CP864"
- "CP865"
- "CP866"
- "CP869"
- "CP932"
- "CP949"
- "CP950"
- "CP1026"
- "CP1125"
- "CP1140"
- "CP1250"
- "CP1251"
- "CP1252"
- "CP1253"
- "CP1254"
- "CP1255"
- "CP1256"
- "CP1257"
- "CP1258"
- "EUC_JIS_2004"
- "EUC_JISX0213"
- "EUC_JP"
- "EUC_KR"
- "GB18030"
- "GBK"
- "HZ"
- "ISO2022_JP"
- "ISO2022_JP_1"
- "ISO2022_JP_2"
- "ISO2022_JP_2004"
- "ISO2022_JP_3"
- "ISO2022_JP_EXT"
- "ISO2022_KR"
- "ISO8859_1"
- "ISO8859_2"
- "ISO8859_3"
- "ISO8859_4"
- "ISO8859_5"
- "ISO8859_6"
- "ISO8859_7"
- "ISO8859_8"
- "ISO8859_9"
- "ISO8859_10"
- "ISO8859_11"
- "ISO8859_13"
- "ISO8859_14"
- "ISO8859_15"
- "ISO8859_16"
- "JOHAB"
- "KOI8_R"
- "KZ1048"
- "LATIN_1"
- "MAC_CYRILLIC"
- "MAC_GREEK"
- "MAC_ICELAND"
- "MAC_LATIN2"
- "MAC_ROMAN"
- "MAC_TURKISH"
- "PTCP154"
- "SHIFT_JIS"
- "SHIFT_JIS_2004"
- "SHIFT_JISX0213"
- "TIS_620"
- "UTF_16"
- "UTF_16_BE"
- "UTF_16_LE"

<a id="headingCall_parameters_items_i0_localmaster"></a>
<a id="Call_parameters_items_i0_localmaster"></a>
##### localmaster

- Schema name: `Localmaster`
- Type: boolean

When set to `true` the NetBIOS name server in TrueNAS participates in elections for the local master browser. When set to `false` the NetBIOS name server does not attempt to become a local master browser on a subnet and loses all browsing elections. NOTE: This parameter has no effect if the NetBIOS name server is disabled.

<a id="headingCall_parameters_items_i0_syslog"></a>
<a id="Call_parameters_items_i0_syslog"></a>
##### syslog

- Schema name: `Syslog`
- Type: boolean

Send log messages to syslog. Enable this option if you want SMB server error logs to be included in information sent to a remote syslog server. NOTE: This requires that remote syslog is globally configured on TrueNAS.

<a id="headingCall_parameters_items_i0_aapl_extensions"></a>
<a id="Call_parameters_items_i0_aapl_extensions"></a>
##### aapl_extensions

- Schema name: `Aapl Extensions`
- Type: boolean

Enable support for SMB2/3 AAPL protocol extensions. This setting makes the TrueNAS server advertise support for Apple protocol extensions as a MacOS server. Enabling this is required for Time Machine support.

<a id="headingCall_parameters_items_i0_search_protocols"></a>
<a id="Call_parameters_items_i0_search_protocols"></a>
##### search_protocols

- Schema name: `Search Protocols`
- Type: array of string

List of enabled search protocols for the SMB server. Currently the only support search protocol is SPOTLIGHT for MacOS clients. When SPOTLIGHT search protocol support is enabled, MacOS clients can send spotlight protocol requests to the TrueNAS samba server and receive results from indexed paths.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_search_protocols_items"></a>
- Type: const
- Specific value: `"SPOTLIGHT"`

<a id="headingCall_parameters_items_i0_admin_group"></a>
<a id="Call_parameters_items_i0_admin_group"></a>
##### admin_group

- Schema name: `Admin Group`

The selected group has full administrator privileges on TrueNAS via the SMB protocol.
<a id="Call_parameters_items_i0_admin_group_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_admin_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_admin_group_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_admin_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_admin_group_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_guest"></a>
<a id="Call_parameters_items_i0_guest"></a>
##### guest

- Schema name: `Guest`
- Type: string

SMB guest account username. This username provides access to legacy SMB shares with guest access enabled. It must be a valid, existing local user account.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_filemask"></a>
<a id="Call_parameters_items_i0_filemask"></a>
##### filemask

- Schema name: `Filemask`

`smb.conf` create mask. DEFAULT applies current server default which is 664.
<a id="Call_parameters_items_i0_filemask_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_filemask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_filemask_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_filemask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_filemask_anyOf_i1)

- Type: const
- Specific value: `"DEFAULT"`

<a id="headingCall_parameters_items_i0_dirmask"></a>
<a id="Call_parameters_items_i0_dirmask"></a>
##### dirmask

- Schema name: `Dirmask`

`smb.conf` directory mask. DEFAULT applies current server default which is 775.
<a id="Call_parameters_items_i0_dirmask_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_dirmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_dirmask_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_dirmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_dirmask_anyOf_i1)

- Type: const
- Specific value: `"DEFAULT"`

<a id="headingCall_parameters_items_i0_ntlmv1_auth"></a>
<a id="Call_parameters_items_i0_ntlmv1_auth"></a>
##### ntlmv1_auth

- Schema name: `Ntlmv1 Auth`
- Type: boolean

Enable legacy and very insecure NTLMv1 authentication. This should never be done except in extreme edge cases and may be against regulations in non-home environments.

<a id="headingCall_parameters_items_i0_multichannel"></a>
<a id="Call_parameters_items_i0_multichannel"></a>
##### multichannel

- Schema name: `Multichannel`
- Type: boolean

Enable SMB3 multi-channel support.

<a id="headingCall_parameters_items_i0_encryption"></a>
<a id="Call_parameters_items_i0_encryption"></a>
##### encryption

- Schema name: `Encryption`
- Type: enum (of string)

SMB2/3 transport encryption setting for the TrueNAS SMB server. `NEGOTIATE`: Enable negotiation of data encryption. Encrypt data only if the client explicitly requests it. `DESIRED`: Enable negotiation of data encryption. Encrypt data on sessions and share connections for clients that support it. `REQUIRED`: Require data encryption for sessions and share connections. NOTE: Clients that do not support encryption cannot access SMB shares. `DEFAULT`: Use the TrueNAS SMB server default encryption settings. Currently, this is the same as `NEGOTIATE`.
###### Must be one of:

- "DEFAULT"
- "NEGOTIATE"
- "DESIRED"
- "REQUIRED"

<a id="headingCall_parameters_items_i0_bindip"></a>
<a id="Call_parameters_items_i0_bindip"></a>
##### bindip

- Schema name: `Bindip`
- Type: array of string

List of IP addresses used by the TrueNAS SMB server.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_bindip_items"></a>
- Type: string
- Type: Format: ipvanyinterface

<a id="headingCall_parameters_items_i0_server_sid"></a>
<a id="Call_parameters_items_i0_server_sid"></a>
##### server_sid

- Schema name: `Server Sid`

The unique identifier for the TrueNAS SMB server. It also serves as the domain SID for all local SMB user and group accounts.
<a id="Call_parameters_items_i0_server_sid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_server_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_server_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_server_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_server_sid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_smb_options"></a>
<a id="Call_parameters_items_i0_smb_options"></a>
##### smb_options

- Schema name: `Smb Options`
- Type: string

Additional unvalidated and unsupported configuration options for the SMB server. WARNING: Using `smb_options` may produce unexpected server behavior.

<a id="headingCall_parameters_items_i0_debug"></a>
<a id="Call_parameters_items_i0_debug"></a>
##### debug

- Schema name: `Debug`
- Type: boolean

Set SMB log levels to debug. Use this setting only when troubleshooting a specific SMB issue. Do not use it in production environments.

<a id="headingCall_parameters_items_i0_stateful_failover"></a>
<a id="Call_parameters_items_i0_stateful_failover"></a>
##### stateful_failover

- Schema name: `Stateful Failover`
- Type: boolean

Enterprise feature to ensure SMB state consistency across HA failover events. This feature is incompatible with the following share purposes: MULTIPROTOCOL*SHARE, LEGACY*SHARE. This feature is also incompatible with `minimum_protocol` set to `SMB1`.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SMBEntry`
- Type: object

The updated SMB service configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the SMB service configuration.

<a id="headingReturn_value_netbiosname"></a>
<a id="Return_value_netbiosname"></a>
#### netbiosname (required)

- Schema name: `Netbiosname`
- Type: string

The NetBIOS name of this server.

<a id="headingReturn_value_netbiosalias"></a>
<a id="Return_value_netbiosalias"></a>
#### netbiosalias (required)

- Schema name: `Netbiosalias`
- Type: array of string

Alternative netbios names of the TrueNAS server. These names are announced through NetBIOS name server and registered in Active Directory when TrueNAS joins the domain.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_netbiosalias_items"></a>
- Type: string

<a id="headingReturn_value_workgroup"></a>
<a id="Return_value_workgroup"></a>
#### workgroup (required)

- Schema name: `Workgroup`
- Type: string

Workgroup name. When TrueNAS joins active directory, it automatically changes this value to match the NetBIOS domain of the Active Directory domain.

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description (required)

- Schema name: `Description`
- Type: string

Description of the SMB server. SMB clients may see this description during some operations.

<a id="headingReturn_value_minimum_protocol"></a>
<a id="Return_value_minimum_protocol"></a>
#### minimum_protocol (required)

- Schema name: `Minimum Protocol`
- Type: enum (of string)

Minimum SMB protocol version permitted for client connections. `SMB1` enables legacy client support (not recommended). `SMB2` is the default. `SMB3` restricts access to modern clients only. NOTE: SMB2 and SMB3 are dialects of the same protocol family; setting `SMB3` as the minimum may break access for networked embedded devices that only support SMB2.
##### Must be one of:

- "SMB1"
- "SMB2"
- "SMB3"

<a id="headingReturn_value_unixcharset"></a>
<a id="Return_value_unixcharset"></a>
#### unixcharset (required)

- Schema name: `Unixcharset`
- Type: enum (of string)

Select character set for file names on local filesystem. Use this option only if you know the names are not UTF-8.
##### Must be one of:

- "UTF-8"
- "GB2312"
- "HZ-GB-2312"
- "CP1361"
- "BIG5"
- "BIG5HKSCS"
- "CP037"
- "CP273"
- "CP424"
- "CP437"
- "CP500"
- "CP775"
- "CP850"
- "CP852"
- "CP855"
- "CP857"
- "CP858"
- "CP860"
- "CP861"
- "CP862"
- "CP863"
- "CP864"
- "CP865"
- "CP866"
- "CP869"
- "CP932"
- "CP949"
- "CP950"
- "CP1026"
- "CP1125"
- "CP1140"
- "CP1250"
- "CP1251"
- "CP1252"
- "CP1253"
- "CP1254"
- "CP1255"
- "CP1256"
- "CP1257"
- "CP1258"
- "EUC_JIS_2004"
- "EUC_JISX0213"
- "EUC_JP"
- "EUC_KR"
- "GB18030"
- "GBK"
- "HZ"
- "ISO2022_JP"
- "ISO2022_JP_1"
- "ISO2022_JP_2"
- "ISO2022_JP_2004"
- "ISO2022_JP_3"
- "ISO2022_JP_EXT"
- "ISO2022_KR"
- "ISO8859_1"
- "ISO8859_2"
- "ISO8859_3"
- "ISO8859_4"
- "ISO8859_5"
- "ISO8859_6"
- "ISO8859_7"
- "ISO8859_8"
- "ISO8859_9"
- "ISO8859_10"
- "ISO8859_11"
- "ISO8859_13"
- "ISO8859_14"
- "ISO8859_15"
- "ISO8859_16"
- "JOHAB"
- "KOI8_R"
- "KZ1048"
- "LATIN_1"
- "MAC_CYRILLIC"
- "MAC_GREEK"
- "MAC_ICELAND"
- "MAC_LATIN2"
- "MAC_ROMAN"
- "MAC_TURKISH"
- "PTCP154"
- "SHIFT_JIS"
- "SHIFT_JIS_2004"
- "SHIFT_JISX0213"
- "TIS_620"
- "UTF_16"
- "UTF_16_BE"
- "UTF_16_LE"

<a id="headingReturn_value_localmaster"></a>
<a id="Return_value_localmaster"></a>
#### localmaster (required)

- Schema name: `Localmaster`
- Type: boolean

When set to `true` the NetBIOS name server in TrueNAS participates in elections for the local master browser. When set to `false` the NetBIOS name server does not attempt to become a local master browser on a subnet and loses all browsing elections. NOTE: This parameter has no effect if the NetBIOS name server is disabled.

<a id="headingReturn_value_syslog"></a>
<a id="Return_value_syslog"></a>
#### syslog (required)

- Schema name: `Syslog`
- Type: boolean

Send log messages to syslog. Enable this option if you want SMB server error logs to be included in information sent to a remote syslog server. NOTE: This requires that remote syslog is globally configured on TrueNAS.

<a id="headingReturn_value_aapl_extensions"></a>
<a id="Return_value_aapl_extensions"></a>
#### aapl_extensions (required)

- Schema name: `Aapl Extensions`
- Type: boolean

Enable support for SMB2/3 AAPL protocol extensions. This setting makes the TrueNAS server advertise support for Apple protocol extensions as a MacOS server. Enabling this is required for Time Machine support.

<a id="headingReturn_value_search_protocols"></a>
<a id="Return_value_search_protocols"></a>
#### search_protocols

- Schema name: `Search Protocols`
- Type: array of string
- Default: []

List of enabled search protocols for the SMB server. Currently the only support search protocol is SPOTLIGHT for MacOS clients. When SPOTLIGHT search protocol support is enabled, MacOS clients can send spotlight protocol requests to the TrueNAS samba server and receive results from indexed paths.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_search_protocols_items"></a>
- Type: const
- Specific value: `"SPOTLIGHT"`

<a id="headingReturn_value_admin_group"></a>
<a id="Return_value_admin_group"></a>
#### admin_group (required)

- Schema name: `Admin Group`

The selected group has full administrator privileges on TrueNAS via the SMB protocol.
<a id="Return_value_admin_group_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_admin_group_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_admin_group_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_admin_group_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_admin_group_anyOf_i1)

- Type: null

<a id="headingReturn_value_guest"></a>
<a id="Return_value_guest"></a>
#### guest (required)

- Schema name: `Guest`
- Type: string

SMB guest account username. This username provides access to legacy SMB shares with guest access enabled. It must be a valid, existing local user account.
- Must be at least `1` characters long

<a id="headingReturn_value_filemask"></a>
<a id="Return_value_filemask"></a>
#### filemask (required)

- Schema name: `Filemask`

`smb.conf` create mask. DEFAULT applies current server default which is 664.
<a id="Return_value_filemask_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_filemask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_filemask_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_filemask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_filemask_anyOf_i1)

- Type: const
- Specific value: `"DEFAULT"`

<a id="headingReturn_value_dirmask"></a>
<a id="Return_value_dirmask"></a>
#### dirmask (required)

- Schema name: `Dirmask`

`smb.conf` directory mask. DEFAULT applies current server default which is 775.
<a id="Return_value_dirmask_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dirmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dirmask_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_dirmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dirmask_anyOf_i1)

- Type: const
- Specific value: `"DEFAULT"`

<a id="headingReturn_value_ntlmv1_auth"></a>
<a id="Return_value_ntlmv1_auth"></a>
#### ntlmv1_auth (required)

- Schema name: `Ntlmv1 Auth`
- Type: boolean

Enable legacy and very insecure NTLMv1 authentication. This should never be done except in extreme edge cases and may be against regulations in non-home environments.

<a id="headingReturn_value_multichannel"></a>
<a id="Return_value_multichannel"></a>
#### multichannel (required)

- Schema name: `Multichannel`
- Type: boolean

Enable SMB3 multi-channel support.

<a id="headingReturn_value_encryption"></a>
<a id="Return_value_encryption"></a>
#### encryption (required)

- Schema name: `Encryption`
- Type: enum (of string)

SMB2/3 transport encryption setting for the TrueNAS SMB server. `NEGOTIATE`: Enable negotiation of data encryption. Encrypt data only if the client explicitly requests it. `DESIRED`: Enable negotiation of data encryption. Encrypt data on sessions and share connections for clients that support it. `REQUIRED`: Require data encryption for sessions and share connections. NOTE: Clients that do not support encryption cannot access SMB shares. `DEFAULT`: Use the TrueNAS SMB server default encryption settings. Currently, this is the same as `NEGOTIATE`.
##### Must be one of:

- "DEFAULT"
- "NEGOTIATE"
- "DESIRED"
- "REQUIRED"

<a id="headingReturn_value_bindip"></a>
<a id="Return_value_bindip"></a>
#### bindip (required)

- Schema name: `Bindip`
- Type: array of string

List of IP addresses used by the TrueNAS SMB server.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_bindip_items"></a>
- Type: string
- Type: Format: ipvanyinterface

<a id="headingReturn_value_server_sid"></a>
<a id="Return_value_server_sid"></a>
#### server_sid (required)

- Schema name: `Server Sid`

The unique identifier for the TrueNAS SMB server. It also serves as the domain SID for all local SMB user and group accounts.
<a id="Return_value_server_sid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_server_sid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_server_sid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_server_sid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_server_sid_anyOf_i1)

- Type: null

<a id="headingReturn_value_smb_options"></a>
<a id="Return_value_smb_options"></a>
#### smb_options (required)

- Schema name: `Smb Options`
- Type: string

Additional unvalidated and unsupported configuration options for the SMB server. WARNING: Using `smb_options` may produce unexpected server behavior.

<a id="headingReturn_value_debug"></a>
<a id="Return_value_debug"></a>
#### debug (required)

- Schema name: `Debug`
- Type: boolean

Set SMB log levels to debug. Use this setting only when troubleshooting a specific SMB issue. Do not use it in production environments.

<a id="headingReturn_value_stateful_failover"></a>
<a id="Return_value_stateful_failover"></a>
#### stateful_failover (required)

- Schema name: `Stateful Failover`
- Type: boolean

Enterprise feature to ensure SMB state consistency across HA failover events. This feature is incompatible with the following share purposes: MULTIPROTOCOL*SHARE, LEGACY*SHARE. This feature is also incompatible with `minimum_protocol` set to `SMB1`.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
