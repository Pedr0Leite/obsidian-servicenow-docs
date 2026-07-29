---
title: "Show case to subject person field is checked on HR serivce, However the subject person is still unable to view the HR case"
aliases:
  - KB2685298
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2685298
kb_number: KB2685298
last_modified: 2026-05-06
---

## Show case to subject person field is checked on HR serivce, However the subject person is still unable to view the HR case

  

### Issue

  
 "Show case to subject person" on the HR Service (CEO – Employee Relations) is Enabled. However, the subject person is still unable to view the HR case

### Release

N/A

### Cause

Access is denied in any one of following cases - COE security policy blocks read access, Locked Case, Subject person is an Involved party.

The Out-of-the-Box (OOTB) ACL logic denies access to the Subject person if they are listed as an involved party in the case. This behavior is expected, as involved parties (e.g., complainant, witness, manager) are restricted from viewing Employee Relations (ER) cases to maintain confidentiality and avoid compromising investigations.

[https://<<instance-name>>.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=6b2d76423b120010d901655593efc485](https://instance-name.service-now.com/nav_to.do?uri=sys_security_acl.do?sys_id=6b2d76423b120010d901655593efc485)

### Resolution

The ideal solution is to avoid including the subject person as an involved party in this use case.

If involved parties are added through a flow, the flow logic should be updated to ensure that the subject person is excluded from the involved party list
