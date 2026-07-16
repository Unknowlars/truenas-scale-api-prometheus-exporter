---
title: webui.enclosure.dashboard
kind: method
source_rst: _sources/api_methods_webui.enclosure.dashboard.rst.txt
source_html: api_methods_webui.enclosure.dashboard.html
required_roles:
  - ENCLOSURE_READ
---

# webui.enclosure.dashboard

## Summary

This endpoint is used by the webUI for the enclosure dashboard page for TrueNAS sold hardware.

An example of what this returns looks like the following (some redundant information cut out for brevity)::

[{ "name": "iX 4024Sp c205", "model": "M40", "controller": true, "dmi": "TRUENAS-M40-HA", "status": ["OK"], "id": "5b0bd6d1a30714bf", "vendor": "iX", "product": "4024Sp", "revision": "c205", "bsg": "/dev/bsg/0:0:23:0", "sg": "/dev/sg25", "pci": "0:0:23:0", "rackmount": true, "top_loaded": false, "front_slots": 24, "rear_slots": 0, "internal_slots": 0, "elements": { "Array Device Slot": { "1": { "descriptor": "slot00", "status": "OK", "dev": "sda", "supports_identify_light": true, "name": "sda", "size": 12000138625024, "model": "HUH721212AL4200", "serial": "XXXXX", "advpowermgmt": "DISABLED", "transfermode": "Auto", "hddstandby": "ALWAYS ON", "description": "", "rotationrate": 7200, "pool_info": { "pool_name": "test", "disk_status": "ONLINE", "disk_read_errors": 0, "disk_write_errors": 0, "disk_checksum_errors": 0, "vdev_name": "mirror-0", "vdev_type": "data", "vdev_disks": [ { "enclosure_id": "5b0bd6d1a30714bf", "slot": 1, "dev": "sda" }, { "enclosure_id": "5b0bd6d1a30714bf", "slot": 2, "dev": "sdb" }, { "enclosure_id": "5b0bd6d1a30714bf", "slot": 3, "dev": "sdc" } ] } } } } }]

## Required Roles

- `ENCLOSURE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of object

Array of enclosure information objects for the web UI dashboard display.
- No Additional Items

#### Each item of this array must be:

- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
