---
title: sharing.s3.query
kind: event
source_rst: _sources/api_events_sharing.s3.query.rst.txt
source_html: api_events_sharing.s3.query.html
required_roles:
  - SHARING_S3_READ
---

# sharing.s3.query

## Summary

Sent on sharing.s3 changes.

## Required Roles

- `SHARING_S3_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `SharingS3AddedEvent`
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

- Schema name: `SharingS3Entry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the bucket.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Bucket name, following the S3 rules. Three to 63 characters of lowercase letters, digits, dots and hyphens, starting and ending with a letter or digit, no adjacent dots, and never an IPv4 address.
- Must match regular expression: `^[a-z0-9][a-z0-9.-]*[a-z0-9]$`
- Must be at least `3` characters long
- Must be at most `63` characters long

<a id="headingADDED_fields_dataset"></a>
<a id="ADDED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

The ZFS dataset the bucket is. Created by `sharing.s3.create` and owned by it. Objects live in the `s3data` directory under its mount point, which the S3 service creates on its next start, owned by `owner`. Under the `MULTIPROTOCOL` permissions model the filesystem permissions on that tree govern S3 callers too, so a grantee other than the owner reaches only what they allow; set an ACL on the directory as for any share. Under `S3` they are ignored and the grants decide instead.
- Must be at least `1` characters long

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the bucket is served. Toggling restarts the S3 service.

<a id="headingADDED_fields_owner"></a>
<a id="ADDED_fields_owner"></a>
##### owner (required)

- Schema name: `Owner`
- Type: string

Account that owns the bucket and bypasses its grants, owns the `s3data` directory when the S3 service creates it, and owns every object written under the `BUCKET_OWNER_ENFORCED` object ownership setting. Given by name, held by uid: the name is resolved when set and again whenever the bucket is read, so a renamed account reads as its new name, a reused name never inherits the bucket, and an account that no longer exists reads as its uid. Changing the owner later moves the grants, not the directory.
- Must be at least `1` characters long

<a id="headingADDED_fields_owner_uid"></a>
<a id="ADDED_fields_owner_uid"></a>
##### owner_uid (required)

- Schema name: `Owner Uid`
- Type: integer

The uid that owns the bucket.

<a id="headingADDED_fields_grants"></a>
<a id="ADDED_fields_grants"></a>
##### grants

- Schema name: `Grants`
- Type: array of object
- Default: []

Who may access the bucket and how, beyond its owner.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_grants_items"></a>
###### S3GrantEntry

