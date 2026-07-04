---
title: "[SAMP] License Type \"Microsoft-core based\""
aliases:
  - KB0824138
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824138
kb_number: KB0824138
last_modified: 2024-04-08
---

## Text

Per the Microsoft guidelines, the license calculation for both the products is specified below.

**Use Case**

Windows Server core Licensing: Need to calculate the total number of cores in a server and thereby assign a minimum of 8 Core licenses Per Processor and 16 core licenses per Server of the physical server/ VM Host.  
SQL Server Core Licensing: Need to calculate the total number of cores in a server and thereby assign a minimum of 4 core licenses per processor of the physical server and for VM, we need to assign a minimum of 4 core licenses per VM.

The metric\_type field on the cmdb\_ci\_hardware references a Software License Calculation record (cmdb\_sw\_license\_calculation) should be set to 'Microsoft core-based'. So, the devices should be tagged with the license calculation in order for the counter to pick it up.  
  
CALCULATION Criteria:  
  
1) If the software is installed on a physical machine, it will calculate based on CPU count \* CPU core count \* core factor. (There is a minimum of 4 rights needed.)  
  
2)If the software is installed on a virtual machine, it will look at the physical machine on which the VM is installed. The calculation will be CPU count \* CPU core count. (Core factor is not applied for virtual.)  
  
3) If there are multiple virtual machines with the software installed and the VMs are all running on the same physical server, one of the VMs will count the rights needed. The others will have valuation 0 if the number of VMs is less than the number of rights needed. However, if there are more VMs with the software installed than the number of rights, the additional right would be needed. For example, if you have a physical server with CPU count = 1, CPU core count = 4, and core factor = 1, you will need 4 rights. If you have 5 VMs each with one install of the software and those 5 VMs are running on the same physical server, one of the VMs will show with valuation 4, 3 of the VMs will show with valuation 0 (since they are already covered), 1 of the VMs will show with valuation 1 (one additional right is needed).

set the value of License Type to "Microsoft-core based" in the Software Model and add any Software License to the Model, In the Software Counter for this Model, Rights used and owned are expected to be calculated

'Microsoft core-based' Licensing is what I think would work out and here are the details-  
  
\- If the software is installed on a physical machine, it will calculate based on CPU count \* CPU core count \* core factor. (There is a minimum of 4 rights needed.)  
\- If the software is installed on a virtual machine, it will look at the physical machine on which the VM is installed. The calculation will be CPU count \* CPU core count. (Core factor is not applied for virtual.)  
\- If there are multiple virtual machines with the software installed and the VMs are all running on the same physical server, one of the VMs will count the rights needed. The others will have valuation 0 if the number of VMs is less than the number of rights needed. However, if there are more VMs with the software installed than the number of rights, the additional right would be needed.  
  
For example, if you have a physical server with CPU count = 1, CPU core count = 4, and core factor = 1, you will need 4 rights.  
If you have 5 VMs each with one install of the software and those 5 VMs are running on the same physical server, one of the VMs will show with valuation 4, 3 of the VMs will show with valuation 0 (since they are already covered), 1 of the VMs will show with valuation 1 (one additional right is needed).
