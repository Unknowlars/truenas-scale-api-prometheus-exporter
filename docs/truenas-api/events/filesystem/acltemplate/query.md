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

### ADDED

- Schema name: `AclTemplateAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `AclTemplateEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the ACL template.

##### builtin (required)

- Schema name: `Builtin`
- Type: boolean

Whether this is a built-in system template or user-created.

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the ACL template.

##### acltype (required)

- Schema name: `Acltype`
- Type: enum (of string)

ACL type this template provides.

##### acl (required)

- Schema name: `Acl`

Array of Access Control Entries defined by this template.
###### Any of

####### Option 1

- Type: array of object
- No Additional Items

######## Each item of this array must be:

######## NFS4ACE

- Schema name: `NFS4ACE`
- Type: object
- No Additional Properties
######### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this ACE. `owner@`: File/directory owner `group@`: File/directory primary group `everyone@`: All users `USER`: Specific user account `GROUP`: Specific group

######### type (required)

- Schema name: `Type`
- Type: enum (of string)

Access control type. `ALLOW`: Grant the specified permissions `DENY`: Explicitly deny the specified permissions

######### perms (required)

- Schema name: `Perms`

Permissions granted or denied by this ACE.
########## Any of

########### NFS4ACE_AdvancedPerms

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
############ READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

############ WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

############ APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

############ READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

############ WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

############ EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

############ DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

############ DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

############ READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

############ WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

############ READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

############ WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

############ WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

############ SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

########### NFS4ACE_BasicPerms

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
############ BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only

######### flags (required)

- Schema name: `Flags`

Inheritance and other behavioral flags for this ACE.
########## Any of

########### NFS4ACE_AdvancedFlags

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
############ FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

############ DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

############ NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

############ INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

############ INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

########### NFS4ACE_BasicFlags

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
############ BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects

######### id

- Schema name: `Id`
- Default: null

UID or GID when `tag` is "USER" or "GROUP". `null` for special entries.
########## Any of

########### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

########### Option 2

- Type: null

######### who

- Schema name: `Who`
- Default: null

Username or group name when `tag` is "USER" or "GROUP". `null` for special entries.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: string
- Must be at least `1` characters long

########### Option 3

- Type: null

####### Option 2

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
######## READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

######## WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

######## APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

######## READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

######## WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

######## EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

######## DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

######## DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

######## READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

######## WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

######## READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

######## WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

######## WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

######## SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

####### NFS4ACE_AdvancedPerms

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
######## BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only

####### NFS4ACE_BasicPerms

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
######## FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

######## DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

######## NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

######## INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

######## INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

####### NFS4ACE_AdvancedFlags

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
######## BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects

####### NFS4ACE_BasicFlags

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

####### Option 3

- Type: array of object
- No Additional Items

######## Each item of this array must be:

######## POSIXACE

- Schema name: `POSIXACE`
- Type: object
- No Additional Properties
######### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this POSIX ACE. `USER_OBJ`: File/directory owner `GROUP_OBJ`: File/directory primary group `OTHER`: All other users `MASK`: Maximum permissions for named users and groups `USER`: Specific user account `GROUP`: Specific group

######### perms (required)

- Schema name: `POSIXACE_Perms`
- Type: object

Read, write, and execute permissions for this ACE.
- No Additional Properties
########## READ (required)

- Schema name: `Read`
- Type: boolean

Permission to read file contents or list directory contents.

########## WRITE (required)

- Schema name: `Write`
- Type: boolean

Permission to write file contents or create/delete files in directory.

########## EXECUTE (required)

- Schema name: `Execute`
- Type: boolean

Permission to execute files or traverse directories.

######### default (required)

- Schema name: `Default`
- Type: boolean

Whether this is a default ACE that applies to newly created child objects.

######### id

- Schema name: `Id`
- Default: null

Numeric user or group ID when tag is `USER` or `GROUP`. `null` for object entries.
########## Any of

########### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

########### Option 2

- Type: null

######### who

