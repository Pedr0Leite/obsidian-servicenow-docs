---
title: "Attachment Functionality Fails on Certain Pages in Employee Center Portal "
aliases:
  - KB2653671
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2653671
kb_number: KB2653671
last_modified: 2025-12-17
---

## Attachment Functionality Fails on Certain Pages in Employee Center Portal

  

### Issue

Attachment functionality does not work on the sc\_cat\_item page when accessed via specific links such as Favorite page or Get HR Support page in Employee Center. Clicking Choose a file does not respond. Attachments work correctly from other links (e.g., AI Search results, My Recent Items widget).

### Release

Any

### Cause

Known defect tracked under PRB1846787, related to the Angular provider (`/sp_angular_provider.do`) causing JavaScript errors that block attachment functionality.

### Resolution

-   Workaround:
    -   Update the Angular provider code by adding a conditional check for `$scope.data && $scope.data.spInstanceId` to prevent JavaScript errors.
    -   Apply this change in a sub-production environment first.
-   Permanent Fix:
    -   Included in the Content Experiences bundle May 2025 release.
    -   Remove the workaround after upgrading to the fixed version.
