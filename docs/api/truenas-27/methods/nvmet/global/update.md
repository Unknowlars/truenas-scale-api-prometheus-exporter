---
title: nvmet.global.update
kind: method
source_rst: _sources/api_methods_nvmet.global.update.rst.txt
source_html: api_methods_nvmet.global.update.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.global.update

## Summary

Update NVMe target global config.

## Required Roles

- `SHARING_NVME_TARGET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: nvmet_update

<a id="Call_parameters_items_i0"></a>
#### nvmet_update

- Schema name: `nvmet_update`
- Type: object

NVMetGlobalUpdateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_basenqn"></a>
<a id="Call_parameters_items_i0_basenqn"></a>
##### basenqn

- Schema name: `Basenqn`
- Type: string

NQN to be used as the prefix on the creation of a subsystem, if a subnqn is not supplied to `nvmet.subsys.create`. Modifying this value will *not* change the subnqn of any existing subsystems.
- Must be at least `11` characters long
- Must be at most `223` characters long

<a id="headingCall_parameters_items_i0_kernel"></a>
<a id="Call_parameters_items_i0_kernel"></a>
##### kernel

- Schema name: `Kernel`
- Type: boolean

Select the NVMe-oF backend.

<a id="headingCall_parameters_items_i0_ana"></a>
<a id="Call_parameters_items_i0_ana"></a>
##### ana

- Schema name: `Ana`
- Type: boolean

Asymmetric Namespace Access (ANA) enabled.

<a id="headingCall_parameters_items_i0_rdma"></a>
<a id="Call_parameters_items_i0_rdma"></a>
##### rdma

- Schema name: `Rdma`
- Type: boolean

RDMA is enabled for NVMe-oF. Enabling is limited to TrueNAS Enterprise-licensed systems and requires the system and network environment have Remote Direct Memory Access (RDMA)-capable hardware. Once enabled one or more `ports` may be configured with RDMA selected as the transport. See `nvmet.port.create`.

<a id="headingCall_parameters_items_i0_xport_referral"></a>
<a id="Call_parameters_items_i0_xport_referral"></a>
##### xport_referral

- Schema name: `Xport Referral`
- Type: boolean

Controls whether cross-port referrals will be generated for ports on this TrueNAS. If ANA is active then referrals will always be generated between the peer ports on each TrueNAS controller node.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NVMetGlobalEntry`
- Type: object

The updated NVMe-oF global configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF global configuration.

<a id="headingReturn_value_basenqn"></a>
<a id="Return_value_basenqn"></a>
#### basenqn (required)

- Schema name: `Basenqn`
- Type: string

NQN to be used as the prefix on the creation of a subsystem, if a subnqn is not supplied to `nvmet.subsys.create`. Modifying this value will *not* change the subnqn of any existing subsystems.

<a id="headingReturn_value_kernel"></a>
<a id="Return_value_kernel"></a>
#### kernel (required)

- Schema name: `Kernel`
- Type: boolean

Select the NVMe-oF backend.

<a id="headingReturn_value_ana"></a>
<a id="Return_value_ana"></a>
#### ana (required)

- Schema name: `Ana`
- Type: boolean

Asymmetric Namespace Access (ANA) enabled.

<a id="headingReturn_value_rdma"></a>
<a id="Return_value_rdma"></a>
#### rdma (required)

- Schema name: `Rdma`
- Type: boolean

RDMA is enabled for NVMe-oF. Enabling is limited to TrueNAS Enterprise-licensed systems and requires the system and network environment have Remote Direct Memory Access (RDMA)-capable hardware. Once enabled one or more `ports` may be configured with RDMA selected as the transport. See `nvmet.port.create`.

<a id="headingReturn_value_xport_referral"></a>
<a id="Return_value_xport_referral"></a>
#### xport_referral (required)

- Schema name: `Xport Referral`
- Type: boolean

Controls whether cross-port referrals will be generated for ports on this TrueNAS. If ANA is active then referrals will always be generated between the peer ports on each TrueNAS controller node.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
