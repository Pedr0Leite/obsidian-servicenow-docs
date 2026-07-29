---
title: "Granular Delegation for HRSD."
aliases:
  - KB3008893
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3008893
kb_number: KB3008893
last_modified: 2026-05-22
---

## Granular Delegation for HRSD.

  

### Issue

**Problem**  
When delegating a user using the OOTB delegate functionality, the delegated user is unable to view complete case details when attempting to open the case via the link provided in the email notification. The delegated user receives an access error message ('Sorry either the record does not exist or you do not have enough access to record') instead of viewing the case details, unlike the original user. This issue affects HR cases and impacts payroll and other HR-related functions in production.  
  

### Release

All

### Cause

**Root Cause**  
1\. Granular Delegation functionality in HR Service Delivery is limited to HR tasks (sn\_hr\_core\_task) and does not apply to HR case tables (sn\_hr\_core\_case).  
2\. OOTB ACLs for HR cases do not evaluate delegation permissions, resulting in access errors for delegated users attempting to view case details via email links.  
  

### Resolution

**Steps to Resolve**  
1\. The issue is confirmed to be working as designed, as Granular Delegation in HR Service Delivery is scoped to HR tasks (sn\_hr\_core\_task) and not HR cases (sn\_hr\_core\_case).  
2\. The OOTB ACLs for HR cases do not include delegation checks, so delegated users cannot access HR case records via email links.  
3\. Please check the below Product document for more details.  
  
[https://www.servicenow.com/docs/r/employee-service-management/granular-delegation/granular-delegation.html](https://www.servicenow.com/docs/r/employee-service-management/granular-delegation/granular-delegation.html)
