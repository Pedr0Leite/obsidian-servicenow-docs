---
title: "COE Security Policy Configuration is not restricting access to HR cases."
aliases:
  - KB2474350
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2474350
kb_number: KB2474350
last_modified: 2025-09-03
---

## COE Security Policy Configuration is not restricting access to HR cases.

  

### Issue

The COE security configuration is not working correctly, allowing users to see HR cases they should not have access to. 

  
  

### Release

All

### Resolution

There are many ways to debug a COE security policy configuration, and one of the most common issues encountered is the presence of extra spaces in the names.

1.  When a COE security policy configuration is created, it is crucial to utilize sys\_id values of the group instead of names in the condition builder to ensure accuracy and prevent potential issues.
2.  Using group names can lead to maintenance challenges, particularly when group names are inadvertently modified, which can result in configuration errors and policy failures.
3.  When encountering issues with a COE security policy that utilizes group names, it is essential to verify that all group names are correctly entered. This involves carefully reviewing the sys\_user\_group record to ensure that the names match exactly with those used in the policy configuration.
4.  In a scenario where a group name had an extra space in the sys\_user\_group record, and the same extra space was not added in the COE security policy condition, the condition would fail. This highlights the importance of meticulous attention to detail when configuring security policies.
5.  Such details can be challenging to check, especially when dealing with a large number of groups. To avoid such situations, it is highly recommended to use sys\_id values of the group instead of names in the condition builder, as this approach reduces the likelihood of human error and ensures greater consistency.
