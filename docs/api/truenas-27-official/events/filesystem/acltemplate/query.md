---
title: filesystem.acltemplate.query
kind: event
source_rst: _sources/api_events_filesystem.acltemplate.query.rst.txt
source_html: api_events_filesystem.acltemplate.query.html
required_roles:
  - FILESYSTEM_ATTRS_READ
---

# filesystem.acltemplate.query

## Summary

Sent on filesystem.acltemplate changes.

## Required Roles

- `FILESYSTEM_ATTRS_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `ACLTemplateAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `ACLTemplateEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the ACL template.

<a id="headingADDED_fields_builtin"></a>
<a id="ADDED_fields_builtin"></a>
##### builtin (required)

- Schema name: `Builtin`
- Type: boolean

Whether this is a built-in system template or user-created.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the ACL template.

<a id="headingADDED_fields_acltype"></a>
<a id="ADDED_fields_acltype"></a>
##### acltype (required)

- Schema name: `Acltype`
- Type: enum (of string)

ACL type this template provides.
###### Must be one of:

- "NFS4"
- "POSIX1E"

<a id="headingADDED_fields_acl"></a>
<a id="ADDED_fields_acl"></a>
##### acl (required)

- Schema name: `Acl`

Array of Access Control Entries defined by this template.
<a id="ADDED_fields_acl_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acl_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_acl_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_acl_anyOf_i0_items"></a>
###### NFS4ACE

- Schema name: `NFS4ACE`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_acl_anyOf_i0_items_tag"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this ACE. `owner@`: File/directory owner `group@`: File/directory primary group `everyone@`: All users `USER`: Specific user account `GROUP`: Specific group
###### Must be one of:

- "owner@"
- "group@"
- "everyone@"
- "USER"
- "GROUP"

<a id="headingADDED_fields_acl_anyOf_i0_items_type"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Access control type. `ALLOW`: Grant the specified permissions `DENY`: Explicitly deny the specified permissions
###### Must be one of:

- "ALLOW"
- "DENY"

<a id="headingADDED_fields_acl_anyOf_i0_items_perms"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms"></a>
###### perms (required)

- Schema name: `Perms`

Permissions granted or denied by this ACE.
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0"></a>
###### [NFS4ACE_AdvancedPerms](#tab-pane_ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_DATA"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_DATA"></a>
###### READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_DATA"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_DATA"></a>
###### WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_APPEND_DATA"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_APPEND_DATA"></a>
###### APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
###### READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
###### WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_EXECUTE"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_EXECUTE"></a>
###### EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_DELETE"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_DELETE"></a>
###### DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_DELETE_CHILD"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_DELETE_CHILD"></a>
###### DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
###### READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
###### WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_ACL"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_ACL"></a>
###### READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ACL"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ACL"></a>
###### WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_OWNER"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_OWNER"></a>
###### WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_SYNCHRONIZE"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i0_SYNCHRONIZE"></a>
###### SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

<a id="tab-pane_ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i1"></a>
###### [NFS4ACE_BasicPerms](#tab-pane_ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i1)

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_acl_anyOf_i0_items_perms_anyOf_i1_BASIC"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_perms_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only
###### Must be one of:

- "FULL_CONTROL"
- "MODIFY"
- "READ"
- "TRAVERSE"

<a id="headingADDED_fields_acl_anyOf_i0_items_flags"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_flags"></a>
###### flags (required)

- Schema name: `Flags`

Inheritance and other behavioral flags for this ACE.
<a id="ADDED_fields_acl_anyOf_i0_items_flags_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0"></a>
###### [NFS4ACE_AdvancedFlags](#tab-pane_ADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0_FILE_INHERIT"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0_FILE_INHERIT"></a>
###### FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

<a id="headingADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
###### DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

<a id="headingADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
###### NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

<a id="headingADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0_INHERIT_ONLY"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0_INHERIT_ONLY"></a>
###### INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

<a id="headingADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0_INHERITED"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_flags_anyOf_i0_INHERITED"></a>
###### INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

<a id="tab-pane_ADDED_fields_acl_anyOf_i0_items_flags_anyOf_i1"></a>
###### [NFS4ACE_BasicFlags](#tab-pane_ADDED_fields_acl_anyOf_i0_items_flags_anyOf_i1)

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_acl_anyOf_i0_items_flags_anyOf_i1_BASIC"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_flags_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects
###### Must be one of:

- "INHERIT"
- "NOINHERIT"

<a id="headingADDED_fields_acl_anyOf_i0_items_id"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

UID or GID when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="ADDED_fields_acl_anyOf_i0_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acl_anyOf_i0_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_acl_anyOf_i0_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_ADDED_fields_acl_anyOf_i0_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_acl_anyOf_i0_items_id_anyOf_i1)

- Type: null

<a id="headingADDED_fields_acl_anyOf_i0_items_who"></a>
<a id="ADDED_fields_acl_anyOf_i0_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="ADDED_fields_acl_anyOf_i0_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acl_anyOf_i0_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_acl_anyOf_i0_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_acl_anyOf_i0_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_acl_anyOf_i0_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_acl_anyOf_i0_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_ADDED_fields_acl_anyOf_i0_items_who_anyOf_i2)

- Type: null

<a id="tab-pane_ADDED_fields_acl_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_acl_anyOf_i1)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_acl_anyOf_i1_items"></a>
###### POSIXACE

- Schema name: `POSIXACE`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_acl_anyOf_i1_items_tag"></a>
<a id="ADDED_fields_acl_anyOf_i1_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this POSIX ACE. `USER_OBJ`: File/directory owner `GROUP_OBJ`: File/directory primary group `OTHER`: All other users `MASK`: Maximum permissions for named users and groups `USER`: Specific user account `GROUP`: Specific group
###### Must be one of:

- "USER_OBJ"
- "GROUP_OBJ"
- "OTHER"
- "MASK"
- "USER"
- "GROUP"

<a id="headingADDED_fields_acl_anyOf_i1_items_perms"></a>
<a id="ADDED_fields_acl_anyOf_i1_items_perms"></a>
###### perms (required)

- Schema name: `POSIXACE_Perms`
- Type: object

Read, write, and execute permissions for this ACE.
- No Additional Properties
<a id="headingADDED_fields_acl_anyOf_i1_items_perms_READ"></a>
<a id="ADDED_fields_acl_anyOf_i1_items_perms_READ"></a>
###### READ (required)

- Schema name: `Read`
- Type: boolean

Permission to read file contents or list directory contents.

<a id="headingADDED_fields_acl_anyOf_i1_items_perms_WRITE"></a>
<a id="ADDED_fields_acl_anyOf_i1_items_perms_WRITE"></a>
###### WRITE (required)

- Schema name: `Write`
- Type: boolean

Permission to write file contents or create/delete files in directory.

<a id="headingADDED_fields_acl_anyOf_i1_items_perms_EXECUTE"></a>
<a id="ADDED_fields_acl_anyOf_i1_items_perms_EXECUTE"></a>
###### EXECUTE (required)

- Schema name: `Execute`
- Type: boolean

Permission to execute files or traverse directories.

<a id="headingADDED_fields_acl_anyOf_i1_items_default"></a>
<a id="ADDED_fields_acl_anyOf_i1_items_default"></a>
###### default (required)

- Schema name: `Default`
- Type: boolean

Whether this is a default ACE that applies to newly created child objects.

<a id="headingADDED_fields_acl_anyOf_i1_items_id"></a>
<a id="ADDED_fields_acl_anyOf_i1_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

Numeric user or group ID when tag is `USER` or `GROUP`. `null` for object entries.
<a id="ADDED_fields_acl_anyOf_i1_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acl_anyOf_i1_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_acl_anyOf_i1_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_ADDED_fields_acl_anyOf_i1_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_acl_anyOf_i1_items_id_anyOf_i1)

- Type: null

<a id="headingADDED_fields_acl_anyOf_i1_items_who"></a>
<a id="ADDED_fields_acl_anyOf_i1_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when tag is `USER` or `GROUP`. `null` for object entries.
<a id="ADDED_fields_acl_anyOf_i1_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_acl_anyOf_i1_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_acl_anyOf_i1_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_acl_anyOf_i1_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_acl_anyOf_i1_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_acl_anyOf_i1_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_ADDED_fields_acl_anyOf_i1_items_who_anyOf_i2)

- Type: null

<a id="headingADDED_fields_comment"></a>
<a id="ADDED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment about the template's purpose.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `ACLTemplateChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `ACLTemplateEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the ACL template.

<a id="headingCHANGED_fields_builtin"></a>
<a id="CHANGED_fields_builtin"></a>
##### builtin (required)

- Schema name: `Builtin`
- Type: boolean

Whether this is a built-in system template or user-created.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the ACL template.

<a id="headingCHANGED_fields_acltype"></a>
<a id="CHANGED_fields_acltype"></a>
##### acltype (required)

- Schema name: `Acltype`
- Type: enum (of string)

ACL type this template provides.
###### Must be one of:

- "NFS4"
- "POSIX1E"

<a id="headingCHANGED_fields_acl"></a>
<a id="CHANGED_fields_acl"></a>
##### acl (required)

- Schema name: `Acl`

Array of Access Control Entries defined by this template.
<a id="CHANGED_fields_acl_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acl_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_acl_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_acl_anyOf_i0_items"></a>
###### NFS4ACE

- Schema name: `NFS4ACE`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_acl_anyOf_i0_items_tag"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this ACE. `owner@`: File/directory owner `group@`: File/directory primary group `everyone@`: All users `USER`: Specific user account `GROUP`: Specific group
###### Must be one of:

- "owner@"
- "group@"
- "everyone@"
- "USER"
- "GROUP"

<a id="headingCHANGED_fields_acl_anyOf_i0_items_type"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Access control type. `ALLOW`: Grant the specified permissions `DENY`: Explicitly deny the specified permissions
###### Must be one of:

- "ALLOW"
- "DENY"

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms"></a>
###### perms (required)

- Schema name: `Perms`

Permissions granted or denied by this ACE.
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0"></a>
###### [NFS4ACE_AdvancedPerms](#tab-pane_CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_DATA"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_DATA"></a>
###### READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_DATA"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_DATA"></a>
###### WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_APPEND_DATA"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_APPEND_DATA"></a>
###### APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
###### READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
###### WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_EXECUTE"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_EXECUTE"></a>
###### EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_DELETE"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_DELETE"></a>
###### DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_DELETE_CHILD"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_DELETE_CHILD"></a>
###### DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
###### READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
###### WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_ACL"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_READ_ACL"></a>
###### READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ACL"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ACL"></a>
###### WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_OWNER"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_OWNER"></a>
###### WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_SYNCHRONIZE"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i0_SYNCHRONIZE"></a>
###### SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

<a id="tab-pane_CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i1"></a>
###### [NFS4ACE_BasicPerms](#tab-pane_CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i1)

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i1_BASIC"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_perms_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only
###### Must be one of:

- "FULL_CONTROL"
- "MODIFY"
- "READ"
- "TRAVERSE"

<a id="headingCHANGED_fields_acl_anyOf_i0_items_flags"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_flags"></a>
###### flags (required)

- Schema name: `Flags`

Inheritance and other behavioral flags for this ACE.
<a id="CHANGED_fields_acl_anyOf_i0_items_flags_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0"></a>
###### [NFS4ACE_AdvancedFlags](#tab-pane_CHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0_FILE_INHERIT"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0_FILE_INHERIT"></a>
###### FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
###### DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
###### NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0_INHERIT_ONLY"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0_INHERIT_ONLY"></a>
###### INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

<a id="headingCHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0_INHERITED"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i0_INHERITED"></a>
###### INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

<a id="tab-pane_CHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i1"></a>
###### [NFS4ACE_BasicFlags](#tab-pane_CHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i1)

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i1_BASIC"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_flags_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects
###### Must be one of:

- "INHERIT"
- "NOINHERIT"

<a id="headingCHANGED_fields_acl_anyOf_i0_items_id"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

UID or GID when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="CHANGED_fields_acl_anyOf_i0_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acl_anyOf_i0_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_acl_anyOf_i0_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_CHANGED_fields_acl_anyOf_i0_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_acl_anyOf_i0_items_id_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_acl_anyOf_i0_items_who"></a>
<a id="CHANGED_fields_acl_anyOf_i0_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="CHANGED_fields_acl_anyOf_i0_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acl_anyOf_i0_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_acl_anyOf_i0_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_acl_anyOf_i0_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_acl_anyOf_i0_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_acl_anyOf_i0_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_CHANGED_fields_acl_anyOf_i0_items_who_anyOf_i2)

- Type: null

<a id="tab-pane_CHANGED_fields_acl_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_acl_anyOf_i1)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_acl_anyOf_i1_items"></a>
###### POSIXACE

- Schema name: `POSIXACE`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_acl_anyOf_i1_items_tag"></a>
<a id="CHANGED_fields_acl_anyOf_i1_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this POSIX ACE. `USER_OBJ`: File/directory owner `GROUP_OBJ`: File/directory primary group `OTHER`: All other users `MASK`: Maximum permissions for named users and groups `USER`: Specific user account `GROUP`: Specific group
###### Must be one of:

- "USER_OBJ"
- "GROUP_OBJ"
- "OTHER"
- "MASK"
- "USER"
- "GROUP"

<a id="headingCHANGED_fields_acl_anyOf_i1_items_perms"></a>
<a id="CHANGED_fields_acl_anyOf_i1_items_perms"></a>
###### perms (required)

- Schema name: `POSIXACE_Perms`
- Type: object

Read, write, and execute permissions for this ACE.
- No Additional Properties
<a id="headingCHANGED_fields_acl_anyOf_i1_items_perms_READ"></a>
<a id="CHANGED_fields_acl_anyOf_i1_items_perms_READ"></a>
###### READ (required)

- Schema name: `Read`
- Type: boolean

Permission to read file contents or list directory contents.

<a id="headingCHANGED_fields_acl_anyOf_i1_items_perms_WRITE"></a>
<a id="CHANGED_fields_acl_anyOf_i1_items_perms_WRITE"></a>
###### WRITE (required)

- Schema name: `Write`
- Type: boolean

Permission to write file contents or create/delete files in directory.

<a id="headingCHANGED_fields_acl_anyOf_i1_items_perms_EXECUTE"></a>
<a id="CHANGED_fields_acl_anyOf_i1_items_perms_EXECUTE"></a>
###### EXECUTE (required)

- Schema name: `Execute`
- Type: boolean

Permission to execute files or traverse directories.

<a id="headingCHANGED_fields_acl_anyOf_i1_items_default"></a>
<a id="CHANGED_fields_acl_anyOf_i1_items_default"></a>
###### default (required)

- Schema name: `Default`
- Type: boolean

Whether this is a default ACE that applies to newly created child objects.

<a id="headingCHANGED_fields_acl_anyOf_i1_items_id"></a>
<a id="CHANGED_fields_acl_anyOf_i1_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

Numeric user or group ID when tag is `USER` or `GROUP`. `null` for object entries.
<a id="CHANGED_fields_acl_anyOf_i1_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acl_anyOf_i1_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_acl_anyOf_i1_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_CHANGED_fields_acl_anyOf_i1_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_acl_anyOf_i1_items_id_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_acl_anyOf_i1_items_who"></a>
<a id="CHANGED_fields_acl_anyOf_i1_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when tag is `USER` or `GROUP`. `null` for object entries.
<a id="CHANGED_fields_acl_anyOf_i1_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_acl_anyOf_i1_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_acl_anyOf_i1_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_acl_anyOf_i1_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_acl_anyOf_i1_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_acl_anyOf_i1_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_CHANGED_fields_acl_anyOf_i1_items_who_anyOf_i2)

- Type: null

<a id="headingCHANGED_fields_comment"></a>
<a id="CHANGED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment about the template's purpose.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `ACLTemplateRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
