---
title: "Cannot trigger flow on SC_Task table"
aliases:
  - KB0791262
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791262
kb_number: KB0791262
last_modified: 2024-04-08
---

## Cannot trigger flow on SC\_Task table

  

### Issue

Users are unable to create a flow triggered by the Creation of 'sc\_task'

### Resolution

-   The sc\_task is not available for the record trigger on the flows from London release, the functionality was removed and is available only for versions before London.
-   The reason behind removing it is because it will create conflicts with other service catalog processes and implementations. Service Catalog tables work in a different way and they have their own business rules and workflows configured to work on them. The new Service Catalog trigger will prevent users from having a workflow and a flow interacting with the same service catalog item.
-   Please refer the below documentation which provides the information :
-   https://docs.servicenow.com/csh?topicname=flow-designer-rn.html&version=latest
