---
title: "Purpose of Calculated Lifecycle Information"
aliases:
  - KB2583214
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2583214
kb_number: KB2583214
last_modified: 2026-05-21
---

## Purpose of Calculated Lifecycle Information

  

### Issue

### How Calculated Lifecycle Templates Work

### Release

Any

### Cause

Calculated lifecycle information is used to automatically generate lifecycle phases for a model based on a predefined template. Instead of manually entering dates for phases like Generally Available, End of Sale, or End of Support, the system calculates them using phase offsets and durations defined in the template.

When a calculated lifecycle template is applied and a lifecycle start date is provided, ServiceNow:

-   Automatically creates all lifecycle phases
-   Calculates each phase’s start and end date in sequence
-   Marks the source as calculated for consistency and accuracy

This ensures lifecycle data is standardized across models and reduces manual work.

### Resolution

1\. Template definition

A calculated model lifecycle template defines:

-   The list of lifecycle phases (for example, Generally Available, End of Sale, End of Support)
-   The start offset for each phase, relative to the lifecycle start date (for example, 0 months)
-   The duration of each phase (for example, 60 months)
-   An optional risk score for each phase

These settings determine how the lifecycle is automatically generated for any model that uses the template.

2\. Automatic phase sequencing

Each phase's start date is calculated based on the end date of the previous phase. For example:

-   Generally Available: 0–60 months
-   End of Sale: begins at month 60, lasts 24 months

This ensures the lifecycle progresses in a logical, sequential order.

3\. Applying the template to a model

When a template is linked to a model:

1.  Navigate to the model record in ServiceNow.
2.  In the Lifecycle section, select the calculated lifecycle template.
3.  Enter a lifecycle start date. This serves as the reference date for all phase calculations.
4.  Select Save.

4\. Automatic lifecycle generation

Once applied:

-   All lifecycle phases are populated with calculated start and end dates.
-   The source of the lifecycle data is marked as "calculated" (not manual or content-sourced).
-   Consistency is maintained across all models that use the same template.
-   Manual data-entry errors are eliminated.
