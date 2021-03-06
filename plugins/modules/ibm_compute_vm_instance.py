#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_vm_instance
short_description: Configure IBM Cloud 'ibm_compute_vm_instance' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_vm_instance' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.8.1
    - Terraform v0.12.20

options:
    dedicated_host_id:
        description:
            - None
        required: False
        type: int
    ipv6_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    ipv6_static_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    public_bandwidth_unlimited:
        description:
            - None
        required: False
        type: bool
        default: False
    datacenter_choice:
        description:
            - The user provided datacenter options
        required: False
        type: list
        elements: dict
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
        default: 90
    evault:
        description:
            - None
        required: False
        type: int
    os_reference_code:
        description:
            - None
        required: False
        type: str
    hourly_billing:
        description:
            - None
        required: False
        type: bool
        default: True
    image_id:
        description:
            - None
        required: False
        type: int
    post_install_script_uri:
        description:
            - None
        required: False
        type: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    secondary_ip_count:
        description:
            - None
        required: False
        type: int
    placement_group_name:
        description:
            - The placement group name
        required: False
        type: str
    private_network_only:
        description:
            - None
        required: False
        type: bool
        default: False
    transient:
        description:
            - None
        required: False
        type: bool
    local_disk:
        description:
            - None
        required: False
        type: bool
        default: True
    dedicated_acct_host_only:
        description:
            - None
        required: False
        type: bool
    user_metadata:
        description:
            - None
        required: False
        type: str
    placement_group_id:
        description:
            - The placement group id
        required: False
        type: int
    network_speed:
        description:
            - None
        required: False
        type: int
        default: 100
    hostname:
        description:
            - None
        required: False
        type: str
    bulk_vms:
        description:
            - None
        required: False
        type: list
        elements: dict
    domain:
        description:
            - None
        required: False
        type: str
    ssh_key_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    notes:
        description:
            - None
        required: False
        type: str
    flavor_key_name:
        description:
            - Flavor key name used to provision vm.
        required: False
        type: str
    dedicated_host_name:
        description:
            - None
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'dedicated_host_id',
    'ipv6_enabled',
    'ipv6_static_enabled',
    'public_bandwidth_unlimited',
    'datacenter_choice',
    'wait_time_minutes',
    'evault',
    'os_reference_code',
    'hourly_billing',
    'image_id',
    'post_install_script_uri',
    'tags',
    'secondary_ip_count',
    'placement_group_name',
    'private_network_only',
    'transient',
    'local_disk',
    'dedicated_acct_host_only',
    'user_metadata',
    'placement_group_id',
    'network_speed',
    'hostname',
    'bulk_vms',
    'domain',
    'ssh_key_ids',
    'notes',
    'flavor_key_name',
    'dedicated_host_name',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    dedicated_host_id=dict(
        required= False,
        type='int'),
    ipv6_enabled=dict(
        default=False,
        type='bool'),
    ipv6_static_enabled=dict(
        default=False,
        type='bool'),
    public_bandwidth_unlimited=dict(
        default=False,
        type='bool'),
    datacenter_choice=dict(
        required= False,
        elements='',
        type='list'),
    wait_time_minutes=dict(
        default=90,
        type='int'),
    evault=dict(
        required= False,
        type='int'),
    os_reference_code=dict(
        required= False,
        type='str'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    image_id=dict(
        required= False,
        type='int'),
    post_install_script_uri=dict(
        required= False,
        type='str'),
    tags=dict(
        required= False,
        elements='',
        type='list'),
    secondary_ip_count=dict(
        required= False,
        type='int'),
    placement_group_name=dict(
        required= False,
        type='str'),
    private_network_only=dict(
        default=False,
        type='bool'),
    transient=dict(
        required= False,
        type='bool'),
    local_disk=dict(
        default=True,
        type='bool'),
    dedicated_acct_host_only=dict(
        required= False,
        type='bool'),
    user_metadata=dict(
        required= False,
        type='str'),
    placement_group_id=dict(
        required= False,
        type='int'),
    network_speed=dict(
        default=100,
        type='int'),
    hostname=dict(
        required= False,
        type='str'),
    bulk_vms=dict(
        required= False,
        elements='',
        type='list'),
    domain=dict(
        required= False,
        type='str'),
    ssh_key_ids=dict(
        required= False,
        elements='',
        type='list'),
    notes=dict(
        required= False,
        type='str'),
    flavor_key_name=dict(
        required= False,
        type='str'),
    dedicated_host_name=dict(
        required= False,
        type='str'),
    id=dict(
        required= False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud_terraform(
        resource_type='ibm_compute_vm_instance',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.8.1',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
