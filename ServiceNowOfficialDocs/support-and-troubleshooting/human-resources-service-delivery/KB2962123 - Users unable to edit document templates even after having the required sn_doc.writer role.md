---
title: "Users unable to edit document templates even after having the required sn_doc.writer role "
aliases:
  - KB2962123
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2962123
kb_number: KB2962123
last_modified: 2026-04-16
---

## Issue

Users with the `sn_doc.writer` role are unable to edit the "body" field in Document Templates 

## Resolution

Restore the `sn_doc.writer` role to the Conditional Script Writer group. This will re-enable the automatic granting of the `snc_required_script_writer_permission` role when `sn_doc.writer` is assigned to a user, restoring the ability to edit all fields in Document Templates. Alternatively the role can be assigned directly to the user.

## Additional Information

[https://www.servicenow.com/docs/r/zurich/release-notes/access-management-rn.html](https://www.servicenow.com/docs/r/zurich/release-notes/access-management-rn.html)

[https://www.servicenow.com/docs/r/platform-security/security-center/identity-and-access-management.html](https://www.servicenow.com/docs/r/platform-security/security-center/identity-and-access-management.html)

[https://www.servicenow.com/community/servicenow-ai-platform-articles/scripting-governance-tool/ta-p/3344420](https://www.servicenow.com/community/servicenow-ai-platform-articles/scripting-governance-tool/ta-p/3344420)
