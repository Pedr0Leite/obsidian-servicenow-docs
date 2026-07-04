---
title: "Missing ESC Portal Search Sources in ais_search_source Table After Employee Center Installation"
aliases:
  - KB2636763
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636763
kb_number: KB2636763
last_modified: 2025-12-16
---

## Missing ESC Portal Search Sources in ais\_search\_source Table After Employee Center Installation

  

### Issue

After installing Employee Center, the following issues occur:

-   ESC Portal Knowledge Bases and ESC Portal Catalogs search sources are missing from the `ais_search_source` table.
-   Employee Center Core Scope is not available for selection in the application scope picker.
-   These issues block project delivery and prevent proper search configuration

### Release

Any Release

### Cause

-   The `ais_search_source` records exist in the Employee Center Core scope.
-   The read ACL for `ais_search_source` is in the global scope, causing the ACL to be skipped and the list to appear empty.
-   Application administration is enabled in Employee Center Core, requiring specific roles for access.

### Resolution

1.  Verify that the Employee Center Core plugin is installed and active.
2.  Check roles for the user:
    -   Ensure the user has both ais\_admin and sn\_hr\_sp.admin roles.
3.  If search sources still do not appear:
    -   Create a read ACL in the Employee Center Core scope for the `ais_search_source` table to grant visibility.
4.  Navigate to AI Search Administration and confirm that search sources for ESC Portal Knowledge Bases and ESC Portal Catalogs are now visible.
5.  Apply any required search source configurations for the ESC portal.

Additional Info:

-   A problem record (PRB1852639) was logged for this behavior.
-   This is expected functionality due to application administration settings in Employee Center Core.
