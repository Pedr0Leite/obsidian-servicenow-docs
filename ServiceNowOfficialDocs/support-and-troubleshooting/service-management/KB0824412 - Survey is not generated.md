---
title: "Survey is not generated"
aliases:
  - KB0824412
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824412
kb_number: KB0824412
last_modified: 2026-02-19
---

## Survey is not generated

  

### Issue

Survey stopped generating even if the Trigger condition is satisfied

### Release

Any

### Cause

The "Category Assessable Records" which is the relationship between Metric Category and Assessable Record is missing or was not generated due to a customization.

### Resolution

To solve the issue, add an entry in \[asmt\_m2m\_category\_assessment\]

Populate with the survey name, category, and the domain of the survey

### Related Links

Ideally, the survey that was created from survey design should have automatically generate the \[asmt\_m2m\_category\_assessment\] record

Check how the survey was created and check any customizations running during the creation
