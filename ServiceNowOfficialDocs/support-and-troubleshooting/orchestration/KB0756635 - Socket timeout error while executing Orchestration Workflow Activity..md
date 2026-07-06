---
title: "Socket timeout error while executing Orchestration Workflow Activity."
aliases:
  - KB0756635
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756635
kb_number: KB0756635
last_modified: 2026-05-29
---

## Socket timeout error while executing Orchestration Workflow Activity.

  

### Issue

-   On executing the HR Integration Connector workflow, it triggers the **"HR Integrations Web Service"** activity which is getting failed due to a timeout error.
-   This article will demonstrate the issue and possible solutions to it. This article will demonstrate the investigations and probable use cases, hence in future, if a similar error occurs then this can be one of the causes and worth trying to fix.

![](sys_attachment.do?sys_id=f7ec0a53db016514b5d6e6be1396198b)

### Release

Any

### Cause

The timeout value is the cause of the issue. If the activity gets triggered, and if it does not get any result in specified time, then it displays the timeout error.

### Resolution

-   HR Integration Web Service" Activity has a timeout value set to 65.
-   The value is updated to 256. Post this change, the workflow is executing successfully and the activity is no more getting timed out.

![](sys_attachment.do?sys_id=7fec0a53db016514b5d6e6be139619b5)
