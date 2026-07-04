---
title: "Error on updating sys_user_group record"
aliases:
  - KB0998513
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998513
kb_number: KB0998513
last_modified: 2024-09-26
---

## Error on updating sys\_user\_group record

  

### Issue

When updating a sys\_user\_group record, the following error message is thrown:

Exception (TypeError: undefined is not a function. (sys\_script.482ec781df232100a9e78b6c3df26312.condition; line 1)) occured while evaluating'Condition: var sc = new sn\_sm.SMConfiguration(); sc.hasGroupType(current.type, 'vendor') && (current.manager == '' || current.manager == null)' in business rule 'Vendor type requires manager' on sys\_user\_group: Vocera Admins; skipping business rule  
  
The business rule 'Vendor type requires manager' is OOB.

### Cause

The business rule 'Vendor type requires manager' present in the instance without its plugin com.snc.service\_management.core

### Resolution

The business rule 'Vendor type requires manager' can be deactivated or deleted to resolve the issue, it is not supposed to be there on the instance without the ServiceManagement Core plugin.

\*Note: This solution does not apply if the plugin is active in the affected instance.