- Schema name: `S3GrantEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_grants_items_principal_type"></a>
<a id="ADDED_fields_grants_items_principal_type"></a>
###### principal_type (required)

- Schema name: `Principal Type`
- Type: enum (of string)

Who the grant applies to. A user, a group, or everyone with a valid access key.
###### Must be one of:

- "USER"
- "GROUP"
- "EVERYONE"

<a id="headingADDED_fields_grants_items_xid"></a>
<a id="ADDED_fields_grants_items_xid"></a>
###### xid

- Schema name: `Xid`
- Default: null

The uid of the user or the gid of the group. Required for `USER` and `GROUP`, forbidden for `EVERYONE`.
<a id="ADDED_fields_grants_items_xid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_grants_items_xid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_grants_items_xid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_grants_items_xid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_grants_items_xid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_grants_items_access"></a>
<a id="ADDED_fields_grants_items_access"></a>
###### access (required)

- Schema name: `Access`
- Type: enum (of string)

What the grant allows. `READONLY`, `WRITEONLY` and `READWRITE` allow the matching operations. `DENY` refuses every operation for the principal and outranks the bucket owner.
###### Must be one of:

- "READONLY"
- "WRITEONLY"
- "READWRITE"
- "DENY"

<a id="headingADDED_fields_grants_items_name"></a>
<a id="ADDED_fields_grants_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the user or group the grant applies to, resolved for display. Empty for `EVERYONE`.

<a id="headingADDED_fields_permissions_model"></a>
<a id="ADDED_fields_permissions_model"></a>
##### permissions_model

- Schema name: `Permissions Model`
- Type: enum (of string)
- Default: "S3"

How the S3 service treats the filesystem permissions on the bucket's tree. `S3` when the S3 service is the only door: those permissions are ignored in their entirety, and access is decided by the bucket's grants and, where `object_ownership` supports them, its S3 ACLs. `MULTIPROTOCOL` when SMB or NFS share the tree: the filesystem ACL is enforced as well as the grants, so an ACL set on the tree governs S3 callers too and narrowing it takes effect for them immediately. S3 ACLs are not supported on such a bucket at all, whatever `object_ownership` says, since no stored S3 record may decide what a write from another protocol could contradict. Which account an S3 operation runs as is `object_ownership`'s answer, not this one's.
###### Must be one of:

- "S3"
- "MULTIPROTOCOL"

<a id="headingADDED_fields_object_ownership"></a>
<a id="ADDED_fields_object_ownership"></a>
##### object_ownership

- Schema name: `Object Ownership`
- Type: enum (of string)
- Default: "BUCKET_OWNER_ENFORCED"

S3 Object Ownership, the bucket-level setting that controls ownership of objects uploaded to the bucket and disables or enables ACLs, and what `GetBucketOwnershipControls` reports. `BUCKET_OWNER_ENFORCED` (the default): ACLs are disabled, and the bucket owner automatically owns and has full control over every object in the bucket. ACLs no longer affect permissions to data in the bucket, and the bucket uses its grants to define access control. Requests to set or update ACLs fail with `AccessControlListNotSupported`; requests to read ACLs are supported. Only uploads with bucket owner full control ACLs, or uploads that do not specify an ACL, are accepted. `BUCKET_OWNER_PREFERRED`: the bucket owner owns and has full control over new objects that other accounts write to the bucket with the `bucket-owner-full-control` canned ACL. Objects uploaded with other ACLs are owned by the writing account. ACLs can be updated and can grant permissions. `OBJECT_WRITER`: the account that uploads an object owns the object, has full control over it, and can grant other users access to it through ACLs. A `MULTIPROTOCOL` bucket is always `OBJECT_WRITER` whatever is given here, and its ACLs stay disabled: the other protocols' users own the filesystem permissions on the tree.
###### Must be one of:

- "BUCKET_OWNER_ENFORCED"
- "BUCKET_OWNER_PREFERRED"
- "OBJECT_WRITER"

<a id="headingADDED_fields_versioning"></a>
<a id="ADDED_fields_versioning"></a>
##### versioning

- Schema name: `Versioning`
- Type: enum (of string)
- Default: "OFF"

Bucket versioning state. One-way: a bucket that has been `ENABLED` or `SUSPENDED` cannot return to `OFF` here, only move between those two, so its stored versions never go unreachable. `sharing.s3.force_disable_versioning` is the one destructive way back, and it destroys every prior object version. NOTE: this is a licensed feature.
###### Must be one of:

- "OFF"
- "ENABLED"
- "SUSPENDED"

<a id="headingADDED_fields_snapshot_versions"></a>
<a id="ADDED_fields_snapshot_versions"></a>
##### snapshot_versions

- Schema name: `Snapshot Versions`
- Type: array of string
- Default: []

Patterns over the names of the bucket dataset's ZFS snapshots, `*` and `?` the only metacharacters, each matched against a whole name. Every snapshot a pattern selects serves each object's state frozen in it as a read-only version: listed by `ListObjectVersions` and read by its version id. Empty serves none. Requires `versioning` to be `ENABLED` or `SUSPENDED`.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_snapshot_versions_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_snapshot_versions_max"></a>
<a id="ADDED_fields_snapshot_versions_max"></a>
##### snapshot_versions_max

- Schema name: `Snapshot Versions Max`
- Type: integer
- Default: 64

How many of the newest selected snapshots one `ListObjectVersions` listing consults. Bounds the listing alone: a selected snapshot beyond it still serves by its version id.
- Value must be greater or equal to `1` and lesser or equal to `4294967295`

<a id="headingADDED_fields_multipart_etag"></a>
<a id="ADDED_fields_multipart_etag"></a>
##### multipart_etag

- Schema name: `Multipart Etag`
- Type: enum (of string)
- Default: "MINTED"

ETag format for objects created by multipart upload. `MINTED` gives the object an opaque token. `COMPOSITE` gives it the standard S3 multipart ETag, built from the MD5 of each part. Choose `COMPOSITE` if a client verifies or resumes uploads by computing that ETag itself and comparing.
###### Must be one of:

- "COMPOSITE"
- "MINTED"

<a id="headingADDED_fields_object_lock"></a>
<a id="ADDED_fields_object_lock"></a>
##### object_lock

- Schema name: `Object Lock`
- Type: boolean
- Default: false

Whether object lock is enabled. Requires `versioning` to be `ENABLED` and a permissions model other than `MULTIPROTOCOL`: a locked bucket is the S3 service's alone. One-way: the lock is latched on the bucket's dataset and cannot be disabled once enabled. NOTE: this is a licensed feature.

<a id="headingADDED_fields_object_lock_default_mode"></a>
<a id="ADDED_fields_object_lock_default_mode"></a>
##### object_lock_default_mode

- Schema name: `Object Lock Default Mode`
- Default: null

Retention mode of the default object lock rule, or `null` for no default rule.
<a id="ADDED_fields_object_lock_default_mode_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_object_lock_default_mode_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_object_lock_default_mode_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "GOVERNANCE"
- "COMPLIANCE"

<a id="tab-pane_ADDED_fields_object_lock_default_mode_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_object_lock_default_mode_anyOf_i1)

- Type: null

<a id="headingADDED_fields_object_lock_default_days"></a>
<a id="ADDED_fields_object_lock_default_days"></a>
##### object_lock_default_days

- Schema name: `Object Lock Default Days`
- Default: null

Retention period of the default object lock rule in days, up to 36500 (a hundred years).
<a id="ADDED_fields_object_lock_default_days_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_object_lock_default_days_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_object_lock_default_days_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `36500`

<a id="tab-pane_ADDED_fields_object_lock_default_days_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_object_lock_default_days_anyOf_i1)

- Type: null

<a id="headingADDED_fields_audit"></a>
<a id="ADDED_fields_audit"></a>
##### audit

- Schema name: `Audit`
- Default: null

Actions audited on this bucket, `ALL`, or an empty list to audit nothing. `null` inherits the service's `default_audit`. `CreateBucket` and `ListAllMyBuckets` never match here — the service `default_audit` governs both — while `DeleteBucket` does match this bucket's own deletion. NOTE: this is a licensed feature.
<a id="ADDED_fields_audit_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_audit_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_audit_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_audit_anyOf_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "GetObject"
- "PutObject"
- "DeleteObject"
- "GetObjectTagging"
- "PutObjectTagging"
- "DeleteObjectTagging"
- "ListBucket"
- "GetBucketLocation"
- "ListBucketMultipartUploads"
- "ListMultipartUploadParts"
- "AbortMultipartUpload"
- "PutObjectRetention"
- "PutObjectLegalHold"
- "ListAllMyBuckets"
- "GetObjectAcl"
- "PutObjectAcl"
- "GetBucketAcl"
- "PutBucketAcl"
- "PutBucketVersioning"
- "CreateBucket"
- "DeleteBucket"

<a id="tab-pane_ADDED_fields_audit_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_audit_anyOf_i1)

- Type: const
- Specific value: `"ALL"`

<a id="tab-pane_ADDED_fields_audit_anyOf_i2"></a>
###### [Option 3](#tab-pane_ADDED_fields_audit_anyOf_i2)

- Type: null

<a id="headingADDED_fields_audit_overflow"></a>
<a id="ADDED_fields_audit_overflow"></a>
##### audit_overflow

- Schema name: `Audit Overflow`
- Default: null

Overflow behavior for this bucket's audit records, or `null` to inherit the service's default.
<a id="ADDED_fields_audit_overflow_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_audit_overflow_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_audit_overflow_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "DROP"
- "BACKPRESSURE"

<a id="tab-pane_ADDED_fields_audit_overflow_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_audit_overflow_anyOf_i1)

- Type: null

<a id="headingADDED_fields_locked"></a>
<a id="ADDED_fields_locked"></a>
##### locked

- Schema name: `Locked`
- Default: null

Whether the bucket's dataset is locked. Read only.
<a id="ADDED_fields_locked_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_locked_anyOf_i1)

- Type: null

<a id="headingADDED_fields_tier"></a>
<a id="ADDED_fields_tier"></a>
##### tier

- Default: null

Storage tier in which the bucket's dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
<a id="ADDED_fields_tier_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_ADDED_fields_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_tier_anyOf_i0_tier_type"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingADDED_fields_tier_anyOf_i0_tier_job"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
###### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.
###### Must be one of:

- "COMPLETE"
- "RUNNING"
- "QUEUED"
- "CANCELLED"
- "STOPPED"
- "ERROR"

<a id="tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_tier_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `SharingS3ChangedEvent`
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

- Schema name: `SharingS3Entry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the bucket.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Bucket name, following the S3 rules. Three to 63 characters of lowercase letters, digits, dots and hyphens, starting and ending with a letter or digit, no adjacent dots, and never an IPv4 address.
- Must match regular expression: `^[a-z0-9][a-z0-9.-]*[a-z0-9]$`
- Must be at least `3` characters long
- Must be at most `63` characters long

