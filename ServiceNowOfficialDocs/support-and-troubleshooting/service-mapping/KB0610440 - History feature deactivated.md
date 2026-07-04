---
title: "History feature deactivated"
aliases:
  - KB0610440
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0610440
kb_number: KB0610440
last_modified: 2025-12-04
---

## Issue

When viewing Service Mapping map, "History feature deactivated" message shows up.

## Resolution

#### Sync to Service Model property is disabled

**From navigator:**

1.  Search for Service Mapping --> Administration --> Properties
2.  Check "Sync Service Mapping operations with Service Modeling"

#### Service Model corruption

**From business service configuration screen:**

1.  Click "Sync with Service Model" and check if the message still exist
2.  If yes
    -   Click "Remove from Service Model" UI action
    -   Click "Sync with Service Model" UI action
    -   Check if the message still exist

**NOTE: Maint** access is needed to perform "Sync with Service Mode" action.
