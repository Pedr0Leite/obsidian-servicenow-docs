---
title: "Export definition not showing value of the Choice field which is present in the record"
aliases:
  - KB0787496
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787496
kb_number: KB0787496
last_modified: 2023-10-31
---

## Export definition not showing value of the Choice field which is present in the record

  

### Issue

Knowledge article describes the choice field that not shown in the preview or the export from the Export definition where the field value is shown in the form view of the record.

### Cause

The field value which is present in the form is not actually set, this can be checked by viewing the XML view of the record. The form shows the value based on the Choice List Specification in the dictionary of the field.

When the dictionary entry has the choice value as "Dropdown without -- None -- (must specify a default value)" which means that the dropdown will show a Value, not none. Then it will show the next value which is based on the sequence order of the choices. The lowest sequence order value will appear in the field which is not actually set.

  

Sample Dictionary record of a Choice Field:

![](https://hi.service-now.com/sys_attachment.do?view=true&sys_id=3e0b19a2db0d40d02be0a851ca961997)

### Resolution

Export Set is not a Form-based export, field values have to be present in the DB (Show XML View). The Records have to be saved with the desired value to store the values for the field.
