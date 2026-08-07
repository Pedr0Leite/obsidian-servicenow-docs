---
title: "Manager View All Cases"
aliases:
  - KB0788872
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788872
kb_number: KB0788872
last_modified: 2025-03-25
---

## Manager View All Cases

  

### Issue

As per the doc here [https://docs.servicenow.com/csh?topicname=c\_CustomerServiceCaseList.html&version=latest,](https://docs.servicenow.com/csh?topicname=c_CustomerServiceCaseList.html&version=latest, "CustomerServiceCaseList") users with the sn\_customerservice\_manager role should be able to view all cases. This KB discusses one reason why managers may not be able to see cases on an instance.

### Cause

If the roles that the sn\_customerservice\_manager role contains have been deleted, managers will not be able to view all cases.

### Resolution

Verify that the sn\_customerservice\_manager role contains the correct roles as per these docs and that these roles have not been modified:

[RolesInstalledWithCustomerService](https://docs.servicenow.com/csh?topicname=r_RolesInstalledWithCustomerService.html&version=latest "RolesInstalledWithCustomerService")

[KB0639072](https://support.servicenow.com/kb_view.do?sysparm_article=KB0639072 "KB0639072")
