---
title: "After submitting the Change Risk assessment the Pop window doesnt get closed."
aliases:
  - KB0747486
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747486
kb_number: KB0747486
last_modified: 2024-04-07
---

## After submitting the Change Risk assessment the Pop window doesnt get closed.

  

### Issue

When submitting a Risk Assessment on a Change record, the window displaying said Risk Assessment is not automatically closed upon submission.

### Release

ALL

### Cause

This behavior is happening because the user has customized UI page "survey\_take".

### Resolution

The reason the behavior is seen is that the user had customized the "survey\_take" UI Page  
  
Reverting this UI Page back to an Out of Box (OOB) state resolves the behavior and the Risk Assessment window closes upon submission.
