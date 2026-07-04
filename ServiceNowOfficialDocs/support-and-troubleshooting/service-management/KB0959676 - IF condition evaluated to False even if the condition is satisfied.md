---
title: "IF condition evaluated to False even if the condition is satisfied"
aliases:
  - KB0959676
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0959676
kb_number: KB0959676
last_modified: 2024-04-18
---

## IF condition evaluated to False even if the condition is satisfied

  

### Issue

IF condition evaluated to False even if the condition is satisfied

### Cause

For a particular variable X, on selecting the value as A, variable Y gets hidden. This is not the case when the variable value of X is selected as B.

Due to this we cant manually update the value of variable Y and the default value for this variable gets updated on the RITM.

If I unhide this variable and fill the value manually while submitting the catalog item, then the issue is not observed and the flow gets executed as expected.

If I again hide this variable on the catalog item while submitting it, the issue could be reproduced again.

The issue is with the hidden variable Y for which is picking up the default value.

### Resolution

Unhide the variable Y for and let the users fill in the values manually after which the issue would not be observed.
