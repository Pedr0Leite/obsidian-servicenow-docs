---
title: "Cloud Management Troubleshooting - Events"
aliases:
  - KB0656553
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656553
kb_number: KB0656553
last_modified: 2024-01-28
---

## Issue

Cloud Management Troubleshooting - Events

  
  

# Overview

* * *

You can configure the Azure Alert service, AWS Config service, or VMware Events service to auto-update the CMDB whenever a lifecycle state or configuration change event occurs for an Azure resource. For detailed configuration information, see the following product documentation topics:

-   [Configure the Azure Alert service to auto-update the CMDB](https://docs.servicenow.com/ "Configure the Azure Alert service to auto-update the CMDB")
-   [Configure the Amazon AWS Config service to auto-update the CMDB](https://docs.servicenow.com/ "Configure the Amazon AWS Config service to auto-update the CMDB")
-   [Configure the VMware Events service to auto-update the CMDB](https://docs.servicenow.com/ "Configure the VMware Events service to auto-update the CMDB")

This article describes how alerts are received and processed so you can troubleshoot alerts that do not show up.

# Troubleshooting

* * *

## Alerts not being received from Cloud Provider (Azure, AWZ, VMWare)

**"**Cloud Event" **Scripted REST Service** pulls events from the Cloud Provider and stores them into the **sn\_cmp\_cloud\_event** table

In case of events not being received, you can check this "raw" **sn\_cmp\_cloud\_event** table for received events.

These events in the **sn\_cmp\_cloud\_event** table are processed by the Cloud Event Scheduler:

**System Definition > Scheduled Jobs > Cloud Event Scheduler**

The "Cloud Event Scheduler" schedule job will then look at the table **sn\_cmp\_cloud\_event** and see which events need processing, then it determines which provider it came from (AWS, Azure, VMWare) so that it invokes the right processor (**sn\_cmp\_cloud\_event\_handler** table).

Notice that "Azure AlertHandler V2" in the **sn\_cmp\_cloud\_event\_handler** table is deprecated.

## Azure alerts not showing up

To receive Azure Alert events, you must provide a username for an account with the **sn\_cmp.cloud\_event\_integration** role. In addition, you must disable Authentication for the Cloud Event Scripted REST API because Azure does not currently support authentication.

1.  Navigate to **System Web Services > Scripted Web Services > Cloud Event**.
    
2.  In the **Related Links > Resources** tab, click Cloud Config Event Post.
    
3.  Make sure the **Requires Authentication** checkbox is unchecked.
    
    ![](sys_attachment.do?sys_id=8cce78a2db0ab450e515c2230596199e)
