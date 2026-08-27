---
title: "Change Risk Assessment window does not close upon submission"
aliases:
  - KB0746227
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746227
kb_number: KB0746227
last_modified: 2024-04-07
---

## Change Risk Assessment window does not close upon submission

  

### Issue

When submitting a Risk Assessment on a Change record, the window displaying said Risk Assessment is not automatically closed upon submission.

### Release

ALL

### Cause

This behavior is happening because the user has customized Script Include "SurveyProcessor".

### Resolution

The reason the behavior is seen is that the user had customized the "SurveyProcessor" Script Include.  
  
Reverting this Script Include back to an Out of Box (OOB) state resolves the behavior and the Risk Assessment window closes upon submission.
