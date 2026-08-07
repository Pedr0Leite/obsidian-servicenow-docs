---
title: "A possible workaround to managing compliance status for concurrent licenses with Software Asset Management"
aliases:
  - KB0787107
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787107
kb_number: KB0787107
last_modified: 2025-01-03
---

## A possible workaround to managing compliance status for concurrent licenses with Software Asset Management

  

### Issue

Out of box, there is no metric that captures concurrent licenses. 

If you decide to configure your software asset entitlement with the number of concurrent licenses, you may find that there is no suitable license type which would work. For example, if you use the per device metric, your reconciliation results will likely show that you have more installs than the allocated number of licenses which will then result in reconciliation having a status of "non-compliant".

### Resolution

A possible workaround to avoid having your software model result show a status of non compliant if you need to configure the entitlement with the number of concurrent software usage is to set the agreement type to "Enterprise License Agreement (ELA)" which will result in the Status remaining as Compliant even if there are unlicensed installations as noted in the following documentation:

Foundation:  
[https://docs.servicenow.com/csh?topicname=t\_ViewSWModelResultsSAMF.html&version=latest](https://docs.servicenow.com/csh?topicname=t_ViewSWModelResultsSAMF.html&version=latest "https://docs.servicenow.com/csh?topicname=t_ViewSWModelResultsSAMF.html&version=latest")

Professional:  
[https://docs.servicenow.com/csh?topicname=t\_ViewSWModelResults.html&version=latest](https://docs.servicenow.com/csh?topicname=t_ViewSWModelResults.html&version=latest)
