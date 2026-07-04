---
title: "Custom Role Unable to Complete Bulk Case Segment Group Creation in HR Agent Workspace (Works in UI16) "
aliases:
  - KB3136953
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3136953
kb_number: KB3136953
last_modified: 2026-07-03
---

## Issue

**Problem**  
Customer is using a customr role and is unable to complete Bulk Case Segment Group creation in the HR Agent Workspace. While the functionality works in the UI16 backend, the created User Segment Group records lack the mandatory reference to the parent Bulk Case Request, rendering them unusable. The issue is isolated to the HR Agent Workspace experience, as the same user and role can successfully create and link Segment Groups in UI16.  
  

## Resolution

**Steps to Resolve**  
1\. Identify the Scripted REST API used for creating Segment Groups in the HR Agent Workspace (https://<instance>.service-now.com/nav\_to.do?uri=sys\_ws\_operation.do?sys\_id=76e67701b7073010a7f9219bee11a9db) and add the custom role to this REST API.

2\. Ensure the custom role is granted access by adding it to the ACL roles for the associated Script Include 'HrBulkCaseRequestAjaxHelper'. Do this by adding the custom role to the HrBulkCaseRequestAjaxHelper: (https://<instance>.service-now.com/sys\_security\_acl.do?sys\_id=047d1e86436406109a6990178fb8f2f1)

3\. Reproduce the process in the HR Agent Workspace to confirm the parent Bulk Case Request reference is now populated correctly.
