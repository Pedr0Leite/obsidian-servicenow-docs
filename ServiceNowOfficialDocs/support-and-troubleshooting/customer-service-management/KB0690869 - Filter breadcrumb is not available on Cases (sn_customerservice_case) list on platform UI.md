---
title: "Filter breadcrumb is not available on Cases (sn_customerservice_case) list on platform UI"
aliases:
  - KB0690869
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690869
kb_number: KB0690869
last_modified: 2024-01-28
---

## Issue

# Symptoms

* * *

The filter breadcrumb is not available on Cases (sn\_customerservice\_case) list on platform UI.

![](sys_attachment.do?sys_id=32f820aedb02b450e515c22305961999)

# Release

* * *

All releases

# Environment

* * *

Customer Service plugin is activated

# Cause

* * *

This behavior only affects users with either of the following roles:

sn\_customerservice.customer

sn\_customerservice.customer\_admin

And it's actually expected behavior. The filter breadcrumb is intentionally hidden on platform UI as users with these roles are meant to operate only on the Customer Service Portal. The filter breadcrumb will be available for these users on the Portal for the Cases (sn\_customerservice\_case) list.

# Resolution

* * *

There's no resolution as this is by design and expected behavior.

The filter breadcrumb is intentionally hidden on platform UI as users with sn\_customerservice.customer or sn\_customerservice.customer\_admin role are meant to operate only on the Customer Service Portal. The filter breadcrumb will be available for these users on the Portal for the Cases (sn\_customerservice\_case) list.

![](sys_attachment.do?sys_id=baf820aedb02b450e515c2230596199e)

# Additional Information

* * *

[Customer Service Management](https://docs.servicenow.com/csh?topicname=c_CustomerServiceManagement.html&version=latest "Customer Service Management")
