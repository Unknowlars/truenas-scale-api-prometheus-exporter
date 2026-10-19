---
title: filesystem.acltemplate.create
kind: method
source_rst: _sources/api_methods_filesystem.acltemplate.create.rst.txt
source_html: api_methods_filesystem.acltemplate.create.html
required_roles:
  - FILESYSTEM_ATTRS_WRITE
---

# filesystem.acltemplate.create

## Summary

Create a new filesystem ACL template.

## Required Roles

- `FILESYSTEM_ATTRS_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: acltemplate_create

<a id="Call_parameters_items_i0"></a>
#### acltemplate_create

- Schema name: `acltemplate_create`
- Type: object

ACL template configuration data for the new template.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the ACL template.

<a id="headingCall_parameters_items_i0_acltype"></a>
<a id="Call_parameters_items_i0_acltype"></a>
##### acltype (required)

- Schema name: `Acltype`
- Type: enum (of string)

ACL type this template provides.
###### Must be one of:

- "NFS4"
- "POSIX1E"

<a id="headingCall_parameters_items_i0_acl"></a>
<a id="Call_parameters_items_i0_acl"></a>
##### acl (required)

- Schema name: `Acl`

Array of Access Control Entries defined by this template.
<a id="Call_parameters_items_i0_acl_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_acl_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_acl_anyOf_i0_items"></a>
###### NFS4ACE

- Schema name: `NFS4ACE`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_tag"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_tag"></a>
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

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_type"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Access control type. `ALLOW`: Grant the specified permissions `DENY`: Explicitly deny the specified permissions
###### Must be one of:

- "ALLOW"
- "DENY"

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms"></a>
###### perms (required)

- Schema name: `Perms`

Permissions granted or denied by this ACE.
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0"></a>
###### [NFS4ACE_AdvancedPerms](#tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_READ_DATA"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_READ_DATA"></a>
###### READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_DATA"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_DATA"></a>
###### WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_APPEND_DATA"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_APPEND_DATA"></a>
###### APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
###### READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
###### WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_EXECUTE"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_EXECUTE"></a>
###### EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_DELETE"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_DELETE"></a>
###### DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_DELETE_CHILD"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_DELETE_CHILD"></a>
###### DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
###### READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
###### WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_READ_ACL"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_READ_ACL"></a>
###### READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ACL"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ACL"></a>
###### WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_OWNER"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_OWNER"></a>
###### WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_SYNCHRONIZE"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i0_SYNCHRONIZE"></a>
###### SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i1"></a>
###### [NFS4ACE_BasicPerms](#tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i1)

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i1_BASIC"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_perms_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only
###### Must be one of:

- "FULL_CONTROL"
- "MODIFY"
- "READ"
- "TRAVERSE"

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_flags"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_flags"></a>
###### flags (required)

- Schema name: `Flags`

Inheritance and other behavioral flags for this ACE.
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0"></a>
###### [NFS4ACE_AdvancedFlags](#tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0_FILE_INHERIT"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0_FILE_INHERIT"></a>
###### FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
###### DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
###### NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0_INHERIT_ONLY"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0_INHERIT_ONLY"></a>
###### INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0_INHERITED"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i0_INHERITED"></a>
###### INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i1"></a>
###### [NFS4ACE_BasicFlags](#tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i1)

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i1_BASIC"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_flags_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects
###### Must be one of:

- "INHERIT"
- "NOINHERIT"

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_id"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

UID or GID when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_id_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_acl_anyOf_i0_items_who"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="Call_parameters_items_i0_acl_anyOf_i0_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_Call_parameters_items_i0_acl_anyOf_i0_items_who_anyOf_i2)

- Type: null

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_acl_anyOf_i1)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_acl_anyOf_i1_items"></a>
###### POSIXACE

- Schema name: `POSIXACE`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_acl_anyOf_i1_items_tag"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i1_items_tag"></a>
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

<a id="headingCall_parameters_items_i0_acl_anyOf_i1_items_perms"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i1_items_perms"></a>
###### perms (required)

- Schema name: `POSIXACE_Perms`
- Type: object

Read, write, and execute permissions for this ACE.
- No Additional Properties
<a id="headingCall_parameters_items_i0_acl_anyOf_i1_items_perms_READ"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i1_items_perms_READ"></a>
###### READ (required)

- Schema name: `Read`
- Type: boolean

Permission to read file contents or list directory contents.

<a id="headingCall_parameters_items_i0_acl_anyOf_i1_items_perms_WRITE"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i1_items_perms_WRITE"></a>
###### WRITE (required)

- Schema name: `Write`
- Type: boolean

Permission to write file contents or create/delete files in directory.

<a id="headingCall_parameters_items_i0_acl_anyOf_i1_items_perms_EXECUTE"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i1_items_perms_EXECUTE"></a>
###### EXECUTE (required)

- Schema name: `Execute`
- Type: boolean

Permission to execute files or traverse directories.

<a id="headingCall_parameters_items_i0_acl_anyOf_i1_items_default"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i1_items_default"></a>
###### default (required)

- Schema name: `Default`
- Type: boolean

Whether this is a default ACE that applies to newly created child objects.

<a id="headingCall_parameters_items_i0_acl_anyOf_i1_items_id"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i1_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

Numeric user or group ID when tag is `USER` or `GROUP`. `null` for object entries.
<a id="Call_parameters_items_i0_acl_anyOf_i1_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i1_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_acl_anyOf_i1_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i1_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_acl_anyOf_i1_items_id_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_acl_anyOf_i1_items_who"></a>
<a id="Call_parameters_items_i0_acl_anyOf_i1_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when tag is `USER` or `GROUP`. `null` for object entries.
<a id="Call_parameters_items_i0_acl_anyOf_i1_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i1_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_acl_anyOf_i1_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i1_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_acl_anyOf_i1_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_acl_anyOf_i1_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_Call_parameters_items_i0_acl_anyOf_i1_items_who_anyOf_i2)

- Type: null

<a id="headingCall_parameters_items_i0_comment"></a>
<a id="Call_parameters_items_i0_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment about the template's purpose.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ACLTemplateEntry`
- Type: object

