---
title: "HR approval not showing up on the Portal Ticket Page"
aliases:
  - KB0761114
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761114
kb_number: KB0761114
last_modified: 2026-03-17
---

## HR approval not showing up on the Portal Ticket Page

  

### Issue

Approval widget is not getting displayed to the requester

Cannot approve HR task on Portal Ticket page

### Release

Not release-specific

### Cause

Approval Widget is missing in the HR Portal Ticket page

The hrj\_ticket\_page is using a customised version of the HRJ Case Info widget

### Resolution

1.  Revert the widget "HRJ Case Info" to the out-of-box (OOB) version. 
2.  Use the OOB widget "HRJ Case Info" in the Portal Page "hrj\_ticket\_page":  
      
      
      
    

### Related Links

[Compare to current version and Revert to Base System](https://docs.servicenow.com/csh?topicname=t_CompareToCurrentVersion.html&version=latest "Compare to current version and Revert to Base System")

[Revert Customization](https://noderegister.service-now.com/kb?id=kb_article_view&sysparm_article=KB0818174 "Revert Customization")
