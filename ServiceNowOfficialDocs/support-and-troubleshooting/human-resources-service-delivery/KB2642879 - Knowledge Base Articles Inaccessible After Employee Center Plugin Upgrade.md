---
title: "Knowledge Base Articles Inaccessible After Employee Center Plugin Upgrade"
aliases:
  - KB2642879
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2642879
kb_number: KB2642879
last_modified: 2025-12-14
---

## Knowledge Base Articles Inaccessible After Employee Center Plugin Upgrade

  

### Issue

After updating several plugins in the production instance, including Employee Center, users lost access to all Knowledge Base (KB) articles.  
Out-of-the-box (OOB) Access Control Lists (ACLs) in production differed from those in DEV and UAT, specifically in the Applies To field, resulting in restricted KB access.  
The issue was not present in DEV/UAT, and screenshots were provided showing missing KB articles in PROD.

### Release

Any

### Cause

KB article access was blocked due to changes in ACLs after plugin upgrades in production.  
Two OOB ACLs had been deactivated, and a defect (PRB1741520) updated the read ACL to apply only to KBs in the Employee Center Core scope.

### Resolution

To restore KB access:

-   Investigate ACL differences between environments.
-   Remove any custom ACLs created as a temporary workaround.
-   Reactivate the two OOB ACLs as per the latest OOB versions.
-   Validate KB access for end users after applying changes.
-   Confirm that ACLs align with the updated plugin behavior.

Testing in a temporary copy of the production instance confirmed that reactivating the OOB ACLs and removing the custom ACL resolved the issue.
