---
title: "Moving Event Management Connector Instances records using update sets"
aliases:
  - KB0786128
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786128
kb_number: KB0786128
last_modified: 2024-04-08
---

## Issue

-   The requirement is to move "Connector Instances" records from one instance to another instance using update sets but the same is not working.

## Resolution

-   Out of the box, for the em\_connector\_instance table, there is no update\_sync=true attribute configured by default and also it is not recommended to configure it. ServiceNow does not recommend moving connector instances records by using update sets.
-   The major reason for this is that the connector instance record is being updated every 2 minutes during the execution of the event collection job and it contains last event connection status and signature that is relevant only for a specific instance where the connector is defined.
-   However, the connector definition table (em\_connector\_definition) and the connector instance parameters (em\_connector\_instance\_value) can be moved by using update sets as they have an update\_sync attribute. below one such sample.

  
![](sys_attachment.do?sys_id=fdcedc85db0c70905a959c41ba9619ac)

## Additional Information

-   [Customizations tracked by update sets](https://docs.servicenow.com/csh?topicname=customizations-tracked-update-sets.html&version=latest "Customizations tracked by update sets")
