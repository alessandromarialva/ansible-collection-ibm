
ibm_storage_block -- Configure IBM Cloud 'ibm_storage_block' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_storage_block' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  tags (False, list, None)
    List of tags associated with the resource


  type (True, str, None)
    (Required for new resource) Storage block type


  iops (True, float, None)
    (Required for new resource) IOPS value required


  os_format_type (True, str, None)
    (Required for new resource) OS formatr type


  hourly_billing (False, bool, False)
    Billing done hourly, if set to true


  datacenter (True, str, None)
    (Required for new resource) Datacenter name


  capacity (True, int, None)
    (Required for new resource) Storage block size


  snapshot_capacity (False, int, None)
    Snapshot capacity in GB


  notes (False, str, None)
    Additional note info


  allowed_ip_addresses (False, list, None)
    Allowed IP addresses


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

