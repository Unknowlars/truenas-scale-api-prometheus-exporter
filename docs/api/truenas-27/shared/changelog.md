---
title: changelog
kind: shared
source_html: changelog.html
---

<a id="changelog"></a>
# Changelog

Summary of API changes since version v25.10.5.

<a id="methods-added"></a>
## Methods Added

**api_key**

- [api_key.convert_raw_key](../methods/api_key/convert_raw_key.md)

**app**

- [app.upgrade_bulk](../methods/app/upgrade_bulk.md)

**catalog**

- [catalog.synced](../methods/catalog/synced.md)

**cloudsync.credentials**

- [cloudsync.credentials.s3_provider_choices](../methods/cloudsync/credentials/s3_provider_choices.md)

**container**

- [container.create](../methods/container/create.md)
- [container.delete](../methods/container/delete.md)
- [container.get_instance](../methods/container/get_instance.md)
- [container.migrate](../methods/container/migrate.md)
- [container.pool_choices](../methods/container/pool_choices.md)
- [container.query](../methods/container/query.md)
- [container.start](../methods/container/start.md)
- [container.stop](../methods/container/stop.md)
- [container.update](../methods/container/update.md)

**container.device**

- [container.device.create](../methods/container/device/create.md)
- [container.device.delete](../methods/container/device/delete.md)
- [container.device.get_instance](../methods/container/device/get_instance.md)
- [container.device.gpu_choices](../methods/container/device/gpu_choices.md)
- [container.device.nic_attach_choices](../methods/container/device/nic_attach_choices.md)
- [container.device.query](../methods/container/device/query.md)
- [container.device.update](../methods/container/device/update.md)
- [container.device.usb_choices](../methods/container/device/usb_choices.md)

**container.image**

- [container.image.query_registry](../methods/container/image/query_registry.md)

**disk**

- [disk.get_instance](../methods/disk/get_instance.md)
- [disk.reset_sed](../methods/disk/reset_sed.md)
- [disk.setup_sed](../methods/disk/setup_sed.md)
- [disk.unlock_sed](../methods/disk/unlock_sed.md)

**interface**

- [interface.available_fec_modes](../methods/interface/available_fec_modes.md)

**lxc**

- [lxc.bridge_choices](../methods/lxc/bridge_choices.md)
- [lxc.config](../methods/lxc/config.md)
- [lxc.update](../methods/lxc/update.md)

**nvmet.global**

- [nvmet.global.sessions](../methods/nvmet/global/sessions.md)

**pool**

- [pool.prefetch](../methods/pool/prefetch.md)
- [pool.reimport](../methods/pool/reimport.md)

**privilege**

- [privilege.become_readonly](../methods/privilege/become_readonly.md)

**reporting**

- [reporting.graphs](../methods/reporting/graphs.md)

**s3**

- [s3.bindip_choices](../methods/s3/bindip_choices.md)
- [s3.config](../methods/s3/config.md)
- [s3.update](../methods/s3/update.md)

**s3.accesskey**

- [s3.accesskey.create](../methods/s3/accesskey/create.md)
- [s3.accesskey.delete](../methods/s3/accesskey/delete.md)
- [s3.accesskey.get_instance](../methods/s3/accesskey/get_instance.md)
- [s3.accesskey.query](../methods/s3/accesskey/query.md)
- [s3.accesskey.update](../methods/s3/accesskey/update.md)

**sharing.s3**

- [sharing.s3.audit_choices](../methods/sharing/s3/audit_choices.md)
- [sharing.s3.create](../methods/sharing/s3/create.md)
- [sharing.s3.delete](../methods/sharing/s3/delete.md)
- [sharing.s3.force_disable_versioning](../methods/sharing/s3/force_disable_versioning.md)
- [sharing.s3.get_instance](../methods/sharing/s3/get_instance.md)
- [sharing.s3.query](../methods/sharing/s3/query.md)
- [sharing.s3.update](../methods/sharing/s3/update.md)

**sharing.webshare**

- [sharing.webshare.create](../methods/sharing/webshare/create.md)
- [sharing.webshare.delete](../methods/sharing/webshare/delete.md)
- [sharing.webshare.get_instance](../methods/sharing/webshare/get_instance.md)
- [sharing.webshare.query](../methods/sharing/webshare/query.md)
- [sharing.webshare.update](../methods/sharing/webshare/update.md)

**smb**

- [smb.status](../methods/smb/status.md)

