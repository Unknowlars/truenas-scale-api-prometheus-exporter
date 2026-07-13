---
title: sharing.smb.setacl
kind: method
source_rst: _sources/api_methods_sharing.smb.setacl.rst.txt
source_html: api_methods_sharing.smb.setacl.html
required_roles:
  - SHARING_SMB_WRITE
---

# sharing.smb.setacl

## Summary

Set an ACL on `share_name`. This only impacts access through the SMB protocol.

## Required Roles

- `SHARING_SMB_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: smb_setacl

#### smb_setacl

- Schema name: `smb_setacl`
- Type: object

SharingSMBSetaclArgs parameters.
- No Additional Properties
##### share_name (required)

- Schema name: `Share Name`
- Type: string

Name of the SMB share.
- Must be at least `1` characters long

##### share_acl

- Schema name: `Share Acl`
- Type: array of object
- Default:
```json
[
  {
    "ae_perm": "FULL",
    "ae_type": "ALLOWED",
    "ae_who_sid": "S-1-1-0",
    "ae_who_id": null,
    "ae_who_str": null
  }
]
```

List of SMB share ACL entries.
- No Additional Items

###### Each item of this array must be:

###### SMBShareAclEntry

- Schema name: `SMBShareAclEntry`
- Type: object

An SMB Share ACL Entry that grants or denies specific permissions to a principal. You can identify the principal by a SID (`ae_who_sid`), or Unix ID (`ae_who_id`).
- No Additional Properties
####### ae_perm (required)

- Schema name: `Ae Perm`
- Type: enum (of string)

Permissions granted or denied to the principal. NOTE: this may appear as CUSTOM on read if user has manually edited the share ACL through unsupported means. In this case users will be required to set it to a supported value on update.

####### ae_type (required)

- Schema name: `Ae Type`
- Type: enum (of string)

The type of SMB share ACL entry. This value determines whether the permissions (ae_perm) are granted (ALLOWED) or denied (DENIED).

####### ae_who_sid

- Schema name: `Ae Who Sid`
- Default: null

The SID of the principal to whom this ACL entry applies.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### ae_who_id

- Default: null

The Unix ID of the principal to whom this ACL entry applies.
######## Any of

######### SMBShareAclEntryWhoId

- Schema name: `SMBShareAclEntryWhoId`
- Type: object
- No Additional Properties
########## id_type (required)

- Schema name: `Id Type`
- Type: enum (of string)

The type of Unix ID. If the type is `USER`, the `xid` value refers to a Unix UID. If the type is `GROUP`, the `xid` value refers to a Unix GID.

########## id (required)

- Schema name: `Id`
- Type: integer

Unix user ID (UID) or group ID (GID) depending on the `id_type` field.
- Value must be greater or equal to `0` and lesser or equal to `2147483647`

######### Option 2

- Type: null

####### ae_who_str

- Schema name: `Ae Who Str`
- Default: null

The User or group name of the principal to whom this ACL entry applies.
######## Any of

######### Option 1

- Type: string
- Must be at least `1` characters long

######### Option 2

- Type: null

### Return value

- Schema name: `SMBShareAcl`
- Type: object

The updated SMB share ACL configuration.
- No Additional Properties
#### share_name (required)

- Schema name: `Share Name`
- Type: string

Name of the SMB share.
- Must be at least `1` characters long

#### share_acl

- Schema name: `Share Acl`
- Type: array of object
- Default:
```json
[
  {
    "ae_perm": "FULL",
    "ae_type": "ALLOWED",
    "ae_who_sid": "S-1-1-0",
    "ae_who_id": null,
    "ae_who_str": null
  }
]
```

List of SMB share ACL entries.
- No Additional Items

##### Each item of this array must be:

##### SMBShareAclEntry

- Schema name: `SMBShareAclEntry`
- Type: object

An SMB Share ACL Entry that grants or denies specific permissions to a principal. You can identify the principal by a SID (`ae_who_sid`), or Unix ID (`ae_who_id`).
- No Additional Properties
###### ae_perm (required)

- Schema name: `Ae Perm`
- Type: enum (of string)

Permissions granted or denied to the principal. NOTE: this may appear as CUSTOM on read if user has manually edited the share ACL through unsupported means. In this case users will be required to set it to a supported value on update.

###### ae_type (required)

- Schema name: `Ae Type`
- Type: enum (of string)

The type of SMB share ACL entry. This value determines whether the permissions (ae_perm) are granted (ALLOWED) or denied (DENIED).

###### ae_who_sid

- Schema name: `Ae Who Sid`
- Default: null

The SID of the principal to whom this ACL entry applies.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### ae_who_id

- Default: null

The Unix ID of the principal to whom this ACL entry applies.
####### Any of

######## SMBShareAclEntryWhoId

- Schema name: `SMBShareAclEntryWhoId`
- Type: object
- No Additional Properties
######### id_type (required)

- Schema name: `Id Type`
- Type: enum (of string)

The type of Unix ID. If the type is `USER`, the `xid` value refers to a Unix UID. If the type is `GROUP`, the `xid` value refers to a Unix GID.

######### id (required)

- Schema name: `Id`
- Type: integer

Unix user ID (UID) or group ID (GID) depending on the `id_type` field.
- Value must be greater or equal to `0` and lesser or equal to `2147483647`

######## Option 2

- Type: null

###### ae_who_str

- Schema name: `Ae Who Str`
- Default: null

The User or group name of the principal to whom this ACL entry applies.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