The created ACL template configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the ACL template.

<a id="headingReturn_value_builtin"></a>
<a id="Return_value_builtin"></a>
#### builtin (required)

- Schema name: `Builtin`
- Type: boolean

Whether this is a built-in system template or user-created.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the ACL template.

<a id="headingReturn_value_acltype"></a>
<a id="Return_value_acltype"></a>
#### acltype (required)

- Schema name: `Acltype`
- Type: enum (of string)

ACL type this template provides.
##### Must be one of:

- "NFS4"
- "POSIX1E"

<a id="headingReturn_value_acl"></a>
<a id="Return_value_acl"></a>
#### acl (required)

- Schema name: `Acl`

Array of Access Control Entries defined by this template.
<a id="Return_value_acl_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_acl_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_acl_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_acl_anyOf_i0_items"></a>
###### NFS4ACE

- Schema name: `NFS4ACE`
- Type: object
- No Additional Properties
<a id="headingReturn_value_acl_anyOf_i0_items_tag"></a>
<a id="Return_value_acl_anyOf_i0_items_tag"></a>
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

<a id="headingReturn_value_acl_anyOf_i0_items_type"></a>
<a id="Return_value_acl_anyOf_i0_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Access control type. `ALLOW`: Grant the specified permissions `DENY`: Explicitly deny the specified permissions
###### Must be one of:

- "ALLOW"
- "DENY"

<a id="headingReturn_value_acl_anyOf_i0_items_perms"></a>
<a id="Return_value_acl_anyOf_i0_items_perms"></a>
###### perms (required)

- Schema name: `Perms`

