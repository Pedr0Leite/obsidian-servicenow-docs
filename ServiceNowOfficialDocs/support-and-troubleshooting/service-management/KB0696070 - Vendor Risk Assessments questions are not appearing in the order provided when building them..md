---
title: "Vendor Risk Assessments questions are not appearing in the order provided when building them."
aliases:
  - KB0696070
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696070
kb_number: KB0696070
last_modified: 2025-10-29
---

## Vendor Risk Assessments questions are not appearing in the order provided when building them.

  

### Issue

Vendor Risk Assessments questions are not appearing in the order provided when building them.

### Release

Kingston+

### Cause

If a question is dependent on another question, it will always follow directly after the dependent question.

### Resolution

If a question is dependent on another question, it will always follow directly after the dependent question. We opened a dev task and the developer stated that this is done to avoid confusion on which question it was dependent on and it is the expected behavior.

  

However, we have opened an Enhancement request FTASK33916 asking the product owners to consider changing this behavior.
