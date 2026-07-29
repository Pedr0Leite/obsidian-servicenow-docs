---
title: "\"Check model and model category\" BR Runs on \"cmdb_ci_ot_field_device\" table"
aliases:
  - KB2707282
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2707282
kb_number: KB2707282
last_modified: 2026-01-15
---

## Issue

When users create or update a CI on `cmdb_ci_ot_field_device`, a red banner appears:

> “Asset class, model class and model category don't match, enterprise-class assets cannot be created or updated.”

## Resolution

To resolve the issue where the Enterprise Asset is not created or an error banner appears, follow the steps below to validate the Industrial Model and Model Category configuration:

1\. Update the Industrial Model on the Affected CI

-   Navigate to the affected Configuration Item (CI).
-   Ensure the Model ID field is populated with a valid Industrial Model.
-   If the CI has a Parent CI, ensure the Parent CI also has a valid Industrial Model assigned.

2\. Verify the Model Record Configuration

-   Open the Model record used in Step 1.
-   Confirm that the record exists in the Industrial Model table (`sn_ent_industrial_model`).
-   Verify that the Model Category field on the model record includes OT Field Device.

3\. Confirm Model Category and Class Alignment Ensure the following classes and categories are aligned for successful asset generation:

-   CI Class: `cmdb_ci_ot_field_device`
-   Product Model Class: `sn_ent_industrial_model`
-   Asset Class: `sn_ent_industrial_asset`

4\. Check Asset Tracking Strategy

-   Navigate to the Model Category record for "OT Field Device".
-   Ensure Asset Tracking is set to Enabled (or the appropriate strategy for your instance) if automatic asset creation is required.

5\. Save and Validate

-   Once all configurations are verified, return to the affected CI record.
-   Save the record to trigger the synchronization.
-   Confirm that the corresponding Enterprise Asset has been created or updated and that the error banner is no longer displayed.
