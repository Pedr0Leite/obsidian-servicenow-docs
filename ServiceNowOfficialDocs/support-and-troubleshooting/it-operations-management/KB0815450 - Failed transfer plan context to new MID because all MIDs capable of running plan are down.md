---
title: "Failed transfer plan context to new MID because all MIDs capable of running plan are down"
aliases:
  - KB0815450
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815450
kb_number: KB0815450
last_modified: 2024-04-08
---

## Failed transfer plan context to new MID because all MIDs capable of running plan are down

  

### Issue

-   -   While testing flow designer flow , one might come across an error message like below:  
        Cancelled : error="Failed transfer plan context: c0beaeebdbf20410a06683305b961900 to new MID because all MIDs capable of running plan are down"  
          
        ![](sys_attachment.do?sys_id=c8622c09db8874d0b55f0b55ca96193f)

### Release

-   -   ALL

### Cause

1.  1.  The MID Server capabilities does not qualify to run the flow.
    2.  Thus it logs , all MIDs capable of running the flow are down.
    3.  This can also be seen while the available MID Servers are down as well.

### Resolution

1.  1.  Add required capabilities or add 'ALL' as capabilities to the MID Server.
    2.  Run the flow designer flow.
    3.  It will be successfully processed.

### Related Links

1.  1.  MID Server capabilities define the specific functions of a MID Server within an IP address range.
    2.  Several applications, such as Discovery, Service Mapping, Cloud Management, and Orchestration can use capabilities, IP ranges, and [MID Server Selection](https://docs.servicenow.com/csh?topicname=c_MIDServerSelector.html&version=latest#c_MIDServerSelector "MID Server Selection") to narrow the pool of MID Servers the applications need.
        
        Note: At least one capability is required for each MID Server used by Orchestration. See [MID Servers for Orchestration](https://docs.servicenow.com/csh?topicname=c_OrchestrationMID.html&version=latest "MID Servers for Orchestration") for more information.
        
        The following capabilities are available by default with Discovery:
        
        -   All
        -   Cloud Management
        -   Nmap
        -   PowerShell
        -   Resolve DNS
        -   REST
        -   SNMP
        -   SOAP
        -   SSH
        -   VMware
        -   WMI