- Schema name: `Who`
- Default: null

Username or group name when tag is `USER` or `GROUP`. `null` for object entries.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: string
- Must be at least `1` characters long

########### Option 3

- Type: null

####### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

####### Option 2

- Type: null

####### Option 1

- Type: string

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 3

- Type: null

##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment about the template's purpose.

### CHANGED

- Schema name: `AclTemplateChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `AclTemplateEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the ACL template.

##### builtin (required)

- Schema name: `Builtin`
- Type: boolean

Whether this is a built-in system template or user-created.

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the ACL template.

##### acltype (required)

- Schema name: `Acltype`
- Type: enum (of string)

ACL type this template provides.

##### acl (required)

- Schema name: `Acl`

Array of Access Control Entries defined by this template.
###### Any of

####### Option 1

- Type: array of object
- No Additional Items

######## Each item of this array must be:

######## NFS4ACE

- Schema name: `NFS4ACE`
- Type: object
- No Additional Properties
######### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this ACE. `owner@`: File/directory owner `group@`: File/directory primary group `everyone@`: All users `USER`: Specific user account `GROUP`: Specific group

######### type (required)

- Schema name: `Type`
- Type: enum (of string)

Access control type. `ALLOW`: Grant the specified permissions `DENY`: Explicitly deny the specified permissions

######### perms (required)

- Schema name: `Perms`

Permissions granted or denied by this ACE.
########## Any of

########### NFS4ACE_AdvancedPerms

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
############ READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

############ WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

############ APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

############ READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

############ WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

############ EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

############ DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

############ DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

############ READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

############ WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

############ READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

############ WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

############ WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

############ SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

########### NFS4ACE_BasicPerms

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
############ BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only

######### flags (required)

- Schema name: `Flags`

Inheritance and other behavioral flags for this ACE.
########## Any of

########### NFS4ACE_AdvancedFlags

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
############ FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

############ DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

############ NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

############ INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

############ INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

########### NFS4ACE_BasicFlags

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
############ BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects

######### id

- Schema name: `Id`
- Default: null

UID or GID when `tag` is "USER" or "GROUP". `null` for special entries.
########## Any of

########### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

########### Option 2

- Type: null

######### who

- Schema name: `Who`
- Default: null

Username or group name when `tag` is "USER" or "GROUP". `null` for special entries.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: string
- Must be at least `1` characters long

########### Option 3

- Type: null

####### Option 2

- Schema name: `NFS4ACE_AdvancedPerms`
- Type: object
- No Additional Properties
######## READ_DATA

- Schema name: `Read Data`
- Type: boolean
- Default: false

Permission to read file data or list directory contents.

######## WRITE_DATA

- Schema name: `Write Data`
- Type: boolean
- Default: false

Permission to write file data or create files in directory.

######## APPEND_DATA

- Schema name: `Append Data`
- Type: boolean
- Default: false

Permission to append data to files or create subdirectories.

######## READ_NAMED_ATTRS

- Schema name: `Read Named Attrs`
- Type: boolean
- Default: false

Permission to read named attributes (extended attributes).

######## WRITE_NAMED_ATTRS

- Schema name: `Write Named Attrs`
- Type: boolean
- Default: false

Permission to write named attributes (extended attributes).

######## EXECUTE

- Schema name: `Execute`
- Type: boolean
- Default: false

Permission to execute files or traverse directories.

######## DELETE

- Schema name: `Delete`
- Type: boolean
- Default: false

Permission to delete the file or directory.

######## DELETE_CHILD

- Schema name: `Delete Child`
- Type: boolean
- Default: false

Permission to delete child files within a directory.

######## READ_ATTRIBUTES

- Schema name: `Read Attributes`
- Type: boolean
- Default: false

Permission to read basic file attributes (size, timestamps, etc.).

######## WRITE_ATTRIBUTES

- Schema name: `Write Attributes`
- Type: boolean
- Default: false

Permission to write basic file attributes.

######## READ_ACL

- Schema name: `Read Acl`
- Type: boolean
- Default: false