**system.advanced**

- [system.advanced.nvidia_present](../methods/system/advanced/nvidia_present.md)

**tn_connect**

- [tn_connect.ips_with_hostnames](../methods/tn_connect/ips_with_hostnames.md)

**truenas.entitlements**

- [truenas.entitlements.check](../methods/truenas/entitlements/check.md)
- [truenas.entitlements.facts](../methods/truenas/entitlements/facts.md)
- [truenas.entitlements.info](../methods/truenas/entitlements/info.md)

**truenas.license**

- [truenas.license.fingerprint](../methods/truenas/license/fingerprint.md)
- [truenas.license.info](../methods/truenas/license/info.md)
- [truenas.license.upload](../methods/truenas/license/upload.md)

**webshare**

- [webshare.bindip_choices](../methods/webshare/bindip_choices.md)
- [webshare.config](../methods/webshare/config.md)
- [webshare.update](../methods/webshare/update.md)

**zfs.resource**

- [zfs.resource.create](../methods/zfs/resource/create.md)
- [zfs.resource.destroy](../methods/zfs/resource/destroy.md)

**zfs.resource.snapshot**

- [zfs.resource.snapshot.clone](../methods/zfs/resource/snapshot/clone.md)
- [zfs.resource.snapshot.count](../methods/zfs/resource/snapshot/count.md)
- [zfs.resource.snapshot.create](../methods/zfs/resource/snapshot/create.md)
- [zfs.resource.snapshot.destroy](../methods/zfs/resource/snapshot/destroy.md)
- [zfs.resource.snapshot.hold](../methods/zfs/resource/snapshot/hold.md)
- [zfs.resource.snapshot.holds](../methods/zfs/resource/snapshot/holds.md)
- [zfs.resource.snapshot.query](../methods/zfs/resource/snapshot/query.md)
- [zfs.resource.snapshot.release](../methods/zfs/resource/snapshot/release.md)
- [zfs.resource.snapshot.rename](../methods/zfs/resource/snapshot/rename.md)
- [zfs.resource.snapshot.rollback](../methods/zfs/resource/snapshot/rollback.md)

**zfs.tier**

- [zfs.tier.config](../methods/zfs/tier/config.md)
- [zfs.tier.dataset_set_tier](../methods/zfs/tier/dataset_set_tier.md)
- [zfs.tier.rewrite_job_cancel](../methods/zfs/tier/rewrite_job_cancel.md)
- [zfs.tier.rewrite_job_create](../methods/zfs/tier/rewrite_job_create.md)
- [zfs.tier.rewrite_job_failures](../methods/zfs/tier/rewrite_job_failures.md)
- [zfs.tier.rewrite_job_query](../methods/zfs/tier/rewrite_job_query.md)
- [zfs.tier.rewrite_job_recover](../methods/zfs/tier/rewrite_job_recover.md)
- [zfs.tier.rewrite_job_status](../methods/zfs/tier/rewrite_job_status.md)
- [zfs.tier.update](../methods/zfs/tier/update.md)

**zpool**

- [zpool.query](../methods/zpool/query.md)

**zpool.scrub**

- [zpool.scrub.run](../methods/zpool/scrub/run.md)
<a id="methods-with-schema-changes"></a>
## Methods with Schema Changes

**alert**

- [alert.list_categories](../methods/alert/list_categories.md) Call parameters: added parameter options (optional)

**api_key**

- [api_key.create](../methods/api_key/create.md) Return value: added client_key (required) added iterations (required) added salt (required) added server_key (required) added stored_key (required) removed keyhash
- [api_key.get_instance](../methods/api_key/get_instance.md) Return value: added iterations (required) added salt (required) added server_key (required) added stored_key (required) removed keyhash
- [api_key.my_keys](../methods/api_key/my_keys.md) Return value: added [].iterations (required) added [].salt (required) added [].server_key (required) added [].stored_key (required) removed [].keyhash
- [api_key.query](../methods/api_key/query.md) Return value: added ApiKeyQueryResultItem.iterations added ApiKeyQueryResultItem.salt added ApiKeyQueryResultItem.server_key added ApiKeyQueryResultItem.stored_key removed ApiKeyQueryResultItem.keyhash added [].iterations added [].salt added [].server_key added [].stored_key removed [].keyhash
- [api_key.update](../methods/api_key/update.md) Return value: added ApiKeyEntry.iterations (required) added ApiKeyEntry.salt (required) added ApiKeyEntry.server_key (required) added ApiKeyEntry.stored_key (required) removed ApiKeyEntry.keyhash added ApiKeyEntryWithKey.client_key (required) added ApiKeyEntryWithKey.iterations (required) added ApiKeyEntryWithKey.salt (required) added ApiKeyEntryWithKey.server_key (required) added ApiKeyEntryWithKey.stored_key (required) removed ApiKeyEntryWithKey.keyhash