<a id="headingCHANGED_fields_dataset"></a>
<a id="CHANGED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

The ZFS dataset the bucket is. Created by `sharing.s3.create` and owned by it. Objects live in the `s3data` directory under its mount point, which the S3 service creates on its next start, owned by `owner`. Under the `MULTIPROTOCOL` permissions model the filesystem permissions on that tree govern S3 callers too, so a grantee other than the owner reaches only what they allow; set an ACL on the directory as for any share. Under `S3` they are ignored and the grants decide instead.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the bucket is served. Toggling restarts the S3 service.

<a id="headingCHANGED_fields_owner"></a>
<a id="CHANGED_fields_owner"></a>
##### owner (required)

- Schema name: `Owner`
- Type: string

Account that owns the bucket and bypasses its grants, owns the `s3data` directory when the S3 service creates it, and owns every object written under the `BUCKET_OWNER_ENFORCED` object ownership setting. Given by name, held by uid: the name is resolved when set and again whenever the bucket is read, so a renamed account reads as its new name, a reused name never inherits the bucket, and an account that no longer exists reads as its uid. Changing the owner later moves the grants, not the directory.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_owner_uid"></a>
<a id="CHANGED_fields_owner_uid"></a>
##### owner_uid (required)

- Schema name: `Owner Uid`
- Type: integer

