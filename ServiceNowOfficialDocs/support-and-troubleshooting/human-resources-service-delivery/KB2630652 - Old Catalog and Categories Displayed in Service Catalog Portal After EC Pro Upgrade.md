---
title: "Old Catalog and Categories Displayed in Service Catalog Portal After EC Pro Upgrade"
aliases:
  - KB2630652
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2630652
kb_number: KB2630652
last_modified: 2026-01-01
---

## Old Catalog and Categories Displayed in Service Catalog Portal After EC Pro Upgrade

  

### Issue

Users reported that the Service Catalog portal continued to display the old Information Technology catalog and outdated backend categories even after upgrading to Employee Center Pro. Breadcrumbs in the portal showed old categories, leading users to the previous version of the catalog. This issue was reproducible across production, development, and training instances and was observed when searching for items such as _Request Support for Google Workspace_.

### Release

Any Release

### Cause

The issue occurred because the Page Route Map that controls navigation from the `sc_cat_item` page to the `esc_sc_cat_item` page was inactive in the customer’s instance. When inactive, the system follows the default routing logic, which displays breadcrumbs with old categories instead of the Back button and updated categories. This behavior is out-of-box (OOB) and expected when the route map is not enable

### Resolution

-   Confirm that the Page Route Map for routing from `sc_cat_item` to `esc_sc_cat_item` is active.
-   If inactive, activate the Page Route Map to ensure navigation uses the updated Employee Center pages.
-   After activation, the portal will display the Back button and updated categories instead of old breadcrumbs.
-   Validate the changes in all relevant instances to ensure consistent behavior.