**app**

- [app.convert_to_custom](../methods/app/convert_to_custom.md) Return value: added action_required (required) added latest_app_version (required)
- [app.create](../methods/app/create.md) Return value: added action_required (required) added latest_app_version (required)
- [app.get_instance](../methods/app/get_instance.md) Return value: added action_required (required) added latest_app_version (required)
- [app.query](../methods/app/query.md) Return value: added AppQueryResultItem.action_required added AppQueryResultItem.latest_app_version added [].action_required added [].latest_app_version
- [app.redeploy](../methods/app/redeploy.md) Return value: added action_required (required) added latest_app_version (required)
- [app.rollback](../methods/app/rollback.md) Return value: added action_required (required) added latest_app_version (required)
- [app.update](../methods/app/update.md) Return value: added action_required (required) added latest_app_version (required)
- [app.upgrade](../methods/app/upgrade.md) Return value: added action_required (required) added latest_app_version (required)

**app.image**

- [app.image.get_instance](../methods/app/image/get_instance.md) Return value: author type changed (string → string | null) comment type changed (string → string | null) created type changed (string → string | null)
- [app.image.query](../methods/app/image/query.md) Return value: AppImageQueryResultItem.author type changed (string → string | null) AppImageQueryResultItem.comment type changed (string → string | null) AppImageQueryResultItem.created type changed (string → string | null) [].author type changed (string → string | null) [].comment type changed (string → string | null) [].created type changed (string → string | null)

**audit**

- [audit.config](../methods/audit/config.md) Return value: added enabled_services.S3 (required)
- [audit.export](../methods/audit/export.md) Call parameters: parameter data became optional removed data.query-options.count removed data.query-options.extra removed data.query-options.get data.query-options default value added data.services[]: added enum value “S3”
- [audit.query](../methods/audit/query.md) Call parameters: parameter data became optional data.query-options default value added data.services[]: added enum value “S3” Return value: added variant AuditQueryResultItemQueryResultItem removed variant AuditQueryResultItem [].service: added enum value “S3” []: additional properties now allowed
- [audit.update](../methods/audit/update.md) Return value: added enabled_services.S3 (required)

**auth**

- [auth.login_ex](../methods/auth/login_ex.md) Call parameters: parameter login_data: added variant AuthSCRAM added login_data.AuthApiKeyPlain.login_options.reconnect_token login_data.AuthApiKeyPlain.login_options default value changed ({“user_info”: true} → {“user_info”: true, “reconnect_token”: false}) added login_data.AuthOTPToken.login_options.reconnect_token login_data.AuthOTPToken.login_options default value changed ({“user_info”: true} → {“user_info”: true, “reconnect_token”: false}) added login_data.AuthPasswordPlain.login_options.reconnect_token login_data.AuthPasswordPlain.login_options default value changed ({“user_info”: true} → {“user_info”: true, “reconnect_token”: false}) added login_data.AuthTokenPlain.login_options.reconnect_token login_data.AuthTokenPlain.login_options default value changed ({“user_info”: true} → {“user_info”: true, “reconnect_token”: false}) Return value: added variant AuthRespDenied added variant AuthRespScram added AuthRespSuccess.reconnect_token (required)
- [auth.login_ex_continue](../methods/auth/login_ex_continue.md) Call parameters: added login_data.login_options.reconnect_token login_data.login_options default value changed ({“user_info”: true} → {“user_info”: true, “reconnect_token”: false}) Return value: added variant AuthRespDenied added AuthRespSuccess.reconnect_token (required)

**boot**

- [boot.get_state](../methods/boot/get_state.md) Return value: added all_sed (required) scan: added variant PoolScan scan: removed variant object

**catalog**

- [catalog.apps](../methods/catalog/apps.md) Call parameters: parameter catalog_apps_options renamed to data
- [catalog.get_app_details](../methods/catalog/get_app_details.md) Return value: added versions (required)
- [catalog.update](../methods/catalog/update.md) Call parameters: parameter catalog_update renamed to data

