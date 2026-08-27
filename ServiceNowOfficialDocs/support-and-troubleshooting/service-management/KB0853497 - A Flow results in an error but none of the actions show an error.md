---
title: "A Flow results in an error but none of the actions show an error"
aliases:
  - KB0853497
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853497
kb_number: KB0853497
last_modified: 2024-04-08
---

## A Flow results in an error but none of the actions show an error

  

### Issue

The execution of a Flow is showing an error but there is no error recorded in the Flow. Additionally an action shows as Not Run but still recorded 50ms.

### Cause

The action that shows Not Run but still took time resulted in an error. You need to check what went wrong. A possible reason could the inline scripting.

### Resolution

Check the action and look for any problems. You most likely will find it in the inline scripting. Logging has been improved in Orlando.
