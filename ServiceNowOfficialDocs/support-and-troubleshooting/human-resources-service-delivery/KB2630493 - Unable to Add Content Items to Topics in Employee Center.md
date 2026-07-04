---
title: "Unable to Add Content Items to Topics in Employee Center"
aliases:
  - KB2630493
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2630493
kb_number: KB2630493
last_modified: 2026-01-01
---

## Unable to Add Content Items to Topics in Employee Center

  

### Issue

-   Users are unable to add content items to topics in Employee Center.
-   Attempts to add categories via UI actions do not result in content items being added to the related list.
-   This impacts taxonomy usage and content organization.

### Release

Xanadu

### Cause

-   The ContentAssociationUtilAjax script include was customized from the Out-of-Box (OOB) version.
-   Customization may prevent proper handling of content association logic.
-   Older instance versions may lack recent defect fixes and feature updates for taxonomy functionality.

### Resolution

To resolve the issue:

1.  Use Workaround for Adding Content:

1.  -   Navigate to the topic record.
    -   Use the Catalog and Knowledge Categories related list to add or remove content items.

2.  Review Script Include Customization:

2.  -   Navigate to System Definition > Script Includes.
    -   Locate ContentAssociationUtilAjax and compare it with the OOB version.
    -   Revert any customizations to restore standard functionality.

3.  Upgrade Instance for Latest Fixes:

3.  -   Upgrade to the latest release (e.g., Xanadu or later) to obtain updated script includes and taxonomy improvements.

4.  Validate After Changes:

4.  -   Test adding content items to topics via UI actions.
    -   Confirm that items appear in the related list as expected.
