---
title: nvmet.global.config
kind: method
source_rst: _sources/api_methods_nvmet.global.config.rst.txt
source_html: api_methods_nvmet.global.config.html
required_roles:
  - SHARING_NVME_TARGET_READ
---

# nvmet.global.config

## Required Roles

- `SHARING_NVME_TARGET_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `NVMetGlobalEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF global configuration.

#### basenqn (required)

- Schema name: `Basenqn`
- Type: string

NQN to be used as the prefix on the creation of a subsystem, if a subnqn is not supplied to `nvmet.subsys.create`. Modifying this value will *not* change the subnqn of any existing subsystems.

#### kernel (required)

- Schema name: `Kernel`
- Type: boolean

Select the NVMe-oF backend.

#### ana (required)

- Schema name: `Ana`
- Type: boolean

Asymmetric Namespace Access (ANA) enabled.

#### rdma (required)

- Schema name: `Rdma`
- Type: boolean

RDMA is enabled for NVMe-oF. Enabling is limited to TrueNAS Enterprise-licensed systems and requires the system and network environment have Remote Direct Memory Access (RDMA)-capable hardware. Once enabled one or more `ports` may be configured with RDMA selected as the transport. See `nvmet.port.create`.

#### xport_referral (required)

- Schema name: `Xport Referral`
- Type: boolean

Controls whether cross-port referrals will be generated for ports on this TrueNAS. If ANA is active then referrals will always be generated between the peer ports on each TrueNAS controller node.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
