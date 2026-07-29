---
title: "Users are unable to access cases on the ER (sn_hr_er_case) table."
aliases:
  - KB2301994
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2301994
kb_number: KB2301994
last_modified: 2025-09-03
---

## Users are unable to access cases on the ER (sn\_hr\_er\_case) table.

  

### Issue

Users are unable to access the ER (sn\_hr\_er\_case) table, resulting in a security constraint error. This issue prevents users from viewing records in the table, despite having the necessary permissions.   
  

### Release

Yokohama

### Cause

Custom COE security 'Read' policies set on the ER (sn\_hr\_er\_case) table.

### Resolution

1\. Review the custom COE security policies set against the Employee relations table. 

2\. Add a group the user is part of to the proper COE security records per business requirements to grant access to the ER table. 

### Related Links

[Create a COE security policy](https://www.servicenow.com/docs/bundle/yokohama-employee-service-management/page/product/human-resources/task/hr-create-coe-security-policy.html "COE security policy")