**cloud_backup**

- [cloud_backup.create](../methods/cloud_backup/create.md) Return value: added dataset (required) added relative_path (required) added credentials.provider.S3CredentialsModel.force_path_style added credentials.provider.S3CredentialsModel.provider added credentials.provider.S3CredentialsModel.sign_accept_encoding
- [cloud_backup.get_instance](../methods/cloud_backup/get_instance.md) Return value: added dataset (required) added relative_path (required) added credentials.provider.S3CredentialsModel.force_path_style added credentials.provider.S3CredentialsModel.provider added credentials.provider.S3CredentialsModel.sign_accept_encoding
- [cloud_backup.query](../methods/cloud_backup/query.md) Return value: added CloudBackupQueryResultItem.dataset added CloudBackupQueryResultItem.relative_path added [].dataset added [].relative_path added [].credentials.provider.S3CredentialsModel.force_path_style added [].credentials.provider.S3CredentialsModel.provider added [].credentials.provider.S3CredentialsModel.sign_accept_encoding
- [cloud_backup.update](../methods/cloud_backup/update.md) Return value: added dataset (required) added relative_path (required) added credentials.provider.S3CredentialsModel.force_path_style added credentials.provider.S3CredentialsModel.provider added credentials.provider.S3CredentialsModel.sign_accept_encoding

**cloudsync**

- [cloudsync.create](../methods/cloudsync/create.md) Return value: added dataset (required) added relative_path (required) added credentials.provider.S3CredentialsModel.force_path_style added credentials.provider.S3CredentialsModel.provider added credentials.provider.S3CredentialsModel.sign_accept_encoding
- [cloudsync.get_instance](../methods/cloudsync/get_instance.md) Return value: added dataset (required) added relative_path (required) added credentials.provider.S3CredentialsModel.force_path_style added credentials.provider.S3CredentialsModel.provider added credentials.provider.S3CredentialsModel.sign_accept_encoding
- [cloudsync.query](../methods/cloudsync/query.md) Return value: added CloudSyncQueryResultItem.dataset added CloudSyncQueryResultItem.relative_path added [].dataset added [].relative_path added [].credentials.provider.S3CredentialsModel.force_path_style added [].credentials.provider.S3CredentialsModel.provider added [].credentials.provider.S3CredentialsModel.sign_accept_encoding
- [cloudsync.restore](../methods/cloudsync/restore.md) Return value: added dataset (required) added relative_path (required) added credentials.provider.S3CredentialsModel.force_path_style added credentials.provider.S3CredentialsModel.provider added credentials.provider.S3CredentialsModel.sign_accept_encoding
- [cloudsync.update](../methods/cloudsync/update.md) Return value: added dataset (required) added relative_path (required) added credentials.provider.S3CredentialsModel.force_path_style added credentials.provider.S3CredentialsModel.provider added credentials.provider.S3CredentialsModel.sign_accept_encoding

**cloudsync.credentials**

- [cloudsync.credentials.create](../methods/cloudsync/credentials/create.md) Call parameters: added cloud_sync_credentials_create.provider.S3CredentialsModel.force_path_style added cloud_sync_credentials_create.provider.S3CredentialsModel.provider added cloud_sync_credentials_create.provider.S3CredentialsModel.sign_accept_encoding Return value: added provider.S3CredentialsModel.force_path_style added provider.S3CredentialsModel.provider added provider.S3CredentialsModel.sign_accept_encoding
- [cloudsync.credentials.get_instance](../methods/cloudsync/credentials/get_instance.md) Return value: added provider.S3CredentialsModel.force_path_style added provider.S3CredentialsModel.provider added provider.S3CredentialsModel.sign_accept_encoding
- [cloudsync.credentials.query](../methods/cloudsync/credentials/query.md) Return value: added [].provider.S3CredentialsModel.force_path_style added [].provider.S3CredentialsModel.provider added [].provider.S3CredentialsModel.sign_accept_encoding
- [cloudsync.credentials.update](../methods/cloudsync/credentials/update.md) Call parameters: added cloud_sync_credentials_update.provider.S3CredentialsModel.force_path_style added cloud_sync_credentials_update.provider.S3CredentialsModel.provider added cloud_sync_credentials_update.provider.S3CredentialsModel.sign_accept_encoding Return value: added provider.S3CredentialsModel.force_path_style added provider.S3CredentialsModel.provider added provider.S3CredentialsModel.sign_accept_encoding
- [cloudsync.credentials.verify](../methods/cloudsync/credentials/verify.md) Call parameters: added cloud_sync_credentials_create.S3CredentialsModel.force_path_style added cloud_sync_credentials_create.S3CredentialsModel.provider added cloud_sync_credentials_create.S3CredentialsModel.sign_accept_encoding

