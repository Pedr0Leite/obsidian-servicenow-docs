---
title: "Feedback Submit Button Not Working After Migrating Feedback Definition"
aliases:
  - KB2651042
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2651042
kb_number: KB2651042
last_modified: 2026-01-01
---

## Feedback Submit Button Not Working After Migrating Feedback Definition

  

### Issue

After migrating a Feedback Definition from the `sn_ex_sp_pro_feedback_definition` table to a higher instance using update sets or XML, the feedback submit button does not work. The issue does not occur when creating a new feedback definition directly in the target instance.

### Release

Any

### Cause

Platform limitation in how update sets handle extended tables. The `sn_ex_sp_pro_feedback_definition` table extends `asmt_metric_type`, and inherited fields such as `table` and `condition` are not captured in update sets. This is expected behavior in ServiceNow.

### Resolution

·  Do not rely on update sets for migrating feedback definitions from extended tables.

·  Export records as XML from the following tables:

-   `sn_ex_sp_pro_feedback_definition`
-   `asmt_metric_category`
-   `asmt_metric`

·  Import these XML files into the target instance to ensure all inherited fields are included.

·  Validate feedback submission functionality after import.

Note: The impacted table (`sn_ex_sp_pro_feedback_definition`) is (OOB), but the migration issue occurs due to platform behavior with extended tables.
