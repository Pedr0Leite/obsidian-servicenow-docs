---
title: "Metric field shows null value in assessment instance (asmt_assessment_instance) record under change request."
aliases:
  - KB0827637
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827637
kb_number: KB0827637
last_modified: 2024-04-08
---

## Metric field shows null value in assessment instance (asmt\_assessment\_instance) record under change request.

  

### Issue

When we open any of the asmt\_assessment\_instance record, metric field under the assessment question is showing null for the user with change\_manager role as well.

The values are shown for maint and admin.

### Release

Orlando 

### Cause

ACL

### Resolution

After adding Change Manager role to ACL -

https://<instance\_name>.service-now.com/sys\_security\_acl.do?sys\_id=af92b034df110100cd7da5f59bf263c7  

Please add the roles under the "Roles Required" to enable those users to view the metric field values.  
This resolves the Issue.  
  

  

### Related Links

The OOB version only has role - snc\_internal customise it depending upon the requirement.
