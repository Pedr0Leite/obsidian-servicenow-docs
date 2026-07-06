---
title: "Understand vCenter Discovery process and troubleshooting"
aliases:
  - KB0813327
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813327
kb_number: KB0813327
last_modified: 2026-01-15
---

## Understand vCenter Discovery process and troubleshooting

  

### vCenter Discovery Process

After classifying vCenter, Discovery launches the VMware - vCenter Datacenters probe, which triggers specific probes that return information about VMware ESX Server (ESX) machines, virtual machines, and other vCenter objects. The vmapp port probe is also configured to launch the VMware - vCenter Datacenters probe.

The VMware - vCenter Datacenters probe can be triggered by either:

-   **Process classification**: When discovering the vCenter application host, the base system process classifier vCenter triggers the probe. To view process classifiers, go to **Discovery Definition** > **CI Classification** > **Processes**.
-   **Port probe**: The vmapp port probe in the Shazzam phase detects the default vCenter port is open. To view port probes, go to **Discovery Definition** > **Port Probes**.

**Note:** If the vCenter to be discovered does not use the standard port, see [Configure an alternate port for vCenter](https://docs.servicenow.com/csh?topicname=t_ConfigureAlternatePortForVCenter.html&version=latest "Configure an alternate port for vCenter").

![Discovery Flow process diagram](sys_attachment.do?sys_id=ab45ff4c93aa3214d744b94c5cba1003 "Discovery Flow")

### Probes

The VMware - vCenter probe that discovered all vCenter objects in previous releases is deprecated in the Istanbul release and replaced by multiple probes. For available vCenter probes and probe parameters, see [Available vCenter probes and probe parameters](https://www.servicenow.com/docs/bundle/zurich-it-operations-management/page/product/discovery/reference/vcenter-probes.html#d524518e67). 

![Probes Diagram](sys_attachment.do?sys_id=ef45ff4c93aa3214d744b94c5cba1011 "Probes Diagram")

Each vCenter discovery probe has a matching MID Server script include that contains the code that is run. The probe's ECC Queue Name matches the name of the MID Server script include. To view MID Server script includes, go to **MID Server** > **Script Includes**. The vCenter probes use the VMware Java API. 

#### **Probe list**

The following probes are available for vCenter discovery:

<table style="border-collapse: collapse; width: 100%; border: 1px solid rgb(149, 165, 166);" border="1"><tbody><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p><strong>Name</strong></p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p><strong>Implemented on script include</strong></p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p><strong>Description</strong></p></td></tr><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWare - vCenter Datacenters</p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWarevCenterDatacentersProbe</p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>Gets information about a vCenter's datacenters. The sensor fires a probe for each type of vCenter object in each datacenter: VMs, clusters, datastores, and networks.&nbsp;</p></td></tr><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWare - vCenter VMs</p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWarevCenterVMsProbe</p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>Explores VMs.</p></td></tr><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWare - vCenter&nbsp;Networks</p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWarevCenterNetworksProbe</p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>Explores virtual networks.</p></td></tr><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWare - vCenter Datastores</p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWarevCenterDatacentersProbe</p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>Explores datastores, datastore host mounts, and datastore disks.</p></td></tr><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWare - vCenter Clusters</p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWarevCenterClustersProbe</p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>Explores clusters and resource pools. Relates each cluster to its resource pools, ESX hosts, and its containing folder or datacenter. The sensor triggers the ESX Hosts probe to explore ESX hosts.&nbsp;</p></td></tr><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWare - vCenter VM NICs</p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWarevCenterVMNICsProbe</p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>Explores NICs installed in virtual machines.</p></td></tr><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWare - vCenter VM Tags</p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWarevCenterVMTagsProbe</p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>Explores tags for the VMs discovered.</p></td></tr><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWare - vCenter ESX Hosts</p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWarevCenterESXHostsProbe</p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>Explores ESX servers and host mounts. The sensor triggers the ESX Hosts Storage probe to explore ESX hardware (disks, SAN disks, and NICs).&nbsp;</p></td></tr><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWare - vCenter ESX Hosts Storage</p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWarevCenterESXHostsStorageProbe</p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>Explores ESX host hardware: network adapters, disks, HBAs, FC ports, iSCSI, and FC disks.</p></td></tr><tr style="height: 13px;"><td style="width: 14.7344%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWare - vCenter ESX Hosts License</p></td><td style="width: 13.1225%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>VMWarevCenterESXHostsLicenseProbe</p></td><td style="width: 72.143%; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);"><p>Explores ESX host licenses.</p></td></tr></tbody></table>

**Note:** If Software Asset Management is active, Discovery also triggers the VMWare - vCenter ESX Hosts License probe. 

### Data Collected and Relationships Created

For information about the data collected, see [Data collected for VMware vCenter Server](link).

The **Virtualizes::Virtualized by** and **Instantiates::Instantiated by** relationships between ESX Server and VM Instance to the Guest are created by the Virtual Computer Check business rule. The guest machine must be discovered after the vCenter is discovered to trigger this business rule and create these relationships.

![Relationships](sys_attachment.do?sys_id=6345ff4c93aa3214d744b94c5cba1019 "Relationships")

The Virtual Computer Check business rule performs the following actions: 

1.  Checks for the serial number on cmdb\_ci\_vmware\_instance and searches for a record with a correlation\_id field that matches the guest device discovered (not the hypervisor). If not found, the business rule ends.
2.  Creates an **Instantiates::Instantiated by** relationship between the server and virtual machine instance record, if no relationship already exists.
3.  Searches for the virtualization server using the findVMWareByImage() call, which looks for a **Registered on::Has registered** relationship for the virtual machine instance and hypervisor.
4.  Creates a Virtualized by::Virtualizes relationship between the server record and hypervisor.

### Credentials

To successfully collect data from vCenter, you must create a VMware type discovery credential. The VMware credentials must have the read-only role and License Admin privilege in vCenter.

The read-only role allows a user limited read access to the system without additional privileges. This role allows ServiceNow users to run Discovery and view resources.

The credential must be assigned Read-Only permission at the Global level. If the credential is defined only at This Object, Discovery cannot collect the hosts and continue.

For more information, see [VMware credentials](https://docs.servicenow.com/csh?topicname=r_VMwareCredentialsForm.html&version=latest "VMware credentials").

### Troubleshooting

#### Probe VMware - vCenter Datacenters not triggered

To troubleshoot this issue:

1.  Confirm the port the vCenter is using. If the vCenter does not use the standard port, see [Configure an alternate port for vCenter](https://docs.servicenow.com/csh?topicname=t_ConfigureAlternatePortForVCenter.html&version=latest "Configure an alternate port for vCenter").
2.  Review the input from the Shazzam probe and check the result for the ports defined in the vmapp port probe.
3.  If the ports are not open, work with the teams managing the network and the vCenter to troubleshoot further.
4.  From the MID Server, use telnet to confirm whether the socket is reachable.

#### Probe VMware - vCenter Datacenters fails with connection error

This probe fails with the error message: ""Unable to establish connection to https://<ip>/sdk". This error means the user either could not establish a connection to the vCenter sdk page or the user could not authenticate.

**Confirm the MOB page loads from the MID Server**

1.  Log in to the MID Server.
2.  Open a browser and go to https://<vCenter\_IP\_Address>/mob, replacing the address with the IP address of the vCenter server.
3.  If the page does not load, contact your vCenter admin and network team for further troubleshooting.

 ![VCenter MOB Authentication](sys_attachment.do?sys_id=6f45ff4c93aa3214d744b94c5cba106a "VCenter MOB Authentication")

**Confirm the credential can authenticate to vCenter** 

1.  Log in to the MID Server host.
2.  Open a browser and go to `https://<vCenter_IP_Address>/mob`. Replace the address with the IP address of the VCenter server.
3.  When the authentication page appears, enter the same username and password combination and format as configured in the credentials table record.
4.  Select **Sign in**.
5.  If authentication fails, work with your VMware team to troubleshoot or provide access to the credential. The credential must be assigned Read-Only permission at the Global level.

  
![MOB page](sys_attachment.do?sys_id=6f45ff4c93aa3214d744b94c5cba100a "MOB page")

The Managed Object Browser (MOB) is a website available on both individual ESX hosts and vCenter that allows you to examine server objects, properties, and values.

**Note:** The MOB could be disabled. For more information, [the Broadcom knowledge article.](https://kb.vmware.com/s/article/2108405)

#### Subsequent probes not triggered after VMware - vCenter Datacenters probe

This occurs when insufficient information is returned in the datacenters probe input. This is typically caused by the user's read-only permission not being set at the global level, which allows the user to log in to vCenter but only collect partial data.

To resolve this issue, review the user roles and permissions in vCenter.

#### Incorrect Virtualizes::Virtualized by relationship

This occurs when there are **Registered on::Has registered** relationships from the virtual machine instance to an older or retired hypervisor.

To resolve this issue, delete the incorrect **Registered on::Has registered** relationships.

#### Records do not reflect identification rules configuration

vCenter Discovery does not use the standard identification rules. Each sensor calls a script include to process the payload. The script include contains a schema for the table where records are inserted, and the schema includes an index that defines the fields used to identify the CI.

The following example shows the schema for cmdb\_ci\_vmware\_instance:

cmdb\_ci\_vmware\_instance: {  
index: \[ \[ 'object\_id', 'vcenter\_uuid' \], \[ 'vm\_instance\_uuid', 'vcenter\_uuid' \], \[ 'vm\_instance\_uuid' \] \],  
fixup: fixupVM,  
preWrite: preWriteVm,  
preWriteRels: preWriteVmRels,  
parentOf: {  
cmdb\_ci\_esx\_server: 'Registered on::Has registered',  
cmdb\_ci\_vcenter\_network: 'Connected by::Connects',  
cmdb\_ci\_vcenter\_dvs: 'Connected by::Connects',  
cmdb\_ci\_vcenter\_dv\_port\_group: 'Connected by::Connects',  
hostedOn: 'Hosted on::Hosts'  
},  
childOf: {  
cmdb\_ci\_vcenter\_datacenter: 'Contains::Contained by',  
cmdb\_ci\_vcenter\_folder: 'Contains::Contained by',  
cmdb\_ci\_vcenter\_datastore: 'Provides storage for::Stored on',  
cmdb\_ci\_esx\_resource\_pool: 'Members::Member of'  
}  
}

In this example, the index field shows that object\_id and vcenter\_uuid are used for identification of cmdb\_ci\_vmware\_instance records.

index: \[ \[ 'object\_id', 'vcenter\_uuid' \], \[ 'vm\_instance\_uuid', 'vcenter\_uuid' \], \[ 'vm\_instance\_uuid' \] \],

## Related links

[Configure an alternate port for vCenter](https://docs.servicenow.com/csh?topicname=t_ConfigureAlternatePortForVCenter.html&version=latest "Configure an alternate port for vCenter")

[Available vCenter probes and probe parameters](link)

[vCenter discovery with Software Asset Management](https://docs.servicenow.com/csh?topicname=r_VCenterDataCollected.html&version=latest#d287204e1998 "vCenter discovery with Software Asset Management")

[Data collected for VMware vCenter Server](link)

[VMware credentials](https://docs.servicenow.com/csh?topicname=r_VMwareCredentialsForm.html&version=latest "VMware credentials")

[VMware documentation](https://www.vmware.com/pdf/ProgrammingGuide201.pdf "VMware documentation")

[Broadcom knowledge article](https://kb.vmware.com/s/article/2108405)
