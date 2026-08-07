---
title: "Survey trigger conditions are not working for a particular survey."
aliases:
  - KB0761205
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761205
kb_number: KB0761205
last_modified: 2026-01-12
---

## Survey trigger conditions are not working for a particular survey.

  

### Issue

Survey is not triggering even though the conditions are being met.

### Cause

Assessable record is missing an associated category.

### Resolution

The behavior seen was due to the assessable record associated to the survey not having a category defined/associated. Once a category was added, this survey fired as expected by the trigger conditions. The following steps were taken:

1.  Navigate to Assessments > Assessable Records.
2.  In the 'Category' related list, add the Category that should be associated to the Assessable record.

### Related Links

Doc: [View an assessable record](https://docs.servicenow.com/csh?topicname=t_ViewAnAssessableRecord.html&version=latest "View an assessable record")

Note: All metric categories associated with the assessable record. An assessable record must be associated to a category to be evaluated.