Permissions granted or denied by this ACE.
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_acl_anyOf_i0_items_perms_anyOf_i0"></a>
###### [NFS4ACE_AdvancedPerms](#tab-pane_Return_value_acl_anyOf_i0_items_perms_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_READ_DATA"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_READ_DATA"></a>
###### READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_DATA"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_DATA"></a>
###### WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_APPEND_DATA"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_APPEND_DATA"></a>
###### APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_READ_NAMED_ATTRS"></a>
###### READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_NAMED_ATTRS"></a>
###### WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_EXECUTE"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_EXECUTE"></a>
###### EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_DELETE"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_DELETE"></a>
###### DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_DELETE_CHILD"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_DELETE_CHILD"></a>
###### DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_READ_ATTRIBUTES"></a>
###### READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ATTRIBUTES"></a>
###### WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_READ_ACL"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_READ_ACL"></a>
###### READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ACL"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_ACL"></a>
###### WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_OWNER"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_WRITE_OWNER"></a>
###### WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i0_SYNCHRONIZE"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i0_SYNCHRONIZE"></a>
###### SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

<a id="tab-pane_Return_value_acl_anyOf_i0_items_perms_anyOf_i1"></a>
###### [NFS4ACE_BasicPerms](#tab-pane_Return_value_acl_anyOf_i0_items_perms_anyOf_i1)

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
<a id="headingReturn_value_acl_anyOf_i0_items_perms_anyOf_i1_BASIC"></a>
<a id="Return_value_acl_anyOf_i0_items_perms_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only
###### Must be one of:

- "FULL_CONTROL"
- "MODIFY"
- "READ"
- "TRAVERSE"

<a id="headingReturn_value_acl_anyOf_i0_items_flags"></a>
<a id="Return_value_acl_anyOf_i0_items_flags"></a>
###### flags (required)

- Schema name: `Flags`

Inheritance and other behavioral flags for this ACE.
<a id="Return_value_acl_anyOf_i0_items_flags_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_acl_anyOf_i0_items_flags_anyOf_i0"></a>
###### [NFS4ACE_AdvancedFlags](#tab-pane_Return_value_acl_anyOf_i0_items_flags_anyOf_i0)

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
<a id="headingReturn_value_acl_anyOf_i0_items_flags_anyOf_i0_FILE_INHERIT"></a>
<a id="Return_value_acl_anyOf_i0_items_flags_anyOf_i0_FILE_INHERIT"></a>
###### FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

<a id="headingReturn_value_acl_anyOf_i0_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
<a id="Return_value_acl_anyOf_i0_items_flags_anyOf_i0_DIRECTORY_INHERIT"></a>
###### DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

<a id="headingReturn_value_acl_anyOf_i0_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
<a id="Return_value_acl_anyOf_i0_items_flags_anyOf_i0_NO_PROPAGATE_INHERIT"></a>
###### NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

<a id="headingReturn_value_acl_anyOf_i0_items_flags_anyOf_i0_INHERIT_ONLY"></a>
<a id="Return_value_acl_anyOf_i0_items_flags_anyOf_i0_INHERIT_ONLY"></a>
###### INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

<a id="headingReturn_value_acl_anyOf_i0_items_flags_anyOf_i0_INHERITED"></a>
<a id="Return_value_acl_anyOf_i0_items_flags_anyOf_i0_INHERITED"></a>
###### INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

<a id="tab-pane_Return_value_acl_anyOf_i0_items_flags_anyOf_i1"></a>
###### [NFS4ACE_BasicFlags](#tab-pane_Return_value_acl_anyOf_i0_items_flags_anyOf_i1)

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
<a id="headingReturn_value_acl_anyOf_i0_items_flags_anyOf_i1_BASIC"></a>
<a id="Return_value_acl_anyOf_i0_items_flags_anyOf_i1_BASIC"></a>
###### BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects
###### Must be one of:

- "INHERIT"
- "NOINHERIT"