**disk**

- [disk.query](../methods/disk/query.md) Return value: added DiskQueryResultItem.sed added DiskQueryResultItem.sed_status added [].sed added [].sed_status
- [disk.update](../methods/disk/update.md) Call parameters: added data.sed_status Return value: added sed (required) added sed_status

**docker**

- [docker.config](../methods/docker/config.md) Return value: added registry_mirrors (required) removed insecure_registry_mirrors removed nvidia removed secure_registry_mirrors
- [docker.update](../methods/docker/update.md) Call parameters: added docker_update.registry_mirrors removed docker_update.insecure_registry_mirrors removed docker_update.nvidia removed docker_update.secure_registry_mirrors Return value: added registry_mirrors (required) removed insecure_registry_mirrors removed nvidia removed secure_registry_mirrors

**fcport**

- [fcport.status](../methods/fcport/status.md) Call parameters: added options.extra.with_lun_access options.extra: additional properties no longer allowed options.extra default value changed ({} → {“with_lun_access”: true}) parameter options default value changed

**filesystem**

- [filesystem.set_zfs_attributes](../methods/filesystem/set_zfs_attributes.md) Call parameters: added set_zfs_file_attributes.options
- [filesystem.setacl](../methods/filesystem/setacl.md) Call parameters: removed filesystem_acl.options.canonicalize filesystem_acl.options default value changed

**filesystem.acltemplate**

- [filesystem.acltemplate.by_path](../methods/filesystem/acltemplate/by_path.md) Call parameters: removed filesystem_acl.format-options.canonicalize filesystem_acl.format-options default value changed removed filesystem_acl.query-options.count removed filesystem_acl.query-options.extra removed filesystem_acl.query-options.get removed filesystem_acl.query-options.select filesystem_acl.query-options default value changed

**interface**

- [interface.create](../methods/interface/create.md) Return value: added fec_mode added state.fec_mode
- [interface.get_instance](../methods/interface/get_instance.md) Return value: added fec_mode added state.fec_mode
- [interface.query](../methods/interface/query.md) Return value: added InterfaceQueryResultItem.fec_mode added [].fec_mode added [].state.fec_mode
- [interface.update](../methods/interface/update.md) Call parameters: added data.fec_mode Return value: added fec_mode added state.fec_mode
- [interface.websocket_interface](../methods/interface/websocket_interface.md) Return value: added InterfaceEntry.fec_mode added InterfaceEntry.state.fec_mode

**iscsi.extent**

- [iscsi.extent.create](../methods/iscsi/extent/create.md) Return value: added dataset (required) added relative_path (required)
- [iscsi.extent.get_instance](../methods/iscsi/extent/get_instance.md) Return value: added dataset (required) added relative_path (required)
- [iscsi.extent.query](../methods/iscsi/extent/query.md) Return value: added [].dataset added [].relative_path added iSCSITargetExtentQueryResultItem.dataset added iSCSITargetExtentQueryResultItem.relative_path
- [iscsi.extent.update](../methods/iscsi/extent/update.md) Return value: added dataset (required) added relative_path (required)

**iscsi.global**

- [iscsi.global.config](../methods/iscsi/global/config.md) Return value: added direct_config (required) added mode (required)
- [iscsi.global.sessions](../methods/iscsi/global/sessions.md) Return value: type changed (array → array | ISCSIGlobalSessionsItemQueryResultItem | integer)
- [iscsi.global.update](../methods/iscsi/global/update.md) Call parameters: added iscsi_update.direct_config added iscsi_update.mode Return value: added direct_config (required) added mode (required)

**mail**

- [mail.send](../methods/mail/send.md) Return value: type changed (boolean → null)

**nvmet.host**

- [nvmet.host.create](../methods/nvmet/host/create.md) Call parameters: added nvmet_host_create.description Return value: added description
- [nvmet.host.get_instance](../methods/nvmet/host/get_instance.md) Return value: added description
- [nvmet.host.query](../methods/nvmet/host/query.md) Return value: added NVMetHostQueryResultItem.description added [].description
- [nvmet.host.update](../methods/nvmet/host/update.md) Call parameters: added nvmet_host_update.description Return value: added description

