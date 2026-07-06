---
title: "Exported PDF, truncated data not shown in the exported report but correctly shown in form view."
aliases:
  - KB0813827
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813827
kb_number: KB0813827
last_modified: 2024-04-08
---

## Exported PDF, truncated data not shown in the exported report but correctly shown in form view.

  

### Issue

In form view, when trying to export the view as a  PDF file, some of the data is not exported, for example the top section may not be shown.

### Cause

This issue happens when there is a split separator field in the form layout. This character is used as a delimited in the PDF export.

When the form section for these fields was starts with a split separator field value, this will cause this issue.

### Resolution

\- Edit the report in form layout.

\- Remove the unwanted split field char from the form Layout , so you will be moving the field records shown in the right side to the left side list view. Those are the unwanted records.Those fields should be easy to identify, they should look like this |xxxx|  
  
\- Try again to export as PDF and you will see that now the full report is generated.
