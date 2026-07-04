---
title: "\"My Profile\" Page Configuration Not Reflecting in Custom Employee Center Portal"
aliases:
  - KB2636896
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636896
kb_number: KB2636896
last_modified: 2026-01-01
---

## "My Profile" Page Configuration Not Reflecting in Custom Employee Center Portal

  

### Issue

Configuration changes to the My Profile page in the Employee Center custom portal (e.g., `/gse`) do not reflect as expected, unlike in the default `/esc` portal.

-   Both portals use the same hri\_user\_profile page.
-   Updates and layout changes apply only to `/esc`, not to the custom portal, even after updating sn\_employee\_portal\_configuration.

### Release

Any Release

### Cause

Out-of-box (OOB) sp\_page\_route\_map records exist only for the `/esc` portal.  
Opting in via the Employee Profile setup module activates the OOB route map for `/esc` but does not automatically create or update records for custom portals.

### Resolution

1.  Navigate to sp\_page\_route\_map in the custom portal instance.
2.  Create two new sp\_page\_route\_map records for the custom portal (e.g., `/gse`):
    -   Use the OOB `/esc` records as a template.
    -   Ensure the Page field points to hri\_user\_profile.
    -   Keep both records Active.
3.  Save the records and clear the cache.
4.  Verify that the My Profile page now reflects configuration changes in the custom portal.

Additional Info:

-   Manual creation of route map records is required for custom portals.
-   This is expected behavior; OOB configuration does not auto-provision for non-standard portals.