**nvmet.host_subsys**

- [nvmet.host_subsys.create](../methods/nvmet/host_subsys/create.md) Return value: added host.description
- [nvmet.host_subsys.get_instance](../methods/nvmet/host_subsys/get_instance.md) Return value: added host.description
- [nvmet.host_subsys.query](../methods/nvmet/host_subsys/query.md) Return value: added [].host.description
- [nvmet.host_subsys.update](../methods/nvmet/host_subsys/update.md) Return value: added host.description

**nvmet.namespace**

- [nvmet.namespace.create](../methods/nvmet/namespace/create.md) Return value: added dataset (required) added relative_path (required)
- [nvmet.namespace.get_instance](../methods/nvmet/namespace/get_instance.md) Return value: added dataset (required) added relative_path (required)
- [nvmet.namespace.query](../methods/nvmet/namespace/query.md) Return value: added NVMetNamespaceQueryResultItem.dataset added NVMetNamespaceQueryResultItem.relative_path added [].dataset added [].relative_path
- [nvmet.namespace.update](../methods/nvmet/namespace/update.md) Return value: added dataset (required) added relative_path (required)

**pool**

- [pool.create](../methods/pool/create.md) Call parameters: added data.all_sed added data.force_topology removed data.encryption_options.algorithm data.encryption_options.pbkdf2iters default value changed (350000 → 1300000) data.topology.data[]: added variant PoolCreateTopologyVdevDRAID data.topology.data[]: added variant PoolCreateTopologyVdevNonDRAID data.topology.data[]: removed variant PoolCreateTopologyDataVdevDRAID data.topology.data[]: removed variant PoolCreateTopologyDataVdevNonDRAID data.topology.special[] type changed (object → PoolCreateTopologyVdevDRAID | PoolCreateTopologyVdevNonDRAID) Return value: added all_sed (required) scan: added variant PoolScan scan: removed variant object
- [pool.get_instance](../methods/pool/get_instance.md) Return value: added all_sed (required) scan: added variant PoolScan scan: removed variant object
- [pool.query](../methods/pool/query.md) Return value: added PoolQueryResultItem.all_sed PoolQueryResultItem.scan type changed (object | null → any | null) added [].all_sed [].scan: added variant PoolScan [].scan: removed variant object
- [pool.update](../methods/pool/update.md) Call parameters: added data.all_sed added data.force_topology data.topology.data[]: added variant PoolCreateTopologyVdevDRAID data.topology.data[]: added variant PoolCreateTopologyVdevNonDRAID data.topology.data[]: removed variant PoolCreateTopologyDataVdevDRAID data.topology.data[]: removed variant PoolCreateTopologyDataVdevNonDRAID data.topology.special[] type changed (object → PoolCreateTopologyVdevDRAID | PoolCreateTopologyVdevNonDRAID) Return value: added all_sed (required) scan: added variant PoolScan scan: removed variant object

**pool.dataset**

- [pool.dataset.change_key](../methods/pool/dataset/change_key.md) Call parameters: options.pbkdf2iters default value changed (350000 → 1300000)
- [pool.dataset.create](../methods/pool/dataset/create.md) Call parameters: removed data.PoolDatasetCreateFilesystem.encryption_options.algorithm data.PoolDatasetCreateFilesystem.encryption_options.pbkdf2iters default value changed (350000 → 1300000) removed data.PoolDatasetCreateVolume.encryption_options.algorithm data.PoolDatasetCreateVolume.encryption_options.pbkdf2iters default value changed (350000 → 1300000) Return value: added tier
- [pool.dataset.get_instance](../methods/pool/dataset/get_instance.md) Return value: added tier
- [pool.dataset.get_quota](../methods/pool/dataset/get_quota.md) Call parameters: parameter options became optional Return value: type changed (array → array | PoolDatasetUserGroupQuota | PoolDatasetDatasetQuota | PoolDatasetProjectQuota | integer)
- [pool.dataset.query](../methods/pool/dataset/query.md) Return value: added PoolDatasetQueryResultItem.tier added [].tier
- [pool.dataset.update](../methods/pool/dataset/update.md) Return value: added tier

**pool.snapshot**

- [pool.snapshot.create](../methods/pool/snapshot/create.md) Call parameters: added data.PoolSnapshotCreateWithName.suspend_vms added data.PoolSnapshotCreateWithSchema.suspend_vms
- [pool.snapshot.rename](../methods/pool/snapshot/rename.md) Call parameters: added options.recursive

