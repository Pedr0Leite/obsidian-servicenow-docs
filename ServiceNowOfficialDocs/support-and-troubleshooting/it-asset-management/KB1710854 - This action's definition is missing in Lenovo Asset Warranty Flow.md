---
title: "This action's definition is missing in Lenovo Asset Warranty Flow"
aliases:
  - KB1710854
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1710854
kb_number: KB1710854
last_modified: 2024-12-06
---

## This action's definition is missing in Lenovo Asset Warranty Flow

  

### Issue

You may see the error "This action's definition is missing" in the "Lenovo Asset Warranty Flow" flow.

![](/sys_attachment.do?sys_id=f8c0e83193929290f2167de86cba1089)

### Release

Any instance with Hardware Asset Management installed.

### Cause

If Hardware Asset Management is installed, that also installs the dependencies com.sn\_itam\_common and com.sn\_phy\_assets, which means the "Lenovo Asset Warranty Flow" flow will be present even if you don't have IntegrationHub or the Lenovo Spoke (sn\_lenovo\_spoke) installed.

Those IntegrationHub apps cannot be automatically installed as a dependency because IntegrationHub is a paid-for optional plugin, not present in all instances. 

### Resolution

If you intend to use this feature, then you will first need an Integration Hub subscription, and have that installed, then you need to add the Lenovo Spoke (sn\_lenovo\_spoke) app.

see [Integration with Lenovo for asset warranty details](https://www.servicenow.com/docs/search?q=Integration%20with%20Lenovo%20for%20asset%20warranty%20details)  
"Integration with Lenovo has the following requirements:

-   The Lenovo Spoke (sn\_lenovo\_spoke) installed on your ServiceNow instance from the ServiceNow Store. For detailed information, see [Lenovo Spoke](https://www.servicenow.com/docs/csh?topicname=lenovo-spoke&version=xanadu&pubname=xanadu-integrate-applications)."
