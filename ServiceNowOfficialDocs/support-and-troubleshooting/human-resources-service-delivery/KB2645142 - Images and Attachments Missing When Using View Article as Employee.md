---
title: "Images and Attachments Missing When Using \"View Article as Employee\""
aliases:
  - KB2645142
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2645142
kb_number: KB2645142
last_modified: 2026-01-01
---

## Images and Attachments Missing When Using "View Article as Employee"

  

### Issue

When using the View Article as Employee feature while impersonating a user, knowledge articles do not display images or attachments as expected.

-   Images may be missing when viewed as employee, even though they appear correctly in the portal.
-   Attachments may not be visible when using the "View as Employee" functionality, despite being accessible to other users.

### Release

Any

### Cause

The issue occurs due to a defect in ACL (Access Control List) logic for attachments in the "View Article as Employee" scenario. The ACL does not account for users with ViewAs permissions, resulting in missing images and attachments.

### Resolution

A workaround was implemented to address the ACL logic:

-   Create a global Script Include extending `KBViewModelSNC` with a method `attachmentCanReadForViewAsUser` to check access for the reportee.
-   Update the ACL script to allow read access if this method returns true.
-   XML files for the workaround should be deployed and tested in a sub-production instance before applying to production.

A permanent fix is planned for a future release.