**replication**

- [replication.run](../methods/replication/run.md) Call parameters: added parameter options (required)
- [replication.target_unmatched_snapshots](../methods/replication/target_unmatched_snapshots.md) Return value: [*] type changed (string → array)

**reporting**

- [reporting.get_data](../methods/reporting/get_data.md) Call parameters: graphs[].name: removed enum value “arcactualrate” graphs[].name: removed enum value “arcrate” graphs[].name: removed enum value “arcresult” Return value: [].aggregations type changed (object → Aggregations | null)
- [reporting.graph](../methods/reporting/graph.md) Return value: [].aggregations type changed (object → Aggregations | null)
- [reporting.netdata_get_data](../methods/reporting/netdata_get_data.md) Call parameters: graphs[].name: removed enum value “arcactualrate” graphs[].name: removed enum value “arcrate” graphs[].name: removed enum value “arcresult” Return value: [].aggregations type changed (object → Aggregations | null)
- [reporting.netdata_graph](../methods/reporting/netdata_graph.md) Return value: [].aggregations type changed (object → Aggregations | null)

**rsynctask**

- [rsynctask.create](../methods/rsynctask/create.md) Return value: added dataset (required) added relative_path (required)
- [rsynctask.get_instance](../methods/rsynctask/get_instance.md) Return value: added dataset (required) added relative_path (required)
- [rsynctask.query](../methods/rsynctask/query.md) Return value: added RsyncTaskQueryResultItem.dataset added RsyncTaskQueryResultItem.relative_path added [].dataset added [].relative_path
- [rsynctask.update](../methods/rsynctask/update.md) Return value: added dataset (required) added relative_path (required)

**sharing.nfs**

- [sharing.nfs.create](../methods/sharing/nfs/create.md) Return value: added dataset (required) added relative_path (required) added tier
- [sharing.nfs.get_instance](../methods/sharing/nfs/get_instance.md) Return value: added dataset (required) added relative_path (required) added tier
- [sharing.nfs.query](../methods/sharing/nfs/query.md) Return value: added SharingNFSQueryResultItem.dataset added SharingNFSQueryResultItem.relative_path added SharingNFSQueryResultItem.tier added [].dataset added [].relative_path added [].tier
- [sharing.nfs.update](../methods/sharing/nfs/update.md) Return value: added dataset (required) added relative_path (required) added tier

**sharing.smb**

- [sharing.smb.create](../methods/sharing/smb/create.md) Return value: added dataset (required) added relative_path (required) added tier
- [sharing.smb.get_instance](../methods/sharing/smb/get_instance.md) Return value: added dataset (required) added relative_path (required) added tier
- [sharing.smb.getacl](../methods/sharing/smb/getacl.md) Return value: share_acl[].ae_perm: added enum value “CUSTOM”
- [sharing.smb.query](../methods/sharing/smb/query.md) Return value: added SharingSMBQueryResultItem.dataset added SharingSMBQueryResultItem.relative_path added SharingSMBQueryResultItem.tier added [].dataset added [].relative_path added [].tier
- [sharing.smb.setacl](../methods/sharing/smb/setacl.md) Call parameters: smb_setacl.share_acl[].ae_perm: added enum value “CUSTOM” Return value: share_acl[].ae_perm: added enum value “CUSTOM”
- [sharing.smb.update](../methods/sharing/smb/update.md) Return value: added dataset (required) added relative_path (required) added tier

**smb**

- [smb.config](../methods/smb/config.md) Return value: added minimum_protocol (required) added search_protocols added stateful_failover (required) removed enable_smb1
- [smb.update](../methods/smb/update.md) Call parameters: added smb_update.minimum_protocol added smb_update.search_protocols added smb_update.stateful_failover removed smb_update.enable_smb1 Return value: added minimum_protocol (required) added search_protocols added stateful_failover (required) removed enable_smb1

**support**

- [support.new_ticket](../methods/support/new_ticket.md) Return value: added debug_attach_error (required)

**system**

- [system.feature_enabled](../methods/system/feature_enabled.md) Call parameters: parameter feature: removed enum value “DEDUP” parameter feature: removed enum value “FIBRECHANNEL” parameter feature: removed enum value “VM”

**system.advanced**

