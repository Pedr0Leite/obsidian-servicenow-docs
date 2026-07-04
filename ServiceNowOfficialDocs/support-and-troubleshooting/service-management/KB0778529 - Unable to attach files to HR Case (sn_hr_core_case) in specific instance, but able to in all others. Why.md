---
title: "Unable to attach files to HR Case (sn_hr_core_case) in specific instance, but able to in all others. Why?"
aliases:
  - KB0778529
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778529
kb_number: KB0778529
last_modified: 2025-09-03
---

## Unable to attach files to HR Case (sn\_hr\_core\_case) in specific instance, but able to in all others. Why?

  

### Issue

When the user attempts to attach a file to a HR Case, the modal shows that is attempting to attach. However, then, the modal just returns to being blank as if no attempt was made to attach a file. Also, no attachment is shown in the header of the HR Case.

### Cause

The "Read" operation ACL for sys\_attachment for HR Core has been customized and is now broken.

### Resolution

As mentioned above, the read ACL for sys\_attachment in the HR Core scope was modified by a non-ServiceNow user.

Reverting this ACL back to the Out of Box (OOB) version resolves the issue. For convenience, here is a link to the ACL:

-   -   /sys\_security\_acl\_list.do?sysparm\_query=nameSTARTSWITHsys\_attachment%5Esys\_package%3Dd4ac3fff5b311200a4656ede91f91af2%5Eoperation%3Dread
