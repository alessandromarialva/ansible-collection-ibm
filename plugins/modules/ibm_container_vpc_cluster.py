#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_vpc_cluster
short_description: Configure IBM Cloud 'ibm_container_vpc_cluster' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_vpc_cluster' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.8.1
    - Terraform v0.12.20

options:
    worker_count:
        description:
            - Number of worker nodes in the cluster
        required: False
        type: int
        default: 1
    name:
        description:
            - (Required for new resource) The cluster name
        required: True
        type: str
    vpc_id:
        description:
            - (Required for new resource) The vpc id where the cluster is
        required: True
        type: str
    disable_public_service_endpoint:
        description:
            - Boolean value true if Public service endpoint to be disabled
        required: False
        type: bool
        default: False
    flavor:
        description:
            - (Required for new resource) Cluster nodes flavour
        required: True
        type: str
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    cos_instance_crn:
        description:
            - A standard cloud object storage instance CRN to back up the internal registry in your OpenShift on VPC Gen 2 cluster
        required: False
        type: str
    zones:
        description:
            - (Required for new resource) Zone info
        required: True
        type: list
        elements: dict
    wait_till:
        description:
            - wait_till can be configured for Master Ready, One worker Ready or Ingress Ready
        required: False
        type: str
        default: IngressReady
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
    ('name', 'str'),
    ('vpc_id', 'str'),
    ('flavor', 'str'),
    ('zones', 'list'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'worker_count',
    'name',
    'vpc_id',
    'disable_public_service_endpoint',
    'flavor',
    'entitlement',
    'cos_instance_crn',
    'zones',
    'wait_till',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    worker_count=dict(
        default=1,
        type='int'),
    name=dict(
        required= False,
        type='str'),
    vpc_id=dict(
        required= False,
        type='str'),
    disable_public_service_endpoint=dict(
        default=False,
        type='bool'),
    flavor=dict(
        required= False,
        type='str'),
    entitlement=dict(
        required= False,
        type='str'),
    cos_instance_crn=dict(
        required= False,
        type='str'),
    zones=dict(
        required= False,
        elements='',
        type='list'),
    wait_till=dict(
        default='IngressReady',
        type='str'),
    id=dict(
        required= False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
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
        resource_type='ibm_container_vpc_cluster',
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
