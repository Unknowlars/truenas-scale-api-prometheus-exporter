---
title: smb.unixcharset_choices
kind: method
source_rst: _sources/api_methods_smb.unixcharset_choices.rst.txt
source_html: api_methods_smb.unixcharset_choices.html
required_roles:
  - READONLY_ADMIN
  - SHARING_SMB_READ
---

# smb.unixcharset_choices

## Summary

Return the available UNIX character set choices for the `unixcharset` field in the SMB service configuration.

## Required Roles

- `READONLY_ADMIN`
- `SHARING_SMB_READ`

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

- Schema name: `Result`
- Type: object

Available character set choices for Unix charset configuration.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: enum (of string)
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

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
