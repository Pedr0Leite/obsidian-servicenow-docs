---
title: "Identify bad or missing form elements causing client-side issues"
aliases:
  - KB0547070
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547070
kb_number: KB0547070
last_modified: 2026-03-24
---

## Identify bad or missing form elements causing client-side issues

  

### Issue

Troubleshoot client-side functionality interrupted by bad or missing form elements, such as a field appearing on a form more than once or a UI policy condition referencing a field or related list record that is no longer on the form.

### Symptoms

-   Field removed from form
-   Cannot change a field
-   Form is broken
-   UI policy not working
-   UI action not working
-   Client scripts not working
-   Form sections not loading
-   Fields not visible
-   Mandatory field not working

### Release

All releases

### Cause

Bad elements on a form can cause a field to appear more than once. This confuses the UI policy because the field is expected to appear only once.

Bad or missing elements can also cause fields to be absent from the form or relationship records to be missing from a related list.

### Resolution

Bad form elements can interrupt client-side functionality in several ways. For example, if you define a related list on your form and then delete the relationship record behind that list, the form points to an invalid record and does not render correctly.

To check whether a bad element exists:

1.  Right-select the header of the record.
2.  Check whether the standard ServiceNow record options appear or whether browser right-select options appear instead.

If the browser right-select options appear, the form has a broken element. Contact Now Support to investigate and correct the issue.

### Related Links

### Videos

* * *

This video describes [how to troubleshoot incorrect mandatory fields on a form](https://www.youtube.com/watch?v=JcEywEXYHaU "how to troubleshoot incorrect mandatory fields on a form")

This video describes [how to troubleshoot incorrect read-only fields on a form](https://www.youtube.com/watch?v=9jeHajE41TQ "how to troubleshoot incorrect read-only fields on a form")
