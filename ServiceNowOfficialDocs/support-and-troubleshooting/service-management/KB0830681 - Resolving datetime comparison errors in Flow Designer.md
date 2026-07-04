---
title: "Resolving date/time comparison errors in Flow Designer"
aliases:
  - KB0830681
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830681
kb_number: KB0830681
last_modified: 2025-08-01
---

## Resolving date/time comparison errors in Flow Designer

  

### Issue

Learn how to fix the "unable to evaluate condition" error when comparing date/time fields in ServiceNow Flow Designer. This article provides a simple solution to ensure your flows run smoothly.

When comparing date/time fields within the **If** logic of Flow Designer, the flow may fail and display the following error message: 

com.snc.process\_flow.exception.OpException: unable to evaluate condition for /if/\_0\_70d5f506dbc59050e9b951295e9619e7 = {0:D}<{1:D} is not a valid conditional expression

### Release

Any supported release

### Resolution

To resolve this issue, change the value of the glide.sys.time\_format system property to its default, out-of-the-box setting. The correct format is HH:mm:ss.
