---
title: "Discovery creates 2 Server CIs for Hyper-V (Windows Server + Hyper-V Server) - Known issues with this design"
aliases:
  - KB0719772
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719772
kb_number: KB0719772
last_modified: 2025-11-14
---

## Discovery creates 2 Server CIs for Hyper-V (Windows Server + Hyper-V Server) - Known issues with this design

  

### Issue

After Discovering your **Hyper-V Windows Server**, you may find you have **Two CIs for the same server hardware**. In the case of a full Windows Server installation that has the Hyper-V role installed, this is normal given the current design, and this article will explain exactly how it is designed and the problems with this design.

## Table of Contents

-   [Where Discovery puts Hyper-V Servers in the CMDB](#mcetoc_1gkne57mk8k)
    -   [Hyper-V Server (Server Core w/ Hyper-V role only)](#mcetoc_1gkne57mk8l)
    -   [Windows Server with Hyper-V role](#mcetoc_1gkne57mk8m)
-   [Notes on the design](#mcetoc_1gkne57mk8n)
-   [CMDB IRE Identification and De-Duplication Tasks](#mcetoc_1gkng43pu2q)
-   [Model Categories and Ci-Asset synchronisation](#mcetoc_1gkng43pu2r)
-   [Selecting the correct CI](#mcetoc_1gkneonauag)
-   [Discovery Console](#mcetoc_1gknglah66)
-   [Imports and Service Graph Connector](#mcetoc_1gknglah67)
-   [ITOM Visibility licensing Node Counts](#mcetoc_1gkngufiv3)

## Where Discovery puts Hyper-V Servers in the CMDB

Depending on whether the server is running the free server core based version of Hyper-V or if its a full Windows Server install, then the main server CIs are created slightly differently:

### Hyper-V Server (Server Core w/ Hyper-V role only)

[https://en.wikipedia.org/wiki/Hyper-V#Hyper-V\_Server](https://en.wikipedia.org/wiki/Hyper-V#Hyper-V_Server)

-   Classifier: Hyper-V Server  
    -   Where OS Name/edition contains "Hyper-V", but does not contain "without Hyper-V" (not used for e.g. "Windows Server 2008 without Hyper-V")
    -   This classifier is ordered first, so only if there is not a match would classification fall back to the normal server classifier below.
-   The "Hyper-V Server" Pattern will be used for these devices.
-   Only a "Hyper-V Server" \[cmdb\_ci\_hyper\_v\_server\] is created. This is the main CI and has all the related lists for Serial numbers, IPs, Network adapters, Disks, Running Processes etc.
-   The Operating System field will contain the Hyper-V OS name.

### Windows Server with Hyper-V role

[https://en.wikipedia.org/wiki/List\_of\_Microsoft\_Windows\_versions#Server\_versions](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions#Server_versions)

-   Classifier: Windows n Server (e.g. Windows 2022 Server)  
    -   Where OS Name/edition contains "Server"
-   The "Windows OS - Servers" Pattern will be used for these devices, which includes the "Windows - Hyper-V" Library.
-   A "Windows Server" \[cmdb\_ci\_win\_server\] CI is created. This is the main CI and has all the related lists for Serial numbers, IPs, Network adapters, Disks, Running Processes etc.
-   Discovered Application CIs that "Runs On" the server will have the relationships links to the cmdb\_ci\_win\_server CI.
-   An additional "Hyper-V Server" \[cmdb\_ci\_hyper\_v\_server\] is created, with a 'Runs on' relationship to the main Windows Server CI. This will not have all attributes and related lists populated.
    -   Since Sept. 2022, the Name has the "@Hyper-V Server" suffix, and Serial Number the "\_hyper\_v\_server" suffix.
    -   The windows\_host  field of the cmdb\_ci\_hyper\_v\_server  record will reference the cmdb\_ci\_win\_server record.
-   The Operating System field of both records will have the full Windows Server version e.g. "Windows 2012 R2 Datacenter"

## Notes on the design

This applies to both Discovery with either Probes+Sensors or Patterns. Pattern Migration continued the same design the Probes used.

In order for all the Hyper-V CIs and relationships with the Virtual CIs to work together consistently, a "Hyper-V Server" \[cmdb\_ci\_hyper\_v\_server\] class CI must exist.

The cmdb\_ci\_hyper\_v\_server class is in the Hardware branch of the CMDB, when in fact it is Software. That doesn't compare well with more modern Discovery implementations, the CI Class Models and suggested relationships, and CSDM, which came long after. If this was designed today, the cmdb\_ci\_win\_server class would probably be used for the main hardware CI for all editions of Windows Server, and then a Hyper-V Application class used for the Hyper-V software running on that server. 

The above is the current design of Hyper-V Server Discovery. To change this design now, would be problematic.

This design is not considered a Product Defect and is Working as Expected. **Customers still have the option of [creating an Enhancement Request](https://support.servicenow.com/ideas?id=create_edit_idea&sysparm_module_id=enhancement_requests)**. This has already been tried in the past with no result, but this time round it might get enough up-votes.

## CMDB IRE Identification and De-Duplication Tasks

So long as the reference/relationship between them is created properly, the CMDB IRE Reconciliation engine's Health jobs should not mark these as Duplicate, even though they are in effect 2 CIs for the same Hardware. Both are in the Hardware branch so are covered by the "Hardware Rule" identifier.

This stopped working at some point and caused this problem:  
[PRB1564552 / KB1118026 Hyper-V Server pattern steps do not differentiate identification fields from Windows Server, causing conflicts with duplicate remediator](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1118026)

This was fixed in the September 2022 version of the "Visibility Content" app v6.1.0, and later.

The "Windows OS - Servers" Pattern now uses the true name/serial number in the Windows Server CI, and add a "@Hyper-V Server" suffix to the name, and "\_hyper\_v\_server" suffix to the Serial Number of the Hyper-V Server record.

The "Hyper-V Server" Pattern, when creating just a single Hyper-V Server CI, does use the true Name/Serial.

## Model Categories and Ci-Asset synchronisation

There is a Model Category \[cmdb\_model\_category\] for Windows Servers, that will cause a linked Hardware Asset to be created automatically, and keep fields synchronised between them.

There is no Model Category for Hyper-V Server, which means when there is just a Hyper-V Server CI, which is the only CI representing the server hardware, no linked Asset is created.

## Selecting the correct CI

Where there is a normal server that happens to also be running Hyper-V, the pair of CIs are in different classes but **will have the same name**.

They are within the same Server/Computer/Hardware branch of the CMDB so lookup select boxes are likely to have both listed. Which do you use, and how do you tell them apart?

-   If a task is related to the Hardware, or configuration of the OS in general, then the cmdb\_ci\_win\_server record would ideally be used.
    -   This is the CI with all the related lists for Serial numbers, CPU/Memory, Network/IP, Running processes etc. 
    -   The CI with name suffixed with "@Hyper-V Server" would not be used.
-   If a task is related to the Configuration of Hyper-V on the server, or related to the VM instances and Services running on those, then the cmdb\_ci\_hyper\_v\_server record would be more suitable.
    -   This is the CI with all the Hyper-V specific relationships.

Customising list layouts, perhaps for the lookup select box popup on incident/problem/change forms, to include the Class column, will help your ITIL/Asset users.

It would also be possible to add a field to form layout of your tasks, dot-walking to the Class of the referenced Configuration Item. It is best to add a UI Policy to make that  field read-only, to avoid accidental CI reclassification.

## Discovery Console

See:  
[KB1216009 Disabling Hyper-V Server in the Discovery Console does not prevent Hyper-V Server class CIs being created](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1216009)

## Imports and Service Graph Connector

**The Microsoft SMS/SCCM Integration Plugin does not do this the same way.** That imports Hyper-V Server (Server Core w/ Hyper-V role only) hosts into the Windows Server class. This means existing Hyper-V class CIs get reclassified/moved to the Windows Server table, together with the related Hyper-V Instances. A rediscovery causes a new Hyper-V CI to be created, and the one moved by SCCM is now a duplicate.

Issues caused by this incompatibility are being tracked by PRB1362155:  
[KB0812251 SCCM integration puts Hyper-V Servers in Windows Server class \[cmdb\_ci\_win\_server\], whereas Discovery has traditionally put them in Hyper-V Server class \[cmdb\_ci\_hyper\_v\_server\]](https://support.servicenow.com/kb_view.do?sysparm_article=KB0812251 "KB0812251 SCCM integration puts Hyper-V Servers in Windows Server class [cmdb_ci_win_server], whereas Discovery has traditionally put them in Hyper-V Server class [cmdb_ci_hyper_v_server]")

## ITOM Visibility licensing Node Counts

The overcounting of server CIs due to this design was fixed back in the Rome version (PRB1483452).

### Release

Any

### Resolution

NA
