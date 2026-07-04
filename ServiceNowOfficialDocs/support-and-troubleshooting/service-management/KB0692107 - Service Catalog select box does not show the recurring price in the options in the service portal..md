---
title: "Service Catalog select box does not show the recurring price in the options in the service portal."
aliases:
  - KB0692107
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692107
kb_number: KB0692107
last_modified: 2024-04-07
---

## Service Catalog select box does not show the recurring price in the options in the service portal.

  

### Issue

# Symptoms

* * *

Service Catalog Select Box rendering error

# Release

* * *

KP5

# Cause

* * *

If the "Include none" field is checked in the "select box variable", then in the service portal, the recurring price is not shown.

# Resolution

* * *

The issue occurs when we check the "Include none" field under "Type specifications" in the "Select box variable". If we uncheck the "include none", the issue does not occur and we can see both the "base price" and "recurring price" in the select box options. 

This issue has been fixed in the London version.

We have a Workaround for this issue, if we uncheck the "include none" field in the select box variable, the issue will not occur.
