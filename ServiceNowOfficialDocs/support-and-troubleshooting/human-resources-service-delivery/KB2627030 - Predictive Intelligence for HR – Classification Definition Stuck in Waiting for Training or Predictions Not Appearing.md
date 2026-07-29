---
title: "Predictive Intelligence for HR – Classification Definition Stuck in \"Waiting for Training\" or Predictions Not Appearing"
aliases:
  - KB2627030
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2627030
kb_number: KB2627030
last_modified: 2026-01-03
---

## Predictive Intelligence for HR – Classification Definition Stuck in "Waiting for Training" or Predictions Not Appearing

  

### Issue

-   Predictive Intelligence for HR case classification is not working as expected.
-   ML solutions remain in "Waiting for Training" state or do not provide predictions for HR cases.
-   Business impact: Unable to use predictive intelligence for HR case assignment and service prediction.

### Release

Any Release

### Cause

-   Required system properties for HR service and assignment group prediction were not enabled:
    -   `sn_hr_core.case_auto_categorization`
    -   `sn_hr_core.case_auto_assignment`
-   Without these properties, predictions do not appear even if the ML solution is trained successfully.
-   Issue may also occur if record producer setup does not include required input fields.

### Resolution

Verify that the classification solution is trained successfully in Predictive Intelligence > Solution Definitions.

Check and enable the following system properties:

-   Case Auto Categorization: `sn_hr_core.case_auto_categorization`
-   Case Auto Assignment: `sn_hr_core.case_auto_assignment`

Ensure HR case creation via record producer includes all required fields for prediction.

Clear cache and allow time for ML predictions to appear after enabling properties.

For assignment group prediction:

-   If the predicted group matches the one set during case creation, no info message is shown.

For HR service prediction:

-   Prediction appears in the info message on the case form.

After verification, revert system property changes to OOB values if required.