- [system.advanced.config](../methods/system/advanced/config.md) Return value: added nvidia (required)
- [system.advanced.update](../methods/system/advanced/update.md) Call parameters: added data.nvidia Return value: added nvidia (required)

**system.general**

- [system.general.config](../methods/system/general/config.md) Return value: added ui_certificate_name (required) ui_certificate type changed (object | null → integer | null)
- [system.general.update](../methods/system/general/update.md) Return value: added ui_certificate_name (required) ui_certificate type changed (object | null → integer | null)

**tn_connect**

- [tn_connect.config](../methods/tn_connect/config.md) Return value: added last_heartbeat_failure_datetime (required) added tier (required) removed interfaces removed interfaces_ips removed ips removed use_all_interfaces
- [tn_connect.update](../methods/tn_connect/update.md) Call parameters: removed tn_connect_update.interfaces removed tn_connect_update.ips removed tn_connect_update.use_all_interfaces Return value: added last_heartbeat_failure_datetime (required) added tier (required) removed interfaces removed interfaces_ips removed ips removed use_all_interfaces

**truecommand**

- [truecommand.config](../methods/truecommand/config.md) Return value: status_reason: added enum value “Truecommand service is disabled on standby controller”
- [truecommand.update](../methods/truecommand/update.md) Return value: status_reason: added enum value “Truecommand service is disabled on standby controller”

**truenas**

- [truenas.set_production](../methods/truenas/set_production.md) Return value: added variant SupportNewTicket removed variant object

**ups**

- [ups.update](../methods/ups/update.md) Call parameters: parameter ups_update renamed to data

**user**

- [user.create](../methods/user/create.md) Call parameters: added user_create.webshare Return value: added webshare
- [user.get_instance](../methods/user/get_instance.md) Return value: added webshare
- [user.query](../methods/user/query.md) Return value: added UserQueryResultItem.webshare added [].webshare
- [user.renew_2fa_secret](../methods/user/renew_2fa_secret.md) Call parameters: twofactor_options.interval: added enum value 30 twofactor_options.interval: added enum value 60 Return value: added webshare
- [user.update](../methods/user/update.md) Call parameters: added user_update.webshare Return value: added webshare

**vm**

- [vm.create](../methods/vm/create.md) Return value: status.domain_state type changed (string → string | null)
- [vm.delete](../methods/vm/delete.md) Return value: type changed (boolean → null)
- [vm.get_instance](../methods/vm/get_instance.md) Return value: status.domain_state type changed (string → string | null)
- [vm.query](../methods/vm/query.md) Return value: [].status.domain_state type changed (string → string | null)
- [vm.status](../methods/vm/status.md) Return value: domain_state type changed (string → string | null)
- [vm.update](../methods/vm/update.md) Return value: status.domain_state type changed (string → string | null)

**vm.device**

- [vm.device.nic_attach_choices](../methods/vm/device/nic_attach_choices.md) Return value: added BRIDGE (required) added MACVLAN (required) additional properties no longer allowed
- [vm.device.usb_controller_choices](../methods/vm/device/usb_controller_choices.md) Return value: [*] type changed (any → string)
- [vm.device.usb_passthrough_choices](../methods/vm/device/usb_passthrough_choices.md) Return value: added [*].description (required)
- [vm.device.usb_passthrough_device](../methods/vm/device/usb_passthrough_device.md) Return value: added description (required)

**vmware**

- [vmware.create](../methods/vmware/create.md) Return value: added state.datetime added state.error added state.state state: additional properties no longer allowed
- [vmware.get_instance](../methods/vmware/get_instance.md) Return value: added state.datetime added state.error added state.state state: additional properties no longer allowed
- [vmware.query](../methods/vmware/query.md) Return value: VMWareQueryResultItem.state type changed (object → any) added [].state.datetime added [].state.error added [].state.state [].state: additional properties no longer allowed
- [vmware.update](../methods/vmware/update.md) Return value: added state.datetime added state.error added state.state state: additional properties no longer allowed

**webui.main.dashboard**

- [webui.main.dashboard.sys_info](../methods/webui/main/dashboard/sys_info.md) Return value: removed codename removed remote_info.RemoteInfo.codename

**zfs.resource**

- [zfs.resource.query](../methods/zfs/resource/query.md) Call parameters: added data.get_tier added data.max_depth data.get_source default value changed (true → false) parameter data default value changed Return value: added [].tier [].properties type changed (object → ZFSPropertiesEntry | null)