<a id="headingReturn_value_acl_anyOf_i0_items_id"></a>
<a id="Return_value_acl_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

UID or GID when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="Return_value_acl_anyOf_i0_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_acl_anyOf_i0_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_acl_anyOf_i0_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_acl_anyOf_i0_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_acl_anyOf_i0_items_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_acl_anyOf_i0_items_who"></a>
<a id="Return_value_acl_anyOf_i0_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when `tag` is "USER" or "GROUP". `null` for special entries.
<a id="Return_value_acl_anyOf_i0_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_acl_anyOf_i0_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_acl_anyOf_i0_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_acl_anyOf_i0_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_acl_anyOf_i0_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_acl_anyOf_i0_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_acl_anyOf_i0_items_who_anyOf_i2)

- Type: null

<a id="tab-pane_Return_value_acl_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_acl_anyOf_i1)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_acl_anyOf_i1_items"></a>
###### POSIXACE

- Schema name: `POSIXACE`
- Type: object
- No Additional Properties
<a id="headingReturn_value_acl_anyOf_i1_items_tag"></a>
<a id="Return_value_acl_anyOf_i1_items_tag"></a>
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

<a id="headingReturn_value_acl_anyOf_i1_items_perms"></a>
<a id="Return_value_acl_anyOf_i1_items_perms"></a>
###### perms (required)

- Schema name: `POSIXACE_Perms`
- Type: object

Read, write, and execute permissions for this ACE.
- No Additional Properties
<a id="headingReturn_value_acl_anyOf_i1_items_perms_READ"></a>
<a id="Return_value_acl_anyOf_i1_items_perms_READ"></a>
###### READ (required)

- Schema name: `Read`
- Type: boolean

Permission to read file contents or list directory contents.

<a id="headingReturn_value_acl_anyOf_i1_items_perms_WRITE"></a>
<a id="Return_value_acl_anyOf_i1_items_perms_WRITE"></a>
###### WRITE (required)

- Schema name: `Write`
- Type: boolean

Permission to write file contents or create/delete files in directory.

<a id="headingReturn_value_acl_anyOf_i1_items_perms_EXECUTE"></a>
<a id="Return_value_acl_anyOf_i1_items_perms_EXECUTE"></a>
###### EXECUTE (required)

- Schema name: `Execute`
- Type: boolean

Permission to execute files or traverse directories.

<a id="headingReturn_value_acl_anyOf_i1_items_default"></a>
<a id="Return_value_acl_anyOf_i1_items_default"></a>
###### default (required)

- Schema name: `Default`
- Type: boolean

Whether this is a default ACE that applies to newly created child objects.

<a id="headingReturn_value_acl_anyOf_i1_items_id"></a>
<a id="Return_value_acl_anyOf_i1_items_id"></a>
###### id

- Schema name: `Id`
- Default: null

Numeric user or group ID when tag is `USER` or `GROUP`. `null` for object entries.
<a id="Return_value_acl_anyOf_i1_items_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_acl_anyOf_i1_items_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_acl_anyOf_i1_items_id_anyOf_i0)

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

<a id="tab-pane_Return_value_acl_anyOf_i1_items_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_acl_anyOf_i1_items_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_acl_anyOf_i1_items_who"></a>
<a id="Return_value_acl_anyOf_i1_items_who"></a>
###### who

- Schema name: `Who`
- Default: null

Username or group name when tag is `USER` or `GROUP`. `null` for object entries.
<a id="Return_value_acl_anyOf_i1_items_who_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_acl_anyOf_i1_items_who_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_acl_anyOf_i1_items_who_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_acl_anyOf_i1_items_who_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_acl_anyOf_i1_items_who_anyOf_i1)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_acl_anyOf_i1_items_who_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_acl_anyOf_i1_items_who_anyOf_i2)

- Type: null

<a id="headingReturn_value_comment"></a>
<a id="Return_value_comment"></a>
#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment about the template's purpose.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
