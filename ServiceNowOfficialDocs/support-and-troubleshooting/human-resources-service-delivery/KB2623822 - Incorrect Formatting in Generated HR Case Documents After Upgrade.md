---
title: " Incorrect Formatting in Generated HR Case Documents After Upgrade"
aliases:
  - KB2623822
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2623822
kb_number: KB2623822
last_modified: 2026-01-03
---

## Incorrect Formatting in Generated HR Case Documents After Upgrade

  

### Issue

When generating or regenerating HR Case documents, the resulting PDF shows incorrect formatting—missing spaces in sections like Incident/Allegations Description and Investigation Results after upgrading.

### Release

Yokohama

### Cause

The new PDF generation engine introduced in the upgrade does not respect the CSS property `white-space: pre-wrap`, causing loss of spacing in generated PDFs.

### Resolution

Follow these steps to apply the workaround:

#### Step 1: Navigate to System Properties

-   Go to System Properties in your instance.

#### Step 2: Locate the PDF Generation Property

-   Search for the property:  
    `com.snc.pdf.generation.v2.enabled`

#### Step 3: Disable the Property

-   Set the property value to False.
-   Click Save.

#### Step 4: Validate Document Formatting

-   Regenerate the HR Case document.
-   Confirm that the PDF now displays correct spacing and formatting.
