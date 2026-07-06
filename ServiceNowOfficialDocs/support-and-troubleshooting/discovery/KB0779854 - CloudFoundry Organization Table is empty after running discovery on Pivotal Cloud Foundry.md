---
title: "CloudFoundry Organization Table is empty after running discovery on Pivotal Cloud Foundry"
aliases:
  - KB0779854
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779854
kb_number: KB0779854
last_modified: 2024-04-07
---

## CloudFoundry Organization Table is empty after running discovery on Pivotal Cloud Foundry

  

### Issue

-   CloudFoundry Organization Table is empty after running discovery on Pivotal Cloud Foundry.
-   Upon discovering PCF, the data is not getting populated in cmdb\_ci\_pcf\_organization table.

![](sys_attachment.do?sys_id=aadccf30dbc434d0471f9c41ba9619df)

### Release

Madrid Patch 6

### Cause

-   Upon reviewing "Serverless Execution Patterns" under "Discovery Pattern Launcher Parameters" Tab, found the value for "Organization" is showing (empty).
-   As per product documentation, the Organization parameter in "Discovery Pattern Launcher Parameters" Tab, should include name of the organization that is required to be discovered, or all where the input is “\*” . 

![](sys_attachment.do?sys_id=a2dccf30dbc434d0471f9c41ba9619e3)

### Resolution

-   Under "Discovery Pattern Launcher Parameters" in "Serverless Execution Patterns", added " \* " for parameter "Organization" and ran discovery. This shows data get populated in cmdb\_ci\_pcf\_organization Table.

![](sys_attachment.do?sys_id=2edccf30dbc434d0471f9c41ba9619e1)

### Related Links

-   For more information, Please refer to Pivotal Cloud Foundry discovery documentation:  
    [https://docs.servicenow.com/csh?topicname=pivotal-cloud-foundry.html&version=latest](https://docs.servicenow.com/csh?topicname=pivotal-cloud-foundry.html&version=latest)