The uid that owns the bucket.

<a id="headingCHANGED_fields_grants"></a>
<a id="CHANGED_fields_grants"></a>
##### grants

- Schema name: `Grants`
- Type: array of object
- Default: []

Who may access the bucket and how, beyond its owner.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_grants_items"></a>
###### S3GrantEntry

- Schema name: `S3GrantEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_grants_items_principal_type"></a>
<a id="CHANGED_fields_grants_items_principal_type"></a>
###### principal_type (required)

- Schema name: `Principal Type`
- Type: enum (of string)

Who the grant applies to. A user, a group, or everyone with a valid access key.
###### Must be one of:

- "USER"
- "GROUP"
- "EVERYONE"

<a id="headingCHANGED_fields_grants_items_xid"></a>
<a id="CHANGED_fields_grants_items_xid"></a>
###### xid

- Schema name: `Xid`
- Default: null

The uid of the user or the gid of the group. Required for `USER` and `GROUP`, forbidden for `EVERYONE`.
<a id="CHANGED_fields_grants_items_xid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_grants_items_xid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_grants_items_xid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_grants_items_xid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_grants_items_xid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_grants_items_access"></a>
<a id="CHANGED_fields_grants_items_access"></a>
###### access (required)

- Schema name: `Access`
- Type: enum (of string)

What the grant allows. `READONLY`, `WRITEONLY` and `READWRITE` allow the matching operations. `DENY` refuses every operation for the principal and outranks the bucket owner.
###### Must be one of:

- "READONLY"
- "WRITEONLY"
- "READWRITE"
- "DENY"

<a id="headingCHANGED_fields_grants_items_name"></a>
<a id="CHANGED_fields_grants_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the user or group the grant applies to, resolved for display. Empty for `EVERYONE`.

<a id="headingCHANGED_fields_permissions_model"></a>
<a id="CHANGED_fields_permissions_model"></a>
##### permissions_model

- Schema name: `Permissions Model`
- Type: enum (of string)
- Default: "S3"

How the S3 service treats the filesystem permissions on the bucket's tree. `S3` when the S3 service is the only door: those permissions are ignored in their entirety, and access is decided by the bucket's grants and, where `object_ownership` supports them, its S3 ACLs. `MULTIPROTOCOL` when SMB or NFS share the tree: the filesystem ACL is enforced as well as the grants, so an ACL set on the tree governs S3 callers too and narrowing it takes effect for them immediately. S3 ACLs are not supported on such a bucket at all, whatever `object_ownership` says, since no stored S3 record may decide what a write from another protocol could contradict. Which account an S3 operation runs as is `object_ownership`'s answer, not this one's.
###### Must be one of:

- "S3"
- "MULTIPROTOCOL"

<a id="headingCHANGED_fields_object_ownership"></a>
<a id="CHANGED_fields_object_ownership"></a>
##### object_ownership

- Schema name: `Object Ownership`
- Type: enum (of string)
- Default: "BUCKET_OWNER_ENFORCED"

S3 Object Ownership, the bucket-level setting that controls ownership of objects uploaded to the bucket and disables or enables ACLs, and what `GetBucketOwnershipControls` reports. `BUCKET_OWNER_ENFORCED` (the default): ACLs are disabled, and the bucket owner automatically owns and has full control over every object in the bucket. ACLs no longer affect permissions to data in the bucket, and the bucket uses its grants to define access control. Requests to set or update ACLs fail with `AccessControlListNotSupported`; requests to read ACLs are supported. Only uploads with bucket owner full control ACLs, or uploads that do not specify an ACL, are accepted. `BUCKET_OWNER_PREFERRED`: the bucket owner owns and has full control over new objects that other accounts write to the bucket with the `bucket-owner-full-control` canned ACL. Objects uploaded with other ACLs are owned by the writing account. ACLs can be updated and can grant permissions. `OBJECT_WRITER`: the account that uploads an object owns the object, has full control over it, and can grant other users access to it through ACLs. A `MULTIPROTOCOL` bucket is always `OBJECT_WRITER` whatever is given here, and its ACLs stay disabled: the other protocols' users own the filesystem permissions on the tree.
###### Must be one of:

- "BUCKET_OWNER_ENFORCED"
- "BUCKET_OWNER_PREFERRED"
- "OBJECT_WRITER"

<a id="headingCHANGED_fields_versioning"></a>
<a id="CHANGED_fields_versioning"></a>
##### versioning

- Schema name: `Versioning`
- Type: enum (of string)
- Default: "OFF"

Bucket versioning state. One-way: a bucket that has been `ENABLED` or `SUSPENDED` cannot return to `OFF` here, only move between those two, so its stored versions never go unreachable. `sharing.s3.force_disable_versioning` is the one destructive way back, and it destroys every prior object version. NOTE: this is a licensed feature.
###### Must be one of:

- "OFF"
- "ENABLED"
- "SUSPENDED"

<a id="headingCHANGED_fields_snapshot_versions"></a>
<a id="CHANGED_fields_snapshot_versions"></a>
##### snapshot_versions

- Schema name: `Snapshot Versions`
- Type: array of string
- Default: []

Patterns over the names of the bucket dataset's ZFS snapshots, `*` and `?` the only metacharacters, each matched against a whole name. Every snapshot a pattern selects serves each object's state frozen in it as a read-only version: listed by `ListObjectVersions` and read by its version id. Empty serves none. Requires `versioning` to be `ENABLED` or `SUSPENDED`.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_snapshot_versions_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_snapshot_versions_max"></a>
<a id="CHANGED_fields_snapshot_versions_max"></a>
##### snapshot_versions_max

- Schema name: `Snapshot Versions Max`
- Type: integer
- Default: 64

How many of the newest selected snapshots one `ListObjectVersions` listing consults. Bounds the listing alone: a selected snapshot beyond it still serves by its version id.
- Value must be greater or equal to `1` and lesser or equal to `4294967295`

<a id="headingCHANGED_fields_multipart_etag"></a>
<a id="CHANGED_fields_multipart_etag"></a>
##### multipart_etag

- Schema name: `Multipart Etag`
- Type: enum (of string)
- Default: "MINTED"

ETag format for objects created by multipart upload. `MINTED` gives the object an opaque token. `COMPOSITE` gives it the standard S3 multipart ETag, built from the MD5 of each part. Choose `COMPOSITE` if a client verifies or resumes uploads by computing that ETag itself and comparing.
###### Must be one of:

- "COMPOSITE"
- "MINTED"

<a id="headingCHANGED_fields_object_lock"></a>
<a id="CHANGED_fields_object_lock"></a>
##### object_lock

- Schema name: `Object Lock`
- Type: boolean
- Default: false

Whether object lock is enabled. Requires `versioning` to be `ENABLED` and a permissions model other than `MULTIPROTOCOL`: a locked bucket is the S3 service's alone. One-way: the lock is latched on the bucket's dataset and cannot be disabled once enabled. NOTE: this is a licensed feature.

<a id="headingCHANGED_fields_object_lock_default_mode"></a>
<a id="CHANGED_fields_object_lock_default_mode"></a>
##### object_lock_default_mode

- Schema name: `Object Lock Default Mode`
- Default: null

Retention mode of the default object lock rule, or `null` for no default rule.
<a id="CHANGED_fields_object_lock_default_mode_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_object_lock_default_mode_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_object_lock_default_mode_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "GOVERNANCE"
- "COMPLIANCE"

<a id="tab-pane_CHANGED_fields_object_lock_default_mode_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_object_lock_default_mode_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_object_lock_default_days"></a>
<a id="CHANGED_fields_object_lock_default_days"></a>
##### object_lock_default_days

- Schema name: `Object Lock Default Days`
- Default: null

Retention period of the default object lock rule in days, up to 36500 (a hundred years).
<a id="CHANGED_fields_object_lock_default_days_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_object_lock_default_days_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_object_lock_default_days_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `36500`

<a id="tab-pane_CHANGED_fields_object_lock_default_days_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_object_lock_default_days_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_audit"></a>
<a id="CHANGED_fields_audit"></a>
##### audit

- Schema name: `Audit`
- Default: null

Actions audited on this bucket, `ALL`, or an empty list to audit nothing. `null` inherits the service's `default_audit`. `CreateBucket` and `ListAllMyBuckets` never match here — the service `default_audit` governs both — while `DeleteBucket` does match this bucket's own deletion. NOTE: this is a licensed feature.
<a id="CHANGED_fields_audit_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_audit_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_audit_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_audit_anyOf_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "GetObject"
- "PutObject"
- "DeleteObject"
- "GetObjectTagging"
- "PutObjectTagging"
- "DeleteObjectTagging"
- "ListBucket"
- "GetBucketLocation"
- "ListBucketMultipartUploads"
- "ListMultipartUploadParts"
- "AbortMultipartUpload"
- "PutObjectRetention"
- "PutObjectLegalHold"
- "ListAllMyBuckets"
- "GetObjectAcl"
- "PutObjectAcl"
- "GetBucketAcl"
- "PutBucketAcl"
- "PutBucketVersioning"
- "CreateBucket"
- "DeleteBucket"

<a id="tab-pane_CHANGED_fields_audit_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_audit_anyOf_i1)

- Type: const
- Specific value: `"ALL"`

<a id="tab-pane_CHANGED_fields_audit_anyOf_i2"></a>
###### [Option 3](#tab-pane_CHANGED_fields_audit_anyOf_i2)

- Type: null

<a id="headingCHANGED_fields_audit_overflow"></a>
<a id="CHANGED_fields_audit_overflow"></a>
##### audit_overflow

- Schema name: `Audit Overflow`
- Default: null

Overflow behavior for this bucket's audit records, or `null` to inherit the service's default.
<a id="CHANGED_fields_audit_overflow_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_audit_overflow_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_audit_overflow_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "DROP"
- "BACKPRESSURE"

<a id="tab-pane_CHANGED_fields_audit_overflow_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_audit_overflow_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_locked"></a>
<a id="CHANGED_fields_locked"></a>
##### locked

- Schema name: `Locked`
- Default: null

Whether the bucket's dataset is locked. Read only.
<a id="CHANGED_fields_locked_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_locked_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_tier"></a>
<a id="CHANGED_fields_tier"></a>
##### tier

- Default: null

Storage tier in which the bucket's dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
<a id="CHANGED_fields_tier_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_CHANGED_fields_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_tier_anyOf_i0_tier_type"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
###### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.
###### Must be one of:

- "COMPLETE"
- "RUNNING"
- "QUEUED"
- "CANCELLED"
- "STOPPED"
- "ERROR"

<a id="tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_tier_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `SharingS3RemovedEvent`
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
