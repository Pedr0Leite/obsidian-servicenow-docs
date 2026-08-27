---
title: "NEW button on Entry points Related List on Application Services show Page not found error"
aliases:
  - KB0787906
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787906
kb_number: KB0787906
last_modified: 2024-04-07
---

## NEW button on Entry points Related List on Application Services show Page not found error

  

### Issue

NEW button on Entry points Related List on Application Services show Page not found error

**Steps to reproduce:**

1.  Open any record of Application Service \[cmdb\_ci\_service\_discovered\]
2.  In the Entry Points related list, click NEW
3.  Check the pop up for error. It will show page not found error

It will look like below screenshot:

![](sys_attachment.do?sys_id=380813b0db08b0d016d2a345ca961937)

### Cause

The 'New' UI acton calls upon a UI page named sa\_add\_connection. However, this UI page comes from a plugin named com.snc.service-mapping. It could be possible that this plugin is not installed on the customer's instance.

### Resolution

This functionality is currently being investigated via PRB1459918, where we are currently expecting 2 outcomes from this PRB, based on the decisions that Development can make:

1\. We allow customers without Service Mapping to use this feature

2\. We remove the NEW button from the related list since customers without Service Mapping should restricted from using it

  

As a workaround, the customer needs to install the above plugin (com.snc.service-mapping) to get the UI page, so the proper URL will open for them to create the Entry Points. Please note that this is a paid plugin.

### Related Links

The following plugins are activated automatically when the Service Mapping plugin (com.snc.service-mapping) is activated:

-   Discovery (com.snc.discovery)
-   Pattern Designer (com.snc.pattern.designer)
-   Cloud Management Core (com.snc.cloud.core)
-   Performance Analytics – Content Pack – Service Mapping (com.snc.service-mapping.pa.content)
-   Event Management and Service Mapping Core (com.snc.service-watch)

More details available on: [Request Service Mapping](https://docs.servicenow.com/csh?topicname=t_ActivateServiceMappingPlugin.html&version=latest "Request Service Mapping")