Permission to read the Access Control List.

######## WRITE_ACL

- Schema name: `Write Acl`
- Type: boolean
- Default: false

Permission to modify the Access Control List.

######## WRITE_OWNER

- Schema name: `Write Owner`
- Type: boolean
- Default: false

Permission to change the file owner.

######## SYNCHRONIZE

- Schema name: `Synchronize`
- Type: boolean
- Default: false

Permission to use the file/directory as a synchronization primitive.

####### NFS4ACE_AdvancedPerms

- Schema name: `NFS4ACE_BasicPerms`
- Type: object
- No Additional Properties
######## BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic permission level for NFS4 ACE. `FULL_CONTROL`: Full read, write, execute, and administrative permissions `MODIFY`: Read, write, and execute permissions `READ`: Read-only permissions `TRAVERSE`: Execute/traverse permissions only

####### NFS4ACE_BasicPerms

- Schema name: `NFS4ACE_AdvancedFlags`
- Type: object
- No Additional Properties
######## FILE_INHERIT

- Schema name: `File Inherit`
- Type: boolean
- Default: false

Apply this ACE to files within directories.

######## DIRECTORY_INHERIT

- Schema name: `Directory Inherit`
- Type: boolean
- Default: false

Apply this ACE to subdirectories within directories.

######## NO_PROPAGATE_INHERIT

- Schema name: `No Propagate Inherit`
- Type: boolean
- Default: false

Do not propagate inheritance beyond immediate children.

######## INHERIT_ONLY

- Schema name: `Inherit Only`
- Type: boolean
- Default: false

This ACE only affects inheritance, not the object itself.

######## INHERITED

- Schema name: `Inherited`
- Type: boolean
- Default: false

This ACE was inherited from a parent directory.

####### NFS4ACE_AdvancedFlags

- Schema name: `NFS4ACE_BasicFlags`
- Type: object
- No Additional Properties
######## BASIC (required)

- Schema name: `Basic`
- Type: enum (of string)

Basic inheritance behavior for NFS4 ACE. `INHERIT`: Apply to child files and directories `NOINHERIT`: Do not apply to child objects

####### NFS4ACE_BasicFlags

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

####### Option 3

- Type: array of object
- No Additional Items

######## Each item of this array must be:

######## POSIXACE

- Schema name: `POSIXACE`
- Type: object
- No Additional Properties
######### tag (required)

- Schema name: `Tag`
- Type: enum (of string)

Subject type for this POSIX ACE. `USER_OBJ`: File/directory owner `GROUP_OBJ`: File/directory primary group `OTHER`: All other users `MASK`: Maximum permissions for named users and groups `USER`: Specific user account `GROUP`: Specific group

######### perms (required)

- Schema name: `POSIXACE_Perms`
- Type: object

Read, write, and execute permissions for this ACE.
- No Additional Properties
########## READ (required)

- Schema name: `Read`
- Type: boolean

Permission to read file contents or list directory contents.

########## WRITE (required)

- Schema name: `Write`
- Type: boolean

Permission to write file contents or create/delete files in directory.

########## EXECUTE (required)

- Schema name: `Execute`
- Type: boolean

Permission to execute files or traverse directories.

######### default (required)

- Schema name: `Default`
- Type: boolean

Whether this is a default ACE that applies to newly created child objects.

######### id

- Schema name: `Id`
- Default: null

Numeric user or group ID when tag is `USER` or `GROUP`. `null` for object entries.
########## Any of

########### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

########### Option 2

- Type: null

######### who

- Schema name: `Who`
- Default: null

Username or group name when tag is `USER` or `GROUP`. `null` for object entries.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: string
- Must be at least `1` characters long

########### Option 3

- Type: null

####### Option 1

- Type: integer
- Value must be greater or equal to `-1` and lesser or equal to `2147483647`

####### Option 2

- Type: null

####### Option 1

- Type: string

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 3

- Type: null

##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment about the template's purpose.

### REMOVED

- Schema name: `AclTemplateRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
