---
title: "MID Server selection for AD Orchestration activities with different Domain Controllers for different environment."
aliases:
  - KB0785104
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785104
kb_number: KB0785104
last_modified: 2024-04-08
---

## MID Server selection for AD Orchestration activities with different Domain Controllers for different environment.

  

### Issue

-   Customer has different Domain Controllers serving different Environments: PROD, STAGE, UAT, and DEV
-   There are separate MID Servers to interact with corresponding Domain Controllers. Ex: PRODMID, STAGEMID, UATMID, and DEVMID
-   Customer wants to know how to configure AD Orchestration activities so that it would select the right MID Server to run the activity against depending on the Domain Controller that was specified.

### Resolution

  
1\. Currently Orchestration Activity MID Server selection criteria is based on Host, Capablility, and Application. Capability and Application are chosen during design time so they cannot be passed in dynamically during execution.  
2\. The only attribute left available to perform the selection is the Domain Controller's IP Address.  
3\. For this requirement to work, you would have to have a step before the AD Orchestration steps that would sort out the Environment and obtain the right IP Address for the Domain Controller.  
4\. You will need to configure your MID Server's IP Range as follows:  
\- Remove "ALL" range. With this, you cannot utilize exclude range.  
\- Configure IP Range that would behave the same as "ALL" range. Ex: 0.0.0.0-255.255.255.255  
\- Configure exclude range. Ex: PROD MID Server would exclude Stage, UAT, and DEV Domain Controller IP Addresses.
