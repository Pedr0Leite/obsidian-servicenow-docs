---
title: "UI11 is rendered when navigating from a catalog item in Service Portal to backend UI"
aliases:
  - KB0814862
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814862
kb_number: KB0814862
last_modified: 2024-04-08
---

## UI11 is rendered when navigating from a catalog item in Service Portal to backend UI

  

### Issue

Navigating back to the normal UI (home) from a Service Portal catalog item may render UI11.

### Release

All releases

### Cause

This can be caused by the incorrect usage of a system parameter named "sysparm\_device."  This parameter is used to determine whether to render the mobile UI or normal UI.  Typically this is done in a script running against a particular catalog item.

### Resolution

We recommend renaming the occurrences of 'sysparm\_device' to something else, which will no longer cause the backend UI to change when navigating back to Home.
