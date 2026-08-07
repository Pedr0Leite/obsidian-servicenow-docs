---
title: "Multiple VM instances or VM templates can be mapped to the same configuration item (CI) record"
aliases:
  - KB0565052
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0565052
kb_number: KB0565052
last_modified: 2024-04-07
---

## Issue

Multiple VM instances or VM templates can be mapped to the same configuration item (CI) record 

Overview

* * *

The **correlation\_id** field in the VMware Virtual Machine Instance \[cmdb\_ci\_vmware\_instance\] and VMware Virtual Machine Template \[cmdb\_ci\_vmware\_template\] tables have the same value as the virtual machine's **serial\_number** field. In all three tables, this value is the BIOS UUID, but is expressed in a different format.  

In versions prior to Helsinki, only the BIOS UUID is used to identify VM templates and VM instances, or to match a VM instance to a virtual machine. In certain vCenter configurations, multiple VM instances, VM templates, and virtual machines can have the same BIOS UUID.

Possible causes

* * *

Example scenarios that can create duplicate BIOS UUID values:  

-   When you convert a virtual machine using the VMware converter or when you clone a virtual machine, the new virtual machine does not have a unique BIOS UUID. For details, see [Editing a virtual machine with a duplicate UUID.bios](https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1002403).
-   When copying VM template files to a standalone ESX host before it is managed by vCenter, all the templates have the same UUID. For details, see [Change your VMware VM UUIDs to be Unique](http://www.derekseaman.com/2010/10/making-your-vmware-vm-uuids-unique.html).
-   Duplicate UUIDs are created if you answer “moved” incorrectly when vCenter asks if you moved or copied a VM Instance that you copied to a new location. For details, see [Changing or keeping a UUID for a moved virtual machine (1541)](https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1541) and [VMware vSphere “I moved it” or “I copied it.”](http://techhead.co/vmware-esx-i-moved-it-or-i-copied-it-whats-the-difference/)

Establishing the relationship between a VM instance and a virtual machine  

* * *

In versions prior to Helsinki, Discovery matches the **correlation\_id** field from the VMware Virtual Machine Instance \[cmdb\_ci\_vmware\_instance\] table to the **serial\_number** field from the Computer \[cmdb\_ci\_computer\] table to determine the relationship. In versions at Helsinki or later, Discovery attempts to match different fields, depending on the CI that is discovered first.  

VM instance discovered after virtual machine  

* * *

The **Instantiates** relationship from the VM instance to the virtual machine is established if both of these conditions are met:  

-   The virtual machine's **serial\_number** field matches the VM instance's **correlation\_id** field.
-   At least one MAC address returned by the sensor for the VM instance matches a MAC address on the virtual machine's network adapters.

Virtual machine discovered after VM instance  

* * *

If the virtual machine's **serial\_number** field matches the VM instance's **correlation\_id**, Discovery creates the **Instantiates** relationship from the VM instance to the virtual machine.

  

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: Discovery cannot match the MAC address because the VM instance sensor does not store addresses.</td></tr></tbody></table>

Identifying VM instances and VM templates  

* * *

In versions prior to Helsinki, Discovery identifies VM instances and VM templates by using the **correlation\_id** field in the VMware Virtual Machine Instance \[cmdb\_ci\_vmware\_instance\] and VMware Virtual Machine Template \[cmdb\_ci\_vmware\_template\] tables.  

In versions at Helsinki or later, Discovery uses the following criteria to identify VM instances and VM templates:

-   Attempts to identify the CI using the **vm\_instance\_uuid** and **vcenter\_uuid.**
-   If no match, attempts to identify the CI using the **correlation\_id**, **object\_id**, and the **vcenter\_uuid**. The **object\_id** is the Managed Object ID from vCenter.
-   If neither of the preceding methods results in a match, Discovery adds the VM instance or VM template as a new CI.
