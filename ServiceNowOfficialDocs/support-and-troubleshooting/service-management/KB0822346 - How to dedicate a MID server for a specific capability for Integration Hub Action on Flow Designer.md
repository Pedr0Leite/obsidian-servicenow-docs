---
title: "How to dedicate a MID server for a specific capability for Integration Hub Action on Flow Designer"
aliases:
  - KB0822346
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0822346
kb_number: KB0822346
last_modified: 2024-04-08
---

## Issue

The Mid Server with a specific capability ("IH\_SSH" as sample) is not picked when specifying this MID application under connection details in the Flow Designer action.

When there are more than one Mid Server in the instance , in IntegrationHub the MID server is selected when testing appears to be random and but the MID server specified as default is not selected.

## Resolution

MID selection happens via IP address range , application and the network capability:

[Configuring MID Servers](https://docs.servicenow.com/csh?topicname=c_MIDServerConfiguration.html&version=latest "Configuring MID Servers")

The Property **mid.server.rba\_default** (Default MID) is only applicable/used with Orchestration. IntegrationHub does not use it.  
IntegrationHub selects mid based on specified HOST,Application and Capabilities. If 2 or more MID server fits in the criteria then one of them is selected randomly.

One way ; always use the same MID for the capability "IntegrationHub" is to create a new Mid Server Application and assign to only 1 MID.

To run for dedicated MID server for Integration Hub for a specific capability "IH\_SSH" , please do below:

1.  Add a new MID server capability "IH\_SSH".  
    2\. Add the capability to the MID server which you want to be dedicated, selected.  
    3\. Navigate to all other MID servers and delete 'ALL' and add other MID server capabilities as needed.  
    4\. Go to the flow designer steps and add the new capability "IH\_SSH" to the flow.

PS: IH\_SSH is a sample capability name , same suggestion can be followed for any specific capabilities to run for a dedicated mid-server.
