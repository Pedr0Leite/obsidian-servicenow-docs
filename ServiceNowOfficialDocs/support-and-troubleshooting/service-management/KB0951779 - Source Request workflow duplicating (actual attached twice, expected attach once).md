---
title: "Source Request workflow duplicating (actual: attached twice, expected: attach once)"
aliases:
  - KB0951779
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0951779
kb_number: KB0951779
last_modified: 2024-09-20
---

## Source Request workflow duplicating (actual: attached twice, expected: attach once)

  

### Issue

Unexpectedly, the user's Source Request workflow was attaching 2x to a single record. They wanted to know why. They were expecting only a single attachment of the Source Request workflow.

### Cause

After reviewing the localhost logs at the time of the creation of the REQ, it was noted that the user's custom Business Rule (henceforth "BR") which contained a `.update()` was firing at the exact same time - triggering a double update and causing the duplicate, unexpected workflow attachment.

### Resolution

As per the above, the user's custom BR fired and triggered a `.update()` against the record during the workflow's attachment.

Hence, the workflow was attaching twice when the conditions on the custom BR.

To resolve the issue, the user was counseled to deactivate the custom BR which was responsible for causing the duplicate workflow attachment. While inactive, the user should review their custom BR internally with their development team, as we in Support are experts in OOB behavior and specialize in resolving OOB break-fix behaviors. Unfortunately, the debugging and implementation of customizations like this is not in Support's area of expertise and is out of scope.
